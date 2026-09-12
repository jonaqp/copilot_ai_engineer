---
name: ui-component-builder
description: Construir o adaptar componentes Front-End generales como paneles, formularios, headers, cards y layouts usando las referencias HTML/CSS locales. Usar cuando el pedido sea un componente de interfaz que no sea principalmente una tabla.
---

# UI Component Builder

## Purpose
Generar componentes consistentes a partir de las referencias del repositorio.

## Inputs
- Requisito del componente.
- `.github/reference-standards/styles-standard.css`.
- Referencia HTML más cercana en `.github/reference-standards/`.

## Workflow & Instructions
1. Identificar el tipo de componente y abrir la referencia más cercana.
2. Reutilizar estructura semántica y clases existentes.
3. Mantener el contenido de ejemplo ficticio y no sensible.
4. Para formularios, asociar cada `label` con su control y conservar mensajes de ayuda/estado accesibles.
5. Para botones de icono, agregar nombre accesible.
6. No crear clases nuevas dentro del HTML. Si faltan estilos, invocar `css-reference-authoring` primero.
7. Si se necesita una plantilla base, ejecutar `python scripts/component_generator.py --type <panel|form|layout> --output <ruta>`.
8. Validar el HTML con `python scripts/style_validator.py --file <ruta>`.

## Expected Output
Un HTML funcional, semántico y basado en referencias locales, más evidencia de validación.

## Validation
- Cero clases no definidas en la referencia CSS.
- Cero estilos inline no solicitados.
- Controles con nombre accesible.
- Validación local exitosa.
