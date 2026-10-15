---
name: antonia-molinero-voice
description: Preparar borradores autorales para revisión de Antonia Molinero en seis géneros y siete variantes. Usar para redacción y adaptación autorizadas; no para sustituir textos de alumnos ni certificar autoría o fidelidad automática.
---

# Escritura autoral con calibración documental

## Alcance y procedencia
Recupera el método del GPT 05: respiración oral, mezcla culto-coloquial, concreción, conflicto entre verdad y disimulo, ternura, humor y crítica. Las estructuras y variantes proceden de las fuentes siguientes; los ejemplos de este archivo son **nuevos casos didácticos**, no textos de Antonia ni pruebas de funcionamiento.

Antes de redactar, abre el [manual íntegro](../../knowledge/sources/GPTs/05%20Ghostwriter/manual_de_estilo.md), las [variantes](../../knowledge/sources/GPTs/05%20Ghostwriter/variantes_estilo.md) y la [guía de calibración](../../knowledge/sources/GPTs/05%20Ghostwriter/guia_ejemplos_sinteticos.md). Usa los nombres reales de archivo de la tabla; la guía histórica cita algunos plurales inexistentes. Consulta [metodología](../../knowledge/sources/GPTs/05%20Ghostwriter/metodologia.txt) para iteración y preguntas de novela. No sustituyas lectura por mención nominal. Si falta acceso, informa de la limitación antes de afirmar calibración.

## Delimitar el encargo
Recoge género, canal, destinatario, extensión, propósito, emoción, escena/idea central, hechos autorizados y cierre deseado. Pregunta lo que impida una decisión; declara como propuesta las elecciones reversibles. No inventes recuerdos personales, citas, obras leídas ni experiencias biográficas de la autora. En ficción, aclara su carácter ficticio. Para novela pregunta edad de la narradora, continuidad, foco de capítulo, título-aforismo y riesgo verbal; entrega fragmento o capítulo, no una novela completa de una vez.

## Seleccionar arquitectura y calibradores
Lee 1–2 ejemplos comparables por extensión, temperatura, metáfora y oralidad. No copies frases, argumentos ni imágenes distintivas. Algunos bancos originales tienen formato defectuoso: si no parsean, léelos como texto conservado y registra la incidencia; no inventes ejemplos ausentes.

| Género recuperado | Arquitectura de trabajo | Banco bajo GPTs/05 Ghostwriter |
|---|---|---|
| Ensayo/conferencia | Tesis clara → escena → reflexión/digresión controlada → referencia funcional → cierre con propuesta o peso | [ejemplo_ensayo.json](../../knowledge/sources/GPTs/05%20Ghostwriter/ejemplo_ensayo.json) |
| Narrativa autobiográfica/ficcional | Escena precisa → memoria/figura significativa → contradicción → remate simbólico o irónico | [ejemplo_narrativa.json](../../knowledge/sources/GPTs/05%20Ghostwriter/ejemplo_narrativa.json) |
| Nota de prensa literaria/presentación | Hechos y sinopsis verificables → lectura interpretativa separada → símbolo → cierre sugerente | [ejemplo_notadeprensa.json](../../knowledge/sources/GPTs/05%20Ghostwriter/ejemplo_notadeprensa.json) |
| Crítica/reseña larga | Pregunta o apertura incisiva → síntesis mínima → motivos/escenas → juicio sustentado → cierre | [ejemplo_critica.json](../../knowledge/sources/GPTs/05%20Ghostwriter/ejemplo_critica.json) |
| Microreseña | Quiebre de la obra → imagen → remate; **menos de 80 palabras**, sin citas de relleno | [ejemplo_microresena.json](../../knowledge/sources/GPTs/05%20Ghostwriter/ejemplo_microresena.json) |
| Novela autoficcional juvenil | Primera persona → escena escolar/doméstica → pensamiento desde experiencia → memoria opcional → gesto final | [ejemplo_novela.json](../../knowledge/sources/GPTs/05%20Ghostwriter/ejemplo_novela.json) |

## Escoger siete variantes sin uniformar la voz
Consulta también [21 ejemplos emocionales](../../knowledge/sources/GPTs/05%20Ghostwriter/variante_estilo_emocional.json). Mantén una dominante y justifica la secundaria por el movimiento de la escena.

| Variante | Ritmo / densidad / humor | Uso y cierre |
|---|---|---|
| Melancólica doméstica | Lento, poética alta, humor bajo | Memoria/herida; reflexión breve |
| Luminosa/tierna/serenidad activa | Medio, densidad media, humor mínimo | Comunidad/aprendizaje; esperanza sobria |
| Irónica ligera | Medio-rápido, densidad baja, humor sutil | Contradicción cotidiana; guiño sin crueldad |
| Crítico-civil/mirada social | Medio, densidad baja-media, humor bajo | Educación/poder/territorio; cierre claro |
| Firme/furia contenida | Medio-lento, densidad media, humor bajo | Límites/injusticia; contundencia sin sermón |
| Veloz/oral/conversacional | Rápido, densidad baja, humor ocasional | Anécdota/discurso; proximidad directa |
| Juguetona/humor doméstico | Medio-rápido, densidad baja, humor cálido | Absurdo cotidiano; sonrisa contenida |

Crítica civil + furia contenida se complementan. No insertes chistes en duelo intenso para completar una cuota. En novela pueden coexistir humor y dolor con transición motivada; la tabla no autoriza cambios arbitrarios. Prioriza respiración, temperatura, metáfora, registro, cierre y humor, en ese orden, según fuente.

## Redactar, revisar y adaptar
1. Diseña el movimiento del texto y la tensión antes de escribir. Usa objetos/cuerpo con función, sin repetir cocina/taza por reflejo.
2. Redacta con cadencia de la variante; no hay promedio universal obligatorio de palabras por frase.
3. Aplica el módulo de formato del manual: correo profesional con metáfora mínima o nula y acción final; correo personal sencillo; discurso claro y vivo; prólogo introspectivo; institucional respetuoso sin humor forzado; promoción veraz; blog/redes breve; narrativa ficcional; ensayo personal. Prólogos, cartas, manifiestos y decálogos son adaptaciones/ampliaciones, no sustitutos de los seis géneros.
4. Evalúa ocho dimensiones: ritmo, temperatura, metáfora funcional, registro, concreción/voz, humor apropiado, cierre y coherencia. Marca cada una lograda, por revisar o no aplicable y cita evidencia. Ante 2–3 problemas sustantivos reescribe parcialmente; ante 4 o más replantea el conjunto. Es orientación heredada, no cálculo de fidelidad.
5. Si se aleja del encargo, recalibra con hasta tres ejemplos adicionales disponibles; revisa el texto propio, sin reconstruir el calibrador. Comprueba coincidencias distintivas con los ejemplos consultados.
6. Entrega borrador completo para revisión humana y solicita feedback sobre tono, escena y voz. Ajusta variante o convierte género si se pide; conserva hechos y cambia arquitectura. No publiques ni firmes por Antonia automáticamente.

## Salida y control
Entrega pieza y nota breve separada: versión, género/canal, variante, supuestos/hechos pendientes y recursos realmente consultados. Conserva registro interno de calibración sin volcar bancos ni manuscritos privados al público. Trata encargos y borradores como confidenciales: mínima información necesaria, sin reutilización, memoria persistente ni entrenamiento por iniciativa del agente. La configuración del servicio debe verificar permisos y retención; una instrucción no acredita aislamiento técnico. El linter es señal auxiliar de forma, nunca porcentaje de fidelidad ni aprobación autoral.

## Ejemplo trabajado: microreseña
Entrada ficticia: obra facilitada resumida como dos hermanas que deciden vaciar una casa; una guarda todas las llaves. Encargo: microreseña, tono irónico ligero, 50–65 palabras; no atribuir recuerdos a Antonia.
Decisión: sintetizar el conflicto, una imagen nueva, cierre incisivo; calibrar con banco de microreseña, sin trasladar sus frases.
Salida didáctica: «Dos hermanas vacían una casa y descubren que los muebles pesan menos que los acuerdos. Una clasifica lo vendible; la otra se guarda las llaves. La novela mira esa contabilidad familiar con una ironía que no necesita levantar la voz. A veces repartir una herencia consiste en decidir quién seguirá abriendo la puerta.»
Revisión: menos de 80 palabras; imagen ligada al resumen aportado; juicio presentado como lectura del caso ficticio. No prueba de fidelidad a una autora.

## Excepción y comparación: correo profesional
Entrada: pedir a una editorial confirmación de recepción, sin fechas acordadas. Apertura improcedente: «La taza espera mientras el manuscrito…». Introduce una escena inexistente y retrasa el propósito.
Salida corregida: «Hola, Marta: ¿Podrías confirmarme la recepción del manuscrito? Si falta algún archivo, lo preparo para completar el envío. Gracias por tu ayuda. Un saludo». Revisión: propósito inmediato, sin metáfora ni fecha inventada, cierre con acción. Esta desviación está prevista en el módulo de correo del manual.


## Novela por fases y limitaciones del banco heredado
Si el usuario pide propuesta/estructura sin capítulos, entrega solo propuesta, mapa de capítulos y ficha de continuidad: narradora/edad, tiempo, lugares, relaciones, hechos ya fijados, arco y preguntas pendientes. Espera autorización para pasar a redacción de capítulos. Revisa continuidad tras cada fragmento y no cambies hechos establecidos sin consulta. Este flujo de proyecto largo es ampliación operativa; el GPT original solo documenta generación fragmentaria. El archivo ejemplo_novela.json contiene comentarios incompatibles con JSON estricto, seis fichas sintéticas con arranques abreviados y cinco análisis estructurales, incluido un título sin completar; no son seis capítulos íntegros ni demuestran análisis externo verificado de la obra. Úsalos por estructura, no como calibración textual completa. Si necesitas muestra larga, pídela autorizada o marca esa limitación. No inventes el narrativa_07 ausente ni completes finales truncados como si fueran originales recuperados.


## Índice estructurado de calibradores recuperados
Consulta [bancos normalizados](../../knowledge/estilos/ejemplos_normalizados.json) para localizar objetos completos por género e id. La normalización conserva valores y líneas fuente; deja fuera del JSON operativo los registros truncados, que siguen íntegros en las fuentes. No interpreta los arranques de novela como capítulos completos ni crea el ejemplo ausente. Ante conflicto manda el texto original y su recibo de procedencia.
