---
name: supervision-identidad-visual-eccl
description: Auditoría determinista de cumplimiento de manual de marca: verificación de códigos HEX oficiales, tipografías autorizadas y descarte de clichés visuales de stock.
---

# 🛡️ Skill: Supervisión de Identidad Visual ECCL
### Auditoría Cromática, Tipográfica y Estética

## 🎯 1. Objetivo
Auditar cualquier pieza gráfica antes de su publicación para asegurar que respeta los colores oficiales, tipografías editoriales y principios estéticos de la Escuela.

## 📥 2. Entradas Requeridas
- `propuesta_grafica`: Archivo o descripción con colores HEX, fuentes y elementos visuales.

## ⚙️ 3. Procedimiento Paso a Paso
1. **Chequeo de Paleta HEX:** Comprobar uso de `#FAF8F5`, `#1A1A1A`, `#C2593F`, `#1E3A5F`, `#D4A346`. Rechazar colores fluorescentes o azules SaaS.
2. **Chequeo Tipográfico:** Validar titulares en *Playfair Display* / *Merriweather* y cuerpos en *Inter* / *Open Sans*.
3. **Filtro Anti-Stock:** Bloquear ilustraciones de plumas mágicas o elementos clichés de banco de imágenes.
4. **Emisión de Dictamen:** Emitir veredicto `APROBADO` o `RECHAZADO` con justificación.
