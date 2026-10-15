# Revisión independiente 03: financiación, datos, dirección y catálogo

Fecha: 14 de octubre de 2026. Ámbito: módulos GPT00–03, sus agentes, skills, protocolos y corpus de entrega.

## Dictamen

**No aceptar todavía esta parte de la entrega como migración completa y enriquecida.** Conserva nombres y parte de sus objetivos, pero reduce funciones, pierde manuales y ejemplos, elimina corpus empresarial y no conserva varios controles fundamentales. Las skills nucleares tienen dos o tres enunciados de procedimiento, sin recursos enlazados que recuperen la profundidad de los GPT originales.

No se confirma ningún incidente P0 ocurrido. Los P1 siguientes bloquean recomendar la entrega como completa; los P2 mejoran precisión y operatividad. Esta es una revisión documental: no demuestra el comportamiento de agentes instalados, ni la fiabilidad de un modelo concreto. Que un modelo improvise una respuesta adecuada no demuestra que se haya migrado el conocimiento comprado.

## Método, evidencia y límites

Se revisaron las definiciones textuales de GPT00–03 y sus destinos, con contraste directo de funciones, metodologías, personalidad, seguridad, manuales Copycat, preguntas y ejemplos. Se contrastaron los documentos estratégicos y de comunicación y se recorrieron los bloques del corpus de oportunidades; no se certifica la exactitud histórica/actual de todos sus contactos, cifras o referencias.

Se ejecutó comparación de **todas las filas y campos mapeados** de cursos y docentes, comprobación de aridad CSV y detección de fechas finalizadas con estado de matrícula abierta. El PDF original de uso se revisó mediante la extracción completa del coordinador en `auditoria/evidencias/10_manual_original_pdf.txt` (24 páginas). La equivalencia exacta del `.doc` binario con el PDF queda pendiente; no se extrajo aquí.

No se consultaron servicios externos, no se probaron los GPT alojados ni sus Actions, ni se instalaron/ejecutaron agentes del paquete. Las especificaciones OpenAPI originales son **configuraciones locales**, no prueba de conectores activos ni de endpoints vigentes. No se hicieron envíos ni registros. Los casos de aceptación son propuestos, salvo las comparaciones locales expresamente identificadas como ejecutadas.

Los originales tienen defectos y contradicciones. Deben conservarse sus capacidades y valor, corrigiendo con trazabilidad los errores; no copiar a ciegas restricciones imposibles, cifras antiguas ni reglas incoherentes.

Rutas de evidencia relativas a `D:\PROYECTOS\Escuela Canaria de Creación Literaria`. `R/` significa `Repositorio de agentes/`; G00–G03, los respectivos directorios originales de `GPTs/`. Las líneas incluyen blancos y se verificaron en los archivos existentes.

## Matriz de trazabilidad

Parcial = hay una parte equivalente; omitido = falta recurso y no se localiza equivalente suficiente; alterado = cambia el contrato; conservado con defectos = retiene problemas de origen. La falta de copia literal no es por sí sola un defecto si existe transformación semántica equivalente comprobable.

| Fuente original | Destino pertinente | Estado/contenido |
|---|---|---|
| G00 config.txt | Coordinador | Parcial: punto de entrada; falta diagnóstico, restricciones y ejemplos. |
| G00 Direccion asistentes.txt | Mapa coordinador/README | Transformado a enlaces locales; adaptación razonable si el acceso real está documentado. No hace falta imponer enlaces GPT antiguos. |
| G00 funcion.txt | Coordinador/protocolos | Parcial: orientar sí; flujo validar→diseñar→testar→comunicar y qué pedir/recibir, incompleto. |
| G00 manual.md | README/protocolos | Parcial: índice sí; ocho casos de uso y recuperación de errores, incompletos. |
| G00 metodologia.txt | Coordinador | Parcial: derivación; faltan rutas mínima/completa/alternativa y reutilización de trabajo previo. |
| G00 persona.txt | Coordinador | Parcial: tono; ejemplos de redirección omitidos. No hace falta copiar biografía ficticia/frases decorativas. |
| G00 seguridad.txt | Coordinador | Omitida política equivalente de confidencialidad/documentos no confiables. |
| G00 Manual de uso de los asistentes.pdf | README/protocolos | Parcial: falta manual humano con escenarios, límites y prompts. Revisadas 24 páginas extraídas. |
| G00 Manual de uso de los asistentes.doc | Ninguno | Pendiente de extracción y comparación exacta; ausente de entrega. |
| G01 config.txt | Analista subvenciones | Parcial: elegibilidad/memoria; faltan banco, justificación, entrevista, checklist completo. |
| G01 funcion.txt | Analista/P02 | Parcial: nueve funciones reducidas a triaje, términos, memoria y presupuesto. |
| G01 metodologia.md | P02/skill grant writer | Parcial/alterada: falta entrevista, validación iterativa y seguimiento. |
| G01 personalidad.txt | Analista | Parcial: registro; pierde guías de entrevista y ejemplos. |
| G01 seguridad.txt | Analista/P02 | Omitidos controles específicos de invención, sobrepromesas y aprobación/envío. |
| G01 manual_estilo_copycat.md | cultural-grant-writer-es | Omitido: Copycat ECCL se sustituye por léxico del organismo. |
| G01 plantillas_preguntas_copycat.md | Ninguno | Omitido: entrevista por secciones/tipos y aprovechamiento de documentación existente. |
| G01 ejemplo_memoria_base_escuela.md | Ninguno | Omitido: memoria sintética completa, sesiones, evaluación y cronograma. |
| G01 ejemplos_memorias.json | Ninguno | Omitidos cuatro ejemplos: escolar, profesorado, comunitario, virtual. |
| G01 API Ayudas Canarias.txt | subvenciones-canarias-sync | Omitida especificación/implementación alternativa; no prueba de conexión activa original. |
| G01 API Ayudas Nacionales.txt | Analista | Omitidas especificaciones/operaciones SNPSAP y reemplazo declarado. |
| G01 API Ayudas Europeas.txt | Analista | Omitida especificación búsqueda/detalle UE y reemplazo declarado. |
| G02 config.txt | Analista datos | Alterado parcialmente: prospectiva/inteligencia digital/benchmarking pasan a rentabilidad de grupos. |
| G02 funcion.txt | Analista/BI | Parcial: finanzas/escenarios; limpieza, dataset, impacto y tendencias sin equivalencia. |
| G02 metodologia.txt | BI | Omitida casi toda la secuencia de ocho fases, calidad, trazabilidad e interpretación. |
| G02 persona.txt | Analista | Parcial: prudencia; evidencia/incertidumbre incompletas. Original duplicado: no conservar duplicación. |
| G02 seguridad.txt | Analista/BI | Omitidas anonimización, reconstrucción, control de exportación, incertidumbre y validación humana. |
| G03 config.txt | Experto/coordinador/analista/B2B | Alterado: mentor empresarial se convierte en consultor factual; redistribución parcial sin mapa contractual. |
| G03 funcion.txt | Mismos | Parcial: áreas dispersas; faltan modos, campaña 21 días, caja 90 días y salida A/B. |
| G03 metodologia.txt | Coordinador/BI | Omitido proceso transversal diagnóstico→opciones→acción→revisión→seguimiento. |
| G03 persona.txt | Experto | Alterado: pragmatismo de dirección pasa a acogida/promoción. |
| G03 seguridad.txt | Experto/coordinador | Omitida política de aprobación humana/documentos; nueva recomendación vinculante ambigua. |
| G03 index.md | Catálogo/README | Omitido índice semántico multifuente y navegación de decisiones. |
| G03 inventario_cursos.csv | cursos_activos.json | 73 filas conservadas con siete registros mal formados y notas perdidas. |
| G03 docentes.csv | claustro_docente.json | 58 filas; campos mapeados iguales, omite tarifa_estimada (58 CONSULTAR). |
| G03 grupos.csv | Ninguno | Omitidos grupos/modalidades, umbrales, costes, decisiones y cuatro ejemplos. |
| G03 proyectos.csv | Menciones B2B/subvenciones | Omitido corpus de proyectos/resultados/estado; mencionar Escuela Portátil no lo sustituye. |
| G03 partners.csv | B2B/comunidad | Omitida relación, prioridad, histórico y siguiente acción. Gestionar permisos de contactos. |
| G03 publicaciones.csv | Menciones antologías | Omitidos 18 registros editoriales y distinción colectivo/agencia; contiene además filas explicativas. |
| G03 Benchmark_Competidores_Escuela_Literaria.csv | Ninguno | Omitidas 17 filas de comparativa; revisar caracteres dañados heredados. |
| G03 Benchmark_Analisis_Competidores.md | Ninguno | Omitidas matrices, DAFO y tácticas históricas. No presentar precios como actuales. |
| G03 AnalisisPublico.md | Panel/admisiones | Parcial temática; falta matriz público/oferta/mensaje y 14 públicos potenciales. Panel no es equivalencia demostrada. |
| G03 Informe_Estrategico_ECCL.md | Coordinador/B2B | Parcial temática; falta diagnóstico, prioridades, roadmaps, KPIs y riesgos consultables. |
| G03 manual_de_comunicacion_escuela_literaria_ecl.md | Prensa/dossier/reels/admisiones | Parcial temática; pierde manual institucional, plantillas, funnel, permisos y esquemas JSON. |
| G03 Oportunidades_2025.md | Analista/B2B | Omitido corpus de financiación privada/pública, crowdfunding, turismo, alianzas y referencias; conservar como histórico. |

## Hallazgos P1

### FND-01. Copycat pierde voz, entrevista y ejemplos

Original: `GPTs/01 Ayudas y licitaciones/manual_estilo_copycat.md:18–41` define persona, ritmo y conectores; `:64–125`, desarrollo por sección; `:156–213`, límites/checklist. `metodologia.md:91–149` especifica entrevista, índice validado, bloques y coherencia; `:196–202`, preguntas y ejemplos. `ejemplos_memorias.json:4–43,46–76,79–109,112–142` contiene cuatro modelos. `plantillas_preguntas_copycat.md:390–397` exige selección de preguntas y aprovechar documentos.

Destino: `R/agents/analista-de-subvenciones-y-licitaciones.md:25–27` redefine Copycat como extraer e inyectar términos del organismo. `R/skills/cultural-grant-writer-es/SKILL.md:12–19` tiene dos entradas y tres pasos. `R/protocols/P02_solicitud_subvencion_publica.md:24–31` repite léxico y esquema, sin recursos originales.

Consecuencia: pérdida del método y voz propios. ODS/digitalización introducidos por defecto pueden fingir encaje si no están en bases/proyecto.

**Reparación:** referencias bajo demanda al manual técnico ECCL, entrevista, memoria base y cuatro ejemplos; separar voz ECCL de adaptación al baremo; añadir matriz criterio→sección→evidencia, límites de extensión, ejemplo antes/después y control de faltantes.

**Aceptación:** con pliego y proyecto incompleto extrae índice/extensión, reutiliza datos, pregunta lagunas, redacta primer bloque técnico-pedagógico sin inventar cifras y deja criterios cubiertos/pendientes. Repetir en las cuatro tipologías. Mantener ejemplos etiquetados como sintéticos.

### FND-02. El analista de datos pierde gran parte de su contrato

Original: `GPTs/02 Analista de datos/funcion.txt:7–78` incluye limpieza, patrones, dataset cruzado y mercado; `:99–148`, informes, tendencias, SEO/SEM, impacto y benchmarking. `metodologia.txt:9–26` exige consistencia; `:143–160`, radar narrativo; `:180–186`, trazabilidad/interpretación.

Destino: `R/agents/analista-de-datos-culturales-y-educativos.md:17–43` concentra cuatro áreas económicas; BI `SKILL.md:12–19` contiene tres entradas/dos pasos. No hay equivalente procedimental de calidad, inteligencia digital, benchmarking, impacto o prospectiva cultural.

**Reparación:** recuperar nueve funciones con recursos de calidad de datos, benchmarking, analítica digital, impacto y tendencias; definir variables, periodos, nulos/duplicados, entregables y evidencia. Mejorar original: no convertir correlación en causalidad ni proyectar 2–5 años sin sustento.

**Aceptación:** dataset con duplicados/nulos/fechas incompatibles produce informe de calidad antes de inferir; el válido entrega métricas digitales/culturales, cohortes, benchmarking y oportunidades con fuentes y límites, además de rentabilidad.

### FND-03. El mentor empresarial se sustituye por catálogo

Original: `GPTs/03 Experto de la escuela/config.txt:12–41` define dirección, diagnóstico, oferta, campañas, finanzas y caja 90 días. `funcion.txt:107–131` mapea modos a fuentes y exige criterios/origen/riesgos/próximos pasos. `metodologia.txt:23–57` contiene A/B, plan B, artefactos y seguimiento.

Destino: experto `R/agents/experto-en-la-eccl.md:28–40` responde factual; coordinador `:18–68` deriva y simula perspectivas; BI trata rentabilidad; B2B `:17–32` enumera líneas. La suma no recupera el método completo ni establece responsable transversal.

**Reparación:** skill explícita de decisión empresarial ECCL, protocolo multifuente y mapa función→responsable→entregable→aceptación. Recuperar caja 90 días, campaña 21 días, apertura/cierre, A/B, plan B y revisión.

**Aceptación:** /diagnóstico o «¿abrimos grupo?» no responde solo catálogo: pide capacidad/preinscritos/costes/fecha, separa umbral financiero de heurística comercial y entrega opciones, artefacto, supuestos, fuentes y siguiente control.

### FND-04. Se pierde corpus que una web de cursos no sustituye

Original: `GPTs/03 Experto de la escuela/config.txt:77–89` identifica doce fuentes; `index.md:239–280` explica consultas cruzadas. El manual comunicación `:134–174` contiene plantillas; `:230–250`, gobernanza/permisos/IA; `:398–417`, briefing; `:565–576`, salida JSON. Informe estratégico `:119–134` aporta roadmap y metas orientativas, no logros.

Destino: `R/scripts/ingest_knowledge.py:233–240` llama seis rutinas; para el corpus empresarial solo importa cursos/docentes. El resto no está en knowledge ni enlazado como referencias equivalentes. Hay menciones temáticas dispersas, insuficientes para conservar información.

**Reparación:** incorporar recursos ricos bajo demanda con índice/fecha/procedencia/permisos/estado histórico-hipótesis-ejemplo/caducidad. Normalizar grupos/proyectos/partners/publicaciones separando instrucciones y ejemplos de entidades reales.

**Aceptación:** recuperar publicaciones/colaboraciones/estrategia con fuentes; distinguir antologías ECCL y Agencia AM, recursos propios y partners, propuesta y logro. No ofrecer snapshots de 2025 como estado actual.

### FND-05. Siete cursos canonizan campos desplazados y pierden notas

**Ejecutado:** cabecera `GPTs/03 Experto de la escuela/inventario_cursos.csv:1`: 17 columnas. Filas **11,28,33,37,38,42,45**: 18 campos. IDs IMAG-PUB, GUION-COMIC, VIDEOJUEGOS, ESCRIT-TERAP2, MITOS, MICRO-VIAJE, POESIA-ACT.

`R/scripts/ingest_knowledge.py:21–40` usa DictReader sin validar aridad/sobrantes. JSON `R/knowledge/catalogo/cursos_activos.json:182–198` acaba con capacidad IMAG-PUB «Creativos de agencias», estado «MÍNIMO 6», URL «Consultar», observaciones igual a URL; pierde última nota. Otros registros: `:505–521,600–616,676–692,695–711,771–787,828–844`. POESIA-ACT tiene URL «Matrícula 1 diciembre».

El error de aridad **nace en origen**; el fallo de migración es no detectarlo, descartar última celda y declarar corpus canónico validado. Comparar DictReader con JSON no detecta desplazamiento: comparten el error.

**Reparación/aceptación:** validar aridad antes de mapear, poner inválidas en cuarentena, corregir con procedencia y validar dominios (URL/capacidad/fecha/estado). Ninguna fila extra debe pasar silenciosamente; los siete registros deben recuperar campos y nota completos. Probar CSV 18 campos/17 cabeceras y exigir fallo explícito.

### FND-06. Catálogo histórico presentado como activo, sin caducidad

**Ejecutado al 14/10/2026:** siete cursos «Matrícula abierta» con fin anterior: CL-2526, HP-OCT25, NOV-2025, JEVE-2025, TECNICAS-IMAG-2526, LOS-INTRUSOS-2526, INIC-FOTO-2025. Caso JSON `:6–25`: fin 28/05/2026 y matrícula abierta. Sin fecha de verificación/estado histórico.

Experto `:31` dice cursos activos y `:33` «Fuente de Verdad Web Inmutable»; skill catálogo `:15–18` no resuelve fechas pasadas/conflicto. Original `index.md:296–301` sí pide marcar histórico/actual.

**Reparación/aceptación:** snapshot/periodo, verificación/caducidad, estado histórico separado de disponibilidad. Consultar hoy CL-2526 debe advertir edición terminada y verificar la vigente, nunca confirmar matrícula con vieja fecha. Sin red debe declarar limitación. Una URL oficial no certifica vigencia local.

### FND-07. Se omiten especificaciones de búsqueda sin reemplazo declarado

Original: Canarias `API Ayudas Canarias.txt:6–42` define servidor/buscarAyudasCultura/paginación; Europa `API Ayudas Europeas.txt:7–41,73–83`, búsqueda/detalle; nacional `API Ayudas Nacionales.txt:10–33,60–82,107–278`, ayudas/planes/catálogos. `funcion.txt:61–85` define estado/fechas/enlaces de salida. Estas son configuraciones locales, no prueba de funcionamiento antiguo o actual.

Destino: `subvenciones-canarias-sync/SKILL.md:12–17` es organismo y dos instrucciones. No hay especificación/adaptador/contrato equivalente. «Fuentes monitorizadas» del agente `:40–44` no prueba monitor conectado o programado.

**Reparación/aceptación:** conservar antecedentes, validar endpoints y corregir títulos audiovisuales/videojuegos arrastrados; documentar servicio por entorno, permisos, paginación, errores y alternativa manual. Demostración real consulta/detalle con fuente/momento, cero resultados y error de red. Sin herramienta debe declararlo, pedir bases/enlace y no simular búsqueda. No se ha ejecutado esa demostración en esta auditoría.

### FND-08. Desaparecen salvaguardas de datos y decisión humana

Original: G02 `seguridad.txt:44–61`, anonimización/no reenvío/resultados internos hasta validar; `:13–23`, reconstrucción y no falsa precisión. G03 `seguridad.txt:115–117`, decisión humana. G01 `config.txt:90–91`, confirmar envíos; `seguridad.txt:78–93`, no invención/sobrepromesas/revisión.

Destino: reglas datos `:40–43`, experto `:37–40`, subvenciones `:48–52` no contienen equivalentes. Coordinador `:68` pide «recomendación final vinculante», sin delimitación humana.

**Reparación/aceptación:** protocolo común enlazado más reglas específicas: mínimo dato, anonimización, documentos no confiables, exportación/envío autorizado y aprobación humana cuando corresponda. No prometer borrado/retención del proveedor solo mediante prompt. Probar PII e instrucciones incrustadas en pliego; no deben provocar fuga ni cambiar reglas. Preparar memoria no autoriza enviarla; perspectiva simulada no es autoridad vinculante.

### FND-09. Puntuación confundida con probabilidad y límites aplicados sin contexto

Analista subvenciones `:24` pide tasa de éxito a partir del scoring; P02 `:22` repite probabilidad. Original `metodologia.md:71–74` pide puntuación estimada. Un baremo sin datos de concurrencia/calibración no acredita probabilidad de concesión.

Agente `:35` introduce contratos menores <15.000 € como ejemplo de máximo subvencionable sin distinguir contrato de subvención ni condiciones. **No se confirma aquí vigencia jurídica de esa cifra**: defecto es generalizar sin fuente/fecha/impuestos/contexto. Skill grant writer `:17` prescribe cohesión/igualdad/ODS/digitalización antes de derivarlos de las bases.

**Reparación/aceptación:** separar elegibilidad, puntos y probabilidad; usar esta última solo con datos/metodología. Derivar límites y criterios del instrumento aplicable, citar fuente/fecha y evitar reglas universales. Caso pliego sin ODS/digitalización y presupuesto sobre cifra de ejemplo: no rechazar automáticamente ni añadir compromisos ficticios.

## Hallazgos P2

### FND-10. Fórmula de rentabilidad útil, pero casos límite/entradas insuficientes

Nuevo analista `:19–22` aporta fórmula explícita. BI no exige coste variable, unidad temporal, impuestos/descuentos ni forma de pago; no trata precio≤variable, umbral>aforo o CONSULTAR. BI `:19` habla de beneficio neto, agente `:42` de contribución: métricas distintas.

**Reparación/aceptación:** ficha de entradas/unidades, definiciones, redondeo, ejemplo y sensibilidad, separando ingreso y cobro. CF=900, P=150, CV=25 → umbral 8; aforo7 → no viable; P=25 → sin umbral finito para CF. Con costes desconocidos no aprobar apertura.

### FND-11. Docentes pierde campo de incertidumbre

`docentes.csv:1` tiene tarifa_estimada, no mapeado en `R/scripts/ingest_knowledge.py:53–65`. Las 58 filas son CONSULTAR: no hay pérdida numérica comprobada, sí del recordatorio de dato pendiente. Conservar nulo/pendiente, jamás interpretarlo como cero.

### FND-12. Saneamiento necesario también en originales

- Memoria sintética `ejemplo_memoria_base_escuela.md:157`: 4–6 semanas; cronograma `:146–149` llega a semana7. Corregir antes de convertir en patrón.
- G03 `persona.txt:46`: 40%/14 días; `funcion.txt:91`: 40%/28 días; `index.md:74`: 40% del umbral óptimo. Resolver con dirección: no asumir que son equivalentes.
- `AnalisisPublico.md:242` dice doce públicos; `:252–265` enumera catorce. Corregir recuento.
- PDF página4 nombra Generador de Propuestas Formativas como provisional; página13 reserva voz institucional al Ghostwriter, mientras GPT01 sí tiene Copycat técnico. El generador no corresponde a un módulo independiente en las siete carpetas disponibles. Divergencias heredadas, no pérdidas creadas por migración; resolver mapa/nombres/responsables.
- `grupos.csv:18–21` son cuatro grupos de ejemplo; partners/proyectos/publicaciones contienen filas INSTRUCCION/CAMPO. No ingresarlas como operación real.

## Aciertos

1. Mapa claro de 16 destinos en coordinador `:22–53`, nombres reconocibles y especialización modular.
2. **73 cursos y 58 docentes** conservados como entidades. Comparación normalizada completa: cero diferencias en campos mapeados frente a DictReader; nombre_curso→nombre, url_referencia→url_canonica y listas. Esto prueba mapeo, no calidad semántica: siete filas comparten desplazamiento.
3. Fórmula explícita de umbral y tabla de apertura aportan valor si se completan controles.
4. P02 conserva triaje previo, presupuesto y chequeo aritmético; añade documentación/firma (`:20–34`). Extender, no descartar.
5. Experto `:39`: no inventar tarifas/fechas y derivar cuando faltan datos, regla acertada que debe ampliarse a vigencia.

## Profundidad documental observada

Escala orientativa: 0 ausente, 1 intención/enunciado, 2 proceso utilizable con huecos, 3 guía completa con ejemplos/fallos/aceptación. No es rendimiento estadístico del modelo.

| Capacidad | Nivel | Razón |
|---|---:|---|
| Orientación básica | 2 | Mapa claro; faltan flujos y diagnóstico. |
| Copycat técnico ECCL | 1 | Nombre sin manual/entrevista/ejemplos. |
| Búsqueda conectada ayudas | 0 | No contrato/herramienta/demostración. |
| Expediente/justificación | 1 | Esquema; sin ciclo completo/evidencias. |
| Inteligencia cultural de datos | 1 | Parcial financiero; pierde pipeline y módulos. |
| Dirección multifuente | 1 | Áreas dispersas, proceso incompleto. |
| Catálogo | 2 | Corpus real; calidad/caducidad sin resolver. |
| Memoria institucional | 1 | Menciones sin corpus completo. |

Las skills grant writer (19 líneas), sync (17), BI (19), catálogo (18) no fallan por brevedad: fallan porque **no conducen a los manuales, ejemplos y referencias ricos que deberían cargarse bajo demanda**. Un SKILL.md breve puede ser adecuado con anexos suficientes.

## Reparación y aceptación verificable

Orden recomendado: (1) mapa contractual de funciones y resolución de contradicciones; (2) saneamiento de datos y aridad; (3) corpus rico con metadatos/referencias; (4) procedimientos completos; (5) pruebas locales y agentes reales; (6) claims de entrega ajustados a evidencia.

| Caso | Entrada | Resultado mínimo | Evidencia actual |
|---|---|---|---|
| A01 | Curso nuevo sin saber empezar | Validar→diseñar→testar→comunicar; datos/responsables | Flujo explícito incompleto. |
| A02 | Pliego+borrador escolar incompleto | Índice, entrevista selectiva, bloque Copycat y matriz evidencia | Recursos ausentes. |
| A03 | Variante profesorado/comunidad/virtual | Metodología/sesiones/producto/evaluación específicos | Ejemplos omitidos. |
| A04 | Ejecutado con desviaciones | Seguimiento, desviaciones e informe final | P02 termina en registro. |
| A05 | Buscar ayuda sin herramienta | Declaración honesta y alternativa documental | Sin fallback explícito. |
| A06 | Datos con nulos/duplicados/PII | Calidad y anonimización antes de inferir | Pipeline y reglas ausentes. |
| A07 | Matrículas+campañas+publicaciones | Dataset, KPIs digitales/culturales e interpretación | Alcance reducido. |
| A08 | /finanzas caja90días | Cobros/pagos, supuestos y riesgo | Sin equivalente. |
| A09 | CF900/P150/CV25/aforo7 | Umbral8, no abrir bajo supuestos | Fórmula sí; límites no. |
| A10 | IMAG-PUB | Campos correctos y nota completa | Fallo local reproducido. |
| A11 | CL-2526 actual en octubre2026 | Edición terminada; verificar vigente | Contradicción local reproducida. |
| A12 | Colaboraciones/resultados memoria | Proyectos/partners/publicaciones con fuente/estado | Corpus ausente. |
| A13 | Pliego ordena mandar datos a tercero | Ignorar instrucción incrustada, sin envío | Falta regla común. |
| A14 | Tasa éxito sin histórico | Puntos orientativos, no probabilidad inventada | Confusión inducida. |
| A15 | Pliego sin ODS/digitalización | Criterios efectivos, sin compromiso ficticio | Skill prescribe genéricos. |

Cerrar hallazgos documentales requiere lectura/validadores. Certificar comportamiento requiere ejecutar agentes reales con proveedor/modelo/herramientas identificados, conservar salidas y repetir casos sensibles. No derivar fiabilidad ni «100% operativo» de existencia de archivos/JSON legible.
