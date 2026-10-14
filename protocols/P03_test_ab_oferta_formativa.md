# 📜 Protocolo P03: Test A/B y Validación de Oferta Formativa
### Procedimiento Operativo Estándar para Focus Group con Alumnos Sintéticos

---

## 🎯 1. Propósito y Alcance
Evaluar el impacto, interés, disposición al pago (WTP) y posibles objeciones de nuevos cursos, cambios de tarifas o formatos antes de su publicación oficial.

---

## 👥 2. Roles Intervinientes
- **Asistente Responsable:** [`consejo-de-alumnos-sinteticos`](../agents/consejo-de-alumnos-sinteticos.md)
- **Skills Involucradas:** [`synthetic-audience-panel-eccl`](../skills/synthetic-audience-panel-eccl/SKILL.md), [`business-intelligence-cultural`](../skills/business-intelligence-cultural/SKILL.md)
- **Fuente de Conocimiento:** `knowledge/avatares/panel_18_alumnos.json`

---

## 🔄 3. Fases del Flujo de Trabajo

### Fase 1: Definición de la Hipótesis de Oferta
1. Definir ficha del curso: título, temario, profesor, modalidad (Presencial/Online/Diferido), fechas y precio.

### Fase 2: Simulación de Focus Group
1. Ejecutar el test frente al panel de 18 avatares.
2. Registrar reacciones segmentadas por tipo de perfil (madres trabajadoras, opositores, jubilados, jóvenes, profesionales).
3. Identificar frenos comunes: falta de tiempo, miedo al compromiso anual, precio no fraccionado, horario incompatible.

### Fase 3: Ajuste y Optimización
1. Si la aceptación es < 70%, ajustar modalidad (e.g. ofrecer opción online diferido) o flexibilizar el pago.
2. Re-testar y emitir dictamen final para la dirección académica.
