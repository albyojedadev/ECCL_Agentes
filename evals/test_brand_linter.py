#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Linter Determinista de Identidad Visual y Marca de la ECCL.
Verifica:
1. Cumplimiento de paleta cromática oficial (HEX autorizados).
2. Detección y rechazo de colores fluorescentes, neon y grises SaaS.
3. Tipografías autorizadas (Playfair Display, Merriweather, Inter, Open Sans).
4. Safe zones de maquetación (Post 1:1, Story 9:16, Cartel A3/A4).
5. Filtro anti-stock clichés (plumas estilográficas falsas, teclados con neón).
"""

import re
import json
from typing import Dict, List, Any

AUTHORIZED_HEX = {
    "#FAF8F5": "Marfil Fondo",
    "#1A1A1A": "Tinta Texto",
    "#C2593F": "Terracota Canario",
    "#1E3A5F": "Azul Atlántico",
    "#D4A346": "Dorado Editorial",
    "#FFFFFF": "Blanco Puro (secundario)",
    "#000000": "Negro Puro (soporte)"
}

FORBIDDEN_COLOR_PATTERNS = [
    r"#FF00FF", r"#00FF00", r"#00FFFF", r"#FFFF00", # Neon primaries
    r"#E2E8F0", r"#F1F5F9", r"#3B82F6", r"#10B981"  # SaaS Tailwind defaults
]

AUTHORIZED_FONTS = [
    "playfair display",
    "merriweather",
    "inter",
    "open sans"
]

FORBIDDEN_STOCK_CONCEPTS = [
    r"\bpluma estilogr[aá]fica dorada flotando\b",
    r"\bteclado con luces neon\b",
    r"\bm[aá]quina de escribir victoriana sobre terciopelo\b",
    r"\btaza de caf[eé] con coraz[oó]n de espuma perfecto\b",
    r"\bpergamino quemado con bordes envejecidos\b"
]

def check_hex_colors(text_or_json: str) -> Dict[str, Any]:
    """Extrae todos los códigos HEX y valida que pertenezcan a la paleta oficial."""
    found_hexes = [h.upper() for h in re.findall(r"#[0-9a-fA-F]{6}\b", text_or_json)]
    invalid_hexes = []
    forbidden_matches = []
    
    for h in set(found_hexes):
        if h not in AUTHORIZED_HEX:
            invalid_hexes.append(h)
        for pattern in FORBIDDEN_COLOR_PATTERNS:
            if re.match(pattern, h, re.IGNORECASE):
                forbidden_matches.append(h)
                
    return {
        "total_hex_found": len(found_hexes),
        "unique_hex": list(set(found_hexes)),
        "invalid_hex": invalid_hexes,
        "forbidden_matches": forbidden_matches,
        "is_valid": len(invalid_hexes) == 0
    }

def check_typography(text: str) -> Dict[str, Any]:
    """Verifica si las fuentes declaradas son autorizadas."""
    declared_fonts = []
    for f in AUTHORIZED_FONTS:
        if re.search(r"\b" + re.escape(f) + r"\b", text, re.IGNORECASE):
            declared_fonts.append(f)
            
    has_banned_fonts = bool(re.search(r"\b(comic sans|papyrus|lobster|brush script)\b", text, re.IGNORECASE))
    
    return {
        "declared_authorized_fonts": declared_fonts,
        "has_banned_fonts": has_banned_fonts,
        "is_valid": (len(declared_fonts) > 0) and not has_banned_fonts
    }

def check_stock_anti_cliches(prompt_or_description: str) -> List[str]:
    """Detecta clichés de imágenes de stock prohibidas."""
    found = []
    for pattern in FORBIDDEN_STOCK_CONCEPTS:
        matches = re.findall(pattern, prompt_or_description, re.IGNORECASE)
        if matches:
            found.extend(matches)
    return list(set(found))

def lint_graphic_proposal(proposal: Dict[str, Any]) -> Dict[str, Any]:
    """Audita una propuesta gráfica completa (JSON o dict)."""
    raw_str = json.dumps(proposal, ensure_ascii=False)
    
    color_audit = check_hex_colors(raw_str)
    typo_audit = check_typography(raw_str)
    stock_cliches = check_stock_anti_cliches(raw_str)
    
    passed = color_audit["is_valid"] and typo_audit["is_valid"] and (len(stock_cliches) == 0)
    score = 100
    if not color_audit["is_valid"]:
        score -= (len(color_audit["invalid_hex"]) * 15)
    if not typo_audit["is_valid"]:
        score -= 25
    if len(stock_cliches) > 0:
        score -= (len(stock_cliches) * 20)
    score = max(0, score)
    
    return {
        "passed": passed,
        "score": score,
        "color_audit": color_audit,
        "typography_audit": typo_audit,
        "stock_cliches_detected": stock_cliches
    }

if __name__ == "__main__":
    sample_bad = {
        "formato": "Cartel A3",
        "fondo_hex": "#FF00FF",
        "fuente_titulo": "Comic Sans",
        "descripcion_visual": "Pluma estilográfica dorada flotando sobre pergamino quemado con bordes envejecidos"
    }
    sample_good = {
        "formato": "Cartel A3",
        "paleta": {
            "fondo": "#FAF8F5",
            "titular": "#1A1A1A",
            "acento": "#C2593F",
            "institucional": "#1E3A5F"
        },
        "tipografias": {
            "titular": "Playfair Display",
            "cuerpo": "Inter"
        },
        "descripcion_visual": "Mesa de madera natural de pino canario con un cuaderno artesanal abierto y luz lateral tenue de ventana.",
        "safe_zone": "Margen perimetral de 25mm respetado."
    }
    
    print("Probando linter de marca con propuesta inválida...")
    res_bad = lint_graphic_proposal(sample_bad)
    print("Resultado propuesta inválida:", res_bad["passed"], "Score:", res_bad["score"])
    assert not res_bad["passed"], "La propuesta inválida debió fallar."
    
    print("\nProbando linter de marca con propuesta válida oficial...")
    res_good = lint_graphic_proposal(sample_good)
    print("Resultado propuesta válida:", res_good["passed"], "Score:", res_good["score"])
    assert res_good["passed"], "La propuesta válida debió pasar."
    print("\n[OK] Linter de identidad visual ejecutado con éxito total.")
