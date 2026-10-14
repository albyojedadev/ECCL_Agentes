# 📜 Protocolo P06: Creación y Supervisión de Cartelería y Redes
### Procedimiento Operativo Estándar para Maquetación y Auditoría Visual

---

## 🎯 1. Propósito y Alcance
Garantizar que todo material gráfico publicitario (carteles impresos, publicaciones en redes sociales, Stories y banners web) cumpla estrictamente los estándares estéticos y el manual de marca de la ECCL.

---

## 👥 2. Roles Intervinientes
- **Creador Gráfico:** [`disenador-grafico-y-carteleria`](../agents/disenador-grafico-y-carteleria.md)
- **Auditor de Marca:** [`guardian-de-marca-e-identidad-visual`](../agents/guardian-de-marca-e-identidad-visual.md)
- **Skills Involucradas:** [`diseno-carteleria-y-redes-eccl`](../skills/diseno-carteleria-y-redes-eccl/SKILL.md), [`supervision-identidad-visual-eccl`](../skills/supervision-identidad-visual-eccl/SKILL.md), [`adaptacion-formatos-graficos-eccl`](../skills/adaptacion-formatos-graficos-eccl/SKILL.md)
- **Fuentes de Conocimiento:** `knowledge/branding/paleta_corporativa.json`, `knowledge/branding/tipografias.json`

---

## 🔄 3. Fases del Flujo de Trabajo

### Fase 1: Briefing y Maquetación
1. Recoger datos clave: título del taller, docente, fechas, aforo, lugar (La Laguna / Online) y precio.
2. Definir formato de salida (Cartel A3/A4, Post Instagram 1:1, Story 9:16 o Banner web).
3. Maquetar jerarquía visual:
   - Titular literario (Playfair Display / Merriweather).
   - Bloque docente y fechas (Inter / Open Sans).
   - Fondo marfil `#FAF8F5`, acentos en terracota `#C2593F` o azul atlántico `#1E3A5F`.

### Fase 2: Auditoría Determinista de Marca
1. Someter la propuesta a la auditoría del Guardián de Marca (`python evals/test_brand_linter.py`).
2. Validar que:
   - Los colores HEX pertenecen exclusivamente a la paleta oficial autorizada.
   - No hay tipografías no autorizadas ni cursivas informales.
   - Las safe zones perimetrales respetan los márgenes para no solapar textos.
   - Cero clichés de stock (sin plumas doradas mágicas ni pergaminos quemados).

### Fase 3: Publicación y Archivo
1. Tras obtener el dictamen `🟢 APROBADO`, exportar a formato final (PDF para imprenta en CMYK / PNG alta resolución para redes en RGB).
2. Publicar en canales oficiales y archivar en el repositorio corporativo.
