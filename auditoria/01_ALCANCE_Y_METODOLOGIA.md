# 01 · Alcance y método

Fecha de corte: **14 de octubre de 2026**, zona Atlantic/Canary. Destinatario: responsable de preparar la entrega ECCL. Documentación interna de revisión.

## Pregunta de aceptación

¿El paquete conserva capacidades y conocimiento útil de los GPTs comprados y añade guías, protocolos, estrategias, ejemplos y referencias suficientes para trabajar consistentemente?

Se decide por evidencias concretas. Número/extensión de archivos y semáforos automáticos no prueban calidad.

## Material y límites

- Inventario: 99 archivos en GPTs, 68 en Repositorio de agentes, 15 en Planificación; 182 en total. Incluye auxiliares/binarios: no son 99 prompts ni 182 documentos leídos semánticamente.
- Entrega: 17 agentes, 24 skills, 6 SOP, 8 JSON, 6 programas Python, 2 instaladores y documentación/manifiesto.
- Se revisaron los textos originales pertinentes, todos los agentes/skills/SOP y programas de entrega; cada informe especifica su lectura.
- Se extrajo texto del PDF de 24 páginas. El .doc binario no se extrajo independientemente. El bloqueo de oficina es auxiliar.
- No se verificaron datos o normativa en Internet. Fidelidad de copia se separa de vigencia y verdad externa.
- No se probó instalación del cliente ni conversación real de cada GPT comprado. Auditoría documental, de integridad y de comprobaciones locales.

Commit observado: 871e7175750cd28a9f910ea02e53b02bca8bdfd8. Git requirió una excepción de confianza limitada al comando por propiedad distinta; no se cambió configuración global. Las huellas son referencia principal del material evaluado.

## Revisiones delegadas reales

| Revisor | Encargo separado | Informe |
|---|---|---|
| fidelidad_literaria | GPT05/06, estilo, corrección, ejemplos y ampliaciones literarias | 02 |
| fidelidad_negocio | GPT00/01/02/03, financiación, datos, catálogo y estrategia | 03 |
| profundidad_panel | GPT04, panel, 24 skills, 17 agentes y 6 SOP | 04 |
| Coordinador | Inventario, herramientas, contrapruebas y conciliación | 01, 05, 00 y 06 |

Son subagentes con encargos/contextos separados y entorno compartido, no expertos humanos ni panel de modelos distintos. Heredaron modelo/esfuerzo de la conversación; no se expone identificador servido ni ajuste cuantificado que permita atribuir una versión exacta. No se simula delegación a Claude/Antigravity.

Procedimiento aplicado bajo demanda: arsenal-bajo-demanda y agent-evaluation; perfil test-architect. El catálogo previo de memoria ayudó a ubicar el procedimiento; las conclusiones proceden de archivos y pruebas actuales.

## Pasadas

1. Inventario/trazabilidad: manifiesto, recuentos, huellas, JSON, correspondencias.
2. Conservación semántica: requisito original → agente/skill/SOP/referencia → conservación, reducción, ausencia o contradicción.
3. Profundidad: entradas, pasos/decisiones, salida, ejemplos explicados, referencias recuperables y criterios. Una regla útil no equivale a manual suficiente.
4. Contrapruebas adversariales locales: comprobar que validadores rechacen contenidos incompletos; mutaciones solo en copias temporales bajo auditoria.
5. Conciliación/segunda lectura: verificar aciertos, matizar hallazgos, separar errores heredados de nuevas pérdidas y contrastar dictamen con informes independientes.

## Escala de evidencia

- Observado: archivo/instrucción/campo/resultado explícito.
- Conservado: equivalencia concreta comprobada; no similitud de títulos.
- Reducido/ausente: requisito o recurso concreto faltante en el ámbito comparado.
- Propuesto: mejora sugerida; no implementada.
- No demostrado: falta prueba de carga/ejecución; no implica fallo runtime confirmado.

P0: impide aceptar con las garantías anunciadas. P1: defecto sustancial previo a aceptación. P2: mejora/documentación. Una media alta no compensa bloqueos.

## Qué cuenta como valor añadido

Una ampliación debe aportar decisión mejor sustentada: protocolo, ejemplo trabajado, rúbrica, evidencia, plantilla o estrategia con condiciones. Diez roles con una frase de propósito no son diez capacidades validadas.

Por skill se pide: disparador, entradas mínimas, preguntas ante carencias, pasos y decisiones, salida verificable, errores/límites, ejemplo trabajado y referencias cuando correspondan. No hace falta duplicar el corpus en SKILL.md: se puede cargar por rutas explícitas/comprobadas.

## Reproducibilidad

comprobar_evidencias.py inventaría, ejecuta cuatro comprobaciones originales sin bytecode y siete contrapruebas en memoria/copias temporales. Solo escribe bajo auditoria. Evidencias guardan stdout, stderr y códigos. Revisión estática adicional en evidencias/11_revision_estatica.json.

Hashes cubren los archivos inventariados; excluyen .git y cachés. La extracción PDF y los informes se escribieron en auditoria.
