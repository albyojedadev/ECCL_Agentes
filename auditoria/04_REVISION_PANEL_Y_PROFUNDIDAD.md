# Revisión independiente: panel de alumnos, profundidad y ampliaciones

Fecha: 14 de octubre de 2026. Revisor: subagente de panel y profundidad. Dictamen: **NO APTO para certificar migración sin pérdidas ni enriquecimiento profesional suficiente de toda la suite**.

## 1. Alcance y método

Lectura completa de los 17 agentes, las 24 skills y los 6 protocolos entregados, y de todos los originales de `GPTs/04 Consejo de alumnos`: config, persona, función, metodología, seguridad, análisis de públicos, maestro, 18 individuales e Informe GPT. Contraste con JSON de panel, marca y legal, generador de conocimiento y especificaciones pertinentes de Planificación. Las otras migraciones históricas son responsabilidad de los revisores literario e institucional; esta revisión evalúa profundidad de todos los componentes sin sustituir ese contraste.

Se valora contenido transmisible: instrucciones específicas, procedimientos aplicables, gestión de entradas incompletas, excepciones, ejemplos de entrada a salida, referencias accesibles y criterios verificables. **No se puntúa por longitud**. Un archivo breve puede bastar si permite actuar consistentemente; una lista de competencias puede ser larga y no ser un procedimiento.

Se ejecutó comparación JSON local en memoria: maestro histórico y panel entregado son objetos completamente iguales. No se ejecutaron agentes, instaladores, ingesta ni servicios externos. No se ha comprobado normativa ni datos comerciales en la web. Las observaciones jurídicas son de procedencia y suficiencia documental, no un dictamen legal.

Rutas de evidencia relativas a la raíz del proyecto. Salvo prefijo `GPTs/` o `Planificación/`, pertenecen a `Repositorio de agentes/`. L = línea. P0 = bloquea núcleo de migración antes de entregar; P1 = defecto importante para la capacidad o garantía prometida; P2 = precisión o mejora necesaria. Los casos de aceptación al final son propuestos, no ejecutados.

## 2. Fortalezas y conclusión

Hay una arquitectura aprovechable: nombres comprensibles, 16 destinos de enrutamiento, dependencias declaradas y 6 flujos compartidos. El crítico contiene reglas concretas de doble destinatario, elogio específico, no reescritura y no diagnóstico psicológico; el compañero aporta preguntas útiles; el analista incluye una fórmula de umbral de apertura; diseño incorpora dimensiones y márgenes explícitos. La separación de funciones y las nuevas reglas aportan valor real.

La integridad del panel, sin embargo, falla: **14/18 perfiles pierden acceso al detalle psicológico disponible en los individuales históricos** y el agente presenta identidades inventadas que contradicen el JSON. Desaparecen límites cualitativos y se introducen porcentajes sin método. Las 24 skills aportan esquemas, pero ninguna contiene un ejemplo trabajado completo; solo crítica tiene sección explícita de salida esperada. En `skills/` solo hay 24 SKILL.md: no están las referencias y plantillas previstas.

No es defendible confirmar conservación completa ni declarar toda la suite profesionalmente enriquecida. Hace falta recuperar conocimiento y convertir esbozos en guías operables, no rellenar con prosa.

## 3. Hallazgos del panel

### PAN-01 — P0: se conserva un maestro resumido, pero no todo el conocimiento histórico

La igualdad semántica del maestro original y `knowledge/avatares/panel_18_alumnos.json` confirma copia íntegra del maestro. **No confirma copia íntegra de las fuentes**. Los avatares 1–4 tienen 25 campos; 5–18 tienen 13. Los doce campos ausentes en los 14 resumidos son: contexto, motivaciones, frenos, miedos, deseos, tono_emocional, frase_arquetipo, objetivo_narrativo, riesgos, modo_de_hablar, expectativas y relacion_con_la_escritura.

Los individuales contienen ese detalle; no se distribuyen dentro del repositorio entregable. La nota original L699–704 y panel L1163–1167 dicen que los perfiles 5–18 están resumidos y remiten a `avatar[N].json`. La afirmación adicional de que mantienen la misma estructura completa es inexacta: es un defecto heredado que la migración debía detectar, no una justificación para omitirlos.

Ejemplo: `GPTs/04 Consejo de alumnos/Individuales/avatar11.json` L5–71 detalla diferencia horaria, pagos internacionales, temor al juicio de su voz latinoamericana, modo de hablar y expectativas de Valentina. El panel L771–802 solo conserva identidad y campos comerciales. Ana pierde lectura asistida, fatiga visual, formatos accesibles y rechazo del paternalismo (individual18 L18–71 frente a panel L1009–1042). No son detalles ornamentales: condicionan las decisiones formativas.

**Corrección y aceptación:** integrar los 18 individuales con campos comerciales del maestro, trazabilidad por campo y discrepancias documentadas; comprobar los 18 perfiles completos, no solo su contador.

### PAN-02 — P0: identidades inventadas en la instrucción del agente

`agents/consejo-de-alumnos-sinteticos.md` L20–25 enumera Elisa38 médica, Santiago67, Lucas16, Marta44 y Carmen52. La fuente contiene Elisa42 sector servicios, Héctor36, Clara15, José68 y Marina33. Santiago, Lucas, Marta y Carmen no figuran entre los 18 nombres. Evidencias destino: panel L165–177, 267–279, 370–382, 472–484 y 573–581; origen: individuales1–5 L2–10.

Esto cambia edad, profesión y biografía, contradiciendo la propia regla de invariancia del agente L48. Tener ambas versiones en contexto no asegura que prevalezca la correcta.

**Corrección:** retirar fichas inventadas, identificar por id_avatar y generar índices desde datos verificados. Probar consultas por nombre, segmento y nombre inexistente.

### PAN-03 — P1: simulación cualitativa convertida en aparente medición de mercado

El original exige tratar la salida como simulación cualitativa y no muestra estadística: `seguridad.txt` L8–11, 56–70; `funcion.txt` L74–77, 159–167; `metodologia.txt` L161–174. Distingue dato de ficha, inferencia y especulación (`config.txt` L131–143; `persona.txt` L22–28).

Destino: agente L3 y skill panel L3 llaman reales a los avatares; agente L33–39 pide índice global porcentual; skill L17–19 exige consolidarlo; P03 L24–30 obliga ajustar si aceptación <70 %. No define aceptación, pesos, abstención, incertidumbre ni fundamento del 70 %. Tampoco separa comparación de hipótesis simuladas de un experimento A/B con participantes.

**Corrección:** restaurar naturaleza cualitativa y necesidad de contraste externo. Si se conserva puntuación, documentar cálculo y llamarla heurística de encaje simulado, sin convertirla en probabilidad de compra ni validación comercial. Separar SOP de simulación y A/B real.

### PAN-04 — P1: pérdida de estrategia, ejemplos y gestión de incertidumbre

Original: tres modos —avatar único, panel comparativo, analista—; selección explicada de 2–4 perfiles por segmentos y bloques; comparación individual, renuncias y ajustes de producto/mensaje/canal (`config.txt` L11–18, 96–127; `metodologia.txt` L29–67, 90–157). `funcion.txt` desarrolla nueve funciones, incluidos claims, co-diseño e insights, con salidas diferenciadas L86–207. `persona.txt` L99–117 contiene ejemplos completos de subida de precio y modalidad online. `Individuales/Informe GPT.txt` L180–308 y 430–465 explica anclaje psicológico y prevención de promedios/complacencia.

Destino: agente reduce a dos modos generales, análisis de todo el panel y reglas finales; skill aporta tres pasos. Preserva propósito y no complacencia, pero no sus operaciones y ejemplos más útiles. `AnalisisPublico.md` no se distribuye ni se vincula como referencia: matriz público–oferta–mensaje L139–146, recomendaciones L179–197, mapa de expansión L248–334 pierden contexto accesible. Parte de segmentación sí permanece en el JSON; no se afirma pérdida total de la estrategia.

**Corrección:** guía con tres modos, entradas mínimas, selección justificada, plantilla comparativa, renuncias e incertidumbre; conservar ejemplos históricos y añadir casos trabajados marcados como nuevos. Distribuir análisis macro fechado distinguiendo propuestas de oferta y catálogo real.

### PAN-05 — P2: defectos heredados que deben repararse sin atribuirlos a la migración

Seis individuales históricos (1,2,3,4,5,10) fallan JSON estricto por cierres de objeto donde corresponde cierre de lista. Se han leído como texto sin descartar contenido. Los otros doce se analizan. El destino maestro es válido: **estos seis errores no los creó el traslado**. La futura integración deberá normalizarlos sin cambiar contenido silenciosamente.

Hay incoherencias heredadas: Carlos/avatar14 figura en relaciones SEG-01 (maestro L21) pero ficha SEG-02 (L543–548); Thomas está relacionado con bloque C en lista macro (L70–73) y ficha E (L483–488). Resolver multisegmentación de manera documentada. Panel L1167 remite a `inventario_cursos.csv`, no distribuido bajo ese nombre.

## 4. Comprobación de los 18 perfiles

Cada individual tiene 73 líneas: identidad L2–4 y contenido psicológico L5–71. Completo aquí significa contenido documental, no validación empírica de personas reales. Las seis fuentes con sintaxis defectuosa se compararon como texto; no se afirma igualdad programática de sus objetos.

| ID / nombre | Campos panel | Líneas identidad panel | Preservación |
|---|---:|---|---|
| 1 Elisa | 25 | 165–177 | Psicología presente; identidad contradicha por agente |
| 2 Héctor | 25 | 267–279 | Psicología presente |
| 3 Clara | 25 | 370–382 | Presente; agente introduce Lucas |
| 4 José | 25 | 472–484 | Presente; agente introduce Santiago |
| 5 Marina | 13 | 573–581 | Faltan doce campos psicológicos |
| 6 Álvaro | 13 | 606–614 | Faltan doce campos psicológicos |
| 7 Beatriz | 13 | 639–647 | Faltan doce campos psicológicos |
| 8 Nico | 13 | 672–680 | Faltan doce campos psicológicos |
| 9 Laura | 13 | 706–714 | Faltan doce campos psicológicos |
| 10 Thomas | 13 | 739–747 | Faltan doce campos; revisar bloques heredados |
| 11 Valentina | 13 | 772–780 | Faltan doce campos psicológicos |
| 12 Diego | 13 | 805–813 | Faltan doce campos psicológicos |
| 13 Amina | 13 | 839–847 | Faltan doce campos psicológicos |
| 14 Carlos | 13 | 873–881 | Faltan doce campos; revisar segmento heredado |
| 15 Sofía | 13 | 907–915 | Faltan doce campos psicológicos |
| 16 Lucía | 13 | 942–950 | Faltan doce campos psicológicos |
| 17 Rafa | 13 | 976–984 | Faltan doce campos psicológicos |
| 18 Ana | 13 | 1010–1018 | Faltan doce campos, incluidas necesidades accesibles |

## 5. Tabla individual de las 24 skills

Parcial = reglas o esquema útiles con decisiones/casos/cierre insuficientes. Esbozo = lista de tareas insuficiente para ejecutar consistentemente la promesa. Ninguna alcanza manual completo validado. La profundidad exigida debe ser proporcional a tarea y riesgo.

**0/24 ejemplos trabajados completos dentro de las skills.** Preguntas, valores y saludos sueltos no equivalen a un caso de entrada a salida. Solo crítica declara sección formal de salida esperada. Sin referencia = el SKILL.md no dirige a material de apoyo específico; puede existir conocimiento complementario en el agente, que no sustituye la reutilización autónoma del módulo. Rutas: `skills/<nombre>/SKILL.md`.

| Skill | Guía/protocolo y evidencia | Ejemplos | Referencias accesibles | Salida/rúbrica | Falta principal |
|---|---|---|---|---|---|
| adaptacion-formatos-graficos-eccl | Parcial: márgenes y reorganización L12–21 | Valores de margen | Sin referencia | Sin plantilla/control geométrico | Escala, recorte, legibilidad y conversión trabajada |
| antonia-molinero-voice | Parcial: objeto, espiral, ritmo, cierre L12–22 | Objetos sueltos | No enlaza corpus/manual | Sin rúbrica de fidelidad | Variantes trabajadas y excepciones |
| business-intelligence-cultural | Esbozo: umbral y escenarios L12–19 | Ninguno | Sin referencia | Sin fórmula/tabla aquí | Costes variables, unidades, denominador inválido, caso numérico |
| catalogo-academico-eccl | Parcial: JSON, modalidad, tarifa L12–18 | Ninguno | Dos JSON catálogo | Sin regla de vigencia/conflicto | Distinguir histórico/activo, ausencia y actualización |
| contratos-editoriales-y-derechos-autor | Esbozo: tres cláusulas L12–19 | Ninguno | No enlaza modelos | Sin contrato ni revisión | Modelos completos, procedencia, control profesional |
| critica-pedagogica-literaria | Parcial: cinco pasos L12–31 | Saludo suelto | Linter L31 | Dos bloques L33–36 | Caso completo, consigna ausente, separación de destinatarios |
| cultural-grant-writer-es | Esbozo: alinear, objetivos, presupuesto L12–19 | Ninguno | Bases como entrada | Sin matriz de evidencia | Guía de requisitos, indicadores, ejemplos y elegibilidad |
| curaduria-antologias-eccl | Parcial: secuencia editorial L12–20 | Signos sueltos | Sin referencia | Estándares no definidos | Rúbrica selección, desempate, revisión autor/galeradas |
| desbloqueo-creativo-socratico | Parcial: preguntas y ejercicios L12–22 | Tres preguntas y dos ejercicios | Sin referencia | Sin bucle evaluable | Clasificar bloqueo y adaptar siguiente paso a respuesta |
| dinamizacion-comunidad-literaria | Esbozo: consigna, respeto, boletín L12–19 | Ninguno | Sin referencia | Sin reglas moderación | Club completo, conflictos, reactivación y difusión |
| diseno-carteleria-y-redes-eccl | Parcial: jerarquía y colores L12–21 | HEX concretos | No enlaza manual/plantillas | Sin entregable verificable | Assets, plantilla, exportación y pieza trabajada |
| dossier-cultural-generator | Esbozo: índice y sobriedad L12–17 | Ninguno | Sin referencia | Sin criterios/plantilla | Dossier completo con datos, extensión y revisión |
| gestion-eventos-y-agenda-cultural | Esbozo: escaleta y técnica L12–18 | Ninguno | Sin referencia | Sin cierre | Responsables, plazos, aforo y contingencias |
| guion-reels-y-pildoras-literarias | Parcial: tiempos L12–19 | Concepto de vídeo | Sin referencia | Sin guion modelo | Adaptar tiempos de 60 a 30 s, audiovisual y accesibilidad |
| lead-scoring-eccl | Esbozo: variables y A/B/C L12–20 | Rangos horarios | Sin baremo de origen | Sin puntos/pesos/umbrales | No es algoritmo definido; C contradice agente |
| orientacion-itinerarios-formativos | Esbozo: ruta lineal L12–18 | Nombres de cursos | No enlaza catálogo | Sin alternativas/criterios | Perfil heterogéneo, publicación no garantizada |
| press-release-cultural-es | Esbozo: 5W, citas, pie L12–18 | Ninguno | Sin citas autorizadas | Sin aprobación/verificación | No inventar declaración; ejemplo íntegro |
| propuestas-b2b-culturales | Esbozo: pedagógica/económica L12–18 | Ninguno | Sin referencia | Sin plantilla ni aceptación | Descubrimiento, alcance, exclusiones, costes y caso |
| seguimiento-habito-escritura | Parcial: mínimo, fases, registro L12–19 | 20 min/3 días | Sin referencia | Sin registro/revisión | Adaptación tras incumplimiento o fatiga |
| soporte-tecnico-aula-virtual | Esbozo: diagnosticar/instruir/cerrar L12–19 | Caché/contraseña como posibilidades | Sin manual plataforma | Cierre por confirmación, sin escalado | Árbol real de cada incidencia, límites de acceso |
| subvenciones-canarias-sync | Esbozo: calendario/topes L12–17 | Organismos | Sin enlaces/feed | Sin fecha/estado | Monitorización real y separación contratación/subvención |
| supervision-identidad-visual-eccl | Parcial: paleta/fuentes/dictamen L12–19 | HEX/fuentes | No enlaza manual/JSON | Dictamen sí, sin baremo/contraste | Origen de marca y evaluación de pieza real |
| synthetic-audience-panel-eccl | Esbozo: tres pasos L12–19 | Ninguno | JSON panel | Porcentaje indefinido | PAN-01 a PAN-04 |
| verificacion-originalidad-y-voz-propia | Parcial: tópico, hallazgo, recomendación L12–19 | Dos tópicos | Sin referencia | Sin originalidad verificable | Crítica de clichés no prueba plagio ni autoría |

### PRO-01 — P1: esquemas insuficientes y materiales previstos ausentes

El patrón objetivo/entradas/dos a cuatro acciones organiza, pero mandatos como determinar, verificar o redactar sustituyen la explicación de cómo hacerlo. Faltan ramas ante datos insuficientes, modelos y controles. **El defecto es la ausencia de conocimiento operativo, no el número de palabras.**

`Planificación/11_DISENO_GRAFICO_E_IDENTIDAD_VISUAL.md` L38–50 prevé ocho referencias: paleta, tipografías, checklist, plantillas Canva, prompts de mockups, formatos, matriz de escalado y zonas seguras. No están en skills/. Planificación/12 L141–157 describe modelos jurídicos y árbol de soporte por incidencias, reducidos en entrega a listas generales.

Aceptación: al menos un caso normal y uno de excepción por skill, con decisiones y salida revisable, referencias pertinentes y criterios verificables. Las de mayor riesgo requieren más modelos; evitar expansión homogénea sin conocimiento del dominio.

## 6. Tabla individual de los 17 agentes

Todos declaran identidad y skills. Ninguno contiene un caso completo de extremo a extremo; crítico y compañero sí aportan ejemplos parciales útiles. Las referencias nominales no acreditan carga real: esa parte corresponde al informe técnico. Rutas: `agents/<nombre>.md`.

| Agente | Guía y protocolo | Ejemplos/referencias/salida | Dictamen y falta |
|---|---|---|---|
| coordinador-de-agentes-de-la-eccl | Enruta a 16 destinos L18–53; siete perspectivas L57–68 | Links locales; matriz final sin esquema; sin ejemplo de transferencia | Parcial útil: paquete de delegación, conflicto de dictámenes y decisión humana; vinculante L68 excede asesoría |
| critico-literario-de-la-eccl | Criterios bifásicos y prohibiciones L18–44 | Saludos, poda, P01; sin caso completo | Núcleo útil: destinatario interno protegido y detalle histórico por restaurar |
| ghostwriter-de-antonia-molinero | Nueve ejes y formatos L17–38 | Objetos/clichés; linter L44–47 | Parcial: corpus no consultado explícitamente, fidelidad ≥90 % sin medida válida |
| experto-en-la-eccl | Identidad, fuentes, no invención L17–39 | Dos JSON y URL; sin caso conflicto | Parcial: fuente inmutable L33 y catálogo activo necesitan gestión de vigencia |
| analista-de-datos-culturales-y-educativos | Fórmula, modalidades/cohortes L19–28 | Dos JSON; histórico no adjunto L36; tabla L42 | Parcial: caso numérico, unidades, denominador y aforos documentados |
| analista-de-subvenciones-y-licitaciones | Triaje y memoria L18–36 | P02, organismos; presupuesto L50 | Parcial: baremo no es tasa de éxito; límites contractuales no son límites universales de ayuda |
| consejo-de-alumnos-sinteticos | Dos modos/no complacencia L29–49 | Biografías falsas L20–25; porcentaje L36 | Bloqueado PAN-01 a PAN-04 |
| orientador-de-admisiones-y-alumnos | Diagnóstico/categorías/acceso L18–30 | Muestra 1–2 páginas; catálogo; tono L36 | Parcial: C contradictorio, disponibilidad y publicación no automáticas |
| companero-de-escritura-y-habito | No escribir por alumno, preguntas/hábito L17–35 | Cuatro preguntas y metas; sin fuentes | Valor práctico parcial: diálogo completo, seguimiento y adaptación |
| editor-de-libros-y-antologias | Índice, ortotipografía, voz/metadatos L18–27 | Signos y asesor; sin modelos | Perfil útil: selección, aceptación autor y galeradas por desarrollar |
| dinamizador-de-comunidad-y-clubes | Tres ámbitos L17–26 | Nombra clubes/docente; sin guías | Esbozo: moderación, guía trabajada y conflictos |
| asesor-de-propiedad-intelectual | Tres módulos L16–26 | Dos JSON L30–33, sin contrato íntegro | No validado: garantías y porcentajes sin expediente; AMP-02 |
| asistente-de-soporte-y-aula-virtual | Cuatro incidencias L16–25 | Tono/cierre L31; sin manual ni árbol | Esbozo: resolver excede conocimiento/capacidad constatada |
| responsable-de-comunicacion-y-prensa | Formatos/5W L18–30 | Declaraciones sin fuente; sin plantilla | Parcial: citas, hechos y aprobación publicación |
| gestor-de-proyectos-institucionales-y-b2b | Cuatro líneas y secciones L17–32 | Públicos, sin caso o presupuesto | Esbozo: diagnóstico, alcance, condiciones y oferta completa |
| disenador-grafico-y-carteleria | Formatos/márgenes/paleta L18–47 | Valores, JSON nominal; sin pieza modelo | Parcial: assets, plantillas y origen aprobado |
| guardian-de-marca-e-identidad-visual | Checklist/salida L17–40 | HEX/fuentes; puntuación sin baremo | Parcial: geometría y marca oficial no acreditadas |

### PRO-02 — P1: métricas superficiales confundidas con garantía sustantiva

Ghostwriter L44–47 pide fidelidad ≥90 % y 10–24 palabras/oración. El linter citado comprueba clichés, rótulos bifásicos, saludo y media de 8–26 palabras (`evals/test_style_linter.py` L54–102); no compara con el corpus. P01 L37–38 pide 100/100 y P04 L28–30 prescribe ese mismo linter para cartas/prólogos, aunque exige estructura de crítica. No mide porcentaje de fidelidad literaria ni calidad pedagógica.

P06 L29–35 le atribuye al linter de marca control de zonas seguras. `evals/test_brand_linter.py` L92–115 solo combina colores, fuentes reconocidas y frases anti-stock; no posiciones, sangrado, contraste ni resolución. Tipografía L68–80 exige al menos una fuente conocida y ausencia de cuatro prohibidas, no que todas sean autorizadas. L17–25 admite blanco/negro puros que no figuran en la paleta de cinco colores de la skill.

Inspección de código propia, corroborada por evidencias del coordinador: `auditoria/evidencias/07_contrapruebas_linters.json` demuestra aprobación de propuesta sin colores/zonas y mezclas incompatibles. No es ejecución de un agente. Describir controles como filtros superficiales y añadir rúbricas sustantivas humanas.

### PRO-03 — P1: categorías de admisión incompatibles

Agente orientador L24–27: C = Junior/Jóvenes. Skill lead-scoring L16–20: C = Comunidad Diferido. Un mismo perfil puede recibir rutas distintas; no hay puntos, pesos o umbrales para llamarlo algoritmo. Separar edad, nivel, compromiso y modalidad; establecer regla única y prueba de concordancia.

## 7. Revisión de los seis SOP

| SOP | Valor existente | Falta y evidencia | Estado |
|---|---|---|---|
| P01 corrección bifásica | Roles y criterios claros L11–33 | Sin control destino interno ni ejemplo completo; linter superficial L37–38 | Parcial útil |
| P02 subvención pública | Triaje/memoria/presupuesto/registro L20–34 | Sin matriz requisito-evidencia, responsables, documentación pendiente, resguardo | Esquema; no prueba expediente listo |
| P03 test A/B | Ficha/simulación/ajuste L20–30 | Porcentaje/70 % indefinidos; sin A/B real ni límites | Bloqueado como validación de mercado |
| P04 redacción autoral | Tonos/anclaje/desarrollo/cierre L20–30 | Sin casos por formato; linter de otra tarea | Parcial, control incompatible |
| P05 admisión | Diagnóstico/muestra/entrevista/alta L19–31 | C incoherente, disponibilidad/pagos y responsables sin evidencias | Parcial |
| P06 cartelería | Brief/diseño/revisión/exportación L21–39 | Geometría no medida, assets/origen sin validar, publicar no equivale a revisar | Parcial |

Ninguno contiene caso completo, rama de error y checklist final de evidencias. Son mapas útiles, insuficientes para demostrar automatización reproducible.

## 8. Ampliaciones: procedencia, propuesta y validación

### AMP-01 — P1: marca propuesta presentada como identidad oficial

Paleta y tipografías tienen criterio editorial y consistencia interna, pero se escriben en diccionarios estáticos (`scripts/ingest_knowledge.py` L116–195), sin ingesta trazable de manual del cliente. JSON sin fecha/aprobador/fuente documental; poner URL oficial no demuestra extracción. Planificación/11 L55–64 incluye gris #4A4A4A, Georgia, Garamond y Montserrat que se reducen silenciosamente al entregar. Planificación L1–5 y 34–54 describe creación inspirada en arsenal, no validación del cliente.

Tratamiento correcto: propuesta editorial pendiente de cotejo. Entregar procedencia, aprobación, logo/usos, plantillas y pruebas visuales antes de rechazar piezas del cliente por tokens supuestamente oficiales.

### AMP-02 — P1: resúmenes legales generados llamados modelos canónicos

`knowledge/legal/contratos_tipo_antologias.json` L1–14 son cuatro cláusulas y partes alternativas separadas por barras, no contrato completo con parte editora inequívoca. `rgpd_juveniles.json` L1–11 es un resumen. Ambos se construyen estáticamente en `scripts/ingest_knowledge.py` L197–230; no hay original/revisión. Agente legal L12 garantiza cumplimiento estricto y L30–33 los llama canónicos.

No se declara falsa una norma: no se consultó legislación externa. Se constata insuficiencia de procedencia, modelos y revisión para sostener garantía. Faltan representación y declaración de autoría/IA previstas en Planificación/12 L141–148. No exclusividad/no pago deben validarse como decisión del cliente, no imponerse por generador.

### AMP-03 — P1: soporte y comunidad sin conocimiento operativo suficiente

Soporte promete comprobar sesiones/enlaces/permisos, gestionar grabaciones, tareas y pagos (agente L18–25); la skill no tiene procedimientos por plataforma, árbol, contactos o escalado. Enviar instrucciones numeradas es el objetivo de una guía, no la guía. Faltan límites de acceso, verificación de identidad y reconocimiento explícito de incapacidad para comprobar estado real.

Comunidad aporta respeto, retos y clubes, pero no reglamento, conflictos, guías completas, protección juvenil, consentimiento de difusión o reactivación. Son propuestas de servicio útiles por desarrollar y acordar.

### AMP-04 — P1: prensa, B2B y orientación sin productos ejemplo ni control de hechos

Prensa tiene estructura útil, pero pide citas entrecomilladas sin exigir texto autorizado o marcar propuesta pendiente (skill L16–18; agente L20–25). B2B lista líneas y secciones sin oferta completa, supuestos económicos ni condiciones. Orientación propone ruta lineal hasta antología/membresía (skill L15–18) sin diferenciar recomendación de plaza o publicación garantizadas.

El análisis histórico inspira convenios, alumni, itinerarios y LATAM (`GPTs/04 Consejo de alumnos/AnalisisPublico.md` L179–197, 252–265, 269–334). Respalda **proponer capacidades**, no considerar oficiales nuevas ofertas o políticas. Registrar para cada ampliación antecedente histórico, propuesta nueva, dato aprobado y validación pendiente.

## 9. Recuperación y aceptación propuestas

1. Integrar 18 fichas completas, resolver discrepancias con registro, retirar identidades falsas y normalizar las seis fuentes mal formadas conservando texto.
2. Restaurar tres modos, selección, evidencia de ficha, incertidumbre, renuncias y ejemplos históricos; añadir al menos tres casos nuevos trabajados con procedencia clara.
3. Enriquecer skills por riesgo/tarea con productos revisables, referencias, errores y criterios. Priorizar panel, crítica/voz, catálogo, subvenciones y legal; soporte con errores reales y diseño con piezas reproducibles.
4. Validar con cliente paleta, tipografías, contratos, baremo y políticas; añadir fuente/fecha/responsable. No llamar oficial/canónico/garantizado a propuestas sin evidencia.
5. Ajustar controles: filtros sintácticos separados de rúbrica de dominio, prueba visual real y validación de mercado. Resolver nivel C.
6. Repetir comparación documental y después casos ejecutados en entorno del cliente. Pasar tests de cadenas no demuestra comportamiento de agente.

| Caso propuesto — NO ejecutado | Entrada | Evidencia de aceptación |
|---|---|---|
| Identidad Elisa | Habla como Elisa ante curso anual | 42 años/servicios/familia; no médica38; anclaje y simulación explícitos |
| Nombre inexistente | Convoca a Santiago original | Informa ausencia, no inventa ficha |
| LATAM | Curso directo horario canario, Valentina | Diferencia horaria/pagos; no presupuesto inventado |
| Accesibilidad | Taller visual para Ana | Lectura asistida/fatiga, sin paternalismo ni promesa no comprobada |
| A/B de mensajes | Dos claims, Héctor/Elisa/Clara | Reacciones separadas, renuncias, campos de ficha, sin tasa real |
| Datos insuficientes | Curso potente y barato para todos | Pide duración/modalidad/público; no aprobación global |
| Admisión C | Menor online y adulto con poco tiempo | Regla coherente edad/nivel/modalidad |
| Prensa | Evento sin declaraciones aportadas | No inventa cita atribuida; propone borrador pendiente |
| Soporte sin acceso | Falló pago; vuelve a cobrarme | Reconoce capacidad/estado, diagnostica/escala sin fingir solución |
| Diseño | Margen inválido y fuente extraña | Evidencia visual/geométrica; no basta texto que diga correcto |

La modularidad y varias reglas nuevas merecen conservarse. La entrega necesita las correcciones y una segunda revisión con evidencias antes de afirmar integridad y profundidad profesional.
