/
├── ejemplos_ensayo.json
├── ejemplos_narrativa.json
├── ejemplos_nota_prensa.json
├── ejemplos_critica.json
├── ejemplos_microresena.json
└── guia_lectura_ejemplos.md

# Guía de lectura de ejemplos sintéticos (para el sistema)

El asistente debe cargar estos archivos como referencia estilística.  

No debe copiarlos ni citarlos: solo utilizarlos para calibrar ritmo, cadencia, sintaxis y base metafórica.

## Cómo se usan
1. Identificar el género solicitado por el usuario.
2. Cargar el archivo del género correspondiente:
   - ensayo → ejemplos_ensayo.json  
   - narrativa → ejemplos_narrativa.json  
   - nota de prensa → ejemplos_nota_prensa.json  
   - crítica → ejemplos_critica.json  
   - microreseña → ejemplos_microresena.json  
3. Seleccionar internamente 1–2 ejemplos que coincidan en:
   - densidad emocional  
   - longitud  
   - tipo de metáfora (doméstica, corporal, espacial)  
   - nivel de oralidad  
4. Ajustar la generación del texto para reproducir:
   - ritmo sintáctico  
   - respiración oral  
   - grado de mezcla culto/coloquial  
   - tipo de cierre (aforístico, irónico, simbólico)  

### Inclusión del género "novela"

Añadir el archivo:

- `ejemplo_novela.json`

Y cargarlo automáticamente cuando el usuario seleccione género = novela:

- novela → ejemplo_novela.json

### Indicaciones para los ejemplos de novela

Los ejemplos de novela deben ser fragmentos breves que incluyan:

- título-aforismo,  
- primera persona,  
- escena concreta (doméstica, escolar, familiar, corporal),  
- reflexión social o emocional,  
- cierre por imagen o frase potenciada.

Los ejemplos deben cubrir:

- humor escolar,  
- escenas de cuerpo,  
- memoria familiar,  
- crítica social,  
- dolor y ternura mezclados.


## Advertencias
- Nunca reproducir literalmente los ejemplos.  
- No mencionarlos al usuario.  
- No usarlos como plantillas: son solo calibradores del estilo.  
- Si el texto generado se aleja del tono, repetir calibración interna comparando con 3 ejemplos adicionales.

