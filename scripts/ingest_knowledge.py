#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de ingesta, normalización y tipado del Corpus Canónico para la Escuela Canaria de Creación Literaria.
Convierte las fuentes de GPTs (CSV, JSON, Markdown) en JSON canónicos validados en `knowledge/`.
"""

import os
import csv
import json

BASE_DIR = r"D:\PROYECTOS\Escuela Canaria de Creación Literaria"
GPTS_DIR = os.path.join(BASE_DIR, "GPTs")
REPO_DIR = os.path.join(BASE_DIR, "Repositorio de agentes")
KNOWLEDGE_DIR = os.path.join(REPO_DIR, "knowledge")

def ingest_catalogo_cursos():
    csv_path = os.path.join(GPTS_DIR, "03 Experto de la escuela", "inventario_cursos.csv")
    cursos = []
    with open(csv_path, mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            cursos.append({
                "id_curso": row.get("id_curso", "").strip(),
                "nombre": row.get("nombre_curso", "").strip(),
                "modalidad": row.get("modalidad", "").strip(),
                "categoria": row.get("categoria", "").strip(),
                "duracion_horas": row.get("duracion_horas", "").strip(),
                "precio_min": row.get("precio_min", "").strip(),
                "precio_max": row.get("precio_max", "").strip(),
                "profesor_principal": row.get("profesor_principal", "").strip(),
                "profesores_invitados": [p.strip() for p in row.get("profesores_invitados", "").split(",") if p.strip()],
                "fecha_inicio": row.get("fecha_inicio", "").strip(),
                "fecha_fin": row.get("fecha_fin", "").strip(),
                "horario": row.get("horario", "").strip(),
                "publico_objetivo": row.get("publico_objetivo", "").strip(),
                "capacidad_plazas": row.get("capacidad_plazas", "").strip(),
                "estado": row.get("estado", "").strip(),
                "url_canonica": row.get("url_referencia", "").strip(),
                "observaciones": row.get("observaciones", "").strip()
            })
    out_path = os.path.join(KNOWLEDGE_DIR, "catalogo", "cursos_activos.json")
    with open(out_path, mode="w", encoding="utf-8") as f:
        json.dump({"total_cursos": len(cursos), "fuente_canonica": "https://www.escuelaliteraria.com/", "cursos": cursos}, f, ensure_ascii=False, indent=2)
    print(f"Cursos procesados: {len(cursos)} -> {out_path}")

def ingest_claustro_docente():
    csv_path = os.path.join(GPTS_DIR, "03 Experto de la escuela", "docentes.csv")
    docentes = []
    with open(csv_path, mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            docentes.append({
                "id_docente": row.get("id_docente", "").strip(),
                "nombre_completo": row.get("nombre_completo", "").strip(),
                "tipo_docente": row.get("tipo_docente", "").strip(),
                "especialidades": [e.strip() for e in row.get("especialidades", "").split(",") if e.strip()],
                "cursos_imparte": [c.strip() for c in row.get("cursos_imparte", "").split(",") if c.strip()],
                "disponibilidad": row.get("disponibilidad", "").strip(),
                "experiencia_anos": row.get("experiencia_anos", "").strip(),
                "premios_reconocimientos": row.get("premios_reconocimientos", "").strip(),
                "bio_breve": row.get("bio_breve", "").strip(),
                "url_canonica": row.get("url_referencia", "").strip(),
                "redes_sociales": row.get("redes_sociales", "").strip(),
                "observaciones": row.get("observaciones", "").strip()
            })
    out_path = os.path.join(KNOWLEDGE_DIR, "catalogo", "claustro_docente.json")
    with open(out_path, mode="w", encoding="utf-8") as f:
        json.dump({"total_docentes": len(docentes), "fuente_canonica": "https://www.escuelaliteraria.com/profesores/", "docentes": docentes}, f, ensure_ascii=False, indent=2)
    print(f"Docentes procesados: {len(docentes)} -> {out_path}")

def ingest_avatares():
    src_path = os.path.join(GPTS_DIR, "04 Consejo de alumnos", "avatares_maestro.json")
    with open(src_path, mode="r", encoding="utf-8") as f:
        data = json.load(f)
    out_path = os.path.join(KNOWLEDGE_DIR, "avatares", "panel_18_alumnos.json")
    with open(out_path, mode="w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"Panel 18 avatares transferido -> {out_path}")

def ingest_estilos():
    mod_path = os.path.join(GPTS_DIR, "06 Critico Literario", "modulo_deteccion_antoniamolinero.json")
    var_path = os.path.join(GPTS_DIR, "05 Ghostwriter", "variante_estilo_emocional.json")
    manual_path = os.path.join(GPTS_DIR, "05 Ghostwriter", "manual_de_estilo.md")
    
    with open(mod_path, mode="r", encoding="utf-8") as f:
        modulo_deteccion = json.load(f)
    with open(var_path, mode="r", encoding="utf-8") as f:
        variantes_emocionales = json.load(f)
    with open(manual_path, mode="r", encoding="utf-8") as f:
        manual_texto = f.read()
        
    corpus = {
        "autor": "Antonia Molinero",
        "institucion": "Escuela Canaria de Creación Literaria",
        "ejes_estilisticos": [
            "Concreción sensorial absoluta (objetos con peso, microacciones, texturas).",
            "Conflicto encarnado y latente, nunca explicado ni discursivo.",
            "Voz íntima, vulnerable y honesta; huida radical de la impostación o barroquismo.",
            "Emoción sugerida y no sentimentalista (sin autocompasión).",
            "Estructura en escenas con movimiento y puentes fluidos.",
            "Riesgo formal y emocional sin pudores protectores.",
            "Finales resonantes por imagen poética o gesto revelador.",
            "Pedagogía del afecto: la exigencia técnica más rigurosa envuelta en calidez.",
            "Cero clichés sintéticos de inteligencia artificial."
        ],
        "modulo_deteccion": modulo_deteccion.get("modulo_deteccion_antoniamolinero", {}),
        "variantes_emocionales": variantes_emocionales,
        "resumen_manual_estilo": manual_texto[:4000]
    }
    out_path = os.path.join(KNOWLEDGE_DIR, "estilos", "corpus_antonia.json")
    with open(out_path, mode="w", encoding="utf-8") as f:
        json.dump(corpus, f, ensure_ascii=False, indent=2)
    print(f"Corpus estilístico Antonia Molinero generado -> {out_path}")

def ingest_branding():
    paleta = {
        "nombre_marca": "Escuela Canaria de Creación Literaria",
        "acronimo": "ECCL",
        "url_oficial": "https://www.escuelaliteraria.com/",
        "colores_principales": {
            "marfil_fondo": {
                "hex": "#FAF8F5",
                "rgb": [250, 248, 245],
                "uso": "Fondos de carruseles, papel editorial, fondos web y cartelería",
                "rol": "Background primario"
            },
            "tinta_texto": {
                "hex": "#1A1A1A",
                "rgb": [26, 26, 26],
                "uso": "Texto principal, títulos oscuros, trazos y logotipos",
                "rol": "Foreground primario (legibilidad máxima)"
            },
            "terracota_canario": {
                "hex": "#C2593F",
                "rgb": [194, 89, 63],
                "uso": "Acentos, botones primarios, llamadas a la acción, fechas y marcos",
                "rol": "Color de acento institucional cálido"
            },
            "azul_atlantico": {
                "hex": "#1E3A5F",
                "rgb": [30, 58, 95],
                "uso": "Fondos de banners institucionales, firmas solemnes, textos secundarios y pie de cartel",
                "rol": "Color corporativo de contraste sereno"
            },
            "dorado_editorial": {
                "hex": "#D4A346",
                "rgb": [212, 163, 70],
                "uso": "Detalles premium, antologías, sellos conmemorativos de 22 años",
                "rol": "Acento de distinción"
            }
        },
        "colores_prohibidos": [
            "#FF00FF", "#00FF00", "#00FFFF", "#FFFF00",
            "Degradados fluorescentes o neon",
            "Gris corporativo frío de software SaaS (#E2E8F0, #F1F5F9)"
        ],
        "safe_zones": {
            "instagram_post": {"ancho": 1080, "alto": 1080, "margen_seguro": 80},
            "instagram_story": {"ancho": 1080, "alto": 1920, "margen_superior": 250, "margen_inferior": 250, "margen_lateral": 60},
            "cartel_a3_a4": {"proporcion": "1:1.414", "sangrado_impresion_mm": 3, "margen_texto_mm": 15}
        }
    }
    paleta_path = os.path.join(KNOWLEDGE_DIR, "branding", "paleta_corporativa.json")
    with open(paleta_path, mode="w", encoding="utf-8") as f:
        json.dump(paleta, f, ensure_ascii=False, indent=2)
    print(f"Paleta corporativa generada -> {paleta_path}")

    tipografias = {
        "editorial_titulares": {
            "familia_primaria": "Playfair Display",
            "familia_alternativa": "Merriweather",
            "clasificacion": "Serif clásica con contraste",
            "pesos_autorizados": ["Bold (700)", "Black (900)", "Italic (400i)"],
            "uso": "Titulares de cartel, portadas de antologías, nombres de cursos destacados",
            "tracking": "-0.02em"
        },
        "cuerpo_lectura": {
            "familia_primaria": "Inter",
            "familia_alternativa": "Open Sans",
            "clasificacion": "Sans-serif geométrica humanista",
            "pesos_autorizados": ["Regular (400)", "Medium (500)", "SemiBold (600)"],
            "uso": "Fechas, horarios, descripción de talleres, claustro docente, textos de pie",
            "interlineado_recomendado": "1.45"
        },
        "reglas_inviolables": [
            "Nunca usar más de dos familias tipográficas en una misma pieza gráfica.",
            "Prohibido el uso de Comic Sans, Papyrus, Lobster o fuentes script de boda.",
            "Jerarquía obligatoria: 1) Título literario (Serif) -> 2) Docente / Fechas (Sans) -> 3) Llamada a la acción / Web."
        ]
    }
    tipo_path = os.path.join(KNOWLEDGE_DIR, "branding", "tipografias.json")
    with open(tipo_path, mode="w", encoding="utf-8") as f:
        json.dump(tipografias, f, ensure_ascii=False, indent=2)
    print(f"Especificación tipográfica generada -> {tipo_path}")

def ingest_legal():
    contrato_antologias = {
        "tipo_documento": "Contrato de Cesión No Exclusiva de Derechos de Reproducción para Antología Colectiva",
        "partes": {
            "editor": "Escuela Canaria de Creación Literaria S.L. / Ediciones Idea / Servicio Editorial Flamboyán",
            "autor": "Alumno / Autor del relato o poema seleccionado"
        },
        "clausulas_clave": [
            "La cesión de derechos sobre la obra es de carácter NO EXCLUSIVO y limitada exclusivamente a la edición física y/o digital de la antología del curso.",
            "El autor conserva en todo momento la titularidad moral y patrimonial de su obra y puede publicarla en libros individuales o futuras publicaciones.",
            "No existe contraprestación económica dineraria; el autor recibe ejemplares de cortesía fijados en la convocatoria.",
            "La Escuela se compromete a respetar la integridad del texto y consignar el nombre o seudónimo del autor en la portada, índice y página correspondiente."
        ],
        "jurisdiccion": "Juzgados y Tribunales de Santa Cruz de Tenerife / San Cristóbal de La Laguna (Canarias, España)."
    }
    contrato_path = os.path.join(KNOWLEDGE_DIR, "legal", "contratos_tipo_antologias.json")
    with open(contrato_path, mode="w", encoding="utf-8") as f:
        json.dump(contrato_antologias, f, ensure_ascii=False, indent=2)
    print(f"Contrato tipo antologías generado -> {contrato_path}")

    rgpd_juveniles = {
        "tipo_documento": "Protocolo RGPD y Autorización Expresa de Menores de Edad",
        "normativa_aplicable": "Reglamento (UE) 2016/679 (RGPD) y Ley Orgánica 3/2018 (LOPDGDD - España)",
        "requisitos_obligatorios": [
            "Para menores de 14 años, consentimiento firmado obligatorio de ambos progenitores o tutor legal.",
            "Para jóvenes entre 14 y 17 años (Taller de Jóvenes Escritores), consentimiento del alumno avalado por el tutor.",
            "Finalidad exclusiva: gestión docente, aula virtual Zoom, envío de materiales didácticos y avisos de horarios.",
            "Derecho a la propia imagen: autorización separada e independiente para fotos grupales en redes o publicaciones."
        ],
        "responsable_tratamiento": "Escuela Canaria de Creación Literaria (info@escuelaliteraria.com)"
    }
    rgpd_path = os.path.join(KNOWLEDGE_DIR, "legal", "rgpd_juveniles.json")
    with open(rgpd_path, mode="w", encoding="utf-8") as f:
        json.dump(rgpd_juveniles, f, ensure_ascii=False, indent=2)
    print(f"Protocolo RGPD juveniles generado -> {rgpd_path}")

if __name__ == "__main__":
    print("Iniciando ingesta del Corpus Canónico ECCL...")
    ingest_catalogo_cursos()
    ingest_claustro_docente()
    ingest_avatares()
    ingest_estilos()
    ingest_branding()
    ingest_legal()
    print("Ingesta completada con éxito.")
