---
name: catalogo-academico-eccl
description: Consultar y cruzar corpus académico e institucional ECCL, diseñar fichas y apoyar decisiones de dirección, oferta, operaciones y campañas sin presentar el catálogo histórico como vigente.
---

# Catálogo académico y decisión empresarial ECCL

## Cuándo aplicar y qué entregar

Usa para consultar cursos/docentes, diseñar programas, abrir/cerrar grupos, revisar itinerarios, preparar campaña o decidir con el corpus de la Escuela. No sustituye corrección literaria ni redacción autoral. Entradas: pregunta/decisión, público, fecha de consulta, materiales existentes, restricciones, datos actuales de grupo y autorización para consultar fuentes externas si procede. Salida: respuesta factual con procedencia o dossier de decisión (diagnóstico, A/B, recomendación, artefacto, plan B, control).

## Fuentes bajo demanda

| Necesidad | Recurso conservado dentro de knowledge/sources/GPTs/03 Experto de la escuela | Uso y límite |
|---|---|---|
| Navegación | [index.md](../../knowledge/sources/GPTs/03%20Experto%20de%20la%20escuela/index.md) | Mapa semántico; referencias antiguas /mnt/data se resuelven aquí |
| Cursos/docentes | [inventario_cursos.csv](../../knowledge/sources/GPTs/03%20Experto%20de%20la%20escuela/inventario_cursos.csv), [docentes.csv](../../knowledge/sources/GPTs/03%20Experto%20de%20la%20escuela/docentes.csv) | Complementar JSON normalizados en knowledge/catalogo; CONSULTAR no es dato confirmado |
| Apertura/operaciones | [grupos.csv](../../knowledge/sources/GPTs/03%20Experto%20de%20la%20escuela/grupos.csv) | Costes, umbrales, ejemplos y observaciones; no inferir vigencia |
| Cartera y alianzas | [proyectos.csv](../../knowledge/sources/GPTs/03%20Experto%20de%20la%20escuela/proyectos.csv), [partners.csv](../../knowledge/sources/GPTs/03%20Experto%20de%20la%20escuela/partners.csv) | Estado/histórico/siguiente acción; contactos bajo finalidad y permisos |
| Editorial | [publicaciones.csv](../../knowledge/sources/GPTs/03%20Experto%20de%20la%20escuela/publicaciones.csv) | Distingue publicaciones Escuela y Agencia AM, instrucciones y filas ejemplo |
| Públicos | [AnalisisPublico.md](../../knowledge/sources/GPTs/03%20Experto%20de%20la%20escuela/AnalisisPublico.md) | Públicos actuales/potenciales, oferta/mensaje, bloques de expansión históricos |
| Estrategia | [Informe_Estrategico_ECCL.md](../../knowledge/sources/GPTs/03%20Experto%20de%20la%20escuela/Informe_Estrategico_ECCL.md) | DAFO, roadmap, KPIs y riesgos; metas no son logros |
| Comunicación | [manual_de_comunicacion_escuela_literaria_ecl.md](../../knowledge/sources/GPTs/03%20Experto%20de%20la%20escuela/manual_de_comunicacion_escuela_literaria_ecl.md) | Tono, plantillas, briefing, funnel, permisos y esquemas de salida |
| Benchmark | [Benchmark_Analisis_Competidores.md](../../knowledge/sources/GPTs/03%20Experto%20de%20la%20escuela/Benchmark_Analisis_Competidores.md), [CSV](../../knowledge/sources/GPTs/03%20Experto%20de%20la%20escuela/Benchmark_Competidores_Escuela_Literaria.csv) | Comparativas históricas; normalizar unidades y verificar precios antes de decidir |
| Financiación/crecimiento | [Oportunidades_2025.md](../../knowledge/sources/GPTs/03%20Experto%20de%20la%20escuela/Oportunidades_2025.md) | Pistas públicas/privadas/crowdfunding/turismo/alianzas, no ayudas abiertas confirmadas |
| Método de dirección | [funcion.txt](../../knowledge/sources/GPTs/03%20Experto%20de%20la%20escuela/funcion.txt), [metodologia.txt](../../knowledge/sources/GPTs/03%20Experto%20de%20la%20escuela/metodologia.txt) | Decisión multifuente, ocho comandos reunidos y seguimiento |

Carga solo fuentes relevantes; no sustituyas esta navegación por visitar una web de cursos. Los originales se conservan como evidencia, incluidos errores y ejemplos. Las guías operativas actuales prevalecen sobre instrucciones históricas incompatibles con permisos o evidencia.

## Procedimiento de consulta y vigencia

1. Define tipo de petición: dato, diseño, decisión o revisión. Para dato usa identificador de entidad (curso/docente/grupo/proyecto/publicación), no solo parecido de título.
2. Busca en JSON normalizado y consulta fila original/notas cuando afecten la respuesta. Usa `id_registro` para distinguir filas; `id_curso` puede repetirse entre modalidades y no es clave única. No fusiones INICIA-ESPACIO o AVANZA-ESPACIO sin revisar ambas filas/modalidades. No repares silenciosamente campos desplazados en CSV: informa incidencia o utiliza la conciliación documentada. Separa entidades de notas/casos.
3. Registra fuente, identificador, fecha del snapshot y fecha de comprobación. Distingue confirmado ahora, histórico, propuesto, ejemplo e incierto. `cursos_activos.json` es nombre técnico: no prueba que las matrículas sigan abiertas.
4. Antes de ofrecer precio/plaza/fecha/docente confirma fuente actual administrada por la Escuela o información actual aportada. Web oficial consultada solo acredita lo que realmente se leyó y cuándo; no crea acceso a plazas o pagos.
5. Si fuentes discrepan, compara fecha, ámbito y autoridad. Prioriza dato actual aprobado; si no se puede resolver, presenta ambas versiones y pregunta al responsable. No promedies precios ni decidas que una nota estratégica reemplaza una fecha operativa.
6. Responde con dato, vigencia y limitación. Una consulta sencilla no necesita consejo de dirección; una decisión sí requiere el procedimiento siguiente.

## Decisión empresarial estructurada

1. Diagnóstico: objetivo, horizonte, captación, ocupación, caja, recursos/proyectos; prioriza cuellos de botella por urgencia/impacto. Reutiliza archivos y pide solo lagunas críticas.
2. Análisis: opciones factibles, capacidad y carga docente, ingresos/costes y plazo. Solicita inscritos/pagados separados de interesados. Consulta reglas comerciales aprobadas; umbrales históricos de grupos no son políticas actuales ni punto de equilibrio.
3. Recomendación: ofrece A/B con pros/contras, supuestos, impacto y condición para cambiar de opción. Si falta dato crítico, entrega diagnóstico parcial y escenarios, no autorización de apertura.
4. Artefacto: ficha, tabla de ocupación, P&L/caja con Analista de Datos, calendario/copy, dossier o checklist según necesidad. No prometas hoja dinámica si entregaste Markdown.
5. Validación: comprueba coherencia docente, pedagógica, económica y comunicativa. Dirección confirma decisiones, tarifas, docentes y compromisos. Preparar no equivale a enviar ni contratar.
6. Seguimiento: acuerda responsable y fecha de revisión; compara resultado real con supuesto, registra aprendizaje y cambio. Alertas se generan al revisar datos, no mediante monitor inexistente.

## Ficha pedagógica de salida

Completa: título/versión/estado (propuesta o aprobado), público y acceso/nivel, necesidad, objetivo general y 2–4 específicos observables, modalidad y carga, secuencia de sesiones, ejercicios/materiales, producto final, metodología de acompañamiento, evaluación/evidencias, accesibilidad prevista y pendiente, docente/disponibilidad, fechas/horario y zona, precio/condiciones, capacidad/mínimo (según aprobación), recursos/logística, requisitos técnicos y fuentes. No garantiza resultados, acreditación, publicación ni plaza. Relaciona cada objetivo con una actividad y evidencia; si no existe relación, revisa la ficha.

## Campaña de 21 días y plantillas de control

Días 1–7: confirmar ficha, mensaje por público y material; preparar email de necesidad/propuesta y landing clara (qué/quién/cuándo/modalidad/condiciones/CTA). Días 8–14: propuesta de clase abierta con fecha/docente confirmados, invitación por canal autorizado, preguntas frecuentes y prueba social solo acreditada. Días 15–21: resolver objeciones reales, informar cierre real y revisar preinscripción/pago; no usar urgencia falsa. Entrega guion de clase abierta, dos emails, dos mensajes y calendario como borradores; adaptar plan a autorización/recursos, no envío automático.

Tabla Leads/Embudo: periodo, canal, contactos con permiso, consultas, preinscritos, pagos confirmados, coste y fuente. Tabla Ocupación: grupo, capacidad, interesados, inscritos, pagos, bajas, próxima decisión. Tabla Caja 90 días: fecha, saldo inicial, cobros esperados/confirmados, pagos comprometidos, saldo final y escenario. Usa códigos anonimizados cuando haga falta; no incluya contactos personales en informes de dirección sin necesidad.

## Ejemplo trabajado: consulta histórica y apertura

Consulta «¿puedo inscribirme hoy en CL-2526?». La fila histórica indica 30/10/2025–28/05/2026 y matrícula abierta. En una consulta posterior al fin, responde que el registro es histórico y no confirma inscripción actual; consulta/solicita oferta vigente, sin cambiar la fecha ni asegurar plaza.

Caso didáctico de dirección nuevo: 12 interesados, 25 plazas, precio neto 120 €, variable 20 €/persona, fijo 900 €, pagos desconocidos. Equilibrio = techo(900/(120−20)) = 9 pagos. A: abrir condicionado a 9 pagos y disponibilidad docente; B: posponer/redimensionar con coste actualizado. Con 12 pagos el margen sería 300 €, no el ingreso bruto 1.440 €. Recomendación: confirmar pagos antes de anunciar apertura. Plan B: si no llegan 9, revisar coste/fecha en vez de prometer curso deficitario. Artefacto: control anonimizado de pagos y checklist docente/fecha; revisión en fecha acordada con dirección.

Excepción: 30 matrículas frente a capacidad 25 no significa éxito automáticamente. Comprueba duplicados, grupos/modalidades y capacidad antes de comunicar ocupación. Si no hay coste o precio confirmado, no calcules margen con tarifas inventadas.

Ejemplo de unidades heredadas: LOS-INTRUSOS-2526 tiene `precio_min` 350 y `precio_max` 60 en origen, pero sus observaciones indican 350 € completo o 60 € mensual. No lo expresa como intervalo 350–60, no intercambia los campos para esconder el problema ni los considera precio vigente. Recupera ambas condiciones históricas con sus unidades y pide comprobación actual. Si otras filas no permiten resolver la unidad, mantiene el precio pendiente.

## Aceptación

El resultado debe permitir localizar origen y estado temporal, distinguir entidades/ejemplos, entender criterio de decisión y ejecutar el próximo paso humano. En diseño, objetivos/sesiones/evaluación se corresponden. En campaña, los hechos son verificables y los copys son propuestas. En decisión económica, fórmula/unidades/supuestos son visibles. Si falla cualquiera, entrega borrador con pendiente concreto, no «catálogo vigente», «curso confirmado» o «decisión aprobada».
