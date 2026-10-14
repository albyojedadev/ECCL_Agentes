#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Linter Determinista de Estilo Literario y Pedagógico de la ECCL.
Verifica:
1. Ausencia total de clichés sintéticos de inteligencia artificial.
2. Estructura bifásica inviolable (Informe Interno Técnico vs Comentario Externo Afectivo).
3. Saludo afectivo y cierre aforístico en la voz de Antonia Molinero.
4. Longitud media de oración y cadencia rítmica.
"""

import re
import sys
from typing import Dict, List, Any

FORBIDDEN_CLICHES = [
    r"\badéntrate\b",
    r"\badentrarse\b",
    r"\bsumergirse en\b",
    r"\bdesentrañar\b",
    r"\bfascinante\b",
    r"\bcautivador\b",
    r"\bcrisol\b",
    r"\btapiz\b",
    r"\bviaje transformador\b",
    r"\brecordatorio constante\b",
    r"\ben resumen\b",
    r"\ben conclusión\b",
    r"\bes importante recordar\b",
    r"\bes crucial destacar\b",
    r"\bvale la pena destacar\b",
    r"\bun halo de misterio\b",
    r"\bun torbellino de emociones\b",
    r"\bpaleta de emociones\b",
    r"\btestimonio elocuente\b",
    r"\bfaro de esperanza\b",
    r"\bsinfonía de sensaciones\b",
    r"\bun sinfín de\b",
    r"\bun mosaico de\b",
    r"\bun caleidoscopio de\b",
    r"\bno dudes en contactarme si tienes dudas\b",
    r"\bquedo a tu entera disposición\b"
]

def check_forbidden_cliches(text: str) -> List[str]:
    """Detecta clichés prohibidos de IA en el texto."""
    found = []
    for pattern in FORBIDDEN_CLICHES:
        matches = re.findall(pattern, text, flags=re.IGNORECASE)
        if matches:
            found.extend(matches)
    return list(set(found))

def check_biphasic_structure(critique_text: str) -> Dict[str, bool]:
    """Verifica la presencia nítida de Informe Interno y Comentario Externo."""
    has_internal = bool(re.search(r"(?:informe(?:\s+\w+)*\s+interno|fase\s*1|diagn[oó]stico\s+t[eé]cnico)", critique_text, re.IGNORECASE))
    has_external = bool(re.search(r"(?:comentario(?:\s+\w+)*\s+externo|fase\s*2|devoluci[oó]n(?:\s+\w+)*\s+al\s+alumno|carta\s+al\s+alumno)", critique_text, re.IGNORECASE))
    return {
        "has_internal_report": has_internal,
        "has_external_comment": has_external,
        "is_biphasic": has_internal and has_external
    }

def check_affectionate_opening(external_comment: str) -> bool:
    """Verifica que el comentario contenga una llamada afectiva al alumno por su nombre."""
    pattern = r"(?:^|\n)\s*(?:###.*?\n\s*)?(?:Querid[oa]\s+)?[A-ZÁÉÍÓÚÑ][a-zñáéíóú]+(?:\s+[A-ZÁÉÍÓÚÑ][a-zñáéíóú]+)?(?:\.{3}|,)\s*"
    return bool(re.search(pattern, external_comment))

def calculate_sentence_metrics(text: str) -> Dict[str, float]:
    """Calcula la longitud media de oración."""
    sentences = [s.strip() for s in re.split(r"[.!?]+", text) if len(s.strip()) > 3]
    if not sentences:
        return {"total_sentences": 0, "avg_words_per_sentence": 0.0}
    total_words = sum(len(s.split()) for s in sentences)
    avg_words = total_words / len(sentences)
    return {
        "total_sentences": len(sentences),
        "avg_words_per_sentence": round(avg_words, 2)
    }

def lint_pedagogical_critique(text: str) -> Dict[str, Any]:
    """Ejecuta la auditoría completa de estilo sobre una corrección literaria."""
    cliches = check_forbidden_cliches(text)
    biphasic = check_biphasic_structure(text)
    metrics = calculate_sentence_metrics(text)
    
    # Separar comentario externo si existe
    parts = re.split(r"(?:comentario\s+externo|fase\s*2|devoluci[oó]n\s+al\s+alumno)", text, flags=re.IGNORECASE)
    external_part = parts[-1] if len(parts) > 1 else text
    opening_ok = check_affectionate_opening(external_part)
    
    sentence_len_ok = 8.0 <= metrics["avg_words_per_sentence"] <= 26.0
    
    passed = (len(cliches) == 0) and biphasic["is_biphasic"] and opening_ok and sentence_len_ok
    
    return {
        "passed": passed,
        "score": 100 if passed else max(0, 100 - (len(cliches) * 20) - (0 if biphasic["is_biphasic"] else 30) - (0 if opening_ok else 15) - (0 if sentence_len_ok else 15)),
        "forbidden_cliches_detected": cliches,
        "biphasic_structure": biphasic,
        "affectionate_opening": opening_ok,
        "sentence_metrics": metrics
    }

if __name__ == "__main__":
    test_sample_bad = "Adéntrate en este viaje transformador. En resumen, es un fascinante tapiz de emociones. Quedo a tu entera disposición."
    test_sample_good = """
### 1. Informe Técnico Interno
- Diagnóstico: Conflicto claro en el diálogo de cocina, pero el final se diluye en explicaciones innecesarias.
- Nivel de concreción: Alto en la primera página (olor a café quemado, taza agrietada), bajo al cierre.
- Recomendación técnica: Cortar los últimos tres párrafos para que la imagen de la puerta cerrada selle el relato.

### 2. Comentario Externo para el Alumno
Elena... qué fuerza tiene esa mesa de formica con las dos tazas enfriándose. Tu historia ya está viva ahí, en el vapor que deja de subir y en la mirada que esquiva responder.
Confía en tu escena. No hace falta que nos expliques al final lo que sintieron: nosotros ya lo hemos visto temblar en las manos de tu protagonista. Corta justo cuando la llave gira en la cerradura. El relato crecerá el doble.
"""
    print("Probando caso inválido...")
    res_bad = lint_pedagogical_critique(test_sample_bad)
    print("Resultado caso inválido:", res_bad["passed"], "Score:", res_bad["score"], "Clichés:", res_bad["forbidden_cliches_detected"])
    assert not res_bad["passed"], "El caso inválido debió fallar."
    
    print("\nProbando caso válido estilo Antonia Molinero...")
    res_good = lint_pedagogical_critique(test_sample_good)
    print("Resultado caso válido:", res_good["passed"], "Score:", res_good["score"], "Métricas:", res_good["sentence_metrics"])
    assert res_good["passed"], "El caso válido debió pasar."
    print("\n[OK] Linter determinista de estilo ejecutado con éxito total.")
