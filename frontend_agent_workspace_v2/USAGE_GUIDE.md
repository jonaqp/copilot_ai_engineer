# Guía de uso — Front-End UI Engineer para GitHub Copilot

Este workspace convierte el agente Front-End en una configuración reutilizable basada en **custom agent + instrucciones de repositorio + Agent Skills + referencias + validación determinista**.

## 1. Estructura

```text
.github/
  copilot-instructions.md
  agents/frontend-ui.agent.md
  skills/
    css-reference-authoring/
    ui-component-builder/
    accessible-table-builder/
    frontend-quality-gate/
reference-standards/
  styles-standard.css
  panel-standard.html
  form-standard.html
  layout-standard.html
  table-standard.html
examples/basic-guide.html
scripts/
  component_generator.py
  style_validator.py
  workspace_check.py
```

## 2. Cómo usarlo en Copilot

1. Abre el repositorio en un entorno de GitHub Copilot compatible con custom agents / Agent Skills.
2. Selecciona el agente **frontend-ui-engineer**.
3. Pide una tarea concreta. El agente debe cargar solo la referencia y skill pertinentes.

Ejemplos:

```text
Crea una tabla de movimientos con fecha, concepto, importe y estado. Usa el estándar local y valida el HTML.
```

```text
Necesito un formulario de alta de cliente dentro de un panel. No inventes clases; reutiliza las referencias.
```

```text
Amplía la referencia CSS con un patrón reutilizable para mensajes de error y actualiza el ejemplo correspondiente.
```

## 3. Generación determinista de plantillas

```bash
python scripts/component_generator.py --type panel --output tmp/panel.html
python scripts/component_generator.py --type table --output tmp/table.html
python scripts/component_generator.py --type form --output tmp/form.html
python scripts/component_generator.py --type layout --output tmp/layout.html
```

## 4. Validación

Valida un HTML:

```bash
python scripts/style_validator.py --file examples/basic-guide.html
```

Valida todo el workspace:

```bash
python scripts/workspace_check.py
```

## 5. Ejemplo HTML básico

Abre `examples/basic-guide.html`. Incluye:
- carga del CSS de referencia;
- layout de página;
- panel con formulario;
- tabla accesible;
- clases `ux-local-*` únicamente.

## 6. Regla para ampliar CSS

Si un componente necesita un estilo que no existe, no crees una clase aislada dentro de la vista. Pide al agente que use `css-reference-authoring`, agregue el patrón a `reference-standards/styles-standard.css`, actualice una referencia HTML y ejecute `workspace_check.py`.

## 7. Flujo recomendado

Para tareas grandes: **diagnóstico -> plan -> implementación -> validación**. Mantén el contexto limitado a los archivos necesarios y trabaja por fases.
