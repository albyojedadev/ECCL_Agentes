# Corrección core — agentes históricos, skills y protocolos

Fecha: 14 de octubre de 2026. Trabajo delegado por el coordinador de esta corrección; ámbito exclusivo GPT00–04. Esta es la revisión del autor de los cambios, no una certificación independiente ni prueba de ejecución en el entorno del cliente.

## Resultado y ámbito

Se reescribieron cinco agentes, cinco skills y dos protocolos de la entrega para recuperar capacidades originales y convertir resúmenes en procedimientos utilizables. No se modificaron originales GPT, JSON de knowledge, generadores, instaladores, evaluaciones del repositorio ni Git/GitHub en esta subtarea. La conservación íntegra del corpus y la integración global corresponden al coordinador.

Archivos modificados en `Repositorio de agentes/`:

- `agents/coordinador-de-agentes-de-la-eccl.md`
- `agents/experto-en-la-eccl.md`
- `agents/analista-de-datos-culturales-y-educativos.md`
- `agents/analista-de-subvenciones-y-licitaciones.md`
- `agents/consejo-de-alumnos-sinteticos.md`
- `skills/catalogo-academico-eccl/SKILL.md`
- `skills/synthetic-audience-panel-eccl/SKILL.md`
- `skills/cultural-grant-writer-es/SKILL.md`
- `skills/subvenciones-canarias-sync/SKILL.md`
- `skills/business-intelligence-cultural/SKILL.md`
- `protocols/P02_solicitud_subvencion_publica.md`
- `protocols/P03_test_ab_oferta_formativa.md`

## Comparación contra auditoría y originales

| Hallazgo previo | Antes | Corrección y evidencia consultable | Mejora incorporada |
|---|---|---|---|
| G00 navegación parcial | Derivación rápida, escasa recuperación de errores y sin contrato de traslado | Coordinador: diagnóstico, rutas mínima/completa/alternativa, paquete de derivación, ocho casos de uso y flujos recuperados; enlaces a manual/metodología | No finge delegación; criterios de aceptación y aprovechamiento del trabajo previo |
| FND-01 Copycat | Inserción de términos del organismo, sin voz propia/entrevista/modelos | Skill cultural-grant-writer: manual completo enlazado, preguntas por bloques, memoria base y cuatro ejemplos originales; procedimiento de diez fases | Matriz requisito/evidencia, límite de extensión, antes/después y tratamiento de sobrepromesas heredadas |
| FND-02 datos | Contrato reducido a rentabilidad de grupos | Agente de Datos recupera nueve capacidades y ocho fases; skill BI añade calidad/dataset/SEO-SEM/benchmark/impacto/radar/escenarios | Cardinalidad de uniones, denominadores, nulos, trazabilidad, causalidad y ejemplo de caja frente a beneficio |
| FND-03 mentor empresarial | Experto sustituido por consulta de catálogo | Agente Experto y skill Catálogo recuperan diagnóstico→opciones→artefacto→validación→seguimiento; ocho comandos, campaña 21 días y caja 90 días | Heurísticas comerciales distintas de punto de equilibrio; escenarios condicionados y plan B |
| FND-04 corpus omitido | Cursos/docentes sin navegación a cartera/estrategia | Skill Catálogo enlaza doce fuentes originales principales y método de dirección, incluidos grupos/proyectos/partners/publicaciones/manual/benchmark/oportunidades | Oferta histórica distinta de actual, objetivos distintos de logros y filas ejemplo distintas de entidades |
| FND-05 campos/fechas | Interpretación insegura del CSV | Consulta exige notas, conciliación, fuente/fecha y estado temporal; caso CL-2526 posterior al fin | id_registro distinto de id_curso repetido; advertencia de unidades LOS-INTRUSOS completo/mensual |
| Panel identidades/fichas | Nombres/edades inventados y detalles insuficientes | Agente/skill consultan panel normalizado y originales, ID/nombre estable, conflicto pendiente explícito | No rellena campos ausentes ni usa estereotipos; ejemplo de nombre inexistente |
| Panel metodología | Un modo genérico y supuesto porcentaje de aceptación | Tres modos originales, ocho fases, selección 2–4, evidencia por campo, tensiones/renuncias | Tres ejemplos trabajados nuevos, LATAM/accesibilidad y separación de test real |
| P02 | Triaje, jerga y presentación sin estados/evidencias | Nueve fases, fuentes, checklist responsable, registro solo acreditado, seguimiento/justificación | Memoria redactada distinta de expediente revisado/presentado; no inventa resguardos |
| P03 | Focus group sintético llamado validación y umbral 70% | Dos etapas: exploración cualitativa y experimento humano, con versiones/condiciones/medición | Sin probabilidades/WTP/tasas fabricadas; sesgos/denominadores/muestra insuficiente visibles |

La recuperación no se basa solo en añadir enlaces. Cada skill desarrolla entradas/salidas, pasos, decisiones ante lagunas, criterios de aceptación y ejemplos completos. Los originales enlazados conservan el material extenso; la guía indica cuándo usarlo y cómo corregir sus defectos sin borrarlo.

## Revisión cualitativa de profundidad

| Skill | Método y decisiones | Ejemplo trabajado | Excepción/control | Dictamen documental del autor |
|---|---|---|---|---|
| Catálogo | Consulta/versiones + seis fases de dirección + ficha pedagógica + campaña/plantillas | Histórico CL-2526, apertura con equilibrio y condiciones | Duplicados/modalidades, unidades de precio y capacidad incompatible | Procedimiento desarrollado con navegación al corpus |
| Panel | Selección/ficha/conciliación + ocho fases + tres salidas | A/B Elisa-Héctor; voz Elisa; LATAM/accesibilidad | Nombre inexistente, precio ausente, datos decisivos faltantes | Simulación cualitativa trazable; no valida mercado |
| Grant writer | Diez fases, entrevista por sección y control de estilo/baremo | Bases parciales → entrevista → índice → primer bloque | Resultados no ejecutados, dato ausente y sobrepromesas del modelo histórico | Recupera método Copycat y referencias originales |
| Sync | Nueve pasos, fuentes/capacidad, estado temporal y registro | Pistas 2025/plan 2026/convocatoria cerrada | 403, CKAN dataset, fecha contradictoria | Método operativo honesto; no integración probada |
| BI | Calidad, dataset, indicadores, escenarios, benchmark/radar e informe | Duplicados/unión, apertura/caja, campaña/impacto | Contribución ≤0, nulos, falta de acceso, sesgo y reidentificación | Amplía economía con analítica cultural/digital y reproducibilidad |

Se revisaron los casos E01–E10 de la batería propuesta como requerimientos documentales: las guías ahora contienen soporte para sus criterios. **No se ejecutaron esos diez casos contra agentes instalados** en esta subtarea; no deben marcarse como superados por esta lectura. E06 sí se contrastó aritméticamente de forma local, lo que prueba la fórmula del caso, no la respuesta futura de un agente.

## Verificaciones locales ejecutadas

Evidencia: [CORRECCION_CORE_ENLACES.json](evidencias/CORRECCION_CORE_ENLACES.json).

- Doce archivos revisados; 84 enlaces locales resueltos; cero enlaces rotos.
- Treinta y tres fuentes originales únicas enlazadas comparadas byte a byte mediante SHA-256 con `GPTs/`: todas iguales en el momento de la comprobación.
- Ocho comandos documentados en Experto: /diagnóstico, /decidir, /oferta, /operaciones, /comercial, /proyectos, /finanzas, /plantillas.
- Caso ficticio E06: fijo 600, precio 120, variable 20, aforo 5 → equilibrio 6 personas; resultado a aforo completo −100. Aforo insuficiente bajo esos supuestos.
- Caso ficticio de caja: nueve pagos × contribución 100 − fijo 900 = resultado cero; caja inicial 500 y pago fijo 900 antes de cobros → saldo −400. Beneficio y liquidez no son intercambiables.
- No se detectaron caracteres de sustitución Unicode en los doce archivos escritos.

El recuento de palabras/ejemplos ayuda a localizar documentos, pero no se usa como garantía de calidad. Tampoco el hecho de que las rutas existan acredita vigencia del contenido ni ejecución de APIs.

## Cambios deliberados respecto a defectos originales

Se conservan métodos y corpus, pero se corrigen aprobación vinculante, simulación como mercado real, probabilidades inventadas, jerga/ODS por defecto, instrucciones de herramientas no disponibles, predicción sin evidencia y afirmaciones de registro sin resguardo. Los enlaces GPT históricos y rutas /mnt/data se sustituyen operativamente por recursos locales del paquete; no se promete acceso al GPT alojado.

La posibilidad de construir plantillas/tablas sigue disponible; crear un archivo o exportar depende de la herramienta real. La memoria entre sesiones, el banco persistente, avisos y sincronización requieren destino/mecanismo autorizado. No se presentan como automatismos instalados.

## Método aplicado y límites pendientes

Se leyó ARSENAL.md, puente arsenal-bajo-demanda y skill-writer canónica; el buscador la localizó realmente. Se leyó el perfil ai-architect para criterios pertinentes, sin adoptar sus herramientas ni modelos históricos como disponibles. Las referencias indicadas por skill-writer no estaban en su ruta canónica; se aplicaron sus criterios presentes sin fingir lectura de anexos ausentes. Modelo y esfuerzo heredados de la sesión, no seleccionados en esta subtarea.

Queda para la revisión global: validar el panel normalizado completo, JSON/ingesta y evaluación endurecida del coordinador; revisar las ampliaciones y el ámbito literario corregidos por los otros agentes; ejecutar pruebas pertinentes y revisión independiente de salida; comprobar permisos/destino de publicación. La exactitud actual de oportunidades, contactos, precios, disponibilidad y normas no fue verificada externamente por esta subtarea. Las guías exigen esa verificación antes de usar esos datos como actuales. La aceptación operativa en la plataforma del cliente requiere pruebas reales de agentes; esta corrección documental no equivale a ellas.
