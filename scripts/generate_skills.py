#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de generación automatizada de las 24 Skills de la suite ECCL.
Crea cada carpeta en skills/<nombre>/ y su correspondiente SKILL.md conforme al estándar Antigravity.
"""

import os

REPO_DIR = r"D:\PROYECTOS\Escuela Canaria de Creación Literaria\Repositorio de agentes"
SKILLS_DIR = os.path.join(REPO_DIR, "skills")

SKILLS_DEFINITIONS = [
    {
        "id": "critica-pedagogica-literaria",
        "name": "critica-pedagogica-literaria",
        "description": "Procedimiento maestro de corrección pedagógica bifásica de textos literarios (Informe Técnico Interno + Comentario Externo Afectivo) según la metodología de Antonia Molinero.",
        "content": """# 📖 Skill: Crítica Pedagógica Literaria
### Procedimiento Maestro de Corrección Bifásica de Textos

## 🎯 1. Objetivo
Guiar la corrección pedagógica de relatos, fragmentos de novela y poemas de alumnos garantizando el doble análisis: rigor técnico interno sin censura y devolución externa cercana, afectiva y constructiva.

## 📥 2. Entradas Requeridas
- `texto_alumno`: Manuscrito entregado por el estudiante.
- `nombre_alumno`: Nombre de pila del alumno.
- `consigna`: Ejercicio o consigna del taller al que responde el texto.
- `curso_pertenencia`: Taller en el que está matriculado (e.g. Iniciación, Creación Anual, Autoficción).

## ⚙️ 3. Procedimiento Paso a Paso
1. **Paso 1: Lectura Fenomenológica:** Leer el texto completo sin intervenir, identificando la emoción latente y el foco temático.
2. **Paso 2: Análisis de Concreción Sensorial:** Evaluar presencia de objetos, gestos, sentidos y microacciones frente a abstracciones explicativas.
3. **Paso 3: Redacción del Informe Técnico Interno:**
   - Cumplimiento de la consigna (o valor del desvío).
   - Diagnóstico del conflicto y la tensión interna.
   - Diagnóstico de la voz y la autenticidad del registro.
   - Puntos exactos de fuga o sobreexplicación.
4. **Paso 4: Redacción del Comentario Externo:**
   - Saludo afectivo llamando al alumno por su nombre (`Elena...`).
   - Elogio quirúrgico de los hallazgos reales.
   - Indicación respetuosa de la poda o reestructuración necesaria sin reescribir.
   - Despedida cálida que devuelva la confianza creadora.
5. **Paso 5: Paso por el Linter:** Verificar que la salida pasa `evals/test_style_linter.py` con 0 clichés de IA.

## 📤 4. Salida Esperada
Texto estructurado en dos bloques claramente delimitados:
- `### 1. Informe Técnico Interno`
- `### 2. Comentario Externo para el Alumno`
"""
    },
    {
        "id": "antonia-molinero-voice",
        "name": "antonia-molinero-voice",
        "description": "Estilística autoral, ensayística y epistolar de Antonia Molinero. Concreción sensorial, objetos cotidianos, conflicto latente, respiración natural y calidez reflexiva.",
        "content": """# ✍️ Skill: Voz Autoral de Antonia Molinero
### Pautas Estilísticas y Modulación Ensayística

## 🎯 1. Objetivo
Garantizar la recreación precisa de la voz literaria de Antonia Molinero en prólogos, cartas institucionales, artículos de prensa y ensayos reflexivos sobre la creación y la lectura.

## 📥 2. Entradas Requeridas
- `tema_central`: Idea, efeméride o proyecto a desarrollar.
- `formato_texto`: Carta institucional, prólogo de libro, artículo de prensa o manifiesto.
- `tono_emocional`: Melancólica doméstica, luminosa tierna, irónica ligera, crítica civil o furia contenida.

## ⚙️ 3. Procedimiento Paso a Paso
1. **Anclaje en un Objeto o Gesto Cotidiano:** Iniciar siempre desde un elemento tangible con peso emocional (una mesa, una taza desportillada, un abrigo, una bombilla).
2. **Desarrollo en Espiral:** Conectar la escena doméstica con la reflexión universal sobre la vida, el miedo, la dignidad o el oficio de escribir.
3. **Control de Ritmo y Respiración:** Alternar oraciones medias con pausas afectivas y puntos suspensivos meditados.
4. **Filtro Anti-Clichés:** Eliminar cualquier adjetivo grandilocuente o fórmula trillada de IA.
5. **Cierre Resonante:** Finalizar con una imagen nítida que permanezca en la memoria.
"""
    },
    {
        "id": "verificacion-originalidad-y-voz-propia",
        "name": "verificacion-originalidad-y-voz-propia",
        "description": "Detección de tópicos literarios, lugares comunes, imitaciones involuntarias y evaluación de la autenticidad de la voz propia del alumno.",
        "content": """# 🔍 Skill: Verificación de Originalidad y Voz Propia
### Detección de Clichés Literarios y Rescate de la Voz Auténtica

## 🎯 1. Objetivo
Identificar cuándo un alumno escribe desde fórmulas prestadas (cine comercial, lugares comunes románticos o policiales) y ayudarle a reconectar con su mirada singular.

## 📥 2. Entradas Requeridas
- `texto`: Relato o fragmento analizado.

## ⚙️ 3. Procedimiento Paso a Paso
1. **Escaneo de Tópicos:** Rastrear lugares comunes de caracterización (e.g. detective alcohólico, anciana bondadosa tejiendo junto al fuego).
2. **Evaluación de Afectación:** Medir si el lenguaje intenta sonar 'demasiado literario' en perjuicio de la verdad humana de la escena.
3. **Identificación de la Pepita de Oro:** Señalar el único detalle o frase donde la voz propia del alumno asoma con fuerza genuina.
4. **Recomendación Pedagógica:** Invitar a podar el andamiaje convencional para centrar el cuento en esa singularidad encontrada.
"""
    },
    {
        "id": "desbloqueo-creativo-socratico",
        "name": "desbloqueo-creativo-socratico",
        "description": "Técnica socrática de acompañamiento para desatascar tramas, superar bloqueos creativos y disolver el miedo al juicio ajeno sin escribir por el alumno.",
        "content": """# 💡 Skill: Desbloqueo Creativo Socrático
### Preguntas Disipadoras de Bloqueos Narrativos

## 🎯 1. Objetivo
Acompañar al estudiante atascado mediante preguntas quirúrgicas que le permitan descubrir por sí mismo el camino narrativo, sin suplantar jamás su autoría.

## 📥 2. Entradas Requeridas
- `bloqueo_declarado`: Descripción del problema por parte del alumno.
- `sinopsis_breve`: Argumento o estado actual de la historia.

## ⚙️ 3. Procedimiento Paso a Paso
1. **Desactivar el Crítico Interno:** Recordar que el bloqueo suele ser miedo al ridículo o exceso de ambición preliminar.
2. **Formular Preguntas de Escena Concreta:**
   - ¿Qué verdad no se atreve a decir el protagonista?
   - ¿Qué objeto hay en la mesa que nadie quiere tocar?
   - ¿Qué pasaría si la escena concluyera con un silencio en vez de con un portazo?
3. **Proponer Micro-Ejercicios de 10 Minutos:** Escribir el monólogo interior del antagonista o cambiar temporalmente de narrador a tercera persona testigo.
"""
    },
    {
        "id": "seguimiento-habito-escritura",
        "name": "seguimiento-habito-escritura",
        "description": "Metodología de diseño y monitorización de hábitos de escritura sostenibles, gestión de energía creativa y prevención del abandono de proyectos largos.",
        "content": """# 📅 Skill: Seguimiento de Hábito de Escritura
### Sostenimiento de la Rutina Creativa y Prevención del Abandono

## 🎯 1. Objetivo
Establecer rutinas de escritura realistas adaptadas al tiempo disponible del estudiante (madres trabajadoras, opositores, jubilados, jóvenes), celebrando la constancia.

## 📥 2. Entradas Requeridas
- `perfil_alumno`: Tiempo real disponible a la semana y compromisos laborales/familiares.
- `meta_proyecto`: Relato para clase, borrador de novela o memorias.

## ⚙️ 3. Procedimiento Paso a Paso
1. **Fijar el Mínimo Innegociable:** Definir bloques breves y sagrados (e.g. 20 minutos 3 días por semana).
2. **Separar Fase de Generación de Fase de Corrección:** Prohibir releer y juzgar mientras se escribe el primer borrador.
3. **Registro de Victorias:** Celebrar las sesiones cumplidas, independientemente del volumen de palabras producidas.
"""
    },
    {
        "id": "curaduria-antologias-eccl",
        "name": "curaduria-antologias-eccl",
        "description": "Criterios editoriales para la selección, ordenación temática, armonización estilística y control de galeradas de las antologías anuales de la Escuela.",
        "content": """# 📚 Skill: Curaduría de Antologías ECCL
### Arquitectura y Armonización de Libros Colectivos

## 🎯 1. Objetivo
Estructurar y preparar el manuscrito de las antologías colectivas anuales publicadas con Ediciones Idea y Servicio Editorial Flamboyán.

## 📥 2. Entradas Requeridas
- `relatos_candidatos`: Conjunto de relatos aprobados del curso.
- `titulo_antologia`: Título propuesto para el volumen.

## ⚙️ 3. Procedimiento Paso a Paso
1. **Evaluación de Calidad y Registro:** Verificar que cada texto cumple los estándares pedagógicos de la Escuela.
2. **Secuenciación Armónica:** Alternar tonos emocionales, temas y extensiones para mantener la tensión lectora a lo largo del libro.
3. **Revisión Ortotipográfica Editorial:** Normalizar rayas de diálogo, comillas latinas y sangrías.
4. **Página de Créditos y Metadatos:** Redactar página legal, notas biobibliográficas de los autores e índice general.
"""
    },
    {
        "id": "dinamizacion-comunidad-literaria",
        "name": "dinamizacion-comunidad-literaria",
        "description": "Estrategias de dinamización comunitaria para foros de alumnos, retos mensuales de escritura y fomento de la pertenencia alumni a la ECCL.",
        "content": """# ☕ Skill: Dinamización de Comunidad Literaria
### Retos Creativos y Cohesión del Alumnado Alumni

## 🎯 1. Objetivo
Estimular la participación activa y el intercambio respetuoso en la Comunidad de Escritores Senior y Junior y en los canales de antiguos alumnos.

## 📥 2. Entradas Requeridas
- `mes_convocatoria`: Mes del reto.
- `eje_tematico`: Disparador creativo propuesto.

## ⚙️ 3. Procedimiento Paso a Paso
1. **Redacción de la Consigna Mensual:** Diseñar un enunciado sugerente basado en un objeto, una fotografía o una situación límite cotidiana.
2. **Pautas de Intercambio:** Recordar a los miembros que la crítica entre iguales debe realizarse desde el elogio de hallazgos y el respeto absoluto.
3. **Cierre de Ciclo:** Recopilar los textos más destacados y publicar el boletín mensual de la comunidad.
"""
    },
    {
        "id": "contratos-editoriales-y-derechos-autor",
        "name": "contratos-editoriales-y-derechos-autor",
        "description": "Modelos y pautas jurídicas para la cesión no exclusiva de derechos de reproducción en antologías, protección de menores (RGPD) y contratos con agencias.",
        "content": """# ⚖️ Skill: Contratos Editoriales y Derechos de Autor
### Gestión Jurídica Autoral de la ECCL

## 🎯 1. Objetivo
Garantizar la protección legal de los textos de los alumnos y la seguridad jurídica de la Escuela en publicaciones colectivas y talleres.

## 📥 2. Entradas Requeridas
- `tipo_acuerdo`: Cesión para antología, contrato de agencia o autorización de menores.
- `datos_autor`: Nombre, DNI y título de la obra.

## ⚙️ 3. Procedimiento Paso a Paso
1. **Aplicación de Cesión No Exclusiva:** Asegurar que la cláusula estipule expresamente que el autor retiene la propiedad de la obra y puede publicarla en otros medios.
2. **Exención de Contraprestación Monetaria:** Especificar entrega de ejemplares de autor pactados.
3. **Cláusula RGPD:** Añadir el consentimiento explícito de tratamiento de datos personales para fines docentes y editoriales.
"""
    },
    {
        "id": "soporte-tecnico-aula-virtual",
        "name": "soporte-tecnico-aula-virtual",
        "description": "Protocolos de resolución técnica de incidencias en Zoom, plataforma de campus virtual, acceso a grabaciones y pasarela de pago para estudiantes.",
        "content": """# 💻 Skill: Soporte Técnico y Aula Virtual
### Resolución de Incidencias en Campus Online y Zoom

## 🎯 1. Objetivo
Asistir a alumnos y docentes en la resolución inmediata de problemas de conexión, accesos o pagos para evitar interrupciones en la docencia.

## 📥 2. Entradas Requeridas
- `tipo_incidencia`: Enlace Zoom caído, grabación no visible, fallo de pago o entrega de tarea.
- `datos_alumno`: Nombre y curso.

## ⚙️ 3. Procedimiento Paso a Paso
1. **Diagnóstico Inmediato:** Comprobar estado de la sesión o del enlace seguro.
2. **Envío de Instrucciones Numeradas:** Proporcionar solución paso a paso (e.g. borrado de caché, regeneración de contraseña, enlace alternativo).
3. **Comprobación de Cierre:** Confirmar con el alumno que ha podido acceder correctamente.
"""
    },
    {
        "id": "supervision-identidad-visual-eccl",
        "name": "supervision-identidad-visual-eccl",
        "description": "Auditoría determinista de cumplimiento de manual de marca: verificación de códigos HEX oficiales, tipografías autorizadas y descarte de clichés visuales de stock.",
        "content": """# 🛡️ Skill: Supervisión de Identidad Visual ECCL
### Auditoría Cromática, Tipográfica y Estética

## 🎯 1. Objetivo
Auditar cualquier pieza gráfica antes de su publicación para asegurar que respeta los colores oficiales, tipografías editoriales y principios estéticos de la Escuela.

## 📥 2. Entradas Requeridas
- `propuesta_grafica`: Archivo o descripción con colores HEX, fuentes y elementos visuales.

## ⚙️ 3. Procedimiento Paso a Paso
1. **Chequeo de Paleta HEX:** Comprobar uso de `#FAF8F5`, `#1A1A1A`, `#C2593F`, `#1E3A5F`, `#D4A346`. Rechazar colores fluorescentes o azules SaaS.
2. **Chequeo Tipográfico:** Validar titulares en *Playfair Display* / *Merriweather* y cuerpos en *Inter* / *Open Sans*.
3. **Filtro Anti-Stock:** Bloquear ilustraciones de plumas mágicas o elementos clichés de banco de imágenes.
4. **Emisión de Dictamen:** Emitir veredicto `APROBADO` o `RECHAZADO` con justificación.
"""
    },
    {
        "id": "diseno-carteleria-y-redes-eccl",
        "name": "diseno-carteleria-y-redes-eccl",
        "description": "Generación de directrices de maquetación, copys persuasivos y prompts de diseño para cartelería A3/A4, posts de Instagram y Stories.",
        "content": """# 🎨 Skill: Diseño de Cartelería y Redes ECCL
### Maquetación de Piezas Publicitarias y Creatividades

## 🎯 1. Objetivo
Diseñar la estructura gráfica, textos publicitarios y directrices visuales para carteles de talleres y publicaciones en redes sociales de la Escuela.

## 📥 2. Entradas Requeridas
- `nombre_curso`: Título del taller o evento.
- `docente`: Profesor que imparte la actividad.
- `fechas_horario`: Calendario oficial de sesiones.
- `formato`: Cartel A3/A4, Instagram Post 1:1 o Story 9:16.

## ⚙️ 3. Procedimiento Paso a Paso
1. **Jerarquía Visual:** Titular literario sugerente -> Docente y fecha -> Información práctica y llamada a la acción -> Logotipo ECCL y web.
2. **Asignación Cromática:** Fondo marfil `#FAF8F5`, texto `#1A1A1A`, llamada en terracota `#C2593F`.
3. **Redacción de Copys:** Texto conciso, literario y evocador para el pie de foto en Instagram con hashtags culturales canarios.
"""
    },
    {
        "id": "adaptacion-formatos-graficos-eccl",
        "name": "adaptacion-formatos-graficos-eccl",
        "description": "Redimensionamiento multiformato y cálculo de safe zones para cartelería impresa, formatos verticales de Stories y banners horizontales.",
        "content": """# 📐 Skill: Adaptación de Formatos Gráficos ECCL
### Cálculo de Safe Zones y Redimensionamiento Multicanal

## 🎯 1. Objetivo
Adaptar una creatividad gráfica aprobada a múltiples soportes garantizando que ningún elemento esencial quede oculto por interfaces de apps o cortes de imprenta.

## 📥 2. Entradas Requeridas
- `diseno_base`: Elementos del cartel o creatividad original.
- `formatos_destino`: Lista de formatos (Post 1:1, Story 9:16, Cartel A3/A4, Banner 1200x630).

## ⚙️ 3. Procedimiento Paso a Paso
1. **Cálculo de Márgenes Seguros:**
   - Story 9:16: Respetar 250 px arriba y abajo.
   - Post 1:1: Margen interior de 80 px.
   - Cartel A3/A4: Sangrado de 3 mm y margen interior de 15 mm.
2. **Reorganización de Elementos:** Reubicar logotipo, textos y fechas para optimizar la lectura según el soporte.
"""
    },
    {
        "id": "guion-reels-y-pildoras-literarias",
        "name": "guion-reels-y-pildoras-literarias",
        "description": "Estructuración de guiones breves de 30 a 60 segundos para Reels y TikTok con consejos narrativos, reflexiones de Antonia y píldoras del claustro.",
        "content": """# 🎬 Skill: Guiones de Reels y Píldoras Literarias
### Creación de Contenido Audiovisual Breve para Redes

## 🎯 1. Objetivo
Elaborar guiones ágiles y profundos para vídeos cortos que transmitan la esencia pedagógica de la Escuela sin caer en trucos vacíos de marketing.

## 📥 2. Entradas Requeridas
- `concepto`: Consejo literario o reflexión (e.g. 'Por qué no debes explicar las emociones de tu personaje').
- `duracion_objetivo`: 30 a 60 segundos.

## ⚙️ 3. Procedimiento Paso a Paso
1. **Gancho Visual e Inicial (0-5 seg):** Pregunta o afirmación contundente que rompa el scroll.
2. **Cuerpo Demostrativo (5-45 seg):** Ejemplo práctico con un objeto cotidiano o frase de autor.
3. **Cierre Reflexivo y CTA (45-60 seg):** Conclusión que invite a escribir o a informarse sobre el curso correspondiente en la web.
"""
    },
    {
        "id": "catalogo-academico-eccl",
        "name": "catalogo-academico-eccl",
        "description": "Consulta y validación canónica de cursos, tarifas, fechas, modalidades y claustro docente contra escuelaliteraria.com y los JSON canónicos.",
        "content": """# 📚 Skill: Catálogo Académico Canónico ECCL
### Consulta Factual de Cursos, Fechas y Profesores

## 🎯 1. Objetivo
Proveer información 100% veraz sobre la oferta docente, precios, modalidades y claustro de la Escuela sin margen de alucinación.

## 📥 2. Entradas Requeridas
- `termino_busqueda`: Nombre de curso, temática, fecha o profesor.

## ⚙️ 3. Procedimiento Paso a Paso
1. **Búsqueda en Base de Conocimiento:** Consultar `knowledge/catalogo/cursos_activos.json` y `claustro_docente.json`.
2. **Validación de Modalidad y Aforo:** Indicar si el curso es presencial (La Laguna), online live o diferido.
3. **Precios y Requisitos:** Detallar tarifas exactas y si exige muestra previa de escritura.
"""
    },
    {
        "id": "lead-scoring-eccl",
        "name": "lead-scoring-eccl",
        "description": "Algoritmo de clasificación y baremación de interesados según compromiso, disponibilidad temporal y madurez de su proyecto de escritura.",
        "content": """# 🎯 Skill: Lead Scoring ECCL
### Baremación de Interesados y Perfil de Entrada

## 🎯 1. Objetivo
Clasificar las solicitudes de información recibidas para orientar a cada persona con la máxima eficacia pedagógica.

## 📥 2. Entradas Requeridas
- `informacion_interesado`: Datos aportados en el formulario de contacto o consulta telefónica.

## ⚙️ 3. Procedimiento Paso a Paso
1. **Cálculo de Variables:**
   - Tiempo disponible semanal (0-3h, 4-8h, >8h).
   - Experiencia de escritura y expectativas de publicación.
   - Disposición al aprendizaje en grupo y feedback constructivo.
2. **Asignación de Puntuación (Scoring):** Nivel A (Curso Anual), Nivel B (Talleres Temáticos/Intensivos), Nivel C (Comunidad Diferido).
"""
    },
    {
        "id": "orientacion-itinerarios-formativos",
        "name": "orientacion-itinerarios-formativos",
        "description": "Mapeo y recomendación de itinerarios progresivos de aprendizaje literario a lo largo de los cursos de la ECCL.",
        "content": """# 🧭 Skill: Orientación de Itinerarios Formativos
### Progresión Pedagógica del Alumno en la Escuela

## 🎯 1. Objetivo
Trazar la ruta de formación ideal para un estudiante desde su llegada hasta la publicación de su obra o consolidación de su voz literaria.

## 📥 2. Entradas Requeridas
- `nivel_partida`: Principiante absoluto, alumno con experiencia o autor con manuscrito.

## ⚙️ 3. Procedimiento Paso a Paso
1. **Fase Inicial:** Recomendar *Iniciación a la Creación Literaria* o talleres intensivos temáticos.
2. **Fase de Consolidación:** Paso al *Curso de Creación Literaria Anual* (50 horas) con Antonia Molinero.
3. **Fase de Publicación y Comunidad:** Integración en la antología colectiva anual y membresía en la Comunidad de Escritores Senior.
"""
    },
    {
        "id": "synthetic-audience-panel-eccl",
        "name": "synthetic-audience-panel-eccl",
        "description": "Invocación y simulación del panel de 18 avatares reales para test de estrés de nuevos cursos, precios, horarios y objeciones de compra.",
        "content": """# 👥 Skill: Panel de Audiencia Sintética ECCL
### Focus Group con los 18 Avatares Maestros

## 🎯 1. Objetivo
Simular la reacción de la comunidad estudiantil real ante cualquier propuesta formativa o comercial antes de su lanzamiento.

## 📥 2. Entradas Requeridas
- `propuesta`: Taller, precio, modalidad y fechas.
- `avatares_objetivo`: Lista de avatares a consultar o panel completo.

## ⚙️ 3. Procedimiento Paso a Paso
1. **Carga de Perfiles:** Consultar `knowledge/avatares/panel_18_alumnos.json`.
2. **Evaluación de Motivaciones vs Frenos:** Contrastar la propuesta con el tiempo, presupuesto y miedos de cada avatar seleccionado.
3. **Consolidación de Métricas:** Calcular porcentaje de aprobación y principales objeciones detectadas.
"""
    },
    {
        "id": "cultural-grant-writer-es",
        "name": "cultural-grant-writer-es",
        "description": "Especialista en redacción técnica de memorias, cronogramas y justificaciones presupuestarias para convocatorias de subvenciones culturales en España.",
        "content": """# 🏛️ Skill: Redacción de Subvenciones Culturales (España)
### Memorias Técnicas y Proyectos para Concurrencia Competitiva

## 🎯 1. Objetivo
Redactar memorias técnicas impecables adaptadas a los criterios de evaluación de organismos culturales públicos.

## 📥 2. Entradas Requeridas
- `bases_convocatoria`: Requisitos y baremo del pliego oficial.
- `proyecto_eccl`: Proyecto presentado (talleres, publicaciones, Escuela Portátil).

## ⚙️ 3. Procedimiento Paso a Paso
1. **Alineación con Criterios Evaluables:** Cohesión territorial, igualdad de género, ODS y digitalización.
2. **Redacción de Objetivos e Indicadores:** Metas cuantitativas y cualitativas verificables.
3. **Cronograma y Presupuesto:** Cuadre financiero estricto y desglose de gastos elegibles.
"""
    },
    {
        "id": "subvenciones-canarias-sync",
        "name": "subvenciones-canarias-sync",
        "description": "Monitorización y mapeo de convocatorias específicas de Canarias: ICDC, Cabildos insulares y ayuntamientos de las islas.",
        "content": """# 🏝️ Skill: Sincronización de Subvenciones Canarias
### Monitorización de ICDC, Cabildos y Pliegos Insulares

## 🎯 1. Objetivo
Detectar oportunidades de financiación pública cultural en el ámbito autonómico e insular canario.

## 📥 2. Entradas Requeridas
- `organismo`: ICDC, Cabildo de Tenerife, Cabildo de Gran Canaria u otros.

## ⚙️ 3. Procedimiento Paso a Paso
1. **Revisión de Calendario Convocatorias:** Plazos de presentación de solicitudes.
2. **Chequeo de Límites Presupuestarios:** Topes de contratos menores y subvenciones directas o en concurrencia.
"""
    },
    {
        "id": "business-intelligence-cultural",
        "name": "business-intelligence-cultural",
        "description": "Cálculo de márgenes de contribución, umbrales de apertura de grupos, aforos y analítica de rentabilidad formativa.",
        "content": """# 📊 Skill: Business Intelligence Cultural
### Modelos Financieros y Rentabilidad Académica

## 🎯 1. Objetivo
Calcular con precisión la viabilidad económica de la apertura de grupos presenciales y online en la Escuela.

## 📥 2. Entradas Requeridas
- `costes_docente`: Honorarios del profesor y gastos directos.
- `precio_matricula`: Precio por alumno.
- `aforo_maximo`: Plazas disponibles.

## ⚙️ 3. Procedimiento Paso a Paso
1. **Cálculo del Break-Even:** Determinar el número mínimo de alumnos para cubrir costes.
2. **Matriz de Escenarios:** Escenario pesimista, base y optimista con márgenes de beneficio neto.
"""
    },
    {
        "id": "gestion-eventos-y-agenda-cultural",
        "name": "gestion-eventos-y-agenda-cultural",
        "description": "Planificación y logística de presentaciones de libros, clausuras de cursos, ferias del libro y encuentros con autores invitados.",
        "content": """# 🎪 Skill: Gestión de Eventos y Agenda Cultural
### Logística y Protocolo de Actividades Literarias

## 🎯 1. Objetivo
Coordinar la producción de eventos literarios presenciales y retransmisiones online de la Escuela.

## 📥 2. Entradas Requeridas
- `tipo_evento`: Presentación de antología, charla magistral o feria del libro.
- `participantes`: Autores, docentes y público esperado.

## ⚙️ 3. Procedimiento Paso a Paso
1. **Escaleta del Evento:** Distribución de tiempos de intervención y turno de preguntas.
2. **Requisitos Técnicos:** Sonido, streaming y firmas de ejemplares.
"""
    },
    {
        "id": "press-release-cultural-es",
        "name": "press-release-cultural-es",
        "description": "Redacción periodística de notas de prensa culturales con estructura de pirámide invertida y contactos para medios insulares y nacionales.",
        "content": """# 📰 Skill: Notas de Prensa Culturales
### Comunicación Periodística para Medios de Comunicación

## 🎯 1. Objetivo
Redactar notas de prensa con gancho informativo para periódicos, radios y suplementos literarios.

## 📥 2. Entradas Requeridas
- `noticia`: Convocatoria de nuevo curso, fallo de concurso o lanzamiento de libro.

## ⚙️ 3. Procedimiento Paso a Paso
1. **Titular y Entradilla:** Las 5W esenciales en el primer párrafo.
2. **Declaraciones y Contexto:** Citas entrecomilladas de Antonia Molinero o del claustro.
3. **Pie Institucional:** Breve dossier de la Escuela Canaria de Creación Literaria y datos de contacto de prensa.
"""
    },
    {
        "id": "dossier-cultural-generator",
        "name": "dossier-cultural-generator",
        "description": "Generación de dossiers ejecutivos y memorias de presentación para bibliotecas, librerías y patrocinadores culturales.",
        "content": """# 📑 Skill: Generador de Dossiers Culturales
### Presentaciones Ejecutivas para Socios y Patrocinadores

## 🎯 1. Objetivo
Crear dossiers atractivos y bien maquetados para presentar proyectos de la Escuela ante entidades públicas y privadas.

## 📥 2. Entradas Requeridas
- `proyecto`: Nombre y descripción del programa cultural.

## ⚙️ 3. Procedimiento Paso a Paso
1. **Estructura Editorial:** Portada institucional, carta de presentación, objetivos, claustro docente y presupuesto.
2. **Diseño sobrio y elegante:** Alineado con la paleta de la Escuela.
"""
    },
    {
        "id": "propuestas-b2b-culturales",
        "name": "propuestas-b2b-culturales",
        "description": "Diseño de ofertas técnicas y económicas de formación literaria in-company para centros educativos, ayuntamientos y fundaciones.",
        "content": """# 🤝 Skill: Propuestas B2B Culturales
### Proyectos a Medida para Administraciones y Empresas

## 🎯 1. Objetivo
Elaborar propuestas formativas a medida para instituciones que deseen contratar talleres de escritura, oratoria o creatividad.

## 📥 2. Entradas Requeridas
- `entidad_cliente`: Ayuntamiento, cabildo, centro educativo o empresa.
- `necesidad_detectada`: Fomento lector juvenil, formación de docentes o comunicación interna.

## ⚙️ 3. Procedimiento Paso a Paso
1. **Propuesta Pedagógica:** Objetivos de aprendizaje y metodología de taller participativo.
2. **Propuesta Económica:** Tarifas por hora/sesión, materiales incluidos y condiciones de contratación.
"""
    }
]

def generate_skills():
    print(f"Generando {len(SKILLS_DEFINITIONS)} skills en {SKILLS_DIR}...")
    for s in SKILLS_DEFINITIONS:
        s_dir = os.path.join(SKILLS_DIR, s["id"])
        os.makedirs(s_dir, exist_ok=True)
        skill_file = os.path.join(s_dir, "SKILL.md")
        
        full_content = f"""---
name: {s["name"]}
description: {s["description"]}
---

{s["content"].strip()}
"""
        with open(skill_file, "w", encoding="utf-8") as f:
            f.write(full_content)
        print(f"  [OK] Creada skill: {s['id']}")
    print("\nTodas las skills fueron generadas con éxito.")

if __name__ == "__main__":
    generate_skills()
