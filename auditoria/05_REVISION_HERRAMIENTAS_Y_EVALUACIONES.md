# 05 · Herramientas, evaluación y entrega

Fecha: 14 de octubre de 2026. Revisor: agente coordinador. Objeto: copia local de Repositorio de agentes, commit observado 871e7175750cd28a9f910ea02e53b02bca8bdfd8. No se instaló ni publicó el paquete.

## Dictamen

**Las comprobaciones existentes pasan, pero no prueban la fidelidad de migración ni la calidad del comportamiento. «100% operativa y lista para uso» excede lo demostrado.** Hay una base estructural coherente, no una certificación de entrega.

P0: bloqueo de la aceptación anunciada; P1: defecto sustancial que debe corregirse antes de aceptar; P2: mejora documental. No son puntuaciones de ciberseguridad.

## Qué sí funciona en la revisión local

- Existen 17 agentes, 24 skills, 6 SOP y 8 JSON de conocimiento, coincidentes con las listas del manifiesto. Las skills citadas en las cabeceras de los 17 agentes existen.
- Los 6 programas Python de entrega tienen sintaxis analizable. Los JSON de entrega se pueden decodificar.
- No se encontraron enlaces Markdown locales rotos con el extractor utilizado. No analiza todas las rutas escritas en prosa ni garantiza que el modelo cargue los archivos.
- Cuatro ejecuciones dieron código 0: evaluador, verificador, muestra del linter de estilo y muestra del linter de marca.
- Las huellas SHA-256 antes/después coinciden para los 182 archivos inventariados en GPTs, Planificación y entrega. Se excluyen .git y __pycache__; esta auditoría se escribe fuera del repositorio de entrega.

Evidencia: evidencias/01_inventario.csv, 02_componentes.json, 03_validez_json.json, 06_pruebas_originales.json, 09_integridad_final.json y 11_revision_estatica.json.

## H-T01 · P0 · Certificación de calidad basada en existencia, no en ejecución de agentes

**Evidencia:** Repositorio de agentes/evals/run_evals.py:27–45,48–66,68–102,109–131; scripts/verify_installation.py:40–78,80–104.

El evaluador prueba dos muestras fijas de estilo y dos de marca. Verifica que ocho JSON existan y sean truthy, y que casos tenga al menos un elemento. No invoca a ninguno de los 17 agentes, no genera respuestas al benchmark, no contrasta salidas esperadas, no llama a un juez semántico ni verifica hechos web. Devuelve 100 por bloques después de controles limitados. El verificador comprueba existencia de archivos declarados, no profundidad ni validez de frontmatter; después presenta un veredicto global de operatividad.

**Contrapruebas ejecutadas en copias desechables dentro de auditoria:**

| Cambio aislado en copia | Comprobación | Resultado observado |
|---|---|---|
| Crítico literario convertido en archivo vacío | verify_installation.py | Código 0; «100% operativa» |
| Catálogo sustituido por {"auditoria":"sin registros de cursos"} | verify_installation.py | Código 0; «100% operativa» |
| Benchmark sustituido por un caso sin entrada, salida ni agente | run_evals.py | Código 0; calidad global 100 |

Logs completos: evidencias/08_contrapruebas_suite.json. Las copias temporales se eliminaron al terminar; se conservaron entradas y resultados.

**Impacto:** la suite puede dejar pasar una entrega sin contenidos funcionales. El verde no sustenta «sin pérdida de información», fidelidad a Antonia ni rigor administrativo.

**Reparación:** separar salud estructural, integridad semántica y comportamiento real; validar esquemas/campos/rutas/carga; ejecutar casos contra agentes en el destino y registrar contexto/salida/juez. Limitar el veredicto a lo probado.

**Aceptación:** las tres mutaciones fallan; cada caso tiene salida real trazable y decisión por criterio; un fallo bloqueante no se compensa por promedio.

## H-T02 · P1 · Los linters permiten incumplimientos que dicen controlar

**Marca:** evals/test_brand_linter.py:47–115. La validez cromática es verdadera si no encuentra HEX; basta encontrar una fuente autorizada y ninguna de las cuatro vetadas. No verifica dimensiones ni márgenes.

| Entrada de contraste | Resultado real |
|---|---|
| {"fuente":"Inter"} sin color, formato ni margen | passed=True, score=100 |
| Paleta autorizada con fuentes Inter y Roboto | passed=True, score=100 |
| Paleta autorizada, Inter y margen de -100 px | passed=True, score=100 |

**Estilo:** evals/test_style_linter.py:54–103. Detecta encabezados, nombre, expresiones y longitud media. No valida respeto al alumno, pruebas textuales, separación semántica de confidencialidad ni autoría. Un comentario «no tienes talento y deberías abandonar este curso» con alusión al informe confidencial obtuvo passed=True y score=100.

Entradas/resultados: evidencias/07_contrapruebas_linters.json. Son pruebas de los validadores, **no pruebas de que un agente haya generado esos mensajes**.

**Reparación:** presencia/esquema, todas las fuentes declaradas, geometría comprobable del artefacto y evaluación semántica pedagógica. Mantener regex como ayuda, sin convertirla en prueba de autenticidad literaria.

**Aceptación:** rechazar los cuatro casos; negativos que fallen por un único criterio; distinguir «no evaluado» de «aprobado». Separar validadores de crítica y ghostwriting.

## H-T03 · P1 · Compatibilidad e instalación anunciadas sin prueba del producto de destino

**Evidencia:** README.md:3–31; plugin.json:2–7; scripts/install.ps1:32–53; scripts/install.sh:26–39.

Se anuncia paquete para Antigravity y Claude Code. Ambos instaladores únicamente apuntan a .gemini/config/plugins/eccl-agent-suite. El manifiesto declara URL de esquema, pero el verificador no consulta ni valida ese esquema. No hay prueba registrada aquí de descubrimiento, invocación, carga de skills ni lectura del corpus en un producto destino. No hay adaptador de instalación específico de Claude/Codex en los archivos inventariados.

**Conclusión acotada:** compatibilidad **no demostrada**. Esto no prueba incompatibilidad técnica definitiva; requiere validación en versiones concretas del entorno elegido por el cliente.

**Reparación:** elegir destino real, preparar el paquete para su descubrimiento y demostrar en instalación limpia invocación, carga de skill y consulta del corpus.

**Aceptación:** transcripción reproducible desde instalación limpia hasta respuesta sustentada en referencia interna, versiones y permisos registrados; actualización/desinstalación documentadas.

## H-T04 · P1 · Ingesta dependiente del ordenador del desarrollador y recorte de contenido

**Evidencia:** scripts/ingest_knowledge.py:12–15,81–114; scripts/generate_skills.py:11–13 y función generate_skills al final.

Ingesta fija D:\PROYECTOS\Escuela Canaria de Creación Literaria y depende de la carpeta hermana GPTs, fuera del repositorio instalable. El generador también usa ruta local fija. manual_texto[:4000] recorta el manual antes de guardar el corpus: causa verificable de pérdida.

**Reparación:** parámetros entrada/salida, manifiesto de fuentes con huellas, validación y registro de transformaciones; conservar manuales íntegros en referencias recuperables y generar índices. No canonizar campos desplazados por CSV mal formado (informe 03).

**Aceptación:** reconstruir en carpeta arbitraria, detectando entradas inválidas y verificando campos/requisitos preservados.

## H-T05 · P2 · Opciones y actualización de instaladores

**Evidencia:** scripts/install.ps1:7–10,36–53,56–62; scripts/install.sh:31–43.

Force y SkipCheck se declaran pero no cambian el flujo. Si el destino existe, se da por vinculado sin actualizar ni comprobar revisión. El fallback PowerShell copia evals pero omite scripts; la verificación posterior se ejecuta contra el repositorio original, no contra esa copia instalada.

**Impacto:** una copia antigua o incompleta puede coexistir con diagnóstico verde sobre la fuente.

**Reparación/aceptación:** implementar opciones o retirarlas, comprobar destino/version efectiva, verificar copia instalada y demostrar actualización/recuperación. Revisión estática; no se ejecutó instalación.

## Planificación frente a implementación

Planificación/07_FRAMEWORK_EVALUACION_CALIDAD.md especifica 5 dimensiones, juez LLM, comprobación factual y 30 casos. El evaluador entregado implementa 4 bloques limitados y el dataset contiene 8 casos. No implementa agent.execute, evaluate_with_judge ni verify_canonical_facts del diseño. Tampoco procesa los argumentos --suite y --min-score mostrados en planificación.

Es una brecha de implementación; no prueba que nunca existiera revisión humana fuera de esta carpeta. No se encontraron salidas que acrediten esa ejecución en el material auditado.

## Límites

No se ejecutaron instaladores, ingesta ni generador; no hubo acceso a APIs, cuentas, pagos/campus, publicación o configuración global. No se midió calidad estocástica instalada ni conformidad jurídica vigente.

El texto del manual PDF se conserva en evidencias/10_manual_original_pdf.txt (24 páginas), sin examen visual/OCR. El .doc antiguo se identificó como binario OLE y no se extrajo independientemente; no se presupone idéntico al PDF/Markdown.
