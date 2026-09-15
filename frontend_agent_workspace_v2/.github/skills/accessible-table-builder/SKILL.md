---
name: accessible-table-builder
description: Crear, adaptar o revisar tablas HTML de datos usando el estándar local. Usar para listados tabulares, movimientos, usuarios, reportes o cualquier solicitud donde la estructura principal sea una tabla, incluyendo accesibilidad, acciones por fila y comportamiento responsive.
---

# Accessible Table Builder

## Purpose
Crear tablas semánticas, accesibles y coherentes con `table-standard.html`.

## Inputs
- Columnas y tipo de datos.
- Acciones disponibles por fila, si existen.
- `.github/reference-standards/table-standard.html` y `styles-standard.css`.

## Workflow & Instructions
1. Partir de `.github/reference-standards/table-standard.html`.
2. Usar `<caption>` descriptivo; puede ser visualmente oculto con `ux-local-sr-only` si el diseño no requiere caption visible.
3. Usar `<th scope="col">` en cabeceras; usar `scope="row"` si la primera celda identifica una fila.
4. Mantener acciones con botones/enlaces reales y nombres claros.
5. Envolver la tabla en `ux-local-table-container` para overflow horizontal en pantallas pequeñas.
6. No simular tablas con `div` salvo requisito técnico explícito.
7. No crear nuevas clases ad hoc; delegar estilos faltantes a `css-reference-authoring`.
8. Ejecutar `python scripts/component_generator.py --type table --output <ruta>` si se necesita una base.
9. Ejecutar `python scripts/style_validator.py --file <ruta>`.

## Expected Output
Tabla HTML basada en la referencia local, con encabezados, caption, acciones y validación.

## Validation
- `<table>`, `<thead>`, `<tbody>` presentes.
- Todos los `<th>` deben tener `scope`.
- Debe existir `<caption>`.
- Las clases deben existir en `styles-standard.css`.
- El validador debe pasar.
