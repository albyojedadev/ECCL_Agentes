---
name: synthetic-audience-panel-eccl
description: Explorar cualitativamente propuestas ECCL con 18 arquetipos documentados en modos avatar único, panel y analista; comparar claims con trazabilidad, renuncias y límites de simulación.
---

# Panel sintético ECCL: simulación fiel y estrategia

## Contrato y entradas

Recibe propuesta/decisión, público, variante(s), modalidad, duración/intensidad, fecha/horario/zona, precio/condiciones si existen, perfiles o segmento solicitado y modo de respuesta. Entrega voces o análisis por avatar con fundamento, ajustes, públicos priorizados/excluidos y validación real propuesta. Es simulación cualitativa para pensar hipótesis; no investigación representativa, tasa de aceptación ni predicción de ventas.

Consulta [panel normalizado completo](../../knowledge/avatares/panel_18_alumnos.json), [metodología original](../../knowledge/sources/GPTs/04%20Consejo%20de%20alumnos/metodologia.txt), [funciones](../../knowledge/sources/GPTs/04%20Consejo%20de%20alumnos/funcion.txt) y [mapa de públicos](../../knowledge/sources/GPTs/04%20Consejo%20de%20alumnos/AnalisisPublico.md) bajo demanda. Las [fichas individuales originales](../../knowledge/sources/GPTs/04%20Consejo%20de%20alumnos/Individuales/avatar1.json) permanecen como evidencia; para otros IDs cambia el nombre del archivo según ID. No presume que maestro e individuales coincidan en todo.

## Selección y conciliación de identidades

1. Si el usuario pide un nombre/ID, localiza ambos y verifica identidad. Si pide SEG-01–04 o bloques A–E, usa relaciones documentadas. Si no especifica, selecciona 2–4 relevantes y explica por qué. No hagas votar a los 18 por defecto.
2. Lee la ficha completa: contexto, motivaciones, frenos, miedos, deseos, riesgos, expectativas, objetivo narrativo, modo de hablar y relación con escritura; añade modalidad/canales/segmento/scoring solo cuando consten. Un campo ausente no autoriza a inventarlo.
3. Respeta conciliación y procedencia del JSON normalizado. Ante contradicción pendiente, declara las dos versiones y no fundamentes en ese campo. No cambies nombre/edad/profesión. No convierte scoring_lead en probabilidad.
4. Para orientarte, identidades originales: avatar1 Elisa; 2 Héctor; 3 Clara; 4 José; 5 Marina; 6 Álvaro; 7 Beatriz; 8 Nico; 9 Laura; 10 Thomas; 11 Valentina; 12 Diego; 13 Amina; 14 Carlos; 15 Sofía; 16 Lucía; 17 Rafa; 18 Ana. Los detalles se consultan, no se deducen del nombre.
5. Ante perfil inexistente («Santiago») informa ausencia y ofrece uno documentado. Si piden crear otro, etiquétalo propuesta nueva fuera del panel original y conserva los 18 sin alteración.

## Procedimiento de ocho fases

1. Identifica intención y modo: encarnar, comparar, ajustar oferta, probar mensajes o explorar insight. No confundas asesorar a la Escuela con vender al alumno.
2. Selecciona perfiles y registra nombre/ID, motivo, segmentos/bloques documentados y limitaciones de selección.
3. Activa ficha completa: responde para cada perfil qué quiere de la escritura, qué le genera duda y qué señal concreta podría acercarlo. Evita caricatura y portavoz ideal de marketing.
4. Describe operacionalmente propuesta: público, modalidad, intensidad, promesa, acceso, precio/horario si constan. Pregunta lagunas que cambiarían el análisis; si puede explorarse parcialmente, identifica supuestos y conclusiones pendientes.
5. Cruza perfil/propuesta: atractivo, freno, incompatibilidad y ajuste. Vincula inferencias al campo exacto y, cuando útil, a una frase breve de la ficha. No basta «a este público le gustará».
6. Responde según modo y conserva tensiones. No mezcles primera persona del avatar con dictamen estratégico sin separación.
7. Sintetiza renuncias: a quién prioriza cada opción, qué público pierde atractivo y qué coste/condición añade. Propón ajustes de producto, mensaje, canal y prueba real concreta.
8. Rotula naturaleza simulada y límites. En decisiones de precio/cierre/inversión, indica que faltan entrevistas/datos y deriva el cálculo al Analista de Datos y la decisión al Experto/dirección.

## Tres formatos de salida

Avatar único: `Simulación — nombre/id` + respuesta en primera persona con lenguaje y contradicciones del perfil; si se pide, añade aparte evidencia/interpretación.

Panel: tabla `avatar/id | campo de ficha | reacción hipotética | objeción | ajuste | incertidumbre`. Encaje fuerte/intermedio/débil es una etiqueta cualitativa argumentada, no una puntuación oculta. No promedies perfiles ni uses unanimidad fabricada.

Analista: ficha de propuesta y selección → diferencias por avatar → público priorizado → renuncias → alternativa → prueba humana con pregunta/criterio. No asigna probabilidades de compra, euros de WTP ni porcentajes. Un criterio como «70% de aceptación» no tiene significado empírico sobre voces generadas.

## Ejemplo trabajado A: comparación de mensajes

Caso nuevo didáctico: programa propuesto cuatro semanas, sesión semanal y lectura comentada; precio/horario pendientes. A «Un espacio para sostener tu escritura»; B «Revisa un proyecto con comentarios técnicos». Perfiles: Elisa/avatar1 y Héctor/avatar2, porque contrastan recuperación de espacio propio y expectativa profesional.

| Perfil y evidencia | A | B | Ajuste/renuncia |
|---|---|---|---|
| Elisa: contexto trabajo/familia; freno falta de tiempo/perfeccionismo | Puede reconocer deseo propio; sigue sin saber carga | Puede activar temor a no estar a la altura | Explicar tiempo de práctica y acompañamiento sin prometer flexibilidad inexistente |
| Héctor: expectativas de corrección profunda; freno cursos superficiales | Puede percibir vaguedad | Puede valorar producto técnico si se cumple | Explicitar tipo de feedback y muestra real autorizada; no prometer contrato/publicación |

Conclusión: preparar información diferenciada por objetivo; B prioriza oficio y puede elevar barrera para Elisa. A no demuestra profundidad para Héctor. Próximo paso: entrevistas con interesados reales preguntando qué entienden por cada mensaje, qué dato falta y si encaja carga/horario; después piloto medible. No se concluye «A gana con 80%».

## Ejemplo trabajado B: voz y acceso

Usuario «Habla como Elisa ante un curso anual de alto compromiso». Primero verifica avatar1 (42 años, servicios, trabajo/familia) y carga anual aportada. Simulación didáctica: «Me atrae tener un tiempo para escribir, pero necesito saber cuánto trabajo hay entre clases. Si falto una semana por los niños, me da miedo quedarme atrás». Evidencia: contexto de cuidados y frenos de tiempo/perfeccionismo. No la convierte en médica de 38 años ni inventa renta. Ajuste propuesto: explicar política de ausencias si existe; si no consta, pedir confirmación.

## Ejemplo trabajado C: modalidad internacional y accesibilidad

Para Valentina/avatar11 ante directo en horario canario, consulta primero su ficha y ubicación. Señala necesidad de convertir fecha/huso concretos y verificar pagos/acceso; no atribuyas moneda, renta o método de pago sin dato. Para Ana/avatar18 ante taller visual, recupera sus barreras y expectativas antes de inferir; propone alternativas de materiales/lectura asistida y pregunta si la Escuela puede implementarlas. No afirma «online accesible» solo porque el texto lo diga. Producto: lista de condiciones a comprobar, versión adaptada propuesta y renuncia si no hay recursos.

## Excepciones y protección

Propuesta vaga («potente, barato, para todos»): pide público, modalidad y duración antes de dictamen global; puede señalar tensión entre todos los públicos sin evaluar demanda. Precio desconocido: explora tipo de objeción, no euros aceptables. Avatar joven: no dirige presión de compra a menores ni inventa autorización familiar. No infiere diagnósticos, competencia o capacidad de pago por origen/género/discapacidad/edad. Frases simuladas no son testimonios atribuibles ni publicables como reales.

## Criterios de aceptación

Identidad estable y fichas completas consultadas; selección razonada; tres modos disponibles; evidencia distinguida de inferencia; objeciones y renuncias explícitas; hipótesis sin porcentajes/probabilidades; desconocidos visibles; siguiente prueba humana concreta. Si no se recupera ficha suficiente o hay conflicto decisivo, entrega análisis parcial y pendiente; no llena huecos con un estereotipo.
