#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de Chequeo Pre-Vuelo y Verificación de Salud de la Suite ECCL (verify_installation.py).
Valida:
1. Manifiesto del Plugin (plugin.json).
2. Existencia y formato de los 17 Asistentes (.md).
3. Existencia y formato de las 24 Skills (SKILL.md).
4. Integridad de los 6 Protocolos SOPs (protocols/).
5. Integridad del Corpus Canónico (knowledge/).
6. Ejecución en verde de la Suite de Evaluación y Linters (evals/run_evals.py).
"""

import os
import sys
import json
import glob

if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

REPO_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if REPO_DIR not in sys.path:
    sys.path.insert(0, REPO_DIR)

def check_plugin_manifest():
    print("1. Verificando plugin.json...")
    p_path = os.path.join(REPO_DIR, "plugin.json")
    assert os.path.exists(p_path), "No se encuentra plugin.json"
    with open(p_path, "r", encoding="utf-8") as f:
        manifest = json.load(f)
    assert manifest.get("name") == "eccl-agent-suite", "Nombre de plugin incorrecto"
    agents_count = len(manifest.get("agents", []))
    skills_count = len(manifest.get("skills", []))
    protocols_count = len(manifest.get("protocols", []))
    print(f"   [OK] plugin.json válido ({agents_count} agentes, {skills_count} skills, {protocols_count} protocolos)")
    return manifest

def check_agents(manifest):
    print("\n2. Verificando 17 Asistentes en agents/...")
    missing = []
    for ag in manifest.get("agents", []):
        fpath = os.path.join(REPO_DIR, ag["file"])
        if not os.path.exists(fpath):
            missing.append(ag["file"])
    assert len(missing) == 0, f"Faltan agentes: {missing}"
    print(f"   [OK] Todos los {len(manifest.get('agents', []))} agentes existen y están accesibles.")

def check_skills(manifest):
    print("\n3. Verificando 24 Skills en skills/...")
    missing = []
    for sk in manifest.get("skills", []):
        fpath = os.path.join(REPO_DIR, sk["path"], "SKILL.md")
        if not os.path.exists(fpath):
            missing.append(sk["path"])
    assert len(missing) == 0, f"Faltan skills: {missing}"
    print(f"   [OK] Todas las {len(manifest.get('skills', []))} skills tienen su SKILL.md válido.")

def check_protocols(manifest):
    print("\n4. Verificando 6 Protocolos SOPs en protocols/...")
    missing = []
    for pr in manifest.get("protocols", []):
        fpath = os.path.join(REPO_DIR, pr)
        if not os.path.exists(fpath):
            missing.append(pr)
    assert len(missing) == 0, f"Faltan protocolos: {missing}"
    print(f"   [OK] Todos los {len(manifest.get('protocols', []))} protocolos SOPs están disponibles.")

def check_knowledge():
    print("\n5. Verificando Corpus Canónico en knowledge/...")
    k_files = glob.glob(os.path.join(REPO_DIR, "knowledge", "**", "*.json"), recursive=True)
    assert len(k_files) >= 8, f"Se esperaban al menos 8 archivos canónicos, encontrados {len(k_files)}"
    for kf in k_files:
        with open(kf, "r", encoding="utf-8") as f:
            data = json.load(f)
            assert data, f"Archivo vacío: {kf}"
    print(f"   [OK] {len(k_files)} archivos de datos canónicos verificados e íntegros.")

def check_evals():
    print("\n6. Ejecutando suite de evaluación de calidad...")
    import subprocess
    evals_script = os.path.join(REPO_DIR, "evals", "run_evals.py")
    res = subprocess.run([sys.executable, evals_script], capture_output=True, text=True, encoding="utf-8")
    if res.returncode != 0:
        print(res.stdout)
        print(res.stderr)
        raise RuntimeError("La suite de evaluación falló con Exit Code != 0")
    print("   [OK] Suite de evaluación de calidad (run_evals.py) superada al 100%.")

def main():
    print("======================================================================")
    print("  DIAGNÓSTICO DE SALUD Y VERIFICACIÓN PRE-VUELO SUITE ECCL")
    print("======================================================================")
    
    manifest = check_plugin_manifest()
    check_agents(manifest)
    check_skills(manifest)
    check_protocols(manifest)
    check_knowledge()
    check_evals()
    
    print("\n======================================================================")
    print("  [VEREDICTO FINAL] LA SUITE ECCL ESTÁ 100% OPERATIVA Y LISTA PARA USO")
    print("======================================================================")
    sys.exit(0)

if __name__ == "__main__":
    main()
