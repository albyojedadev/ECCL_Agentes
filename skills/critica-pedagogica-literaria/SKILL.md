---
name: critica-pedagogica-literaria
description: Procedimiento maestro de corrección pedagógica bifásica de textos literarios (Informe Técnico Interno + Comentario Externo Afectivo) según la metodología de Antonia Molinero.
---

# 📖 Skill: Crítica Pedagógica Literaria
### Procedimiento Maestro de Corrección Bifásica de Textos

## 🎯 1. Objetivo
Guiar la corrección pedagógica de relatos, fragmentos de novela y poemas de alumnos garantizando el doble análisis: rigor técnico interno sin censura y devolución externa cercana, afectiva y constructiva.

## 📥 2. Entradas Requeridas
- `texto_alumno`: Manuscrito entregado por el estudiante.
- `nombre_alumno`: Nombre de pila del alumno.
- `consigna`: Ejercicio o consigna del taller al que responde el texto.
- `curso_pertenencia`: Taller en el que está matriculado (e.g. Iniciación, Creación Anual, Autoficción).

## ⚙️ 3. Procedimiento Paso a Paso
1. **Paso 1: Lectura Fenomenológica:** Leer el texto completo sin intervenir, identificando la emoción latente y el foco temático.
2. **Paso 2: Análisis de Concreción Sensorial:** Evaluar presencia de objetos, gestos, sentidos y microacciones frente a abstracciones explicativas.
3. **Paso 3: Redacción del Informe Técnico Interno:**
   - Cumplimiento de la consigna (o valor del desvío).
   - Diagnóstico del conflicto y la tensión interna.
   - Diagnóstico de la voz y la autenticidad del registro.
   - Puntos exactos de fuga o sobreexplicación.
4. **Paso 4: Redacción del Comentario Externo:**
   - Saludo afectivo llamando al alumno por su nombre (`Elena...`).
   - Elogio quirúrgico de los hallazgos reales.
   - Indicación respetuosa de la poda o reestructuración necesaria sin reescribir.
   - Despedida cálida que devuelva la confianza creadora.
5. **Paso 5: Paso por el Linter:** Verificar que la salida pasa `evals/test_style_linter.py` con 0 clichés de IA.

## 📤 4. Salida Esperada
Texto estructurado en dos bloques claramente delimitados:
- `### 1. Informe Técnico Interno`
- `### 2. Comentario Externo para el Alumno`
