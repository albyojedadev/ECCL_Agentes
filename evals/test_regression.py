"""Pruebas de regresión sobre fallos reales de la auditoría inicial."""
from pathlib import Path
from tempfile import TemporaryDirectory
import copy,importlib.util,json,shutil,sys,unittest,subprocess

REPO=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(REPO/'scripts'))
from verify_installation import verify
from ingest_knowledge import repair_delimiters,courses,strip_block_comments
from eccl import build_context,resolve
from test_brand_linter import lint_graphic_proposal
from test_style_linter import lint_pedagogical_critique

def data(relative):return json.loads((REPO/relative).read_text(encoding='utf-8-sig'))
def write(p,value):p.write_text(json.dumps(value,ensure_ascii=False),encoding='utf-8')
class QualityRegression(unittest.TestCase):
    def test_package_integrity(self):self.assertEqual(verify()['fuentes_conservadas'],98)
    def test_entire_authorial_manual(self):
        self.assertEqual(data('knowledge/estilos/corpus_antonia.json')['manual_estilo_completo'],(REPO/'knowledge/sources/GPTs/05 Ghostwriter/manual_de_estilo.md').read_text(encoding='utf-8-sig'))
    def test_eighteen_complete_avatars(self):
        a=data('knowledge/avatares/panel_18_alumnos.json')['avatares']
        self.assertEqual(len(a),18);self.assertTrue(all('modo_de_hablar'in x and 'expectativas'in x for x in a));self.assertEqual(a[0]['edad'],42)
    def test_seven_courses_keep_notes_and_period(self):
        a={x['id_curso']:x for x in data('knowledge/catalogo/cursos_activos.json')['cursos']}
        self.assertEqual(a['IMAG-PUB']['capacidad_plazas'],'MÍNIMO 6');self.assertEqual(a['IMAG-PUB']['publico_objetivo'],'Creativos de agencias')
        self.assertEqual(a['POESIA-ACT']['estado'],'Matrícula 1 diciembre');self.assertTrue(a['MICRO-VIAJE']['horario'].startswith('Miércoles'))
        for k in ['IMAG-PUB','GUION-COMIC','VIDEOJUEGOS','ESCRIT-TERAP2','MITOS','MICRO-VIAJE','POESIA-ACT']:
            self.assertEqual(a[k]['observaciones'],a[k]['fila_origen'][-1]);self.assertEqual(a[k]['periodo_textual'],a[k]['fila_origen'][11])
    def test_ended_course_not_current(self):
        a=next(x for x in data('knowledge/catalogo/cursos_activos.json')['cursos'] if x['id_curso']=='CL-2526')
        self.assertEqual(a['vigencia'],'edicion_finalizada');self.assertEqual(a['disponibilidad_actual'],'no_verificada')
    def test_historical_duplicate_ids_are_explicit(self):
        d=data('knowledge/catalogo/cursos_activos.json');self.assertEqual(d['total_registros'],73);self.assertEqual(d['ids_curso_distintos'],71);self.assertEqual(set(d['duplicados_origen']),{'INICIA-ESPACIO','AVANZA-ESPACIO'})
    def test_prices_with_different_units_not_an_interval(self):
        r=next(r for r in data('knowledge/catalogo/cursos_activos.json')['cursos'] if r['id_curso']=='LOS-INTRUSOS-2526');self.assertTrue(r['advertencias_precio']);self.assertIn('unidades',r['precios_interpretacion'])
    def test_pending_teacher_rates_retained(self):
        a=data('knowledge/catalogo/claustro_docente.json')['docentes'];self.assertEqual(len(a),58);self.assertTrue(all(x['tarifa_estimada']=='CONSULTAR' for x in a))
    def test_delimiter_repair_preserves_values(self):
        d,changes=repair_delimiters('{"ejemplos":["una llave } dentro de texto", "otra" }}')
        self.assertEqual(d,{'ejemplos':['una llave } dentro de texto','otra']});self.assertEqual(len(changes),1)
    def test_comment_stripping_preserves_quoted_content(self):
        t='{/* nota */"texto":"no borrar /* dentro */", "x":1}';self.assertEqual(json.loads(strip_block_comments(t)),{'texto':'no borrar /* dentro */','x':1})
    def test_normalized_banks_keep_complete_records_and_truncation_receipts(self):
        b={b['genero']:b for b in data('knowledge/estilos/ejemplos_normalizados.json')['bancos']};self.assertEqual(len(b),6);self.assertEqual(sum(len(x['registros_completos']) for x in b.values()),57)
        self.assertEqual(len(b['critica']['fragmentos_no_parseables']),1);self.assertEqual(len(b['narrativa']['fragmentos_no_parseables']),1)
        self.assertTrue(all('id' in r['registro_original'] for x in b.values() for r in x['registros_completos']))
    def test_truncated_document_rejected(self):
        with self.assertRaises(ValueError):repair_delimiters('{"texto":"sin cerrar')
    def test_no_geometry_cannot_pass(self):self.assertFalse(lint_graphic_proposal({'fuente':'Inter'})['passed'])
    def good_graphic(self):
        return {'colores':['#FAF8F5','#1A1A1A'],'tipografias':['Inter'],'geometria':{'ancho_px':1080,'alto_px':1080,'margen_px':80,'caja_texto':[80,80,900,900]}}
    def test_complete_proposal_passes_filter_only(self):
        r=lint_graphic_proposal(self.good_graphic());self.assertTrue(r['passed']);self.assertTrue(r['requiere_inspeccion_artefacto'])
    def test_mixed_unapproved_font_rejected(self):
        p=self.good_graphic();p['tipografias'].append('Roboto');self.assertFalse(lint_graphic_proposal(p)['passed'])
    def test_negative_margin_rejected(self):
        p=self.good_graphic();p['geometria']['margen_px']=-100;self.assertFalse(lint_graphic_proposal(p)['passed'])
    def test_overflow_text_rejected(self):
        p=self.good_graphic();p['geometria']['caja_texto']=[0,0,2000,2000];self.assertFalse(lint_graphic_proposal(p)['passed'])
    def test_non_finite_geometry_rejected(self):
        for v in [float('nan'),float('inf'),float('-inf')]:
            for key in ['ancho_px','alto_px','margen_px']:
                p=self.good_graphic();p['geometria'][key]=v;self.assertFalse(lint_graphic_proposal(p)['passed'])
            for i in range(4):
                p=self.good_graphic();p['geometria']['caja_texto'][i]=v;self.assertFalse(lint_graphic_proposal(p)['passed'])
    def test_absent_color_rejected(self):
        p=self.good_graphic();p.pop('colores');self.assertFalse(lint_graphic_proposal(p)['passed'])
    def test_aggression_and_internal_leak_rejected(self):
        t='Informe Interno\nEscena con detalle.\nComentario Externo\nElena, no tienes talento y deberías abandonar este curso.\nEl informe confidencial dice que no aprenderás.'
        self.assertFalse(lint_pedagogical_critique(t)['passed'])
    def test_psychologizing_and_rewriting_rejected(self):
        t='Informe Interno\nDiagnostica inestabilidad emocional.\nComentario Externo\nAna, debes copiar literalmente mi párrafo para sustituir todas tus palabras.'
        self.assertFalse(lint_pedagogical_critique(t)['passed'])
    def test_authorial_does_not_need_critique_sections(self):
        t='La taza conserva una mancha que nadie sabe explicar. Mi madre nunca habló de ella.'
        r=lint_pedagogical_critique(t,'authorial');self.assertTrue(r['passed']);self.assertTrue(r['requiere_revision_semantica'])
    def test_critique_sections_required(self):self.assertFalse(lint_pedagogical_critique('Ana, leo tu cuento con atención.')['passed'])
    def test_context_all_agents_and_skill_paths(self):
        for a in data('plugin.json')['agents']:
            c=build_context(a['id'],'Consulta de prueba')
            self.assertGreaterEqual(len(c['archivos_cargados']),3);self.assertEqual(c['estado'],'contexto_preparado_no_respuesta_de_modelo')
    def test_context_unknown_agent_rejected(self):
        with self.assertRaises(ValueError):build_context('no-existe')
    def test_context_outside_package_rejected(self):
        with self.assertRaises(ValueError):resolve('../GPTs/SecureInstructionsv3.txt')
    def test_context_reference_actually_loaded(self):
        r='knowledge/sources/GPTs/05 Ghostwriter/manual_de_estilo.md'
        c=build_context('ghostwriter-de-antonia-molinero',references=[r]);self.assertIn(r,[x['ruta'] for x in c['archivos_cargados']]);self.assertIn('Novela',c['prompt'])
    def test_source_corruption_detected(self):
        self.mutation('knowledge/sources/GPTs/05 Ghostwriter/manual_de_estilo.md','recortado')
    def test_cli_does_not_ignore_requested_behavior_results(self):
        for mode in ['all','structural']:
            r=subprocess.run([sys.executable,'-B',str(REPO/'evals/run_evals.py'),'--suite',mode,'--results-file',str(REPO/'evals/does-not-exist.json')],capture_output=True)
            self.assertNotEqual(r.returncode,0)
    def test_empty_agent_detected(self):self.mutation('agents/critico-literario-de-la-eccl.md','')
    def test_catalog_without_courses_detected(self):self.mutation('knowledge/catalogo/cursos_activos.json','{"auditoria":"sin cursos"}')
    def test_benchmark_without_input_output_detected(self):self.mutation('evals/benchmark_dataset.json','{"casos":[{"auditoria":"sin entrada/salida"}]}')
    def mutation(self,rel,text):
        with TemporaryDirectory(prefix='eccl_regression_') as tmp:
            clone=Path(tmp)/'suite';shutil.copytree(REPO,clone,ignore=shutil.ignore_patterns('.git','__pycache__'))
            (clone/rel).write_text(text,encoding='utf-8')
            with self.assertRaises((ValueError,KeyError)):verify(clone)
if __name__=='__main__':unittest.main()
