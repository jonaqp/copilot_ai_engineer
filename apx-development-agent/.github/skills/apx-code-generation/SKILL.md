---
name: apx-code-generation
description: "Preparar un plan de generacion de codigo APX y crear esqueletos solo a partir de parametros y plantillas aprobadas del repositorio. Usar para nuevos componentes APX sin inventar APIs propietarias."
---

# apx-code-generation

## Objetivo

Aplicar un flujo repetible y auditable para esta capacidad dentro de GitHub Copilot. Usar evidencia del repositorio, parametros del usuario y referencias aprobadas; no completar datos corporativos por suposicion.

## Flujo

1. Clasificar tipo de recurso APX.
2. Buscar patrones equivalentes en el repo y documentacion aprobada.
3. Ejecutar `scripts/generate_apx_workplan.py` con parametros.
4. Si existe una plantilla aprobada, ejecutar `scripts/render_from_approved_template.py` para materializarla con parametros explicitos.
5. Revisar el diff generado con GitHub MCP/Copilot; despues ejecutar tests y validadores.

## Script ejecutable

Ejecutar `python scripts/generate_apx_workplan.py --help` y `python scripts/render_from_approved_template.py --help` para ver parametros. El segundo script solo renderiza una plantilla ya aprobada; no contiene conocimiento propietario APX. Usar los scripts para la parte determinista y dejar al modelo la interpretacion, priorizacion y redaccion.

## Referencias

Consultar `references/bbva_peru_rules.md` antes de emitir una conclusion de cumplimiento. Si el documento interno vigente contradice esta Skill, prevalece el documento vigente.

## Salida esperada

Entregar: objetivo, entradas utilizadas, evidencia, hallazgos clasificados, riesgos, acciones propuestas, validaciones pendientes y cualquier aprobacion humana requerida.

## Guardrails

- No inventar IDs Jira, nombres de UUAA, endpoints, credenciales, APIs propietarias o resultados de pipeline.
- Diferenciar hecho observado, inferencia y dato pendiente.
- No afirmar que tests/quality gates pasaron sin evidencia de ejecucion.
- No ejecutar acciones productivas o destructivas desde esta Skill.

## Prompts de referencia

Consultar `references/prompts_es.md` para ejemplos en español orientados a BBVA Perú.
