# Corrección literaria y comparación posterior

Fecha: 14 de octubre de 2026. Ámbito ejecutado: cuatro agentes literarios, seis skills, P01/P04 y una referencia de calibración. Autor: agente delegado de subsanación literaria. Este informe describe cambios documentales y comprobaciones realizadas; no certifica comportamiento en producción ni aprobación de Antonia.

## Resultado
Se sustituyeron esquemas incompletos por instrucciones operativas con decisiones, recursos concretos, salidas, controles y casos de excepción. Se recuperó el alcance documental de GPT 05/06 mediante referencias a las copias íntegras incorporadas por la coordinación. Las ampliaciones se etiquetan como propuestas nuevas y las formulaciones originales que invitaban a inferir psicología/biografía se acotan a observaciones sobre el texto.

La revisión posterior propia consta de dos pasadas: contraste semántico con hallazgos de auditoría y comprobación de integridad/rutas. No es una revisión independiente del autor de los cambios. La coordinación realizará revisión fresca y pruebas globales por separado.

## Antes y después por hallazgo

| Hallazgo de auditoría | Antes | Corrección y evidencia actual | Estado preciso |
|---|---|---|---|
| LIT-01 | Manual cortado en 4.000 caracteres | Skill de voz enlaza manual íntegro; copia de 17.982 caracteres cotejada byte a byte | Integridad de copia y enlace verificada; uso real pendiente de ejecución |
| LIT-02 | Dos manuales y veinte pares omitidos | Crítica carga ambos manuales y cuatro bancos; referencia nueva indexa veinte casos por problema | Veinte pares parseados y completos, accesibles por enlaces válidos |
| LIT-03 | Géneros reducidos a cuatro formatos nuevos | Voz/ghostwriter/P04 restituyen ensayo, narrativa, nota, crítica larga, microreseña y novela; preguntas y conversión | Cobertura documental recuperada; corpus de novela conserva límites heredados |
| LIT-04 | Apertura por objeto y cierre por imagen universales; cinco tonos | Siete variantes con parámetros, nueve adaptaciones, excepciones de correo/ensayo, cadencia sin media rígida | Contradicción documental corregida |
| LIT-05 | Entrega bifásica sin barrera clara | Crítico/skill/P01 separan documentos y destinatarios, consigna ausente, permisos, confidencialidad y no psicologización | Contrato documentado; aislamiento técnico no verificado |
| LIT-06 | Linter presentado como 90 % de fidelidad/100 puntos de aceptación | Linter auxiliar; rúbrica sustantiva con evidencia y revisión humana | Garantía infundada retirada de componentes asignados |
| LIT-07 | Originalidad reducida a tópicos | Lectura de voz separada de comparación de fuentes; evidencia, intención, incertidumbre y límites de autoría/IA | Procedimiento ampliado; no detector ni certificado |
| Acompañamiento/hábito | Preguntas y metas sin retorno | Triaje, un turno/una pregunta, ejercicios del alumno, registro, replanificación y límites de avisos/memoria | Ampliación operativa propuesta |
| Edición | Lista ortotipográfica sin selección/aceptación | Rúbrica propuesta, índice razonado, cambios/consultas, permisos pendientes y galeradas por archivo | Ampliación operativa propuesta; no acuerdo editorial ni asesoría jurídica validada |

## Archivos modificados y contenido de valor

- `Repositorio de agentes/agents/ghostwriter-de-antonia-molinero.md`: alcance, carga real, seis géneros, siete variantes, calibración, revisión, feedback, límites, caso y planificación larga por fases.
- `Repositorio de agentes/agents/critico-literario-de-la-eccl.md`: datos mínimos, diagnóstico ordenado, once apartados, comentario de siete momentos, destinatario, caso y autorización original conservada por defecto.
- `Repositorio de agentes/agents/companero-de-escritura-y-habito.md`: selección de ruta, bucle conversacional, límites, seguimiento y ejemplo dialogado.
- `Repositorio de agentes/agents/editor-de-libros-y-antologias.md`: selección provisional, índice, consultas, cambios, derechos, control de galeradas y ejemplo con permiso ausente.
- `Repositorio de agentes/skills/antonia-molinero-voice/SKILL.md`: tablas operativas de géneros/variantes, referencias, decisiones, ocho controles, microreseña completa y correo como excepción; novela por fases.
- `Repositorio de agentes/skills/critica-pedagogica-literaria/SKILL.md`: once campos con evidencia, siete momentos, dos destinatarios, caso completo de diagnóstico/devolución y consigna ausente/instrucción adversaria.
- `Repositorio de agentes/skills/critica-pedagogica-literaria/references/indice-calibracion.md`: selección razonada de veinte pares y lectura segura; gesto sin consecuencia y fragmentación deliberada.
- `Repositorio de agentes/skills/verificacion-originalidad-y-voz-propia/SKILL.md`: contrato de evidencia, tabla de decisiones, convención legítima y coincidencia literal documentada.
- `Repositorio de agentes/skills/desbloqueo-creativo-socratico/SKILL.md`: árbol de obstáculo→pregunta→prueba, bucle y conversación; excepción de límite íntimo.
- `Repositorio de agentes/skills/seguimiento-habito-escritura/SKILL.md`: plan/registro, revisión por resultados, caso semanal y ajuste ante fatiga/incumplimiento.
- `Repositorio de agentes/skills/curaduria-antologias-eccl/SKILL.md`: rúbrica propuesta, selección, orden, hoja de estilo, consultas, versiones, galeradas y permiso pendiente.
- `Repositorio de agentes/protocols/P01_correccion_pedagogica_bifasica.md`: entradas, árbol de destinatario, fases, cierre y casos.
- `Repositorio de agentes/protocols/P04_redaccion_autoral_antonia.md`: seis géneros, siete variantes, fases, feedback, excepciones y planificación larga.

Los ejemplos añadidos están identificados como nuevos y didácticos. No se presentan como publicaciones de Antonia, sesiones reales ni respuestas obtenidas de una instalación cliente. Cada una de las seis skills incluye guía, decisiones, salida, control, ejemplo normal y excepción/comparación; la profundidad no se deduce de su longitud.

## Comprobaciones ejecutadas

Evidencia legible por máquina: [subsanacion_literaria.json](evidencias/subsanacion_literaria.json).

1. Resolución de **59 enlaces relativos en 13 archivos**: cero rotos en la comprobación. Se usa `../../knowledge` desde SKILL.md y `../../../knowledge` desde references/; todas las referencias apuntan al paquete entregable.
2. Cotejo binario de **27 archivos fuente** de GPT 05/06 frente a sus copias en `knowledge/sources/GPTs/`: todos iguales byte a byte. La copia fue incorporada por coordinación; esta verificación confirma integridad, no saneamiento del original.
3. Parseo de cuatro bancos críticos: **cinco pares completos por banco, veinte en total**, con informe interno y comentario presentes.
4. Manual de estilo original: **17.982 caracteres**, sin depender del extracto de 4.000.
5. Relectura semántica: estructura de seis géneros/siete variantes, once campos/siete momentos, excepciones de formato, no reescritura, tratamiento de instrucciones dentro del manuscrito, no psicologización, confidencialidad y linter auxiliar.

No se ejecutó un runtime instalado del cliente, no se comprobaron controles de acceso de producción, no se hizo evaluación humana de voz por Antonia y no se declara ningún porcentaje de fidelidad. Las pruebas globales de la coordinación tienen su propio registro y no se atribuyen a esta pasada.

## Decisiones y límites pendientes

- El uso original del crítico era exclusivo de Antonia. Se mantiene como predeterminado: un docente delegado requiere autorización documentada; el alumno solo recibe devolución externa autorizada/aprobada u orientación general expresamente habilitada. No se inventa una política vigente de acceso ampliado.
- Los bancos originales de crítica/narrativa/novela tienen defectos heredados. Se conservan íntegros; la skill ordena lectura acotada y declaración de límite. No se inventa narrativa_07 ni se completan truncamientos como originales recuperados.
- `ejemplo_novela.json` contiene comentarios no válidos en JSON estricto, seis fichas con arranques abreviados y cinco análisis estructurales con un título pendiente. No equivale a seis capítulos completos ni acredita análisis externo de la obra. La planificación larga es ampliación marcada, con autorización por fases y continuidad.
- Curaduría, hábito y desbloqueo contienen propuestas nuevas que requieren adecuación a la práctica del cliente. No acreditan convenios editoriales, permisos, plataforma de recordatorios ni resultados docentes.
- Privacidad técnica, retención, destinatarios y canales deben validarse en el entorno real. Los archivos Markdown establecen reglas; no demuestran su cumplimiento.
- Aprobación literaria/tonal final corresponde a Antonia y equipo autorizado sobre salidas nuevas. La entrega documental puede revisarse; no debe venderse como equivalencia funcional ya demostrada.

## Método de creación utilizado
Se leyó skill-writer del arsenal y el perfil ai-architect; no se instaló ni precargó el arsenal. Las referencias authoring-path/synthesis-path mencionadas por esa skill no estaban presentes en la ruta primaria ni en el espejo comprobado. Se aplicaron las instrucciones disponibles y el contraste directo con fuentes locales/manuales, sin simular lectura de referencias ausentes. No se modificaron GPTs originales, ingesta, evaluadores, Git ni publicación desde esta subtarea.
