# Suite ECCL · versión 2.0

17 agentes y 24 skills para la Escuela Canaria de Creación Literaria, con manuales, ejemplos y conocimiento histórico recuperado de los GPTs originales. Seis protocolos organizan el trabajo y un cargador local prepara contexto con trazabilidad.

## Instalar todo el sistema en ChatGPT

El cliente **no necesita instalar Python, Node.js ni ninguna otra tecnología**. La entrega principal es un único plugin que agrupa los 17 roles y las 24 skills.

Un administrador del workspace realiza una sola importación:

1. Abrir **Admin → Plugins → Add → Import marketplace** en ChatGPT.
2. Pegar `https://github.com/albyojedadev/ECCL_Agentes` en **Source**.
3. Dejar **Path** vacío y usar la rama predeterminada.
4. Importar `Suite de Agentes ECCL` y marcarla como instalada para los roles autorizados.

OpenAI exige esta autorización administrativa; un prompt no puede saltársela. Una vez importado el marketplace, ChatGPT instala el plugin completo y sincroniza futuras versiones desde GitHub.

Como alternativa, [ECCL_ChatGPT_Plugin.zip](dist/ECCL_ChatGPT_Plugin.zip) permite crear el mismo plugin mediante Plugin Creator. El paquete no contiene scripts ni ejecutables. Consulte la [guía de instalación](docs/INSTALACION.md).

La carpeta `chatgpt_ready/` y `ECCL_ChatGPT_Pack.zip` se conservan únicamente como alternativa manual para reconstruir Custom GPTs antiguos; no son el sistema de instalación recomendado.

Consulte también el [manual de uso](docs/MANUAL_DE_USO.md) y el [informe de entrega y reevaluación](docs/INFORME_ENTREGA.md).

## Qué incluye

- [Agentes](agents/): coordinación, financiación, datos culturales, dirección/catálogo, panel cualitativo, voz de Antonia, crítica, admisiones, hábito, edición, comunidad, contratos, soporte, prensa, B2B, diseño y supervisión visual.
- [Skills](skills/): procedimientos por tarea con decisiones, ejemplos trabajados y referencias bajo demanda.
- [Protocolos](protocols/): corrección, expediente público, contraste de oferta, autoría, acogida y diseño.
- [Fuentes preservadas](knowledge/sources/source_manifest.json): 98 archivos originales íntegros; solo se excluye un bloqueo temporal de oficina, documentado.
- [Procedencia y normalización](docs/PROCEDENCIA.md): recibos de reparación y separación de histórico, propuesta y comprobación actual.
- [Reglas comunes](docs/REGLAS_COMUNES.md): destinatarios, confidencialidad, honestidad de herramientas y decisión humana.
- [Evaluación](evals/): regresiones locales y 26 casos de comportamiento. Pasar comprobaciones de integridad no equivale a «100% de calidad».
- [Auditoría completa](auditoria/09_REEVALUACION_Y_DICTAMEN_FINAL.md): diagnóstico inicial, correcciones, reevaluación independiente y evidencias reproducibles.
- [Plugin ChatGPT](plugins/eccl-agent-suite/): paquete declarativo con 42 skills instalables: 17 roles, 24 procedimientos y una skill de puesta en marcha.
- [Marketplace](.agents/plugins/marketplace.json): catálogo que permite importar todo el sistema desde la URL del repositorio.

## Entornos

El paquete tiene un manifiesto nativo de Claude Code en .claude-plugin/plugin.json. Su carga de componentes puede comprobarse con el validador del producto. La inferencia necesita una sesión/autenticación válida y pruebas específicas.

La carga portable permite usar los documentos en una conversación local con acceso a archivos. Para Codex no se afirma un registro nativo de los 17 subagentes por el solo hecho de copiar este paquete. Para Antigravity se ofrece material portable; no se anuncia un plugin nativo probado ni se escribe en rutas supuestas de Gemini.

## Límites del conocimiento

El catálogo es un snapshot histórico no verificado en la web: no confirma plazas, tarifas o fechas actuales. Los 18 perfiles son simulaciones cualitativas y no miden demanda real. Marca, modelos de contratos y políticas propuestas no se presentan como aprobaciones del cliente. Las especificaciones de APIs originales están conservadas, sin afirmar conexiones activas.

La voz y pedagogía requieren revisión humana de muestras nuevas. No se garantizan resultados de subvenciones, publicación editorial ni conformidad jurídica por un prompt o un filtro.

## Mantenimiento técnico opcional

Este apartado es solo para el equipo que mantiene el repositorio. Las comprobaciones reproducibles usan Python 3.10 o posterior y únicamente su biblioteca estándar:

~~~text
python -B scripts/verify_installation.py
python -B evals/run_evals.py
~~~

Estas órdenes no son necesarias para instalar o utilizar los asistentes en ChatGPT.

## Mantenimiento y licencia

Las fuentes originales son inmutables dentro del paquete y se verifican por SHA-256. Regenerar datos con scripts/ingest_knowledge.py conserva los manuales completos y los recibos de normalización. El antiguo generador de skills ahora valida y no sobrescribe enriquecimientos.

Paquete y corpus propietarios: véase [LICENSE](LICENSE). Su contenido está destinado al cliente; la difusión debe ajustarse a las autorizaciones aplicables.
