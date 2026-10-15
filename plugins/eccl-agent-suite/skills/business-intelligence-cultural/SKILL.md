---
name: business-intelligence-cultural
description: Validar y cruzar datos ECCL para analizar matrículas, captación SEO/SEM, rentabilidad, caja 90 días, benchmarking, impacto cultural y tendencias con escenarios y trazabilidad reproducibles.
---

# Inteligencia cultural, educativa y económica ECCL

## Encargo y productos

Usa para diagnóstico cuantitativo, preparación/limpieza, comparables, finanzas ligeras, digital, impacto y radar narrativo. Entradas: pregunta de decisión, archivos/permisos, periodo, unidad de observación, definiciones de métricas y restricciones. Salidas: informe de calidad, dataset derivado con diccionario/procedencia, indicadores reproducibles, comparables/radar, escenarios, informe ejecutivo y registro de decisiones. Sin datos suficientes entrega plantilla o análisis parcial; no genera resultados ficticios para completar un panel.

Referencias: [metodología original de ocho fases](../../knowledge/sources/GPTs/02%20Analista%20de%20datos/metodologia.txt), [nueve funciones](../../knowledge/sources/GPTs/02%20Analista%20de%20datos/funcion.txt), [seguridad](../../knowledge/sources/GPTs/02%20Analista%20de%20datos/seguridad.txt), [benchmark histórico](../../knowledge/sources/GPTs/03%20Experto%20de%20la%20escuela/Benchmark_Analisis_Competidores.md) y [CSV de competencia](../../knowledge/sources/GPTs/03%20Experto%20de%20la%20escuela/Benchmark_Competidores_Escuela_Literaria.csv). Para datos institucionales utiliza el índice y reglas de [catalogo-academico-eccl](../catalogo-academico-eccl/SKILL.md). Precios/cursos/competidores históricos no prueban estado actual.

## 1. Definir pregunta y calidad antes de inferir

1. Escribe decisión, horizonte y unidad: persona, matrícula, grupo, sesión, evento, publicación, campaña o transacción. Una persona puede tener varias matrículas; no confunde ambas.
2. Registra archivo/origen, versión/fecha de extracción, periodo, propietario del dato, permisos y columnas. Conserva original y trabaja sobre copia derivada permitida. Si no puedes crear copia, documenta transformaciones propuestas sin afirmar ejecución.
3. Comprueba formato/codificación/aridad CSV, tipos, monedas/unidades, fechas y zona, claves, duplicados exactos y de negocio, nulos y valores atípicos. CONSULTAR/NO APLICA/ILIMITADO no se convierten indiscriminadamente en cero. Un valor negativo puede ser devolución: verifica antes de borrar.
4. Identifica coherencia: inicio ≤ fin, inscritos frente a capacidad, pagos frente a matriculados, periodos comparables y denominadores. No rellena campos desplazados por intuición; registra incidencia y la conciliación autorizada.
5. Entrega tabla de incidencias: fuente/fila/clave, campo, hallazgo, severidad, tratamiento propuesto/aplicado, responsable y efecto en análisis. Una corrección propuesta no está confirmada.
6. Gate de datos: bloquea solo métricas afectadas por incidentes críticos. Puede informar del subconjunto válido, indicando cobertura/faltantes. No llama validado al conjunto entero si parte sigue incierta.

## 2. Construir dataset estratégico reproducible

Define claves y granularidad de cada tabla antes de unir. Documenta cardinalidad esperada (uno-a-uno/uno-a-muchos), número de filas antes/después y totales de control. Si una matrícula se une a cuatro sesiones, no suma su importe cuatro veces; agrega al nivel adecuado antes del cruce. Usa diccionario `variable | definición | unidad | fórmula/origen | periodo | nulos | límites` y registro de transformaciones con versión.

Cruces útiles originales: ingreso × estacionalidad × modalidad; engagement × consultas/matrícula × coste; financiación × colaboraciones × impacto cultural. Solo si periodos y claves permiten compararlos. Correlación exploratoria es asociación, no causalidad; un aumento simultáneo de campaña y matrículas puede coincidir con calendario o un cambio de precio.

## 3. Indicadores y denominadores

| Indicador | Fórmula y unidad | Límite de interpretación |
|---|---|---|
| Ocupación | Matriculados confirmados / capacidad del mismo grupo | Si capacidad ilimitada o desconocida, no procede porcentaje |
| Conversión consulta→matrícula | Matrículas atribuibles / consultas comparables de la misma cohorte/ventana | Distingue personas/consultas y retraso de conversión |
| CTR | Clics / impresiones × 100 | No equivale a matrícula; plataformas/campañas comparables |
| CAC | Gasto de captación atribuible / nuevos alumnos atribuidos | Denominador cero: no definido; no mezclar atribución duplicada |
| Ticket medio | Ingresos netos / matrículas comparables | Distingue descuentos, impuestos, devolución y cobro |
| Margen de contribución | Precio neto − coste variable unitario | Debe ser positivo para equilibrio convencional |
| Resultado de grupo | n × (precio neto − variable) − fijo atribuible | Aclara costes incluidos/excluidos y devengo frente a caja |
| Equilibrio en personas pagadas | techo(fijo / contribución unitaria) | Solo con contribución >0 y coste/precio confirmados; capacidad limita viabilidad |
| Continuidad | Personas elegibles que continúan / personas elegibles de cohorte | Define ventana, bajas y reingresos |
| Caja final | Inicial + cobros de periodo − pagos de periodo | Ingreso facturado no es cobro; ayuda solicitada no es caja |
| Impacto de producción | Productos finalizados/verificados, participantes únicos y seguimiento | Una producción/satisfacción no demuestra mejora causal |

SEO: consultas/páginas, clics orgánicos, periodo, posiciones si fuente las aporta y contexto. SEM: gasto, clics, leads y atribución. Redes: define engagement y denominador por plataforma; no suma métricas incompatibles. Explica resultado en lenguaje claro y no recomienda gastar por un CTR alto si no hay conversión/coste posterior.

## 4. P&L, caja 90 días y escenarios

Recoge capacidad, preinscritos, pagos confirmados, precio neto, descuentos/devoluciones, coste docente, fijos/variables y calendario. Umbral de ocupación histórico no sustituye punto de equilibrio. Con contribución ≤0, declara inviabilidad de la fórmula ordinaria y revisa estructura, no devuelve un número negativo de alumnos.

Caja 90 días: saldo inicial confirmado; filas con fecha, concepto, cobro/pago, comprometido/estimado, importe, fuente y escenario. Resume por semana/mes según decisión. Separa pendiente de cobro, solicitado y concedido; no mete subvención posible como cobro seguro. Señala semana de saldo insuficiente y alternativas de calendario/costes, sin inventar crédito o cofinanciación.

Escenarios conservador/base/expansivo varían supuestos justificados (matrículas pagadas, coste, demora de cobro), muestran sensibilidad y condición de revisión. No asigna probabilidad ni intervalo estadístico sin modelo/datos válidos. Horizonte 2–5 años: exploración estratégica con señales y contingencias; no predicción precisa por la autoridad del agente.

## 5. Benchmark y radar narrativo-cultural

Selecciona comparables por público/nivel, horas, formato, territorio, producto y apoyo docente. Matriz `entidad | curso | fecha/fuente | precio neto/condiciones | horas | modalidad | público | propuesta | comparabilidad/vacíos`. No ordena por precio absoluto sin horas, tamaño y servicios. Histórico sirve para hipótesis, no tarifa actual.

Radar: tema/género/formato → señal histórica → evidencia actual fechada y alcance → explicación alternativa → hipótesis ECCL → experimento → criterio de revisión. Google Trends, redes y medios solo cuando herramientas realmente consultadas; si no, registra búsqueda pendiente. Volumen relativo de interés no prueba ventas ni calidad literaria. Combina señales con matrículas/entrevistas antes de priorizar turismo literario, narrativa digital u otras líneas.

Financiación inteligente: cruza calendario oficial y capacidad del proyecto con Analista de Subvenciones; no puntúa elegibilidad por palabras clave. Impacto: separa actividades realizadas, productos, resultados observados y cambio atribuible. Cada indicador tiene instrumento, momento, responsable y limitación; no mide reputación sumando likes sin marco.

## 6. Informe y control humano

Entrega pregunta/alcance → fuentes/calidad/cobertura → resultados/fórmulas → interpretación y límites → opciones A/B y escenarios → recomendación condicionada → responsable/fecha de revisión. Usa tablas/gráficos si aclaran, siempre con interpretación. Describe formatos creados de verdad; sin herramienta de exportación, entrega tabla editable y no afirma haber generado Excel/PDF. Revisa totales, unidades y fechas antes de cerrar. Dirección confirma decisiones; no envías bases ni actúas en cuentas por elaborar informe.

## Ejemplo trabajado 1: calidad y duplicación de uniones

Caso nuevo didáctico: matrículas M01/G1/100 €, M01/G1/100 € duplicada, M02/G1/importe vacío; sesiones G1/S1 y G1/S2. Original tres filas de matrícula. Registra duplicado posible y nulo, pide confirmación. Confirmado duplicado, dataset derivado tiene M01 por 100 € y M02 desconocida: ingreso conocido 100 €, no total cerrado. Si une cada fila a ambas sesiones obtiene cuatro filas derivadas; sumar importe daría 200 € conocidos, error. Agrega ingresos por grupo antes de unir con conteo de sesiones. Informe: dos matrículas distintas, una con ingreso conocido, dos sesiones; ticket medio global pendiente. No convierte M02 a cero.

## Ejemplo trabajado 2: apertura y caja

Caso ficticio: fijo 900 €, precio neto 120 €, variable 20 €, capacidad 15. Equilibrio = 9 pagos. Conservador 6: resultado −300 €; base 9: 0 €; expansivo 12: 300 €. Opción A abrir con 9 pagos y docente confirmado; B posponer/reducir fijo si no llegan. Caja inicial 500 €, cobro de 9 matrículas 1.080 € en día 10, pago fijo 900 € día 1 y variable 180 € día 20. Resultado final de grupo 0 €, pero caja en día 1 = −400 €: no puede abrir sin resolver calendario/tesorería. Pide acuerdos reales de cobro/pago; no inventa financiación. Sensibilidad: fijo 1.300 € exige 13 pagos; 12 ya no cubre costes.

## Ejemplo trabajado 3: campaña e impacto

Caso ficticio de una misma ventana/cohorte: 10.000 impresiones, 200 clics, 20 consultas distintas, cuatro nuevas matrículas atribuidas y gasto 160 €. CTR 2%; consulta→matrícula 20%; CAC 40 €. No denomina conversión 20% a clic→matrícula (sería 2%). Si otra plataforma atribuye esas mismas cuatro personas, deduplica antes de sumar. Seis participantes entregan borrador y cuatro revisión: informa cuatro revisiones verificadas, sin concluir mejora causal o éxito de todos. Propón rúbrica inicial/final y seguimiento con permisos para observar evolución.

## Excepciones y seguridad

Sin acceso a analytics/CRM/Trends, solicita exportación o presenta método pendiente; no simula ejecución. Dataset pequeño o sesgado: describe limitación, evita segmentación que identifique personas y no generaliza a todo el alumnado. Coste/fecha contradictorios: retén conclusión afectada, presenta versiones y responsable. No reconstruyas identidad de menores por cruces; agrega o suprime celdas si hace falta para la finalidad. Exporta solo columnas necesarias a destino autorizado.

## Criterios de aceptación

Pregunta/unidad/periodo definidos; calidad y transformaciones registradas; nulos no inventados; claves y totales conciliados; fórmulas/denominadores trazables; métricas digitales/culturales además de economía; escenarios separados de hechos; evidencia actual distinta de histórico; interpretación sin causalidad infundada; opciones y siguiente control humano. Un gráfico bonito o JSON válido no reemplaza ninguno de estos controles.
