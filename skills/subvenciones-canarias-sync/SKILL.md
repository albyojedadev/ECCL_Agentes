---
name: subvenciones-canarias-sync
description: Buscar y registrar oportunidades culturales de Canarias, España y UE con fuentes oficiales, fechas, deduplicación y límites de acceso; preparar mapa de financiación sin fingir monitorización ni APIs activas.
---

# Búsqueda y registro trazable de financiación cultural

## Alcance y entregables

Activa para mapa de ayudas/licitaciones, revisión de oportunidades o actualización puntual del banco. «Sync» es nombre de la skill; no crea una sincronización, vigilancia ni aviso periódico. Entradas: actividad, entidad/tipo jurídico, territorio, público, madurez, periodo y preferencias abierto/histórico, presupuesto/capacidad y fuentes disponibles. Salida: registro de búsquedas, listado deduplicado de pistas, ficha oficial por oportunidad, pendientes y recomendación de análisis. No estima concesión ni firma solicitudes.

## Fuentes y capacidad real

Conserva tres configuraciones originales para lectura técnica:

- [API Ayudas Canarias.txt](../../knowledge/sources/GPTs/01%20Ayudas%20y%20licitaciones/API%20Ayudas%20Canarias.txt): CKAN `package_search`, parámetros q/start/rows/sort. Buscar datasets no prueba que cada resultado sea una ayuda abierta o un buscador jurídico exhaustivo.
- [API Ayudas Nacionales.txt](../../knowledge/sources/GPTs/01%20Ayudas%20y%20licitaciones/API%20Ayudas%20Nacionales.txt): operaciones descritas SNPSAP, incluidos catálogos/búsquedas/detalles según especificación. Su título audiovisual/videojuegos no establece cobertura literaria.
- [API Ayudas Europeas.txt](../../knowledge/sources/GPTs/01%20Ayudas%20y%20licitaciones/API%20Ayudas%20Europeas.txt): búsquedas/detalles descritos para Funding & Tenders; especificación local no equivale a endpoint vigente/probado.

Son archivos históricos, no credenciales, conectores activos ni implementación. Antes de usarlos técnicamente verifica documentación oficial actual, operación disponible y resultados reales; si no hay herramienta, no simules respuesta API. Alternativa: consulta páginas oficiales/boletín/sede disponibles o solicita documentos al usuario, marcando revisión pendiente. Nunca afirma que buscó lo que no pudo consultar.

## Procedimiento

1. Define perfil de búsqueda: actividad cultural/educativa, territorio local/insular/autonómico/estatal/UE, entidad solicitante, importe orientativo, calendario y madurez. No presupone que ECCL sea elegible por su sector.
2. Elige fuentes oficiales pertinentes del organismo convocante, publicación/boletín y sede, o buscador oficial disponible. Usa catálogos abiertos como pistas; no confunde concesión publicada, plan estratégico, noticia y convocatoria abierta.
3. Registra consulta literal/filtros, fuente/URL, fecha/hora de consulta y herramienta/acceso. Si hay paginación, documenta páginas/alcance y cualquier truncado. Un resultado vacío solo significa que esa búsqueda no halló resultados en ese alcance.
4. Recoge pistas con título, organismo, identificador/expediente, territorio, tipo de instrumento y documento primario. Deduplica por identificador y organismo; títulos parecidos con años distintos no se fusionan automáticamente.
5. Verifica cada candidata en bases/anexos/correcciones oficiales: publicación, apertura/cierre/hora/zona, beneficiarios, actividades, gastos/periodo, cuantía/intensidad, cofinanciación, incompatibilidades, documentación y sede. Si no hay bases, estado «pista, pendiente de comprobar».
6. Determina estado a fecha de consulta: abierta/cerrada/próxima/histórica/indeterminado. No infiere abierta por fecha de indexación o palabra «2026». Prórrogas/correcciones solo se aplican con fuente, y no se resuelven conflictos en silencio.
7. Compara requisitos con proyecto/entidad: confirmado/no cumple/pendiente. Prioriza por encaje acreditado, carga administrativa, capacidad de ejecución y calendario. No calcula probabilidad de éxito ni ratio esfuerzo/probabilidad inventado.
8. Prepara mapa temporal con próximas acciones y responsables humanos. Complementar fuentes exige comprobar compatibilidad y evitar doble financiación, sin sugerir mezclar partidas solo para agotar ayudas. Remite candidata a [cultural-grant-writer-es](../cultural-grant-writer-es/SKILL.md) y [P02](../../protocols/P02_solicitud_subvencion_publica.md) para expediente.
9. Si se autoriza guardar/actualizar un banco, preserva versión anterior, fuente/fecha y cambio, sin borrar evidencias. Un seguimiento recurrente requiere mecanismo y encargo explícito; de otro modo entrega control para revisión humana.

## Plantilla de registro

| Campo | Contenido obligatorio |
|---|---|
| Identidad | ID interno + expediente oficial si existe, título y organismo |
| Tipo/territorio | Subvención, licitación u otro; ámbito |
| Procedencia | URL/documento/versión/apartado, fecha de publicación y consulta |
| Plazo | Inicio/fin/hora/zona y fuente; desconocido cuando falte |
| Estado | A la fecha de consulta y con evidencia, no definitivo para siempre |
| Encaje | Entidad, actividad, gasto, periodo; confirmado/no/pendiente |
| Economía | Importe/intensidad/cofinanciación según bases; no estimación gratuita |
| Operación | Documentación, sede, responsable propuesto, siguiente acción |
| Límites | Acceso fallido, alcance no exhaustivo, anexos ausentes, conflictos |

## Ejemplo trabajado y excepción

Caso didáctico nuevo: una búsqueda devuelve «Ayudas culturales 2025», noticia «plan 2026» y bases «Convocatoria X» con cierre 30 de septiembre de 2026 a las 14:00 hora canaria. Consultado el 14 de octubre de 2026, sin prórroga acreditada: primera pista histórica por verificar, segunda plan sin convocatoria y tercera cerrada. No presenta ninguna como abierta. Registra cada fuente/fecha y prepara revisión de próximas publicaciones, sin prometer alerta automática. Si falta tipo jurídico de la entidad, encaje pendiente aunque la actividad parezca adecuada.

Si CKAN devuelve success=true con datasets, inspecciona metadatos/recursos y busca bases oficiales; success no prueba elegibilidad ni que haya ayudas. Si API da 403, tiempo de espera o esquema inesperado, registra fallo de acceso, usa fuente oficial alternativa si disponible y no rellena con resultados inventados. Si dos fuentes dan distinta fecha, muestra discrepancia y localiza resolución/corrección antes de recomendar presentar.

## Reglas de riesgo y aceptación

No uses umbral jurídico universal de 15.000 € ni equipares contrato menor/subvención directa/concurrencia. Para asesorar sobre reglas actuales consulta fuentes oficiales competentes. Esta skill organiza documentación, no declara una norma vigente por memoria.

Acepta salida solo si búsqueda/acceso están descritos con honestidad, cada candidata tiene fuente y fecha, estado y requisitos pendientes son visibles, duplicados están reconciliados y el próximo paso es ejecutable por un responsable. No llamas «sin ayudas» a un fallo de acceso ni «lista completa» a unas pocas consultas. No envías mensajes ni registra solicitudes por leer la skill.
