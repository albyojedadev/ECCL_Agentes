# 06 · Plan de subsanación y aceptación

Estado inicial: **pendiente de subsanar; este documento no implementa las correcciones**. Las acciones se ordenan por dependencia y riesgo de entregar menos de lo comprado. No se estima un plazo sin dimensionar la recuperación del corpus y elegir el entorno del cliente.

## Orden de trabajo

| Prioridad | Acción concreta | Fuentes y destino | Evidencia exigida para cerrar |
|---|---|---|---|
| P0 | Retirar/limitar la certificación automática de calidad y de «100% operativo» | README, verify_installation.py y run_evals.py; informe 05 | Mensajes separan estructura, contenido y runtime; tres mutaciones de evidencia08 fallan |
| P1 | Crear matriz de requisitos y recursos de los 7 módulos históricos | GPTs00–06 → agentes/skills/SOP/references | Cada función, comando, regla y recurso útil queda conservado, sustituido justificadamente o excluido por decisión expresa; nada se da por cubierto solo por nombre |
| P0 | Recuperar corpus literario íntegro y navegación bajo demanda | GPT05/06 → referencias y skills de voz/crítica | Manual completo, variantes y ejemplos accesibles; comprobación de carga por género y crítica; ausencia de recortes arbitrarios |
| P0 | Restaurar metodología de crítica y sus pares de ejemplos | Manuales GPT06 y cuatro bancos → crítico/skill/P01 | Matriz diagnóstica cargada, evidencia textual, formatos separados, ejemplos anotados y manejo de consigna ambigua |
| P1 | Recuperar Copycat administrativo y diagnóstico estratégico | GPT01/02/03 → financiación/datos/experto y skills | Entrevista, bancos de memorias, trazabilidad de criterios, diagnóstico A/B/plan B y entregables por comando |
| P0 | Reconstruir panel desde maestro y 18 individuales | GPT04 → panel/skill/agente/P03 | Identidades coherentes; campos detallados recuperados con origen; conflictos resueltos; simulación nunca presentada como demanda observada |
| P1 | Validar CSV y catálogo antes de llamarlos canónicos | CSV03 → JSON catálogo, ingesta | Cero filas con desplazamiento; campos tipados/plausibles; excepciones y vigencia registradas; 73/58 filas no bastan por sí solas |
| P1 | Desarrollar las 24 skills con guías aplicables | Tabla completa del informe04 | Entradas, decisiones, salida, errores, ejemplo trabajado y referencias pertinentes por skill; ninguna se acepta por longitud sola |
| P1 | Etiquetar y validar ampliaciones de marca, contratos y políticas | Planificación + datos generados → knowledge | Fuentes/fecha/aprobación por elemento; separar propuesta de regla institucional aprobada; no afirmar conformidad jurídica automática |
| P1 | Elegir entorno de ejecución y validar paquete instalado | Manifiesto/instaladores → producto concreto | Versiones, instalación limpia, invocación, carga de skill/corpus, permisos efectivos y respuesta trazable |
| P1 | Ejecutar evaluación de comportamiento con casos nuevos | Batería07 + rúbricas originales → salidas archivadas | Todos los agentes cubiertos, fallos críticos bloquean; revisión semántica independiente y validación de voz por quien conoce a Antonia |
| P2 | Alinear manual de usuario, alcance y versiones | PDF/MD00 y README/Planificación | Catálogo único de funciones reales; no se promete una función del manual si no tiene agente/proceso disponible |
| P2 | Hacer regeneración portable y actualización verificable | ingest/generate/install | Rutas parametrizadas, fuentes versionadas, reconstrucción comparable; verificación del destino instalado y actualización demostrada |

La prioridad P0 de la certificación no resta gravedad a la recuperación del conocimiento: impide usar el verde actual como autorización de entrega mientras se subsanan los P0/P1.

## Contrato de calidad por skill

No se fija un mínimo artificial de palabras. La revisión debe poder responder:

1. ¿Cuándo se usa y cuándo se deriva a otro agente?
2. ¿Qué información mínima necesita y qué pregunta si falta?
3. ¿Qué decisiones toma, con qué criterios y qué hace ante excepciones?
4. ¿Qué produce y cómo se comprueba que está completo?
5. ¿Qué ejemplo muestra el procedimiento de entrada a salida y explica por qué funciona?
6. ¿Qué referencia concreta carga y puede recuperarla en el paquete instalado?
7. ¿Qué evita inventar y qué aprobación humana requiere para actuar?

Una skill breve puede ser buena si carga un protocolo/referencia suficiente. La auditoría detecta que esa profundidad no está disponible de forma equivalente en la entrega actual.

## Ejemplo de profundidad exigible: rentabilidad formativa

**Propuesta del auditor, no regla ya aprobada de ECCL.**

La skill actual pide costes, precio y aforo, y manda calcular break-even; faltan definición de costes fijos/variables, fórmula y ejemplo. Un desarrollo revisable debería:

- Pedir horizonte temporal, ingresos netos efectivamente cobrables, coste fijo total del grupo, coste variable por alumno, capacidad y ocupación estimada.
- Calcular margen unitario = ingreso neto por alumno − coste variable por alumno.
- Si el margen es cero/negativo, informar que no hay umbral viable bajo esas hipótesis; no dividir por cero.
- Con margen positivo, calcular mínimo = techo(coste fijo / margen unitario); comparar con aforo.
- Separar viabilidad económica de tesorería y de aprobación pedagógica; no llamar beneficio neto a una contribución sin todos los costes.
- Ejemplo exclusivamente ficticio: fijo 600 €, ingreso 120 €, variable 20 € → margen 100 €, mínimo 6; con aforo5 el grupo es inviable bajo esas hipótesis. Con 8 alumnos la contribución tras ese fijo es200 €, antes de cualquier coste/impuesto no incluido.
- Entregar tabla de hipótesis, cálculo, escenarios y dudas pendientes; enlazar su plantilla.

No hay asesoramiento económico sobre cifras reales del cliente en este ejemplo.

## Ejemplo de recuperación editorial

No basta añadir «sé cálido». Una referencia de crítica debe contener: texto fuente autorizado, consigna, diagnóstico con citas, decisión técnica, comentario afectivo separado y explicación de cómo conserva la voz del alumno. Los 20 pares de corrección originales son material prioritario para esa recuperación, con revisión de permisos/anónimos según el uso previsto.

Para ghostwriting, distinguir género y tono, cargar ejemplos del género, seguir el procedimiento y revisar sin imponer a toda pieza una apertura doméstica. Los originales sintéticos se etiquetan como sintéticos; no se presentan como textos publicados de Antonia.

## Puertas de aceptación

- [ ] Matriz de los 7 módulos cerrada y revisión cruzada de pérdidas resuelta.
- [ ] Manuales, ejemplos y referencias útiles recuperados y cargables desde la entrega.
- [ ] Contradicciones del panel y datos desplazados resueltos sin inventar sustituciones.
- [ ] 24 skills y 17 agentes revisados con los criterios anteriores.
- [ ] Políticas y datos propuestos distinguidos de los aprobados por la institución.
- [ ] Suite estructural rechaza archivos/casos inválidos y no certifica calidad no medida.
- [ ] Instalación/carga probadas en el destino acordado.
- [ ] Batería de comportamiento ejecutada con salidas, incidencias y segunda evaluación.
- [ ] Validación humana de voz y pedagogía sobre ejemplos nuevos.
- [ ] README/manual reflejan capacidades y limitaciones demostradas.

**Ninguna casilla se marca por la existencia de este plan.** El cierre requiere evidencias posteriores a las correcciones.
