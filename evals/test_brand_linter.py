"""Filtro de especificación gráfica propuesta; no certifica identidad institucional."""
import argparse,json,re,math
from pathlib import Path
AUTHORIZED_HEX={'#FAF8F5','#1A1A1A','#C2593F','#1E3A5F','#D4A346','#FFFFFF','#000000'}
AUTHORIZED_FONTS={'playfair display','merriweather','inter','open sans'}
def check_hex_colors(text):
    found=[c.upper() for c in re.findall(r'#[0-9a-fA-F]{6}\b',text)]
    invalid=sorted(set(found)-AUTHORIZED_HEX)
    return {'unique_hex':sorted(set(found)),'invalid_hex':invalid,'is_valid':bool(found) and not invalid}
def font_values(proposal):
    found=[]
    for key,value in proposal.items():
        if key in {'tipografias','fuentes'}:found.extend(value.values() if isinstance(value,dict) else value if isinstance(value,list) else [value])
        elif key.startswith('fuente'):found.append(value)
    return found
def check_typography(proposal):
    fonts=font_values(proposal)
    invalid=[f for f in fonts if not isinstance(f,str) or f.casefold().strip() not in AUTHORIZED_FONTS]
    return {'declared_fonts':fonts,'invalid_fonts':invalid,'is_valid':bool(fonts) and not invalid}
def geometry(proposal):
    g=proposal.get('geometria')
    if not isinstance(g,dict):return {'is_valid':False,'error':'geometria_estructurada_ausente'}
    try:
        w,h,m=[g[k] for k in ['ancho_px','alto_px','margen_px']]
        if any(isinstance(n,bool) or not isinstance(n,(int,float)) or not math.isfinite(n) for n in [w,h,m]):raise ValueError()
        if w<=0 or h<=0 or m<0 or 2*m>=min(w,h):raise ValueError()
        box=g.get('caja_texto')
        if not isinstance(box,list) or len(box)!=4:raise ValueError()
        x,y,bw,bh=box
        if any(isinstance(n,bool) or not isinstance(n,(int,float)) or not math.isfinite(n) for n in box):raise ValueError()
        if bw<=0 or bh<=0 or x<m or y<m or x+bw>w-m or y+bh>h-m:raise ValueError()
        return {'is_valid':True,'limite':'Solo comprueba números declarados, no píxeles de un artefacto.'}
    except (KeyError,ValueError,TypeError):return {'is_valid':False,'error':'dimensiones_margen_o_caja_invalidos'}
def check_stock_anti_cliches(text):
    return re.findall(r'pluma estilogr[aá]fica dorada flotando|teclado con luces ne[oó]n',text,re.I)
def lint_graphic_proposal(proposal):
    colors=check_hex_colors(json.dumps(proposal,ensure_ascii=False));fonts=check_typography(proposal);geo=geometry(proposal);stock=check_stock_anti_cliches(json.dumps(proposal,ensure_ascii=False))
    errors=[]
    if not colors['is_valid']:errors.append('colores_ausentes_o_no_admitidos_en_propuesta')
    if not fonts['is_valid']:errors.append('fuentes_ausentes_o_no_admitidas_en_propuesta')
    if not geo['is_valid']:errors.append(geo['error'])
    if stock:errors.append('cliche_visual')
    return {'passed':not errors,'errores':errors,'color_audit':colors,'typography_audit':fonts,'geometry':geo,'stock_cliches_detected':stock,
        'estado_identidad':'propuesta_no_validada_por_cliente','requiere_inspeccion_artefacto':True,'limite':'Filtro de propuesta; no acredita marca oficial, contraste real, permisos ni calidad estética.'}
def main():
    p=argparse.ArgumentParser();p.add_argument('--input',type=Path,required=True);a=p.parse_args()
    result=lint_graphic_proposal(json.loads(a.input.read_text(encoding='utf-8-sig')));print(json.dumps(result,ensure_ascii=False,indent=2));raise SystemExit(0 if result['passed'] else 1)
if __name__=='__main__':main()
