---
name: css-reference-authoring
description: Crear o ampliar estándares CSS reutilizables del proyecto. Usar cuando falten tokens, estados o clases `ux-local-*`, cuando se pida definir una referencia visual compartida, o cuando un componente requiera estilos nuevos que deben incorporarse primero a `reference-standards/styles-standard.css`.
---

# CSS Reference Authoring

## Purpose
Extender el estándar visual compartido sin generar CSS aislado por componente.

## Inputs
- `reference-standards/styles-standard.css`.
- HTML de referencia relacionado, si existe.
- Requisito visual o funcional solicitado.

## Workflow & Instructions
1. Leer el bloque de `:root` y reutilizar tokens existentes.
2. Buscar una clase equivalente antes de crear una nueva.
3. Si hace falta una clase nueva, nombrarla con prefijo `ux-local-` y describir una responsabilidad concreta.
4. Preferir composición de clases pequeñas antes que selectores muy específicos.
5. Mantener estados `:hover`, `:focus-visible` y `:disabled` cuando el componente sea interactivo.
6. Evitar `!important`, selectores por ID y estilos inline.
7. Mantener contraste, foco visible y tamaños de interacción razonables.
8. Actualizar o crear el HTML de referencia que demuestre el nuevo patrón.
9. Ejecutar `python scripts/workspace_check.py`.

## Expected Output
- CSS reutilizable en `reference-standards/styles-standard.css`.
- Referencia HTML actualizada cuando aplique.
- Resumen de tokens/clases añadidos o reutilizados.

## Validation
- No duplicar tokens con el mismo propósito.
- Todas las clases nuevas deben usar `ux-local-`.
- No introducir framework externo.
- `workspace_check.py` debe finalizar sin errores.
