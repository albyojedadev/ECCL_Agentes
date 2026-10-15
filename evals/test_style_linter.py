"""Filtro de edición; no mide fidelidad autoral ni sustituye revisión semántica."""
import argparse,json,re
from pathlib import Path
FORBIDDEN_CLICHES=[r'\badéntrate\b',r'\bfascinante\b',r'\btapiz\b',r'\bcrisol\b',r'\bviaje transformador\b',r'\ben conclusión\b']
def check_forbidden_cliches(text):
    return sorted({m.group(0) for p in FORBIDDEN_CLICHES for m in re.finditer(p,text,re.I)})
def check_biphasic_structure(text):
    internal=bool(re.search(r'(?im)^\s*(?:#+\s*)?(?:1[.)]?\s*)?informe(?:\s+t[eé]cnico)?\s+interno\b',text))
    external=bool(re.search(r'(?im)^\s*(?:#+\s*)?(?:2[.)]?\s*)?comentario\s+externo\b',text))
    return {'has_internal_report':internal,'has_external_comment':external,'is_biphasic':internal and external}
def calculate_sentence_metrics(text):
    sentences=[s for s in re.split(r'[.!?]+',text) if s.strip()]
    return {'total_sentences':len(sentences),'avg_words_per_sentence':round(sum(len(s.split()) for s in sentences)/len(sentences),2) if sentences else 0}
def check_affectionate_opening(text):
    return bool(re.search(r'(?m)^\s*[A-ZÁÉÍÓÚÑ][a-záéíóúñ]+(?:\s+[A-ZÁÉÍÓÚÑ][a-záéíóúñ]+)?(?:,|\.{3}|…)',text))
def lint_pedagogical_critique(text,mode='critique'):
    errors=[];cliches=check_forbidden_cliches(text);structure=check_biphasic_structure(text)
    if not text.strip():errors.append('texto_vacio')
    if cliches:errors.append('cliches_editoriales')
    external=re.split(r'(?im)^\s*(?:#+\s*)?(?:2[.)]?\s*)?comentario\s+externo[^\n]*\n?',text)[-1]
    if mode=='critique':
        if not structure['is_biphasic']:errors.append('faltan_secciones_diferenciadas')
        if not check_affectionate_opening(external):errors.append('destinatario_no_identificado')
        for pattern,label in [
            (r'no tienes talento|nunca aprender[aá]s|deber[ií]as abandonar','descalificacion_personal'),
            (r'problemas cl[ií]nicos|inestabilidad emocional|tu personalidad presenta','psicologizacion'),
            (r'informe confidencial|diagn[oó]stico interno|informe interno dice','posible_fuga_interna'),
            (r'copiar literalmente|sustituir todas tus palabras','sustitucion_autoria')]:
            if re.search(pattern,external if label!='psicologizacion' else text,re.I):errors.append(label)
    elif mode!='authorial':raise ValueError('Modo desconocido')
    return {'passed':not errors,'estado':'filtro_superado_pendiente_revision' if not errors else 'requiere_correccion',
            'errores':errors,'forbidden_cliches_detected':cliches,'biphasic_structure':structure,'sentence_metrics':calculate_sentence_metrics(text),
            'requiere_revision_semantica':True,'limite':'No acredita voz, verdad factual, privacidad completa ni calidad pedagógica; la cadencia es informativa.'}
def main():
    p=argparse.ArgumentParser();p.add_argument('--input',type=Path,required=True);p.add_argument('--mode',choices=['critique','authorial'],default='critique');a=p.parse_args()
    result=lint_pedagogical_critique(a.input.read_text(encoding='utf-8-sig'),a.mode);print(json.dumps(result,ensure_ascii=False,indent=2))
    raise SystemExit(0 if result['passed'] else 1)
if __name__=='__main__':main()
