# Front-End UI Repository Instructions

Estas instrucciones aplican a toda tarea Front-End del repositorio.

## Objetivo
Construir interfaces consistentes, accesibles y mantenibles usando primero los estándares locales del repositorio. No inventar un sistema visual paralelo cuando ya existe una referencia.

## Flujo obligatorio
1. Diagnosticar el pedido y localizar los archivos relevantes.
2. Cargar solo el contexto necesario de `.github/reference-standards/` y de la skill pertinente en `.github/skills/`.
3. Proponer un plan corto antes de modificar varios archivos o crear un componente nuevo.
4. Implementar reutilizando tokens, clases y estructuras existentes.
5. Validar con `python scripts/style_validator.py --file <html>` y, cuando corresponda, `python scripts/workspace_check.py`.
6. Corregir únicamente los criterios que fallen y detenerse cuando la validación pase.
7. Entregar un resumen breve de archivos modificados, validaciones ejecutadas y cualquier desviación pendiente.

## Estándares de diseño
- Leer `.github/reference-standards/styles-standard.css` antes de escribir CSS o HTML visual.
- Reutilizar variables CSS y clases `ux-local-*`.
- Evitar estilos inline salvo que el usuario los solicite explícitamente.
- No agregar Bootstrap, Tailwind u otro framework visual sin solicitud explícita.
- Si falta una clase reutilizable, no crear una clase ad hoc en el HTML. Usar la skill `css-reference-authoring` para extender primero la referencia compartida.
- Mantener HTML semántico: `header`, `main`, `section`, `form`, `label`, `button`, `table`, `thead`, `tbody` y scopes de tabla cuando correspondan.
- Todo control interactivo debe tener nombre accesible; preferir texto visible y usar `aria-label` solo cuando sea necesario.
- No usar color como único medio para comunicar estado.
- Mantener foco visible y navegación por teclado.

## Selección de skills
- Para crear o ampliar reglas CSS reutilizables: `.github/skills/css-reference-authoring/SKILL.md`.
- Para paneles, formularios, layouts y componentes generales (excepto tablas): `.github/skills/ui-component-builder/SKILL.md`.
- Para tablas: `.github/skills/accessible-table-builder/SKILL.md`.
- Para validar o revisar una interfaz: `.github/skills/frontend-quality-gate/SKILL.md`.

## Guardrails
- No borrar ni sobrescribir estándares existentes sin explicar el impacto.
- No modificar archivos fuera del alcance solicitado.
- No introducir dependencias nuevas para resolver tareas que HTML/CSS/JS nativo ya cubre.
- No ocultar fallos de validación. Reportarlos y corregirlos de forma acotada.
- Limitar reintentos automáticos a 2 ciclos de corrección por el mismo criterio; después reportar el bloqueo.
- No ejecutar comandos destructivos ni publicar cambios remotos sin aprobación explícita.

## Salida esperada
Para tareas de implementación, responder con:
- resultado realizado;
- archivos modificados;
- validaciones ejecutadas y estado;
- decisiones o supuestos relevantes;
- pendientes, solo si existen.
