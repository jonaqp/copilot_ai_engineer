---
name: jira-quality-gate
description: Consolida validaciones de formato, readiness, adjuntos, issue links y subtareas para decidir si un ticket Jira esta READY, READY WITH CONDITIONS o NOT READY. Usar al final de una revision o despues de una correccion.
---
# Decision
- `READY`: no FAIL y no UNKNOWN critico.
- `READY WITH CONDITIONS`: no FAIL bloqueante; solo WARNING o UNKNOWN no criticos.
- `NOT READY`: al menos un FAIL bloqueante o UNKNOWN critico.

# Output obligatorio
Tabla `Area | Rule | Result | Evidence | Action` seguida de:
- blockers;
- warnings;
- campos corregibles;
- decision final exacta.
