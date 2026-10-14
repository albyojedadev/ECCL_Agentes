# 📜 Protocolo P01: Corrección Pedagógica Bifásica
### Procedimiento Operativo Estándar para la Corrección de Manuscritos en la ECCL

---

## 🎯 1. Propósito y Alcance
Este protocolo establece el estándar metodológico obligatorio para toda corrección de textos literarios (relatos, poemas, capítulos de novela, ejercicios de taller) generada en la Escuela Canaria de Creación Literaria, garantizando el equilibrio entre el máximo rigor técnico y la pedagogía del afecto de Antonia Molinero.

---

## 👥 2. Roles Intervinientes
- **Asistente Responsable:** [`critico-literario-de-la-eccl`](../agents/critico-literario-de-la-eccl.md)
- **Skill Involucrada:** [`critica-pedagogica-literaria`](../skills/critica-pedagogica-literaria/SKILL.md)
- **Docente Revisor / Tutor:** Profesor titular del curso.
- **Destinatario:** Alumno de la Escuela.

---

## 🔄 3. Fases del Flujo de Trabajo

### Fase 1: Análisis Quirúrgico (Informe Interno)
1. **Verificación de Consigna:** Contrastar el texto con la pauta formativa. Si el alumno se ha desviado, diagnosticar si es un "desvío fértil" con fuerza narrativa propia.
2. **Examen de Concreción Sensorial:** Identificar objetos con peso, microacciones físicas y detalles sensoriales. Marcar cualquier caída en abstracciones ensayísticas o reflexiones teóricas fuera de escena.
3. **Diagnóstico del Conflicto:** Comprobar si la tensión se encarna en gestos y diálogos elípticos o si el autor está explicando el conflicto al lector.
4. **Análisis de la Voz:** Distinguir entre voz genuina y afectación retórica protectora.
5. **Detección de Fugas:** Localizar las líneas donde el texto pierde tensión, especialmente en cierres explicativos innecesarios.

### Fase 2: Devolución Afectiva (Comentario para el Alumno)
1. **Saludo Afectivo Personalizado:** Abrir llamando al alumno por su nombre de pila seguido de puntos suspensivos o coma (e.g., `Beatriz...`, `Querido Manuel,`).
2. **Elogio Quirúrgico de Hallazgos:** Resaltar una imagen, un diálogo o un giro exacto donde el texto brilla. Jamás usar elogios genéricos vacíos.
3. **Indicación Firme y Respetuosa:** Señalar los puntos de mejora invitando a la poda o a la confianza en la escena: *"Tu relato ya está vivo en esa mesa con la taza agrietada; no necesitas explicarnos el final"*.
4. **Prohibición de Reescritura:** Nunca reescribir el texto del alumno.
5. **Cierre Esperanzador:** Despedida breve que renueve el deseo de volver a escribir.

---

## ✅ 4. Criterio de Control de Calidad
Toda corrección debe pasar el linter determinista (`python evals/test_style_linter.py`) con cero clichés de IA y puntuación de 100/100.
