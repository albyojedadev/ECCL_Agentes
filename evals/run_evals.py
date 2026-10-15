"""Ejecuta regresiones; separa resultados estructurales y evaluación de modelos."""
from pathlib import Path
import argparse,json,sys,unittest
REPO=Path(__file__).resolve().parents[1]
def review_behavior(path):
    data=json.loads(path.read_text(encoding='utf-8-sig'))
    expected={c['id']:c for c in json.loads((REPO/'evals/benchmark_dataset.json').read_text(encoding='utf-8-sig'))['casos']}
    rows=data.get('casos',[])
    if len(rows)!=len(expected) or {r.get('id') for r in rows}!=set(expected):raise ValueError('Faltan casos o hay duplicados')
    for r in rows:
        if not r.get('salida') or not r.get('archivos_cargados') or not r.get('entorno') or not r.get('revision'):raise ValueError(f'Traza incompleta: {r.get("id")}')
        criteria=r['revision']
        if len(criteria)!=len(expected[r['id']]['debe']):raise ValueError('Faltan criterios revisados')
        if any(c.get('resultado')!='cumple' or not c.get('evidencia') for c in criteria):raise ValueError(f'Caso no aceptado: {r["id"]}')
    return {'estado':'revision_de_salidas_registrada','casos':len(rows),'limite':'No acredita despliegue del cliente ni validación humana de voz.'}
def main():
    p=argparse.ArgumentParser();p.add_argument('--suite',choices=['all','structural','behavior'],default='structural');p.add_argument('--results-file',type=Path);a=p.parse_args()
    if a.suite=='structural' and a.results_file:p.error('--results-file requiere --suite behavior o --suite all')
    if a.suite in {'behavior','all'}:
        if not a.results_file:p.error('La evaluación de comportamiento requiere trazas reales --results-file')
        if not a.results_file.is_file():p.error('No existe el archivo de trazas: '+str(a.results_file))
    if a.suite=='behavior':
        if not a.results_file:p.error('La evaluación de comportamiento requiere trazas reales --results-file')
        try:print(json.dumps(review_behavior(a.results_file),ensure_ascii=False,indent=2));return 0
        except (ValueError,KeyError,OSError) as e:print(str(e),file=sys.stderr);return 1
    suite=unittest.defaultTestLoader.discover(str(REPO/'evals'),pattern='test_regression.py')
    result=unittest.TextTestRunner(verbosity=2).run(suite)
    print(json.dumps({'regresiones_ejecutadas':result.testsRun,'fallos':len(result.failures),'errores':len(result.errors),'alcance':'integridad_filtros_y_carga_contexto','comportamiento_modelo':'consultar_trazas_separadas_no_inferir_de_este_resultado'},ensure_ascii=False))
    if not result.wasSuccessful():return 1
    if a.suite=='all':
        try:print(json.dumps(review_behavior(a.results_file),ensure_ascii=False,indent=2))
        except (ValueError,KeyError,OSError) as e:print(str(e),file=sys.stderr);return 1
    return 0
if __name__=='__main__':sys.exit(main())
