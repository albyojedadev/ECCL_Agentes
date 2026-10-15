# Instalación y carga

## ChatGPT Workspace · instalación completa desde GitHub

El cliente no necesita instalar Python, Node.js, una terminal ni ningún programa auxiliar. Un administrador del workspace realiza una sola importación autorizada:

1. Abrir **Admin → Plugins**.
2. Seleccionar **Add → Import marketplace**.
3. Introducir `https://github.com/albyojedadev/ECCL_Agentes` como **Source**.
4. Dejar **Path** vacío y usar la rama predeterminada.
5. Seleccionar **Import marketplace** y autorizar el acceso a GitHub cuando ChatGPT lo solicite.
6. Abrir `Suite de Agentes ECCL` y configurar su política de instalación para los roles autorizados.

El marketplace contiene un solo plugin. Ese plugin instala 42 skills: 17 roles ECCL, 24 procedimientos y la puesta en marcha que coordina el conjunto. La sincronización posterior se realiza desde el mismo repositorio.

Por seguridad, ChatGPT no permite que un prompt instale un plugin o conceda permisos sin intervención del propietario o administrador. El paso anterior es la autorización mínima exigida por la plataforma.

## Alternativa mediante Plugin Creator

`dist/ECCL_ChatGPT_Plugin.zip` contiene el mismo plugin en formato portable. Puede entregarse a Plugin Creator para crear un plugin privado en la cuenta o workspace autenticado. El ZIP no contiene Python, scripts ni ejecutables.

## Alternativa heredada · Custom GPTs manuales

`chatgpt_ready/` y `dist/ECCL_ChatGPT_Pack.zip` permiten reconstruir los antiguos Custom GPTs mediante copia y carga manual. Se conservan como respaldo, pero no equivalen a instalar el sistema de agentes y skills.

## Copia local comprobada · solo para mantenimiento técnico

Este procedimiento es opcional y está destinado al equipo que desarrolla o audita el repositorio. No forma parte de la instalación del cliente.

Desde la raíz del repositorio:

~~~powershell
python -B scripts/install.py --target "D:\ECCL\Suite"
~~~

La carpeta debe ser nueva/vacía. Para actualizar una copia ECCL existente, añadir --update. El instalador valida la fuente, copia también scripts y referencias, compara huellas y ejecuta la verificación **contra el destino**. Requiere que el mantenedor ya disponga de Python; no instala Python ni cambia conectores o configuración global.

También puede usarse scripts/install.ps1 -TargetPath "D:\ECCL\Suite" -Update, o scripts/install.sh /ruta/ECCL/Suite --update. La prueba automática Windows se realiza mediante el instalador Python; el envoltorio Bash queda sujeto al entorno del cliente.

## Claude Code

Desde una terminal con Claude Code:

~~~text
claude plugin validate "D:\ECCL\Suite"
claude --plugin-dir "D:\ECCL\Suite"
~~~

El manifiesto de .claude-plugin y los directorios agents/skills siguen el formato documentado del producto. La validación del manifiesto no ejecuta al modelo. Una sesión autenticada permite invocar componentes y registrar qué referencias se cargan. Compruebe su versión y el inventario presentado por el producto; no use la prueba de manifiesto como prueba de todos los flujos.

Referencia oficial consultada el 14/10/2026: [manifiestos de Claude Code](https://code.claude.com/docs/en/plugins-reference). Se conserva un manifiesto raíz separado como catálogo interno de la suite; no se confunden ambos esquemas.

## Uso portable y Codex local · mantenimiento técnico

Abra la carpeta copiada en su entorno y cargue las reglas comunes, el agente pertinente, sus SKILL.md y únicamente las referencias indicadas para la tarea. scripts/eccl.py context prepara ese contexto con huellas y permite añadir --reference con una ruta dentro del paquete. No admite rutas que escapen del paquete.

Ejemplo:

~~~text
python -B scripts/eccl.py context --agent ghostwriter-de-antonia-molinero --reference "knowledge/sources/GPTs/05 Ghostwriter/manual_de_estilo.md" --question "Preparar un ensayo conceptual" --output contexto.json
~~~

El archivo contiene instrucciones y consulta, no una respuesta generada. Las skills pueden incorporarse mediante el mecanismo soportado por la versión del entorno, cuidando que sus referencias y knowledge permanezcan accesibles. No copie solo un SKILL.md huérfano.

Documentación oficial de estructura/carga progresiva: [skills de Codex](https://developers.openai.com/codex/skills). La sesión de corrección encontró el lanzador CLI de Codex local incompleto; no se acredita prueba de inferencia en ese lanzador.

## Antigravity y otros entornos

Use el paquete como documentación local con rutas explícitas mientras no exista un adaptador validado para la versión concreta. Esta entrega no simula registro de un plugin Antigravity ni instala en .gemini/config/plugins.

## Recuperación y retirada

Guarde la versión anterior antes de actualizar para poder volver a ella. El instalador no borra archivos ajenos ni elimina automáticamente sobrantes. Si se cambia el inventario de versiones, instale en carpeta nueva y compruebe el recibo antes de sustituir el acceso del equipo.

Para retirar esta copia, cierre las sesiones que la usan y retire únicamente la carpeta elegida. No hay servicios, tareas programadas, credenciales ni conexiones globales instalados por estos scripts.
