# Prompt examples

## Validacion completa
Valida el PR owner/repo#123 usando el MCP github-bbva. No hagas cambios. Devuelve la tabla completa de evidencias y la recomendacion de merge.

## Solo metadata
Valida solamente el titulo y la descripcion del PR owner/repo#123. El titulo debe ser `[ISSUE-123] - PR DEVELOP` y la primera linea de descripcion `feat(ISSUE-123): <descripcion>`.

## Diagnostico de bloqueo
Analiza por que el PR owner/repo#123 no esta listo para merge. Separa errores de formato, CI, approvals, conflictos, review threads y seguridad. No ejecutes el merge.
