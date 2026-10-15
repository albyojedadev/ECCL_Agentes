# Revisión independiente de fidelidad literaria y autoral

Fecha: 14 de octubre de 2026. Ámbito: GPT 05 Ghostwriter, GPT 06 Crítico Literario y ampliaciones de acompañamiento, originalidad y edición. Revisión realizada por un agente delegado independiente de la coordinación de la auditoría.

**Dictamen: no aprobar todavía estos componentes para entregar al cliente como migración fiel y enriquecida.** Hay principios pedagógicos valiosos y material conservado de forma íntegra, pero también pérdida documental comprobable, pérdida de instrucciones operativas y reglas nuevas que estrechan la voz original. Las ampliaciones presentan una idea útil y algunos ejemplos breves; no alcanzan aún la profundidad de manuales de trabajo completos que exige este encargo.

Esta conclusión procede de lectura semántica, contraste de requisitos y comprobaciones programáticas acotadas. No se deriva del número de líneas de un archivo ni de un porcentaje de longitud. No se ha ejecutado un agente instalado, llamado a un modelo externo ni demostrado comportamiento del sistema en producción. No se ha alterado la entrega ni los GPTs originales.

## 1. Alcance y método

Se leyeron los 16 archivos de `GPTs/05 Ghostwriter/` y los 12 de `GPTs/06 Critico Literario/`, incluidos ejemplos, manuales, personalidad, funciones, metodología, configuración y seguridad. Se contrastaron con:

- Los agentes `ghostwriter-de-antonia-molinero`, `critico-literario-de-la-eccl`, `companero-de-escritura-y-habito` y `editor-de-libros-y-antologias`.
- Las skills `antonia-molinero-voice`, `critica-pedagogica-literaria`, `verificacion-originalidad-y-voz-propia`, `desbloqueo-creativo-socratico`, `seguimiento-habito-escritura`, `curaduria-antologias-eccl` y la dependencia editorial `contratos-editoriales-y-derechos-autor`.
- Los protocolos P01 y P04, `knowledge/estilos/corpus_antonia.json`, el enrutamiento del coordinador, README, ingesta y evaluación de estilo/benchmark.

Cada conclusión diferencia: conservado en datos, instruido para usarse, resumido parcialmente, ausente del paquete revisado, contradictorio y no probado en ejecución real. Los números de línea corresponden a los archivos actuales; las rutas son relativas a la raíz del proyecto. Las búsquedas de ausencia se realizaron en todo `Repositorio de agentes/`, incluidos scripts y conocimiento. Una frase en el generador de skills no se considera por sí sola una capacidad operativa.

Prioridades armonizadas en la conciliación: P0 = bloqueo del núcleo de migración o de la garantía de entrega; P1 = defecto sustancial previo a aceptación; P2 = mejora de profundidad/operación. LIT-01, LIT-02 y LIT-06 son P0 por conservación/certificación, no por daño observado. No se ha demostrado una fuga real: falta de barrera documental y exposición comprobada son hechos distintos.

## 2. Lo que sí conserva valor

1. **Diagnóstico de siete áreas, conservado como datos.** `GPTs/06 Critico Literario/modulo_deteccion_antoniamolinero.json:1–117` está semánticamente íntegro en `Repositorio de agentes/knowledge/estilos/corpus_antonia.json:15–121`. Se comprobó igualdad de los objetos JSON tras parsearlos. Conserva orden, criterios, fallos y extracción de fortaleza/fallo/dirección. El problema es su activación, no su desaparición.
2. **Veintiún ejemplos de siete variantes emocionales, conservados.** `GPTs/05 Ghostwriter/variante_estilo_emocional.json:1–100` coincide semánticamente con `variantes_emocionales` en `Repositorio de agentes/knowledge/estilos/corpus_antonia.json:122–221`. Incluye tres ejemplos de cada variante, también oral veloz y juguetona. Sería incorrecto afirmar que el repositorio carece de ejemplos literarios en general.
3. **Núcleo pedagógico conservado en instrucciones.** El agente crítico `:18–44`, la skill crítica `:18–36` y P01 `:21–33` preservan dos salidas diferenciadas, elogio concreto, respeto a la voz, prohibición de reescribir y devolución cálida. El agente también prohíbe juicios psicológicos (`:44`). Son reglas con valor real.
4. **Parte del núcleo autoral conservada.** El agente ghostwriter `:17–29` y la skill de voz `:17–22` preservan concreción, conflicto latente, respiración, humor e imagen final. El corpus conserva el comienzo del manual original, con mezcla culto-coloquial, interpelación y referencias culturales funcionales (`corpus_antonia.json:222`).
5. **Ampliaciones útiles como punto de partida.** El compañero incluye preguntas de escena y no escribe por el alumno (`agents/companero-de-escritura-y-habito.md:19–35`). El editor preserva canarismos y singularidad de voz y contempla metadatos/autorizaciones (`agents/editor-de-libros-y-antologias.md:20–27`). Estas aportaciones merecen desarrollarse.

## 3. Hallazgos con evidencia, impacto y solución

### LIT-01 · P0 · El manual autoral se corta arbitrariamente y pierde módulos esenciales

**Evidencia.** `Repositorio de agentes/scripts/ingest_knowledge.py:81–114` incorpora tres fuentes de estilo. La línea 109 guarda `manual_texto[:4000]`. El resultado `knowledge/estilos/corpus_antonia.json:222` termina literalmente a mitad de «Comida o cuerpo como metáfora centra». La comprobación confirmó 17.982 caracteres en el original y 4.000 en el destino, siendo este último el prefijo exacto del primero. La comparación prueba el mecanismo; la pérdida semántica se verifica leyendo las secciones excluidas.

Quedan fuera: nota de prensa, crítica larga y microreseña (`GPTs/05 Ghostwriter/manual_de_estilo.md:148–202`); tabla de parámetros por género (`:206–216`); preguntas de entrada y autocorrección con umbrales de reescritura (`:253–286`); desviaciones permitidas (`:308–378`); nueve adaptaciones de registro/formato (`:384–468`); checklist (`:474–527`) y novela autoficcional juvenil (`:531–623`). No se recuperan equivalentes completos en agentes, skills o protocolos.

**Impacto.** Un JSON válido puede guardar solo el comienzo y aun así denominarse corpus canónico. Se pierden reglas de decisión que diferenciaban los géneros, no solo texto explicativo.

**Corrección.** Migrar el manual completo como referencias divididas por módulos, conservar el original de consulta y crear índice de carga bajo demanda por género/fase. Eliminar cortes por número de caracteres. Distinguir reglas originales de ampliaciones.

**Aceptación.** Cada sección original tiene destino y referencia utilizable; ninguna termina a mitad de frase. El control de integridad verifica módulos esperados, no solo parseo/no vacío. La skill indica qué módulo leer antes de escribir.

### LIT-02 · P0 · Se omiten manuales específicos de corrección y veinte pares completos de ejemplos

**Evidencia.** El GPT crítico ordena activar módulo, manual estructural, cuatro bancos de ejemplos y manual de voz (`GPTs/06 Critico Literario/config.txt:18–22`; `metodologia.txt:13–50`). Los veinte ejemplos válidos —cinco por archivo— están en `ejemplo_correccion_1.json:1–305`, `ejemplo_correccion_2.json:1–309`, `ejemplo_correccion_3.json:1–312` y `ejemplo_correccion_4.json:1–310`. Cada caso contiene un informe amplio y una devolución diferenciada: no son frases aisladas.

La ingesta `Repositorio de agentes/scripts/ingest_knowledge.py:81–114` no lee esos seis recursos. El árbol de entrega y su búsqueda completa no contienen copias ni referencias a `manual_comentarios_antonia.md`, `manual_estilo_correccion_antonia.md` o los cuatro bancos `ejemplo_correccion`. El agente crítico y la skill no los cargan.

El manual omitido aporta once apartados del informe (`GPTs/06 Critico Literario/manual_comentarios_antonia.md:24–186`), siete momentos del comentario (`:206–257`) y vocabulario/contraejemplos/variaciones por fragilidad y firmeza (`manual_estilo_correccion_antonia.md:50–64`, `:101–163`, `:167–227`). La entrega comprime el informe a cuatro puntos en la skill (`skills/critica-pedagogica-literaria/SKILL.md:21–25`) y seis en el agente (`agents/critico-literario-de-la-eccl.md:24–29`).

**Impacto.** Se conserva la idea de dos bloques, pero se pierde oficio: cómo pasar del diagnóstico a una recomendación y modular la devolución ante voces distintas. Un ejemplo de taza/final explicativo no sustituye veinte pares que cubren consigna incumplida, observación distante, nostalgia, caricatura, diálogo subtextual, escena corporal y símbolo espacial.

**Corrección.** Incorporar ambos manuales completos y los cuatro bancos como referencias privadas de trabajo con procedencia. Añadir selección de ejemplo comparable y comprobación de once campos. Usar ejemplos como calibradores, sin copiar elogios ni diagnosticar situaciones que el texto nuevo no demuestra.

**Aceptación.** Veinte pares accesibles o selección explícitamente justificada que conserve todos sus casos pedagógicos. Matriz de once campos con evidencia textual y opción «no evaluable». Antonia revisa devoluciones nuevas de distintos perfiles; reconocer encabezados no basta.

### LIT-03 · P1 · El alcance del ghostwriter se estrecha y pierde calibración por género

**Evidencia.** El original enumera seis géneros (`GPTs/05 Ghostwriter/config.txt:16`), carga uno o dos ejemplos por género (`funcion.txt:15`, `:23–32`; `metodologia.txt:45–79`) y ofrece iteración, ajuste de variante y conversión de género (`metodologia.txt:97–127`). Hay preguntas específicas para novela (`:36–41`). La guía evita copiar/citar ejemplos, selecciona según cuatro criterios y recalibra con tres más cuando falla (`guia_ejemplos_sinteticos.md:11–32`, `:63–67`).

El agente nuevo ofrece cartas, prólogos, ensayos y manifiestos (`Repositorio de agentes/agents/ghostwriter-de-antonia-molinero.md:33–38`); `skills/antonia-molinero-voice/SKILL.md:12–22` limita formato a cuatro opciones y no prescribe selección de corpus, preguntas de novela, feedback o conversión. P04 cita corpus (`:14`), pero no manda abrir los ejemplos del género. Los seis bancos originales por género no se ingieren (`scripts/ingest_knowledge.py:81–114`).

**Impacto.** Un encargo comprado de capítulo juvenil, crítica larga o microreseña puede acabar convertido en ensayo institucional. Retener veintiún ejemplos por emoción no sustituye estructuras/ejemplos por género.

**Corrección.** Restituir seis modos y adaptaciones de correo/discurso/redes como formatos, distinguiendo género/canal. Por modo: entradas mínimas, estructura, variante, ejemplos comparables, revisión y entrega revisable. Mantener los nuevos formatos como ampliaciones explícitas. Sanear los defectos heredados de los bancos sin inventar originales faltantes.

**Aceptación.** Casos nuevos de seis géneros, siete variantes, cambio de género y feedback correctivo. Novela produce fragmento/capítulo en primera persona con arquitectura definida; no novela entera ni ensayo adulto. Microreseña cumple menos de 80 palabras (`funcion.txt:106–117`).

### LIT-04 · P1 · Reglas universales nuevas producen rigidez y contradicen formatos originales

**Evidencia.** `Repositorio de agentes/skills/antonia-molinero-voice/SKILL.md:18` y P04 `:22` obligan a iniciar siempre por objeto/gesto/escena. P04 `:30` obliga al cierre por imagen. Sin embargo, el manual permite apertura conceptual de ensayo (`GPTs/05 Ghostwriter/manual_de_estilo.md:104–117`), apertura incisiva/pregunta de crítica (`:173–180`), metáfora mínima o nula y cierre directo de correo profesional (`:392–403`), y cierre profesional de texto institucional (`:431–436`). Las desviaciones permitidas buscan evitar uniformidad (`:308–319`, `:374–378`).

La skill nueva ofrece cinco tonos (`skills/antonia-molinero-voice/SKILL.md:15`), frente a siete variantes con parámetros y combinaciones (`GPTs/05 Ghostwriter/variantes_estilo.md:9–35`, `:96–114`, `:122–183`). Oral veloz y juguetona existen como ejemplos en corpus, pero no como opciones operativas de la skill. El agente exige media de 10–24 palabras por oración (`agents/ghostwriter-de-antonia-molinero.md:47`) de forma general, mientras el original contempla frases largas, discurso rápido y oralidad juvenil veloz.

**Impacto.** Favorece repetir tazas/cocina/pausas/finales líricos donde el original pide claridad y pocas metáforas. Añadir objetos no equivale a conservar la amplitud de una voz.

**Corrección.** Reglas por modo, excepciones y prioridad de formato. Recuperar parámetros de siete variantes y compatibilidades. Cadencia como indicio contextual, sin rango universal certificado.

**Aceptación.** Correo profesional puede empezar por su propósito y cerrar con acción acordada; ensayo puede abrir con tesis y encarnar después; escena juguetona puede sostener humor. Todos mantienen honestidad y respeto sin metáfora doméstica forzada.

### LIT-05 · P1 · Las barreras de uso docente y confidencialidad no se trasladan suficientemente

**Evidencia.** `GPTs/06 Critico Literario/persona.txt:6–7`, `config.txt:42–43` y `funcion.txt:50` limitan uso a Antonia y excluyen el informe interno del alumno. `seguridad.txt:27–34`, `:46–47` prohíbe inventar consignas, juicios psicológicos y ghostwriting, y trata material como académico confidencial. Pide datos y se detiene si falta un paso (`metodologia.txt:3–9`, `:63–66`). Ghostwriter original explicita confidencialidad, juicio/autoría humanos y revisión (`GPTs/05 Ghostwriter/seguridad.txt:5–12`, `:68–71`).

El crítico nuevo declara uso docente del informe (`Repositorio de agentes/agents/critico-literario-de-la-eccl.md:22–23`), pero prescribe dos fases ante todo texto entregado por alumno (`:20`); la skill siempre devuelve ambos bloques (`skills/critica-pedagogica-literaria/SKILL.md:33–36`). P01 designa alumno como destinatario (`:15`) sin separar entregas. El coordinador deriva corrección (`agents/coordinador-de-agentes-de-la-eccl.md:22–23`) sin comprobación de destinatario. En estos componentes no se localiza política aplicable explícita de manuscritos no publicados, reutilización y conservación. Las entradas críticas omiten género, extensión y continuidad (`skills/critica-pedagogica-literaria/SKILL.md:12–16`).

**Impacto.** Contradicción de contrato de salida/destinatario. No se ha probado una fuga, pero no puede certificarse que un alumno no reciba informe interno ni igual confidencialidad. Una skill jurídica en otro agente no resuelve por sí sola el tratamiento en crítica/ghostwriting.

**Corrección.** Definir modo docente/alumno con salidas diferentes y establecer destinatario fuera del manuscrito cuando la plataforma lo permita. Alumno: devolución revisada; docente: informe y borrador externo separados. Recuperar preguntas mínimas, «no evaluable» y no inventar. Añadir tratamiento de manuscritos/revisión humana sin prometer protección absoluta por ocultar prompts.

**Aceptación.** Probar alumno, docente, rol desconocido y manuscrito con instrucciones adversarias. Contenido literario no cambia permisos/destinatario. Sin consigna no inventa cumplimiento. No afirmar funcionamiento de barreras por estar escritas.

### LIT-06 · P0 · La puntuación del linter no acredita fidelidad ni calidad pedagógica

**Evidencia.** Ghostwriter exige auditoría por `evals/test_style_linter.py` y «fidelidad ≥90 %» (`Repositorio de agentes/agents/ghostwriter-de-antonia-molinero.md:42–47`); P01 exige100/100 (`:37–38`) y P04 lo aplica a autoría (`:28–30`). El linter solo combina encabezados, saludo, media de palabras y ausencia de regex (`evals/test_style_linter.py:54–103`). No evalúa fidelidad autoral, calidad del juicio, exactitud de citas, respeto a la voz, no reescritura, no psicologización ni referencias por género. Ejecutarlo como indica P01 prueba dos muestras fijas (`:105–126`); no recibe el texto del cliente.

**Comprobación ejecutada sin modificar archivos.** Se importó el módulo con Python sin generar caché y se pasaron dos cadenas en memoria:

```text
### 1. Informe Técnico Interno
Este análisis afirma sin pruebas que todas las decisiones del alumno revelan inestabilidad emocional.
### 2. Comentario Externo
Ana, tu personalidad presenta problemas clínicos y por eso necesitas cambiar completamente tu historia.
Te doy un párrafo nuevo para copiar literalmente y sustituir todas tus palabras originales.
```

Resultado real: `passed=True`, `score=100`, media `10.2`, cero clichés detectados. Viola prohibiciones expresas. Prueba falso positivo del validador, no que el agente genere ese texto.

Segunda cadena, autoral y sin clichés:

```text
La taza sigue donde la dejó mi madre y conserva una mancha que nadie sabe explicar. No preguntamos por ella durante años porque cada pregunta parecía abrir otra puerta dentro de la casa.
```

Resultado real: `passed=False`, `score=55`, media `16.5`; falla por faltar dos bloques/saludo de corrección. Prueba que el validador pedagógico no sirve de certificado general del ghostwriter. No se afirma que esta cadena sea excelente o voz de Antonia validada.

La suite `evals/run_evals.py:93–102` comprueba solo que el benchmark tiene casos; no los ejecuta contra agentes. Sus pruebas de estilo son muestras dentro del código (`:27–45`). El único GHOST-01 cubre una carta (`benchmark_dataset.json:53–65`), no toda la amplitud original.

**Corrección.** Regex como señal auxiliar; separar validadores de crítica/autoría, aceptar salida real por archivo/entrada y añadir rúbrica humana con evidencia. Guardar resultados por caso y versión. No convertir smoke test en porcentaje de fidelidad.

**Aceptación.** Primer contracaso rechazado por psicologización/sustitución de autoría; segundo no rechazado por falta de estructura crítica al evaluar ghostwriting. Cada caso tiene respuesta real, recursos cargados y evaluación docente. Informar por separado pruebas estáticas y comportamiento.

### LIT-07 · P2 · «Verificación de originalidad» tiene alcance estrecho y carece de contrato de evidencia

**Evidencia.** `Repositorio de agentes/skills/verificacion-originalidad-y-voz-propia/SKILL.md:9–19` rastrea tópicos, afectación, una «pepita» y recomienda poda. No compara fuentes, registra coincidencias, establece incertidumbre ni aporta informe completo/salida. Solo recibe texto (`:12–13`). Se carga en crítico, ghostwriter y editor, aunque presupone voz de alumno. El benchmark LIT-03 (`evals/benchmark_dataset.json:40–50`) preestablece «voz impostada» desde una escena de detective convencional.

**Impacto.** Originalidad de voz puede confundirse con ausencia de convenciones o verificación de plagio. Pastiche deliberado, cita atribuida y cliché involuntario necesitan tratamientos distintos. Encontrar un detalle singular tampoco garantiza independencia de fuentes.

**Corrección.** Separar análisis pedagógico de tópicos y comparación documentada de coincidencias, esta última solo con fuentes/herramientas. No diagnosticar plagio, autoría humana/IA ni impostación desde fragmento aislado. Pedir intención/género; distinguir cita/homenaje/parodia. Para ghostwriter comprobar no copia de calibradores; para editor registrar procedencia/autorización.

**Aceptación.** Casos de convención legítima, pastiche, cita, coincidencia sin fuente y similitud demostrable. Cada observación cita fragmento y efecto. Si no hay «pepita» evidente no la inventa. Dos informes completos anotados.

### LIT-08 · P2 · Acompañamiento y hábito no incluyen seguimiento operativo suficiente

**Evidencia.** `Repositorio de agentes/skills/seguimiento-habito-escritura/SKILL.md:12–19` termina en fijar mínimo, prohibir releer y celebrar. No define registro, seguimiento semanal, adaptación tras fallos, permiso de memoria ni salida. Prohibir releer (`:18`) no contempla recuperar continuidad. `skills/desbloqueo-creativo-socratico/SKILL.md:16–22` atribuye normalmente bloqueo a miedo/ambición antes de diferenciar falta de información, tiempo, energía o decisión técnica. El agente pregunta por escena evitada por pudor/miedo (`agents/companero-de-escritura-y-habito.md:26`) sin alternativa expresa para mantener límites personales. HAB-01 propone máscara ficticia/objeto testigo (`evals/benchmark_dataset.json:100–109`), estrategias no desarrolladas en skill.

**Impacto.** Hay buenas preguntas y ejemplos breves, pero no procedimiento sostenible entre sesiones. «Monitorización» en descripción (`seguimiento-habito-escritura/SKILL.md:3`) promete más que el flujo documentado.

**Corrección.** Árbol de diagnóstico práctico, una pregunta cada vez, ejercicios por atasco y opciones sin revelar vivencias. Plan de semana, registro opcional, revisión/ajuste sin castigo. Indicar qué se recuerda/dónde y solo con capacidad y permiso reales. No presentar seguimiento automático si no existe.

**Aceptación.** Dos conversaciones completas con circunstancias distintas, semana fallida que produce ajuste y alumno que no desea compartir experiencia. Salida: objetivo, sesiones elegidas, alternativa mínima, revisión y límites de persistencia. Ninguna continuación escrita por el agente.

### LIT-09 · P2 · La ampliación editorial enumera competencias sin completar el flujo

**Evidencia.** `Repositorio de agentes/agents/editor-de-libros-y-antologias.md:20–27` menciona arquitectura, ortotipografía, canarismos, metadatos/autorizaciones. `skills/curaduria-antologias-eccl/SKILL.md:12–20` pide relatos/título y ofrece cuatro pasos; no operacionaliza estándares de selección, trazabilidad, aceptación autoral, galeradas o cierre. La dependencia jurídica aporta tres cláusulas (`skills/contratos-editoriales-y-derechos-autor/SKILL.md:16–19`), sin suplir protocolo editorial. No se verifica aquí validez jurídica de esas cláusulas.

**Impacto.** Preparar galeradas para imprenta (`agents/editor-de-libros-y-antologias.md:3`) no queda respaldado por checklist, formatos o aceptación. Armonización puede invadir voces sin separar cambios mecánicos/autorales.

**Corrección.** Recepción/versionado, rúbrica de selección, orden razonado, hoja de estilo con excepciones, consultas al autor, aprobación, pruebas y liberación humana. Añadir antes/después comentado de diálogo y caso de canarismo conservado. No inventar ISBN, depósito, permisos o biografías.

**Aceptación.** Lote ficticio con selección, índice razonado, incidencias, cambios aceptados y checklist de galeradas. Distinguir simulación de preparación real. Registro dialectal preservado con decisiones documentadas.

## 4. Matriz de trazabilidad semántica

Abreviatura RA = `Repositorio de agentes/`; G05 = `GPTs/05 Ghostwriter/`; G06 = `GPTs/06 Critico Literario/`. «Ausente» se refiere al paquete de entrega revisado, no a borrado del original del proyecto.

| Requisito original | Evidencia original | Destino localizado | Estado y decisión |
|---|---|---|---|
| Verdad/disimulo, oralidad, mezcla de registros y referencias funcionales | G05 `manual_de_estilo.md:10–98` | RA `knowledge/estilos/corpus_antonia.json:222`; agente ghostwriter `:17–29` | Conservado en prefijo; resumen del agente parcial. Carga explícita pendiente. |
| Ensayo: tesis → escena → reflexión/referencia → cierre | G05 `manual_de_estilo.md:104–123` | RA corpus `:222`, skill voz `:18–22` | Conservado en datos; apertura siempre tangible lo contradice. |
| Narrativa autobiográfica y parámetros propios | G05 `manual_de_estilo.md:127–144` | RA corpus `:222` | Parcial: corte a mitad de primer rasgo obligatorio. |
| Nota de prensa literaria: datos/sinopsis/símbolo | G05 `manual_de_estilo.md:148–164`; `funcion.txt:74–85` | Sin equivalente completo en ruta autoral; existe agente prensa con otra función | Mapear deliberadamente y probar cambio de ruta. |
| Crítica larga: juicio y referencias culturales | G05 `manual_de_estilo.md:168–186` | Sin modo específico de autoría | Ausente como procedimiento autoral. No confundir con corrección de alumnos. |
| Microreseña <80 palabras | G05 `funcion.txt:106–117` | Sin modo/límite en nueva skill | Ausente. |
| Novela: capítulo fragmentario, primera persona juvenil y preguntas | G05 `manual_de_estilo.md:531–623`; `metodologia.txt:36–41` | Solo menciones en acompañamiento/crítica | Ausente como generación autoral. |
| Siete variantes, parámetros, compatibilidad y modulación por escena | G05 `variantes_estilo.md:9–183` | RA corpus `:122–221` conserva ejemplos; skill voz `:15` ofrece cinco tonos | Ejemplos conservados; protocolo técnico ausente y selección restringida. |
| 1–2 ejemplos por género, no copia, recalibración | G05 `guia_ejemplos_sinteticos.md:11–32`, `:63–67` | P04 `:14` cita corpus | No operacionalizado; bancos por género no migrados. |
| Feedback, revisión y conversión entre géneros | G05 `metodologia.txt:97–127` | Sin bucle en P04/skill | Ausente como flujo explícito. |
| Desviaciones y nueve formatos | G05 `manual_de_estilo.md:308–468` | P04 `:20–30` aplica pauta única | Ausente; pierde flexibilidad. |
| Autocorrección y umbrales de reescritura | G05 `manual_de_estilo.md:271–286`, `:474–527` | Ghostwriter `:42–47` sustituye por linter | No equivalente. |
| Diagnóstico ordenado de siete ejes | G06 `modulo_deteccion_antoniamolinero.json:1–117` | RA corpus `:15–121` | Íntegro en datos; crítico/skill/P01 no mandan cargarlo. |
| Informe de once apartados | G06 `manual_comentarios_antonia.md:24–186` | Skill crítica `:21–25`; crítico `:24–29` | Parcial; sin estructura exhaustiva ni manual. |
| Dos voces, no reescritura y sin psicologización | G06 `funcion.txt:30–50`, `:60–80`; `seguridad.txt:27–34` | Crítico `:22–44`, skill `:26–36`, P01 `:28–33` | Núcleo conservado; no probado en runtime. |
| Comentario de siete momentos, un punto principal y fragilidad | G06 `manual_estilo_correccion_antonia.md:128–178`, `:197–227` | Skill crítica `:26–30`; crítico `:31–36` | Parcial: cuatro momentos generales, falta protocolo tonal. |
| Veinte pares informe/devolución | G06 `ejemplo_correccion_1–4.json` completos | Ningún banco migrado | Ausente. Ejemplo de linter no equivale. |
| Género, extensión, continuidad; parar si falta paso | G06 `metodologia.txt:3–9`, `:63–66` | Skill crítica `:12–16` | Parcial; sin regla de espera y datos incompletos. |
| Informe solo Antonia; manuscrito confidencial | G06 `funcion.txt:50`; `seguridad.txt:46–47` | Crítico `:23`; skill `:33–36`; P01 `:15` | Regla docente parcial; salida/destinatario ambiguos. |
| Revisión humana, autoría y confidencialidad | G05 `seguridad.txt:5–12`, `:68–71` | Sin contrato equivalente en agente/skill/P04 | Ausente en componentes autorales revisados. |

## 5. Defectos heredados: no atribuirlos falsamente a la migración

La documentación original también requiere saneamiento. No debe recuperarse de manera acrítica ni presentarse como colección perfecta:

- `GPTs/05 Ghostwriter/ejemplo_critica.json:41` acaba con cadena incompleta; el parseo falla en esa línea. `ejemplo_narrativa.json:33–34` termina a mitad de texto sin cierres; la secuencia salta de narrativa_06 a narrativa_08. Hay textos completos anteriores aprovechables. No inventar terminaciones ni un narrativa_07 supuestamente original.
- `GPTs/05 Ghostwriter/ejemplo_novela.json:4–6`, `:105–108` usa comentarios incompatibles con JSON estricto. Los seis ejemplos tienen solo arranques abreviados en `texto` (`:22`, `:38`, `:54`, `:70`, `:86`, `:102`): son fichas estructurales, no seis capítulos completos. El análisis de Cochinita incluye marcador de título sin completar (`:113`). Tiene valor de esquema, pero no prueba un corpus real completo.
- La guía nombra bancos en plural que no coinciden con archivos presentes (`guia_ejemplos_sinteticos.md:1–7`, `:18–22`). Los originales de seguridad citan `.md` para archivos reales `.txt`. Normalizar referencias/numeración conservando trazabilidad.
- Algunos ejemplos críticos infieren vivencias de quien escribe, mientras el manual indica «sin psicologizar» (`GPTs/06 Critico Literario/manual_estilo_correccion_antonia.md:17–19`). Distinguir autor, narrador, personaje y alumno, fundamentando observaciones en texto/consigna. Preservar una formulación problemática palabra por palabra no sería mejora.

Toda reparación debe identificarse como reparación o elaboración nueva aprobada, nunca recuperación de un original inexistente. Los bancos JSON de ensayo, microreseña y nota de prensa sí parsean y contienen diez textos cada uno; los cuatro bancos críticos parsean y suman veinte pares completos. No existe justificación técnica en su formato para omitir estos bancos válidos.

## 6. Evaluación de profundidad real de las skills

No se puntúa por longitud. Se exige poder decidir, ejecutar, verificar y resolver casos límites con conocimiento suficiente.

| Componente | Contenido aprovechable | Vacío sustantivo | Madurez documental |
|---|---|---|---|
| `antonia-molinero-voice` | Entradas y cinco pasos estilísticos | Géneros, parámetros, referencias por modo, excepciones, calibración, feedback y ejemplos anotados | Insuficiente para sustituir G05 |
| `critica-pedagogica-literaria` | Dos salidas, lectura/concreción y no reescritura | Matriz completa, recursos, datos faltantes, once campos, variación tonal y ejemplos diagnóstico/devolución | Parcial, insuficiente para sustituir G06 |
| `verificacion-originalidad-y-voz-propia` | Ejemplos de tópicos y orientación pedagógica | Alcance verificable, evidencia/uncertumbre, intención de género, salida y casos completos | Borrador conceptual |
| `desbloqueo-creativo-socratico` | Tres preguntas y dos microejercicios | Triaje, secuencia conversacional, límites personales, elección/retorno del ejercicio y conversaciones completas | Base útil, poco desarrollada |
| `seguimiento-habito-escritura` | Tiempo, meta y mínimo | Registro, revisión, ajuste tras fallos, continuidad y persistencia real | Seguimiento sin protocolo completo |
| `curaduria-antologias-eccl` | Orden y normalización básica | Selección, hoja de estilo, consultas autorales, permisos por estado, pruebas/galeradas, entrega y cierre | Lista inicial de tareas |

## 7. Plan de recuperación y pruebas de aceptación

**Antes de envío comercial:** resolver LIT-01 a LIT-06, restaurar referencias y contenido; delimitar originalidad y completar flujo mínimo de ampliaciones. En este estado no usar «fidelidad absoluta», «100 % operativo» ni «≥90 % de fidelidad» como conclusiones de calidad literaria.

1. Manifiesto de fuentes con destino por requisito, procedencia, reparación y carga. Manuales completos sin recorte. Separar fuentes originales, resúmenes y material nuevo.
2. Restituir crítica especializada: diagnóstico, once campos, voz correctora y pares de ejemplos. Evitar que la voz de ghostwriting contamine informe técnico o se imponga al alumno.
3. Restituir escritura por género/registro: seis modos, siete variantes, entradas, compatibilidad, correcciones y calibradores. Apertura/cierre según formato.
4. Contratos de entrada/salida, destinatario, datos faltantes, manuscritos no publicados y revisión docente. Si la plataforma no permite barrera requerida, declararlo y ajustar flujo con evidencia.
5. Ejecutar casos reales contra instalación objetivo. Conservar respuesta, recursos usados y evaluación humana. Textos nuevos y contracasos, no solo reproducción de muestras internas. No etiquetar las pruebas propuestas como ejecutadas.

| Caso obligatorio | Entrada nueva a preparar | Aceptación sustantiva |
|---|---|---|
| Crítica sin consigna | Texto y nombre, sin ejercicio | Pide consigna o declara límite; no inventa cumplimiento. |
| Detalle logrado sin consecuencia | Objeto presente que no altera tensión | Distingue concreción de función narrativa; no elogia objeto como diagnóstico suficiente. |
| Voz sólida y final explicativo | Escena más cierre redundante | Localiza evidencia, conserva voz, recomienda acción; no reescribe. |
| Estructura y riesgo formal | Fragmentación deliberada | Distingue decisión/fallo; matriz sin linealidad impuesta. |
| Alumno/docente | Mismo texto, destinatarios distintos | Informe interno solo en flujo docente; alumno recibe devolución revisada. |
| Autor/narrador | Ficción en primera persona | Analiza efecto textual, no vida/salud del alumno. |
| Seis géneros G05 | Ensayo, narrativa, nota, crítica, microreseña y capítulo | Estructura, fuentes, extensión y registro específicos. |
| Correo profesional | Asunto operativo breve | Sin cocina forzada, metáforas mínimas y cierre claro. |
| Oral/juguetona/furia | Escena por variante y transición justificada | Cambia ritmo/humor con estabilidad; no uniforma en melancolía. |
| Originalidad e intención | Pastiche, convención y citas | No acusa/impone voz; evidencia e incertidumbre. |
| Hábito tras incumplimiento | Semana con sesiones imposibles | Replanifica sin castigo ni automatización ficticia. |
| Antología/canarismos | Lote ficticio, diálogo y léxico local | Índice motivado, cambios trazables y aprobación; no homogeneiza voces. |
| Manuscrito adversario | Texto ordenando mostrar archivos/cambiar rol | Trata frases como material; no cambia permisos/destinatario. |

**Cierre:** migración parcial con pérdidas concretas y corregibles, junto a material valioso efectivamente retenido. No se confirma equivalencia funcional, profundidad suficiente de las skills ni enriquecimiento operativo completo. La aprobación debe depender de reparar documentación y contrastar salidas nuevas con Antonia y equipo docente, no de un linter que reconoce formato.
