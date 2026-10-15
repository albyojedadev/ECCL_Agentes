#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de Exportación y Adaptación para ChatGPT (OpenAI Custom GPTs).
Genera en `chatgpt_ready/` las configuraciones completas, instrucciones autocontenidas,
iniciadores de conversación y paquetes de archivos de conocimiento listos para copiar,
pegar y arrastrar al GPT Builder de ChatGPT.
También genera el archivo comprimido `dist/ECCL_ChatGPT_Pack.zip`.
"""

import os
import shutil
import zipfile
import json

REPO_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CHATGPT_DIR = os.path.join(REPO_DIR, "chatgpt_ready")
DIST_DIR = os.path.join(REPO_DIR, "dist")
KNOWLEDGE_DIR = os.path.join(REPO_DIR, "knowledge")

GPTS_CONFIG = [
    {
        "folder": "01_coordinador_agentes",
        "name": "Coordinador de agentes de la ECCL",
        "description": "Orquestador central y despacho de la suite de la Escuela Canaria de Creación Literaria. Orienta sobre qué asistente usar y modera el Consejo Maestro.",
        "agent_file": "agents/coordinador-de-agentes-de-la-eccl.md",
        "skills": ["catalogo-academico-eccl", "synthetic-audience-panel-eccl", "business-intelligence-cultural"],
        "knowledge_files": [
            ("catalogo", "cursos_activos.json"),
            ("catalogo", "claustro_docente.json")
        ],
        "conversation_starters": [
            "¿Qué asistente debo usar para corregir un relato de un alumno?",
            "¿Cuál es el mejor itinerario formativo para alguien que empieza a escribir?",
            "Quiero convocar al Consejo Maestro para evaluar el lanzamiento de un nuevo taller.",
            "¿Qué subvenciones culturales están abiertas actualmente en Canarias?"
        ],
        "capabilities": {"web_search": True, "code_interpreter": False, "dall_e": False}
    },
    {
        "folder": "02_analista_subvenciones",
        "name": "Analista de Subvenciones y Licitaciones",
        "description": "Especialista en ayudas públicas culturales (ICDC, Cabildos, GobCan, Ministerio, UE) y redacción técnica en Modo Copycat para la ECCL.",
        "agent_file": "agents/analista-de-subvenciones-y-licitaciones.md",
        "skills": ["cultural-grant-writer-es", "subvenciones-canarias-sync", "propuestas-b2b-culturales"],
        "knowledge_files": [
            ("catalogo", "cursos_activos.json"),
            ("catalogo", "claustro_docente.json")
        ],
        "conversation_starters": [
            "Analiza esta convocatoria del ICDC para proyectos de fomento lector.",
            "Redacta la memoria técnica para el proyecto de la Escuela Portátil.",
            "Estructura un cronograma trimestral y presupuesto menor a 15.000 € para el Cabildo.",
            "¿Qué términos clave del pliego debemos inyectar en Modo Copycat?"
        ],
        "capabilities": {"web_search": True, "code_interpreter": True, "dall_e": False}
    },
    {
        "folder": "03_analista_datos",
        "name": "Analista de Datos Culturales y Educativos",
        "description": "Business intelligence cultural: umbrales de apertura de grupos, break-even, costes y márgenes de contribución de la ECCL.",
        "agent_file": "agents/analista-de-datos-culturales-y-educativos.md",
        "skills": ["business-intelligence-cultural", "catalogo-academico-eccl"],
        "knowledge_files": [
            ("catalogo", "cursos_activos.json"),
            ("catalogo", "claustro_docente.json")
        ],
        "conversation_starters": [
            "Calcula el umbral mínimo de alumnos (break-even) para abrir este taller.",
            "Compara la rentabilidad entre el formato Presencial y Online Live para 20 plazas.",
            "¿Cuál es el impacto en tesorería de ofrecer pago fraccionado en 3 plazos?",
            "Analiza el histórico de matrículas y sugiere precio óptimo para el curso anual."
        ],
        "capabilities": {"web_search": False, "code_interpreter": True, "dall_e": False}
    },
    {
        "folder": "04_experto_escuela",
        "name": "Experto en la ECCL",
        "description": "Memoria institucional y consulta canónica de la Escuela Canaria de Creación Literaria: 73 cursos, 58 docentes, tarifas oficiales y 22 años de historia.",
        "agent_file": "agents/experto-en-la-eccl.md",
        "skills": ["catalogo-academico-eccl", "gestion-eventos-y-agenda-cultural"],
        "knowledge_files": [
            ("catalogo", "cursos_activos.json"),
            ("catalogo", "claustro_docente.json")
        ],
        "conversation_starters": [
            "¿Qué cursos de poesía o microrrelato hay disponibles este trimestre?",
            "¿Cuáles son los requisitos de acceso para el Curso Anual de Creación Literaria?",
            "Dime la biografía y especialidades docentes de Coriolano González Montañez.",
            "¿Qué incluye la matrícula de la Comunidad de Escritores Senior?"
        ],
        "capabilities": {"web_search": True, "code_interpreter": False, "dall_e": False}
    },
    {
        "folder": "05_consejo_alumnos",
        "name": "Consejo de alumnos sintéticos",
        "description": "Panel de simulación y focus group de 18 avatares reales representativos del alumnado de la ECCL. Evalúa cursos, precios y objeciones.",
        "agent_file": "agents/consejo-de-alumnos-sinteticos.md",
        "skills": ["synthetic-audience-panel-eccl", "lead-scoring-eccl"],
        "knowledge_files": [
            ("avatares", "panel_18_alumnos.json")
        ],
        "conversation_starters": [
            "Simula un focus group con el panel para evaluar este taller de autoficción a 180 €.",
            "¿Qué opinan Elisa y Santiago sobre un horario de clases los sábados por la mañana?",
            "Evalúa las principales objeciones de los alumnos ante el nuevo curso anual.",
            "Calcula el índice de aceptación global y la disposición a pagar (WTP) de la propuesta."
        ],
        "capabilities": {"web_search": False, "code_interpreter": True, "dall_e": False}
    },
    {
        "folder": "06_ghostwriter_antonia",
        "name": "Ghostwriter de Antonia Molinero",
        "description": "Voz autoral, ensayística íntima y estilo literario de Antonia Molinero para prólogos, cartas institucionales, artículos y manifiestos de la ECCL.",
        "agent_file": "agents/ghostwriter-de-antonia-molinero.md",
        "skills": ["antonia-molinero-voice", "verificacion-originalidad-y-voz-propia"],
        "knowledge_files": [
            ("estilos", "corpus_antonia.json")
        ],
        "conversation_starters": [
            "Escribe la carta de bienvenida para los alumnos del nuevo curso académico.",
            "Redacta el prólogo para la antología anual de relatos de la Escuela.",
            "Escribe un artículo de opinión cultural sobre el valor de nombrar lo doméstico en la literatura.",
            "Redacta una reflexión en tono de 'luminosa tierna' sobre la paciencia del que escribe."
        ],
        "capabilities": {"web_search": False, "code_interpreter": False, "dall_e": False}
    },
    {
        "folder": "07_critico_literario",
        "name": "Crítico Literario de la ECCL",
        "description": "Corrección pedagógica bifásica de textos literarios (Informe Técnico Interno + Comentario Externo Afectivo) según la metodología de Antonia Molinero.",
        "agent_file": "agents/critico-literario-de-la-eccl.md",
        "skills": ["critica-pedagogica-literaria", "verificacion-originalidad-y-voz-propia", "antonia-molinero-voice"],
        "knowledge_files": [
            ("estilos", "corpus_antonia.json")
        ],
        "conversation_starters": [
            "Corrige este relato de un alumno aplicando la estructura bifásica.",
            "Evalúa si este texto tiene desvío fértil respecto a la consigna de narrador testigo.",
            "Analiza si este fragmento cae en sobreexplicación emocional y cómo podarlo con calidez.",
            "Redacta el comentario para Elena destacando la fuerza de los objetos en su escena."
        ],
        "capabilities": {"web_search": False, "code_interpreter": False, "dall_e": False}
    },
    {
        "folder": "08_orientador_admisiones",
        "name": "Orientador de Admisiones y Alumnos",
        "description": "Triaje pedagógico, scoring de motivación y recomendación del itinerario formativo ideal en la ECCL según nivel, aspiraciones y disponibilidad.",
        "agent_file": "agents/orientador-de-admisiones-y-alumnos.md",
        "skills": ["lead-scoring-eccl", "orientacion-itinerarios-formativos", "catalogo-academico-eccl"],
        "knowledge_files": [
            ("catalogo", "cursos_activos.json"),
            ("catalogo", "claustro_docente.json")
        ],
        "conversation_starters": [
            "Un interesado escribe que quiere publicar su novela pero no tiene tiempo entre semana. ¿Qué le recomiendas?",
            "Calcula el scoring de este lead y clasifícalo (A, B o C).",
            "Explica a un candidato el proceso de selección y muestra de escritura para el curso anual.",
            "¿Qué diferencia hay entre Iniciación a la Creación y el Curso Anual de 50 horas?"
        ],
        "capabilities": {"web_search": True, "code_interpreter": False, "dall_e": False}
    },
    {
        "folder": "09_companero_escritura",
        "name": "Compañero de Escritura y Hábito",
        "description": "Tutor socrático y compañero creativo semanal de la ECCL. Facilita el desbloqueo narrativo mediante preguntas lúcidas y sostiene el hábito de escritura.",
        "agent_file": "agents/companero-de-escritura-y-habito.md",
        "skills": ["desbloqueo-creativo-socratico", "seguimiento-habito-escritura"],
        "knowledge_files": [
            ("estilos", "corpus_antonia.json")
        ],
        "conversation_starters": [
            "Estoy bloqueado en el nudo de mi relato y no sé qué decisión debe tomar el protagonista.",
            "Diseña un plan de escritura semanal de 20 minutos al día para una persona con poco tiempo.",
            "¿Cómo venzo la parálisis por perfeccionismo al escribir el primer borrador?",
            "Hazme 3 preguntas socráticas para profundizar en el conflicto silencioso de mi escena."
        ],
        "capabilities": {"web_search": False, "code_interpreter": False, "dall_e": False}
    },
    {
        "folder": "10_editor_libros",
        "name": "Editor de Libros y Antologías",
        "description": "Curaduría editorial, selección de relatos de alumnos, corrección ortotipográfica y maquetación de galeradas para imprenta (Ediciones Idea / Flamboyán).",
        "agent_file": "agents/editor-de-libros-y-antologias.md",
        "skills": ["curaduria-antologias-eccl", "verificacion-originalidad-y-voz-propia", "contratos-editoriales-y-derechos-autor"],
        "knowledge_files": [
            ("legal", "contratos_tipo_antologias.json")
        ],
        "conversation_starters": [
            "Estructura el orden armónico de estos 15 relatos para la antología anual.",
            "Revisa la ortotipografía de este diálogo conforme a las normas RAE (rayas, comillas latinas).",
            "Redacta la página de créditos legales y nota curatorial para la edición en imprenta.",
            "¿Cómo alternar los tonos emocionales de los textos para mantener la tensión lectora?"
        ],
        "capabilities": {"web_search": False, "code_interpreter": True, "dall_e": False}
    },
    {
        "folder": "11_dinamizador_comunidad",
        "name": "Dinamizador de Comunidad y Clubes de Lectura",
        "description": "Fidelización alumni, retos mensuales de escritura y coordinación de clubes de lectura guiados por Teresa Pulido en la ECCL.",
        "agent_file": "agents/dinamizador-de-comunidad-y-clubes.md",
        "skills": ["dinamizacion-comunidad-literaria", "gestion-eventos-y-agenda-cultural"],
        "knowledge_files": [
            ("catalogo", "cursos_activos.json")
        ],
        "conversation_starters": [
            "Diseña el enunciado del reto de escritura creativa para el próximo mes.",
            "Prepara una guía de lectura crítica con 5 preguntas de debate para la tertulia mensual.",
            "¿Cómo dinamizar el foro de la Comunidad de Escritores Senior para fomentar el feedback respetuoso?",
            "Redacta una convocatoria para el encuentro presencial y online de antiguos alumnos."
        ],
        "capabilities": {"web_search": False, "code_interpreter": False, "dall_e": False}
    },
    {
        "folder": "12_asesor_propiedad_intelectual",
        "name": "Asesor de Propiedad Intelectual y Contratos",
        "description": "Consultoría legal autoral: contratos de cesión no exclusiva para antologías de la ECCL, Agencia Literaria AM y cumplimiento de RGPD juvenil.",
        "agent_file": "agents/asesor-de-propiedad-intelectual.md",
        "skills": ["contratos-editoriales-y-derechos-autor"],
        "knowledge_files": [
            ("legal", "contratos_tipo_antologias.json"),
            ("legal", "rgpd_juveniles.json")
        ],
        "conversation_starters": [
            "Redacta un contrato de cesión no exclusiva para un relato seleccionado en la antología.",
            "¿Qué cláusulas RGPD debemos incluir para el Taller de Jóvenes Escritores (menores de edad)?",
            "Un alumno pregunta si pierde sus derechos al publicar en el libro de la Escuela. ¿Qué responderle?",
            "Revisa este borrador de acuerdo de representación para la Agencia Literaria AM."
        ],
        "capabilities": {"web_search": False, "code_interpreter": False, "dall_e": False}
    },
    {
        "folder": "13_soporte_aula_virtual",
        "name": "Asistente de Soporte y Aula Virtual",
        "description": "Atención técnica al alumno: resolución de incidencias en Zoom, acceso a grabaciones, pasarela de pago y entregas en el campus virtual de la ECCL.",
        "agent_file": "agents/asistente-de-soporte-y-aula-virtual.md",
        "skills": ["soporte-tecnico-aula-virtual"],
        "knowledge_files": [
            ("catalogo", "cursos_activos.json")
        ],
        "conversation_starters": [
            "Un alumno no puede entrar a la sala de Zoom porque le pide contraseña. ¿Cómo resolverlo?",
            "¿Dónde y cómo pueden acceder a las grabaciones en diferido los alumnos ausentes?",
            "Explica los pasos para abonar el curso mediante transferencia bancaria o pago fraccionado.",
            "Instrucciones paso a paso para subir un relato al campus virtual antes del día 15."
        ],
        "capabilities": {"web_search": False, "code_interpreter": False, "dall_e": False}
    },
    {
        "folder": "14_comunicacion_prensa",
        "name": "Responsable de Comunicación y Prensa",
        "description": "Comunicación periodística, notas de prensa en pirámide invertida y dossiers culturales para medios insulares, radios y librerías de la ECCL.",
        "agent_file": "agents/responsable-de-comunicacion-y-prensa.md",
        "skills": ["press-release-cultural-es", "dossier-cultural-generator", "guion-reels-y-pildoras-literarias"],
        "knowledge_files": [
            ("catalogo", "cursos_activos.json"),
            ("catalogo", "claustro_docente.json")
        ],
        "conversation_starters": [
            "Redacta una nota de prensa cultural anunciando la apertura de matrícula del nuevo curso anual.",
            "Prepara un dossier de presentación de la Escuela para la Feria del Libro.",
            "Elabora una nota breve sobre el premio literario obtenido por uno de nuestros docentes.",
            "¿Cuáles son los contactos y medios clave para la difusión cultural en Tenerife y Canarias?"
        ],
        "capabilities": {"web_search": True, "code_interpreter": False, "dall_e": False}
    },
    {
        "folder": "15_proyectos_b2b",
        "name": "Gestor de Proyectos Institucionales y B2B",
        "description": "Diseño de propuestas formativas a medida para centros educativos (CEP), ayuntamientos, cabildos y talleres de la Escuela Portátil.",
        "agent_file": "agents/gestor-de-proyectos-institucionales-y-b2b.md",
        "skills": ["propuestas-b2b-culturales", "gestion-eventos-y-agenda-cultural"],
        "knowledge_files": [
            ("catalogo", "cursos_activos.json"),
            ("catalogo", "claustro_docente.json")
        ],
        "conversation_starters": [
            "Diseña una propuesta técnica para un taller de fomento lector en un instituto de secundaria.",
            "Prepara el proyecto 'Escuela Portátil' para presentarlo al Área de Cultura de un ayuntamiento.",
            "Estructura un taller intensivo de oratoria y hablar en público para una entidad cultural.",
            "Desglosa la propuesta económica y logística para un ciclo de 4 sesiones formativas."
        ],
        "capabilities": {"web_search": False, "code_interpreter": True, "dall_e": False}
    },
    {
        "folder": "16_disenador_grafico",
        "name": "Diseñador Gráfico y Cartelería",
        "description": "Maquetación publicitaria de carteles A3/A4, posts de Instagram, Stories y banners web respetando la identidad visual editorial de la ECCL.",
        "agent_file": "agents/disenador-grafico-y-carteleria.md",
        "skills": ["diseno-carteleria-y-redes-eccl", "adaptacion-formatos-graficos-eccl", "supervision-identidad-visual-eccl"],
        "knowledge_files": [
            ("branding", "paleta_corporativa.json"),
            ("branding", "tipografias.json")
        ],
        "conversation_starters": [
            "Diseña el cartel A3 y el post de Instagram para el Taller Hablar en Público de Jorge Soriano.",
            "Maqueta una creatividad para Stories (9:16) respetando las safe zones perimetrales.",
            "Genera el copy persuasivo y las directrices visuales para anunciar el Curso Anual en redes.",
            "Indica la jerarquía tipográfica y paleta HEX para un carrusel de 5 diapositivas en Instagram."
        ],
        "capabilities": {"web_search": False, "code_interpreter": True, "dall_e": True}
    },
    {
        "folder": "17_guardian_marca",
        "name": "Guardián de Marca e Identidad Visual",
        "description": "Auditoría estética y control de marca de la ECCL: validación determinista de colores HEX, tipografías autorizadas y descarte de clichés de stock de IA.",
        "agent_file": "agents/guardian-de-marca-e-identidad-visual.md",
        "skills": ["supervision-identidad-visual-eccl", "adaptacion-formatos-graficos-eccl"],
        "knowledge_files": [
            ("branding", "paleta_corporativa.json"),
            ("branding", "tipografias.json")
        ],
        "conversation_starters": [
            "Audita esta propuesta gráfica y verifica si cumple la paleta cromática oficial.",
            "¿Esta tipografía y composición respeta los principios editoriales de la Escuela?",
            "Detecta si este prompt para imagen contiene clichés de stock prohibidos (plumas doradas, etc.).",
            "Emite un dictamen formal de aprobación o rechazo para esta creatividad publicitaria."
        ],
        "capabilities": {"web_search": False, "code_interpreter": True, "dall_e": False}
    }
]

def compile_instructions(agent_file, skills_list):
    """Compila el prompt base del agente junto con el texto de sus skills en un único prompt autocontenido para ChatGPT."""
    with open(os.path.join(REPO_DIR, agent_file), "r", encoding="utf-8") as f:
        agent_raw = f.read()
    
    # Quitar el frontmatter YAML para ChatGPT
    if agent_raw.startswith("---"):
        parts = agent_raw.split("---", 2)
        if len(parts) >= 3:
            agent_body = parts[2].strip()
        else:
            agent_body = agent_raw
    else:
        agent_body = agent_raw

    compiled_skills = []
    for sk in skills_list:
        sk_path = os.path.join(REPO_DIR, "skills", sk, "SKILL.md")
        if os.path.exists(sk_path):
            with open(sk_path, "r", encoding="utf-8") as sk_fp:
                sk_raw = sk_fp.read()
                if sk_raw.startswith("---"):
                    sk_parts = sk_raw.split("---", 2)
                    sk_body = sk_parts[2].strip() if len(sk_parts) >= 3 else sk_raw
                else:
                    sk_body = sk_raw
                compiled_skills.append(f"### HABILIDAD INTEGRADA: {sk}\n{sk_body}")

    skills_text = "\n\n---\n\n".join(compiled_skills)
    
    footer = """
---
## REGLAS GENERALES Y GUARDRAILS ECCL:
1. FUENTE CANÓNICA: La información de cursos, claustro y tarifas se valida contra escuelaliteraria.com y los archivos de conocimiento adjuntos en Knowledge.
2. CERO CLICHÉS DE IA: Prohibido usar palabras artificiales como 'fascinante', 'adéntrate', 'crisol', 'tapiz', 'viaje transformador', 'en conclusión'.
3. PEDAGOGÍA DEL AFECTO: Mantener siempre la calidez, la precisión técnica y el respeto profundo al proceso creativo.
"""
    return f"{agent_body}\n\n---\n\n## PROCEDIMIENTOS Y HABILIDADES DISPONIBLES:\n{skills_text}\n{footer}"

def build_chatgpt_ready():
    print("Iniciando exportación para ChatGPT...")
    os.makedirs(CHATGPT_DIR, exist_ok=True)
    os.makedirs(DIST_DIR, exist_ok=True)

    summary_list = []

    for cfg in GPTS_CONFIG:
        target_dir = os.path.join(CHATGPT_DIR, cfg["folder"])
        knowledge_target_dir = os.path.join(target_dir, "knowledge")
        os.makedirs(knowledge_target_dir, exist_ok=True)

        instructions = compile_instructions(cfg["agent_file"], cfg["skills"])

        # 1. Guardar INSTRUCCIONES.txt (para copiar y pegar en Instructions de ChatGPT)
        with open(os.path.join(target_dir, "INSTRUCCIONES_CHATGPT.txt"), "w", encoding="utf-8") as f:
            f.write(instructions)

        # 2. Guardar FICHA_CONFIGURACION.md (guía visual para el creador)
        knowledge_names = [f[1] for f in cfg["knowledge_files"]]
        ficha_md = f"""# 📋 Ficha de Configuración para ChatGPT GPT Builder
## Asistente: {cfg["name"]}

### 1. Pestaña "Create" / "Configure"
* **Name:** `{cfg["name"]}`
* **Description:** `{cfg["description"]}`
* **Instructions:** (Copiar íntegramente el contenido del archivo adjunto `INSTRUCCIONES_CHATGPT.txt`)

### 2. Conversation Starters (Iniciadores de conversación)
1. `{cfg["conversation_starters"][0]}`
2. `{cfg["conversation_starters"][1]}`
3. `{cfg["conversation_starters"][2]}`
4. `{cfg["conversation_starters"][3]}`

### 3. Knowledge (Archivos de Conocimiento a Subir)
Arrastra y suelta en la sección **Knowledge** los siguientes archivos ubicados en la carpeta `knowledge/`:
{chr(10).join([f"- `{kf}`" for kf in knowledge_names])}

### 4. Capabilities (Capacidades)
* **Web Search:** {"[X] Activado" if cfg["capabilities"]["web_search"] else "[ ] Desactivado"}
* **Code Interpreter:** {"[X] Activado" if cfg["capabilities"]["code_interpreter"] else "[ ] Desactivado"}
* **DALL-E Image Generation:** {"[X] Activado" if cfg["capabilities"]["dall_e"] else "[ ] Desactivado"}
"""
        with open(os.path.join(target_dir, "FICHA_CONFIGURACION.md"), "w", encoding="utf-8") as f:
            f.write(ficha_md)

        # 3. Copiar los archivos de conocimiento específicos a su carpeta knowledge/
        for cat, fname in cfg["knowledge_files"]:
            src_file = os.path.join(KNOWLEDGE_DIR, cat, fname)
            dst_file = os.path.join(knowledge_target_dir, fname)
            if os.path.exists(src_file):
                shutil.copy2(src_file, dst_file)

        summary_list.append({
            "folder": cfg["folder"],
            "name": cfg["name"],
            "description": cfg["description"],
            "knowledge_count": len(cfg["knowledge_files"])
        })
        print(f"  [OK] Exportado para ChatGPT: {cfg['name']} -> chatgpt_ready/{cfg['folder']}/")

    # 4. Crear Guía de Instalación Rápida para el Cliente en chatgpt_ready/
    guia_md = """# 🚀 Guía de Instalación de Asistentes en ChatGPT (Paso a Paso)
### Escuela Canaria de Creación Literaria (ECCL)

Esta carpeta contiene todo lo necesario para crear o actualizar los **17 asistentes de la Escuela** en tu cuenta de ChatGPT (ChatGPT Plus, Team o Enterprise) en menos de 2 minutos por asistente.

---

## 🛠️ ¿Cómo instalar un Asistente en ChatGPT?

Para cada asistente que desees tener en tu barra lateral de ChatGPT:

1. **Abre el editor de GPTs en ChatGPT:**  
   Ve a [https://chatgpt.com/gpts/editor](https://chatgpt.com/gpts/editor) (o haz clic en tu nombre -> *My GPTs* -> *Create a GPT*).
2. **Selecciona la pestaña "Configure"** (en la parte superior).
3. **Abre la carpeta del asistente que quieras instalar** (por ejemplo, `07_critico_literario`).
4. **Copia los datos de la `FICHA_CONFIGURACION.md`:**
   - Pega el **Name** (Nombre).
   - Pega la **Description** (Descripción corta).
   - Abre `INSTRUCCIONES_CHATGPT.txt`, copia todo su contenido y pégalo en la casilla **Instructions**.
   - Copia los 4 **Conversation starters** (preguntas sugeridas).
5. **Sube los archivos de conocimiento:**
   - En la sección **Knowledge**, haz clic en *Upload files* y selecciona los archivos que están dentro de la subcarpeta `knowledge/` de ese asistente.
6. **Activa las casillas de Capabilities:**
   - Según lo indicado en la ficha (Web Search, Code Interpreter o DALL-E).
7. **Guarda el asistente:**
   - Haz clic en el botón verde **Save** (o *Update*) arriba a la derecha. Puedes guardarlo como *Only me* (Privado) o *Anyone with a link* (para compartirlo con tu equipo o alumnos).

¡Listo! El asistente estará activo y disponible en tu ChatGPT.
"""
    with open(os.path.join(CHATGPT_DIR, "GUIA_INSTALACION_CHATGPT.md"), "w", encoding="utf-8") as f:
        f.write(guia_md)

    # 5. Comprimir todo en dist/ECCL_ChatGPT_Pack.zip
    zip_path = os.path.join(DIST_DIR, "ECCL_ChatGPT_Pack.zip")
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(CHATGPT_DIR):
            for file in files:
                abs_path = os.path.join(root, file)
                rel_path = os.path.relpath(abs_path, REPO_DIR)
                zipf.write(abs_path, rel_path)
    print(f"\n[ÉXITO] Paquete zip descargable generado en: {zip_path}")

if __name__ == "__main__":
    build_chatgpt_ready()
