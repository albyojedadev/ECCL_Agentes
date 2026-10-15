# 09 · Reevaluación y dictamen final

**Fecha:** 15 de octubre de 2026.
**Versión evaluada:** ECCL Agent Suite 2.0.0.
**Dictamen:** **APTA para entregar como repositorio corregido y base de una prueba piloto controlada.**

Este dictamen sustituye el estado operativo del informe inicial del 14 de octubre. La primera auditoría se conserva como evidencia del punto de partida y no se ha reescrito para ocultar los defectos encontrados.

## Qué ha cambiado

| Hallazgo inicial | Estado tras la corrección | Evidencia principal |
|---|---|---|
| Manual de Antonia truncado | Cerrado | Copia íntegra de 17.982 caracteres, comparada con el original y cargada por las skills autorales |
| Manuales y veinte pares de crítica omitidos | Cerrado | Dos manuales y 20 pares completos accesibles; índice de calibración y protocolo bifásico |
| Panel de alumnos incompleto y contradictorio | Cerrado | 18 perfiles normalizados; los 15 campos originales de cada ficha individual se conservan y los conflictos quedan explícitos |
| Capacidades históricas reducidas | Cerrado documentalmente | Agentes, skills y protocolos recuperan coordinación, Copycat, BI cultural, dirección, panel, voz y crítica con procedimientos y ejemplos |
| Siete filas de cursos desplazadas | Cerrado sin inventar datos | 73 registros conservados, 71 ID de curso distintos, id_registro estable, fila original, recibos y periodo textual separado |
| Datos históricos tratados como actuales | Cerrado como regla de uso | Disponibilidad no_verificada, ediciones terminadas identificadas y verificación exigida antes de comunicar |
| Skills demasiado breves | Cerrado documentalmente | Las 24 incluyen método, decisiones, salida, ejemplo, excepción/control y referencias aplicables |
| Evaluador y linters con falsos positivos | Cerrado para los casos reproducidos | 32 regresiones cubren agentes vacíos, catálogos incompletos, benchmark inválido, fuga de rutas, estilo, geometría y valores no finitos |
| Instalación y compatibilidad afirmadas sin prueba | Cerrado con alcance preciso | Instalación real en carpeta separada, validación del destino, carga de contexto, reconstrucción reproducible y manifiesto Claude validado |

## Conservación y trazabilidad

- Se volvieron a comparar 114 archivos de fuentes y planificación: cero modificaciones.
- El manifiesto registra 99 entradas originales: 98 archivos conservados íntegros y un bloqueo temporal de ofimática excluido con motivo.
- La reconstrucción portable produce los mismos archivos normalizados y las mismas huellas.
- Los nueve JSON de origen defectuosos permanecen archivados; las reparaciones son mecánicas, limitadas y tienen recibo.
- El corpus literario normalizado contiene 57 objetos completos de seis bancos. Dos fragmentos truncados de origen se registran como tales y no se completan con texto inventado.
- Se conservan 73 filas de cursos, 58 docentes y 18 avatares. Los datos no confirmados mantienen ese estado.

## Calidad del contenido

La revisión posterior no se limitó a contar secciones. Los equipos de corrección y el revisor independiente comprobaron procedimientos, ejemplos, excepciones y referencias en los 17 agentes, 24 skills y 6 protocolos.

Los documentos explican cómo actuar ante falta de información, conflictos de fuente, permisos insuficientes, datos históricos, decisiones editoriales, riesgos de privacidad y herramientas no disponibles. También incluyen casos trabajados: viabilidad económica y caja, memoria de subvención, panel sintético, crítica bifásica, curaduría con derechos, comunicación, soporte y control gráfico.

## Pruebas de comportamiento

Se ejecutaron los 26 casos definidos para cubrir los 17 agentes. Cada traza contiene entrada, salida generada, archivos cargados, entorno y revisión manual criterio por criterio. La consolidación pasó el validador con 26 casos y tres criterios por caso.

La prueba se amplió cuando el input inicial no permitía evaluar la tarea completa:

- E13, E14 y E25 se repitieron después de endurecer el control de acceso a manuscritos; las tres salidas piden autorización/contexto y no producen crítica.
- E13-C y E14-C usan textos sintéticos completos y autorización docente de prueba para comprobar la crítica bifásica.
- E17-C usa tres textos sintéticos y permisos diferenciados para comprobar selección, orden y límites de derechos.
- Nueve respuestas del commit anterior se conservaron como baseline. Sirven para demostrar mejoras concretas, como el bloqueo de crítica sin rol, una escala de admisiones coherente y la separación entre propuesta de marca y política oficial.

La prueba no es una tasa estadística de calidad ni una validación de la voz por Antonia Molinero. E03 y E05 demuestran respuesta prudente y método ante inputs incompletos; no demuestran reutilización de antecedentes ni análisis de tres filas reales. Esos dos escenarios quedan recomendados para la aceptación del cliente con materiales autorizados.

## Pruebas técnicas finales

| Prueba | Resultado | Qué acredita |
|---|---|---|
| Verificación del paquete | Superada | Inventario 17/24/6, enlaces activos, schemas, fuentes y manifiestos |
| Regresiones | 32/32 | Fallos concretos reproducidos y controles estructurales |
| Revisión de trazas | 26/26 registros válidos | Integridad de evidencia y revisión manual; no calidad estadística |
| Linter gráfico adversarial | 21/21 casos | Rechazo de NaN, ±Inf y geometría inválida |
| Instalación a destino limpio | Superada | Copia, huellas y verificación contra el destino |
| Carga desde instalación | Superada | Contexto, referencias y manual completo accesibles en la copia |
| Reconstrucción portable | Idéntica | Mismos archivos y huellas normalizadas |
| Manifiesto Claude | Válido | Estructura del plugin; no inferencia autenticada |

## Dictamen y límites de aceptación

La pérdida documental detectada en la primera auditoría está subsanada. Los componentes ya no son frases sueltas creadas para cumplir una lista: contienen guías de decisión, protocolos, ejemplos, referencias, condiciones de rechazo y trazabilidad al material comprado. Las ampliaciones nuevas se distinguen del material heredado y las propuestas institucionales no se presentan como aprobadas.

El repositorio queda apto para entrega y para una prueba piloto controlada. Antes de producción, el cliente debe validar tres elementos que solo puede aprobar él: voz autoral, marca/políticas institucionales y comportamiento en su sesión autenticada con sus materiales. También debe confirmar la vigencia de cursos, convocatorias, precios y normas cuando una tarea los use.

No quedan pérdidas documentales conocidas que bloqueen la entrega. Quedan validaciones humanas y operativas del destino, expresamente documentadas para que no se confundan con garantías ya obtenidas.

## Expediente consultable

- Auditoría inicial: 00_DICTAMEN_EJECUTIVO.md a 08_CONCILIACION_Y_SEGUNDA_REVISION.md.
- Correcciones: CORRECCION_CORE.md, CORRECCION_LITERARIA.md y CORRECCION_OPERATIVA.md.
- Revisión independiente: reevaluacion/REVISION_ADVERSARIAL_FINAL.md.
- Trazas consolidadas: reevaluacion/RESULTADOS_COMPORTAMIENTO.json.
- Cierre reproducible: reevaluacion/PRUEBAS_DE_CIERRE.json y reevaluacion/COMPARACION_DOCUMENTAL.json.
