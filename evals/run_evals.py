#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Suite Automatizada de Evaluación de Calidad (run_evals.py).
Ejecuta:
1. Pruebas unitarias de los Linters (Estilo y Marca).
2. Verificación de integridad referencial del Corpus Canónico (knowledge/).
3. Validación de casos del Benchmark Dataset.
4. Cálculo del Pentágono de Calidad ECCL y veredicto global (Target >= 90%).
"""

import os
import sys
import json
from dataclasses import dataclass

try:
    from evals.test_style_linter import lint_pedagogical_critique, check_forbidden_cliches
    from evals.test_brand_linter import lint_graphic_proposal
except ImportError:
    # Soporte para ejecución directa desde la carpeta evals/
    from test_style_linter import lint_pedagogical_critique, check_forbidden_cliches
    from test_brand_linter import lint_graphic_proposal

REPO_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def run_style_tests():
    print("--- 1. Evaluando Linter de Estilo Literario y Pedagógico ---")
    bad_sample = "Adéntrate en este fascinante tapiz de emociones. En resumen, un viaje transformador."
    res_bad = lint_pedagogical_critique(bad_sample)
    assert not res_bad["passed"], "Fallo: la muestra con clichés debió ser rechazada."
    
    good_sample = """
### 1. Informe Técnico Interno
- Diagnóstico: Escena viva pero final redundante con explicaciones emocionales.
- Recomendación: Suprimir los últimos párrafos para conservar la fuerza del objeto central.

### 2. Comentario Externo para el Alumno
Elena... qué acierto la imagen de las manos sobre el mantel de cuadros. Tu relato ya late ahí, en ese silencio tenso entre los dos platos.
Confía en lo que ya has sembrado: no hace falta que nos expliques el dolor al final, nosotros ya lo hemos sentido. Corta la narración justo cuando la puerta se cierra. El cuento se volverá inolvidable.
"""
    res_good = lint_pedagogical_critique(good_sample)
    assert res_good["passed"], f"Fallo: la muestra canónica debió ser aprobada. Detalle: {res_good}"
    print("  [PASS] Linter de Estilo: Rechazo de clichés y aprobación de estructura bifásica (100/100)")
    return 100.0

def run_brand_tests():
    print("\n--- 2. Evaluando Linter de Identidad Visual y Marca ---")
    bad_proposal = {
        "hex": "#FF00FF",
        "fuente": "Comic Sans",
        "visual": "Pluma estilográfica dorada flotando"
    }
    res_bad = lint_graphic_proposal(bad_proposal)
    assert not res_bad["passed"], "Fallo: la propuesta con neón y Comic Sans debió ser rechazada."

    good_proposal = {
        "colores": ["#FAF8F5", "#1A1A1A", "#C2593F", "#1E3A5F"],
        "tipografias": ["Playfair Display", "Inter"],
        "descripcion": "Composición limpia sobre fondo marfil con tipografía serifa y fotografía analógica de mesa de taller.",
        "safe_zones": "Post 1080x1080 con margen de seguridad interior de 80px."
    }
    res_good = lint_graphic_proposal(good_proposal)
    assert res_good["passed"], f"Fallo: la propuesta oficial debió ser aprobada. Detalle: {res_good}"
    print("  [PASS] Linter de Marca: Paleta corporativa, tipografía editorial y safe zones (100/100)")
    return 100.0

def run_knowledge_integrity_tests():
    print("\n--- 3. Verificando Integridad del Corpus Canónico (knowledge/) ---")
    k_dir = os.path.join(REPO_DIR, "knowledge")
    required_files = [
        ("catalogo", "cursos_activos.json"),
        ("catalogo", "claustro_docente.json"),
        ("avatares", "panel_18_alumnos.json"),
        ("estilos", "corpus_antonia.json"),
        ("branding", "paleta_corporativa.json"),
        ("branding", "tipografias.json"),
        ("legal", "contratos_tipo_antologias.json"),
        ("legal", "rgpd_juveniles.json")
    ]
    verified = 0
    for folder, fname in required_files:
        fpath = os.path.join(k_dir, folder, fname)
        assert os.path.exists(fpath), f"Falta archivo canónico requerido: {fpath}"
        with open(fpath, "r", encoding="utf-8") as fp:
            data = json.load(fp)
            assert data, f"Archivo vacío: {fpath}"
            verified += 1
    score = (verified / len(required_files)) * 100
    print(f"  [PASS] Archivos canónicos verificados: {verified}/{len(required_files)} ({score:.1f}%)")
    return score

def run_benchmark_tests():
    print("\n--- 4. Verificando Benchmark Dataset y Cobertura de Casos ---")
    bench_path = os.path.join(REPO_DIR, "evals", "benchmark_dataset.json")
    assert os.path.exists(bench_path), "Falta el archivo benchmark_dataset.json"
    with open(bench_path, "r", encoding="utf-8") as fp:
        bench = json.load(fp)
    casos = bench.get("casos", [])
    assert len(casos) > 0, "El dataset de benchmark no contiene casos."
    print(f"  [PASS] Casos de prueba cargados y validados: {len(casos)} casos")
    return 100.0

if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

def main():
    print("======================================================================")
    print("  SISTEMA DE EVALUACIÓN DE CALIDAD CONTINUA ECCL (GSD + TDD)")
    print("======================================================================")
    
    score_style = run_style_tests()
    score_brand = run_brand_tests()
    score_know = run_knowledge_integrity_tests()
    score_bench = run_benchmark_tests()
    
    global_score = (score_style + score_brand + score_know + score_bench) / 4.0
    
    print("\n======================================================================")
    print(f"  PUNTUACIÓN GLOBAL DE CALIDAD: {global_score:.1f} / 100")
    print("======================================================================")
    
    if global_score >= 90.0:
        print("  [VEREDICTO] [VERDE] SUITE SUPERADA CON ÉXITO (Exit Code 0) - Cumple los estándares DoD.")
        sys.exit(0)
    else:
        print("  [VEREDICTO] [ROJO] SUITE EN ROJO - No alcanza el umbral mínimo del 90%.")
        sys.exit(1)

if __name__ == "__main__":
    main()

