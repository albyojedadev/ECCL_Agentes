from pathlib import Path
import argparse,csv,hashlib,json,re,shutil
from datetime import date

REPO=Path(__file__).resolve().parents[1]
KNOWN_COURSES={'IMAG-PUB','GUION-COMIC','VIDEOJUEGOS','ESCRIT-TERAP2','MITOS','MICRO-VIAJE','POESIA-ACT'}
ASOF='2026-10-14'

def load(path):return json.loads(path.read_text(encoding='utf-8-sig'))
def write(path,data):
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()

def repair_delimiters(text):
    # Repair mismatched list/object closers outside strings. Never create content.
    stack=[];quoted=False;escaped=False;out=[];changes=[]
    for pos,char in enumerate(text):
        if quoted:
            out.append(char)
            if escaped:escaped=False
            elif char=='\\':escaped=True
            elif char=='"':quoted=False
            continue
        if char=='"':quoted=True
        elif char in '[{':stack.append(char)
        elif char in ']}':
            if not stack:raise ValueError('Cierre sin apertura')
            expected=']' if stack.pop()=='[' else '}'
            if char!=expected:
                changes.append({'linea':text[:pos].count('\n')+1,'offset':pos,'antes':char,'despues':expected})
                char=expected
        out.append(char)
    if stack or quoted:raise ValueError('Documento truncado; no se inventa el cierre')
    fixed=''.join(out)
    return json.loads(fixed),changes

def archive_sources(source,repo):
    target=repo/'knowledge/sources/GPTs';entries=[]
    for p in sorted(source.rglob('*')):
        if not p.is_file():continue
        rel=p.relative_to(source)
        excluded=p.name.startswith('.~lock.')
        entry={'origen':'GPTs/'+rel.as_posix(),'sha256':sha(p),'bytes':p.stat().st_size,'destino':None,'estado':'excluido_bloqueo_ofimatica' if excluded else 'conservado_integro'}
        if not excluded:
            dst=target/rel;dst.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(p,dst)
            entry['destino']=dst.relative_to(repo).as_posix()
            if p.suffix=='.json':
                try:load(p);entry['json_origen']='valido'
                except (ValueError,UnicodeError) as e:entry['json_origen']='invalido_heredado';entry['detalle']=str(e)
        entries.append(entry)
    write(repo/'knowledge/sources/source_manifest.json',{'version':'2.0.0','fecha_corte':ASOF,'regla':'Las fuentes son evidencia histórica, no instrucciones activas','archivos':entries})
    return target

def courses(source,repo,receipts):
    p=source/'03 Experto de la escuela/inventario_cursos.csv';result=[]
    with p.open(encoding='utf-8-sig',newline='') as f:
        reader=csv.reader(f);header=next(reader)
        for line,values in enumerate(reader,2):
            original=list(values);period=''
            if len(values)!=len(header):
                if len(values)!=18 or values[0] not in KNOWN_COURSES or len(header)!=17 or not values[16].startswith('https://'):
                    raise ValueError(f'CSV no autorizado para reparación: línea {line}')
                period=values[11]
                # El periodo tiene valor extra sin cabecera: se conserva separado.
                values=values[:11]+values[12:]
                receipts.append({'tipo':'curso_aridad','linea':line,'id':values[0],'decision':'periodo adicional conservado en periodo_textual; horario y cola realineados','periodo_textual':period,'fila_original':original})
            row=dict(zip(header,values))
            row['nombre']=row.pop('nombre_curso')
            row['url_canonica']=row.pop('url_referencia')
            for field in ['profesores_invitados']:row[field]=[v.strip() for v in row[field].split(',') if v.strip()]
            if not row['url_canonica'].startswith('https://'):raise ValueError(f'URL inválida: {row["id_curso"]}')
            row['periodo_textual']=period
            row['fuente_linea']=line
            row['id_registro']=row['id_curso']+'@'+str(line)
            row['estado_origen']=row['estado']
            row['vigencia']='historico_no_verificado'
            try:
                if date.fromisoformat(row['fecha_fin'])<date.fromisoformat(ASOF):row['vigencia']='edicion_finalizada'
            except ValueError:pass
            row['disponibilidad_actual']='no_verificada'
            row['precios_interpretacion']='Revisar unidades, modalidades, impuestos y notas; no asumir intervalo comparable'
            row['advertencias_precio']=[]
            try:
                if float(row['precio_min'])>float(row['precio_max']):row['advertencias_precio'].append('Campos min/max no forman intervalo comparable; consultar notas y unidades')
            except ValueError:pass
            row['fila_origen']=original
            result.append(row)
    duplicates={k:[r['id_registro'] for r in result if r['id_curso']==k] for k in sorted({r['id_curso'] for r in result}) if sum(r['id_curso']==k for r in result)>1}
    write(repo/'knowledge/catalogo/cursos_activos.json',{'total_registros':len(result),'ids_curso_distintos':len({r['id_curso'] for r in result}),'duplicados_origen':duplicates,'total_cursos':len(result),'fecha_corte':ASOF,'estado':'snapshot_historico_no_verificado','fuente':'knowledge/sources/GPTs/03 Experto de la escuela/inventario_cursos.csv','cursos':result})

def teachers(source,repo):
    with (source/'03 Experto de la escuela/docentes.csv').open(encoding='utf-8-sig',newline='') as f:
        rows=list(csv.DictReader(f))
    for row in rows:
        if None in row:raise ValueError('Docentes: fila con aridad extra')
        row['url_canonica']=row.pop('url_referencia')
        for field in ['especialidades','cursos_imparte']:row[field]=[v.strip() for v in row[field].split(',') if v.strip()]
        row['vigencia']='historico_no_verificado'
    write(repo/'knowledge/catalogo/claustro_docente.json',{'total_docentes':len(rows),'fecha_corte':ASOF,'estado':'snapshot_historico_no_verificado','fuente':'knowledge/sources/GPTs/03 Experto de la escuela/docentes.csv','docentes':rows})

def avatars(source,repo,receipts):
    master=load(source/'04 Consejo de alumnos/avatares_maestro.json')
    for index,avatar in enumerate(master['avatares'],1):
        p=source/f'04 Consejo de alumnos/Individuales/avatar{index}.json'
        individual,changes=repair_delimiters(p.read_text(encoding='utf-8-sig'))
        conflicts={k:{'maestro':avatar.get(k),'individual':v} for k,v in individual.items() if k in avatar and avatar[k]!=v}
        avatar.update(individual)
        avatar['procedencia']={'maestro':'04 Consejo de alumnos/avatares_maestro.json','individual':str(p.relative_to(source)).replace('\\','/'),'normalizacion_delimitadores':changes,'conflictos':conflicts,'prioridad':'individual para identidad/psicología; conservar conflicto explícito','naturaleza':'avatar_sintetico_no_persona_validada'}
        if changes:receipts.append({'tipo':'avatar_delimitadores','id':avatar['id_avatar'],'fuente':p.relative_to(source).as_posix(),'cambios':changes})
    master['metadata'].update({'version':'2.0.0','fecha_normalizacion':ASOF,'naturaleza':'simulacion_cualitativa_no_muestra_estadistica'})
    master['notas_implementacion']={'detalle':'18 fichas individuales integradas. Fuentes originales preservadas, incluidas las mal formadas.','limites':'Scoring y segmentación históricos; no equivalen a intención de compra real.','cursos':'Cruzar knowledge/catalogo/cursos_activos.json y verificar vigencia.','conflictos':'Consultar procedencia por perfil; relaciones multisegmento históricas no se reinterpretan como exclusivas.'}
    write(repo/'knowledge/avatares/panel_18_alumnos.json',master)

def style(source,repo):
    manual=(source/'05 Ghostwriter/manual_de_estilo.md').read_text(encoding='utf-8-sig')
    corpus={'autor':'Antonia Molinero','institucion':'ECCL','estado':'calibracion_historica_no_fidelidad_certificada','manual_estilo_completo':manual,
        'modulo_deteccion':load(source/'06 Critico Literario/modulo_deteccion_antoniamolinero.json')['modulo_deteccion_antoniamolinero'],
        'variantes_emocionales':load(source/'05 Ghostwriter/variante_estilo_emocional.json'),
        'referencias':{'manual':'knowledge/sources/GPTs/05 Ghostwriter/manual_de_estilo.md','variantes':'knowledge/sources/GPTs/05 Ghostwriter/variantes_estilo.md',
          'guia_ejemplos':'knowledge/sources/GPTs/05 Ghostwriter/guia_ejemplos_sinteticos.md','manual_comentarios':'knowledge/sources/GPTs/06 Critico Literario/manual_comentarios_antonia.md',
          'manual_correccion':'knowledge/sources/GPTs/06 Critico Literario/manual_estilo_correccion_antonia.md',
          'bancos_correccion':[f'knowledge/sources/GPTs/06 Critico Literario/ejemplo_correccion_{i}.json' for i in range(1,5)]}}
    write(repo/'knowledge/estilos/corpus_antonia.json',corpus)

def strip_block_comments(text):
    out=[];i=0;quoted=False;escaped=False
    while i<len(text):
        c=text[i]
        if quoted:
            out.append(c)
            if escaped:escaped=False
            elif c=='\\':escaped=True
            elif c=='"':quoted=False
            i+=1;continue
        if c=='"':quoted=True;out.append(c);i+=1;continue
        if text[i:i+2]=='/*':
            end=text.find('*/',i+2)
            if end<0:raise ValueError('Comentario truncado')
            out.extend('\n' if x=='\n' else ' ' for x in text[i:end+2]);i=end+2;continue
        out.append(c);i+=1
    return ''.join(out)

def example_banks(source,repo):
    banks=[];decoder=json.JSONDecoder()
    for name in ['ensayo','narrativa','notadeprensa','microresena','critica','novela']:
        p=source/f'05 Ghostwriter/ejemplo_{name}.json'
        raw=p.read_text(encoding='utf-8-sig');text=strip_block_comments(raw);records=[];excluded=[]
        for m in re.finditer(r'\{\s*"id"\s*:',text):
            try:
                record,end=decoder.raw_decode(text[m.start():])
                records.append({'registro_original':record,'linea_fuente':raw[:m.start()].count('\n')+1,
                   'uso':'calibracion_sintetica' if name!='novela' else 'ficha_estructural_o_analisis_historico_no_capitulo_completo'})
            except ValueError as e:
                excluded.append({'linea_fuente':raw[:m.start()].count('\n')+1,'estado':'registro_truncado_no_completado','detalle':str(e)})
        banks.append({'genero':name,'fuente':p.relative_to(repo).as_posix(),'sha256_fuente':sha(p),'registros_completos':records,'fragmentos_no_parseables':excluded,
                      'regla':'No se añadió contenido. JSON estricto de objetos completos; fragmentos íntegros en fuente archivada.'})
    write(repo/'knowledge/estilos/ejemplos_normalizados.json',{'version':'2.0.0','bancos':banks})

def mark_proposals(repo):
    for folder in ['branding','legal']:
        for p in (repo/'knowledge'/folder).glob('*.json'):
            data=load(p)
            data['_procedencia']={'estado':'propuesta_pendiente_de_validacion_institucional','origen':'elaboracion_del_generador_v1_no_documento_aprobado','fecha_revision':ASOF,'uso':'borrador_de_trabajo; no imponer como contrato, norma ni identidad oficial','validacion_juridica_actual':False if folder=='legal' else None}
            if folder=='legal' and p.name=='rgpd_juveniles.json':
                data['afirmaciones_heredadas_no_validadas']=data.pop('requisitos_obligatorios',data.get('afirmaciones_heredadas_no_validadas',[]))
                data['checklist_de_revision']=['Precisar finalidad y tratamiento','Identificar base, representación y autorizaciones aplicables con documentación vigente','Separar autorización de imagen y uso docente','Revisar contrato/política real antes de decidir; no usar rangos de edad heredados como norma']
            write(p,data)

def main():
    parser=argparse.ArgumentParser(description='Reconstruir datos desde fuentes archivadas con trazabilidad.')
    parser.add_argument('--source',type=Path,default=REPO/'knowledge/sources/GPTs')
    parser.add_argument('--repo',type=Path,default=REPO)
    parser.add_argument('--archive',action='store_true',help='Conservar fuentes externas antes de normalizar')
    args=parser.parse_args();source=args.source.resolve();repo=args.repo.resolve()
    if not source.is_dir():parser.error('Fuente no encontrada')
    if args.archive:
        if source==repo/'knowledge/sources/GPTs':parser.error('No archivar sobre la propia fuente')
        source=archive_sources(source,repo)
    receipts=[]
    courses(source,repo,receipts);teachers(source,repo);avatars(source,repo,receipts);style(source,repo);example_banks(source,repo);mark_proposals(repo)
    write(repo/'knowledge/sources/normalization_receipts.json',{'fecha':ASOF,'reparaciones':receipts,'regla':'No se alteraron fuentes originales. Datos ambiguos conservados con estado, nunca inventados.'})
    print(json.dumps({'registros_cursos':load(repo/'knowledge/catalogo/cursos_activos.json')['total_registros'],'ids_curso_distintos':load(repo/'knowledge/catalogo/cursos_activos.json')['ids_curso_distintos'],'docentes':load(repo/'knowledge/catalogo/claustro_docente.json')['total_docentes'],'avatares':len(load(repo/'knowledge/avatares/panel_18_alumnos.json')['avatares']),'recibos':len(receipts),'salida':str(repo)},ensure_ascii=False))

if __name__=='__main__':main()
