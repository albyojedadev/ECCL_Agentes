---
name: adaptacion-formatos-graficos-eccl
description: Adaptar una pieza a cuadrado, vertical, banner e impresión mediante reflujo, cajas y márgenes verificables; no asumir que escalar conserva lectura o que la interfaz actual está validada.
---

# Adaptación multiformato con control geométrico

## Entradas
Pide editable/cajas o imagen real, tamaño original, elementos esenciales, destinos, copy aprobado, fotos/logos y permisos. Una imagen plana permite recorte/escala, pero no remaquetación tipográfica exacta sin reconstrucción. Si solo hay descripción, entrega especificación y controles pendientes; no afirma archivo convertido.

## Parámetros de trabajo
| Destino | Tamaño | Área segura propuesta |
|---|---|---|
| Post cuadrado |1080×1080 px|x/y entre 80 y 1000|
| Story vertical |1080×1920 px|x 60..1020, y 250..1670|
| Banner |1200×630 px|margen de trabajo 60 px, verificar recorte del canal|
| A4 |210×297 mm al corte|texto 15 mm dentro; sangrado 3 mm si imprenta confirma|
| A3 |297×420 mm al corte|texto 15 mm dentro; sangrado 3 mm si imprenta confirma|

Son parámetros de la propuesta visual local, no especificación oficial del cliente ni garantía de UI de una red. Verifica vista previa del canal y ficha de imprenta actuales. Sangrado es exterior al corte y no sustituye margen interior.

## Procedimiento
1. Inventaría título, docente/fecha/lugar, CTA, logo y prueba. Asigna prioridad; datos imprescindibles no se eliminan para caber.
2. Calcula escala uniforme: contener=min(ancho_dest/ancho_ori, alto_dest/alto_ori); cubrir=max(...). Contener añade espacio; cubrir recorta. Para cada caja transformada compara límites; no estires proporciones de logo/foto.
3. Prefiere reflujo por soporte a escalar todo. Vertical apila; horizontal reduce copy y separa dos columnas; impresión conserva cuerpo legible a distancia prevista. Si texto no cabe, divide pieza o remite detalles al pie/canal accesible, sin esconder información contractual relevante.
4. Verifica cada caja: x≥margen_izq, y≥margen_sup, x+ancho≤límite_der, y+alto≤límite_inf. En impresión trabaja en mm al corte; fondos/fotos llegan al sangrado requerido. Revisa también recorte de foto, rostro y créditos.
5. Lee a tamaño de uso. Ajusta saltos manuales y jerarquía; registra contraste/legibilidad realmente medidos. Revisa textos tras reconstruir: no perder fecha, signo, tilde ni precio.
6. Exporta solo con herramienta real: digital según canal, impresión según perfil/PDF de imprenta. Mantén editable, versión y alt/pie asociados. No asegurar CMYK, fuentes incrustadas o resolución por una extensión de archivo.
7. Compara contenido entre versiones y remite supervisión/P06. Cambiar dimensiones reabre aprobación de recorte y lectura.

## Plantilla de entrega
Original/destino → escala o reflujo elegido y razón → tabla elemento/caja original/caja destino/segura sí-no → copy conservado/abreviado → archivo real/especificación → comprobaciones pendientes.

## Ejemplo trabajado nuevo, sintético
**Entrada:** cuadrado 1080; título en(100,120,880,180), cuerpo(100,350,880,350), CTA(100,800,880,100). Destino Story.

**Salida:** conservar escala 1 y centrar contenido cuadrado añadiendo 420 px a y. Título(100,540,880,180), cuerpo(100,770,880,350), CTA(100,1220,880,100). Todas las cajas: x 100..980 dentro 60..1020 y y 540..1320 dentro 250..1670. Extender fondo, no foto deformada. La geometría pasa; lectura/contraste y vista previa siguen pendientes hasta ver archivo. Para A4 con sangrado 3, soporte 216×303 mm y área de texto al corte x 15..195, y 15..282; no confundir ambos rectángulos.

**Excepción:** banner tiene seis líneas al escalado. Reescribir/refluir: título+fecha+CTA, detalles al pie, en lugar de texto ilegible. **Antipatrón:** aprobación cuadrada transferida a Story sin revisar. **Corrección:** nueva revisión por destino.

## Referencias
- [Parámetros propuestos](../../knowledge/branding/paleta_corporativa.json).
- [Manual histórico, §§5.2,6–7 y manual 8](../../knowledge/sources/GPTs/03%20Experto%20de%20la%20escuela/manual_de_comunicacion_escuela_literaria_ecl.md).
- [Supervisión](../supervision-identidad-visual-eccl/SKILL.md), [P06](../../protocols/P06_creacion_y_supervision_carteleria.md).
