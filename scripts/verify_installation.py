"""Comprobaciones estructurales y de integridad; no certifica calidad del modelo."""
from pathlib import Path
import hashlib,json,re,sys
from urllib.parse import unquote
REPO_DIR=Path(__file__).resolve().parents[1]
def load(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def fail(message):raise ValueError(message)
def require(condition,message):
    if not condition:fail(message)
def within(repo,relative):
    p=(repo/relative).resolve();require(p.is_relative_to(repo.resolve()) and p.is_file(),f'Archivo fuera del paquete/inexistente: {relative}');return p
def frontmatter(path):
    text=path.read_text(encoding='utf-8-sig');require(text.startswith('---\n'),f'Sin frontmatter: {path}')
    parts=text.split('---',2);require(len(parts)==3,f'Frontmatter sin cerrar: {path}')
    fields=dict(re.findall(r'^([a-z_-]+):\s*(.+)$',parts[1],re.M))
    require(fields.get('name') and fields.get('description'),f'Falta name/description: {path}')
    require(bool(parts[2].strip()) and len(parts[2].strip())>100,f'Cuerpo vacío/incompleto: {path}')
    return fields,text
def verify(repo=REPO_DIR):
    repo=Path(repo).resolve();m=load(repo/'plugin.json')
    require(m.get('name')=='eccl-agent-suite' and m.get('version'), 'Manifiesto incorrecto')
    require(len(m.get('agents',[]))==17 and len(m.get('skills',[]))==24 and len(m.get('protocols',[]))==6,'Inventario esperado17/24/6')
    ids={a['id'] for a in m['agents']};skills={s['id'] for s in m['skills']}
    require(len(ids)==17 and len(skills)==24,'IDs duplicados')
    active=[]
    for kind in ['agents','skills']:
        for entry in m[kind]:
            rel=entry['file'] if kind=='agents' else entry['path']+'/SKILL.md'
            p=within(repo,rel);fields,text=frontmatter(p)
            require(fields['name']==entry['id'],f'Nombre inconsistente: {rel}')
            if kind=='agents':
                refs=re.findall(r'^  - ([-a-z0-9]+)\s*$',text.split('---',2)[1],re.M)
                require(refs and set(refs)<=skills,f'Dependencias skills inválidas: {rel}')
            active.append(p)
    for rel in m['protocols']:active.append(within(repo,rel))
    for p in active:
        for ref in re.findall(r'\]\(([^)]+)\)',p.read_text(encoding='utf-8-sig')):
            ref=ref.strip('<>').split('#')[0]
            if not ref or '://' in ref or ref.startswith('mailto:'):continue
            target=(p.parent/unquote(ref)).resolve()
            require(target.is_relative_to(repo) and target.is_file(),f'Link roto: {p.relative_to(repo)} -> {ref}')
    sm=load(repo/'knowledge/sources/source_manifest.json')
    entries=sm.get('archivos',[]);require(len(entries)==99,'Inventario fuentes incompleto')
    for e in entries:
        if e['destino'] is None:
            require(e['estado']=='excluido_bloqueo_ofimatica','Exclusión no justificada');continue
        p=within(repo,e['destino']);require(hashlib.sha256(p.read_bytes()).hexdigest()==e['sha256'],f'Fuente alterada: {e["origen"]}')
    base=repo/'knowledge/sources/GPTs'
    for rel,key,total in [('catalogo/cursos_activos.json','cursos',73),('catalogo/claustro_docente.json','docentes',58)]:
        data=load(repo/'knowledge'/rel);require(isinstance(data.get(key),list) and len(data[key])==total,f'Corpus incompleto: {rel}')
    courses=load(repo/'knowledge/catalogo/cursos_activos.json')['cursos']
    require(len({r['id_registro'] for r in courses})==73,'Registros de curso duplicados')
    require(load(repo/'knowledge/catalogo/cursos_activos.json').get('ids_curso_distintos')==71,'Duplicados históricos no documentados')
    for row in courses:
        require(row.get('url_canonica','').startswith('https://') and row.get('disponibilidad_actual')=='no_verificada',f'Curso sin dominio/vigencia: {row["id_curso"]}')
        require(row.get('publico_objetivo') is not None and row.get('fila_origen'),f'Curso sin procedencia: {row["id_curso"]}')
    teachers=load(repo/'knowledge/catalogo/claustro_docente.json')['docentes'];require(all('tarifa_estimada' in t for t in teachers),'Tarifas pendientes perdidas')
    panel=load(repo/'knowledge/avatares/panel_18_alumnos.json')['avatares']
    required={'contexto','motivaciones','frenos','miedos','deseos','tono_emocional','frase_arquetipo','objetivo_narrativo','riesgos','modo_de_hablar','expectativas','relacion_con_la_escritura'}
    require(len(panel)==18 and len({a['id_avatar'] for a in panel})==18,'Panel incompleto/duplicado')
    for avatar in panel:require(required<=set(avatar) and 'procedencia' in avatar,f'Perfil incompleto: {avatar.get("nombre")}')
    style=load(repo/'knowledge/estilos/corpus_antonia.json')
    require(style.get('manual_estilo_completo')==(base/'05 Ghostwriter/manual_de_estilo.md').read_text(encoding='utf-8-sig'),'Manual autoral truncado/modificado')
    require(style.get('modulo_deteccion')==load(base/'06 Critico Literario/modulo_deteccion_antoniamolinero.json')['modulo_deteccion_antoniamolinero'],'Diagnóstico alterado')
    require(style.get('variantes_emocionales')==load(base/'05 Ghostwriter/variante_estilo_emocional.json'),'Variantes alteradas')
    require(sum(len(next(iter(load(base/f'06 Critico Literario/ejemplo_correccion_{i}.json').values()))) for i in range(1,5))==20,'Bancos de corrección incompletos')
    for folder in ['branding','legal']:
        for p in (repo/'knowledge'/folder).glob('*.json'):
            require(load(p).get('_procedencia',{}).get('estado')=='propuesta_pendiente_de_validacion_institucional',f'Propuesta sin estado: {p}')
    b=load(repo/'evals/benchmark_dataset.json');cases=b.get('casos')
    require(isinstance(cases,list) and len(cases)>=17,'Benchmark sin cobertura mínima')
    require(len({c.get('id') for c in cases})==len(cases),'Caso duplicado')
    for case in cases:require(case.get('agente') in ids and case.get('entrada') and isinstance(case.get('debe'),list) and case['debe'] and case.get('fuente_local'),f'Caso inválido: {case.get("id")}')
    require({c['agente'] for c in cases}==ids,'Benchmark no cubre17agentes')
    native=load(repo/'.claude-plugin/plugin.json');require(native['name']==m['name'] and native['version']==m['version'],'Manifiesto nativo distinto')
    require(set(native['agents'])=={'./'+a['file'] for a in m['agents']},'Agentes nativos incompletos')
    return {'estado':'integridad_estructural_superada','agentes':17,'skills':24,'protocolos':6,'fuentes_conservadas':sum(bool(e['destino']) for e in entries),'casos_diseno':len(cases),'calidad_modelo':'no_inferida_de_esta_prueba'}
def main():
    try:print(json.dumps(verify(),ensure_ascii=False,indent=2))
    except (ValueError,OSError,KeyError,TypeError) as e:print('FALLO DE INTEGRIDAD: '+str(e),file=sys.stderr);return 1
    return 0
if __name__=='__main__':sys.exit(main())
