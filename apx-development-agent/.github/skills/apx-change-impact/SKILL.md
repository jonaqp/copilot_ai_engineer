---
name: apx-change-impact
description: "Extraer dependencias Maven/modulos y generar un mapa de impacto tecnico para cambios APX. Usar para responder que componentes pueden verse afectados por una modificacion."
---

# apx-change-impact

## Objetivo

Aplicar un flujo repetible y auditable para esta capacidad dentro de GitHub Copilot. Usar evidencia del repositorio, parametros del usuario y referencias aprobadas; no completar datos corporativos por suposicion.

## Flujo

1. Ejecutar `scripts/analyze_apx_dependencies.py` para Maven.
2. Consultar repos/PR y consumidores visibles por MCP.
3. Agregar dependencias runtime/catalogo solo si hay evidencia.
4. Entregar impacto confirmado, probable y desconocido.

## Script ejecutable

Ejecutar `python scripts/analyze_apx_dependencies.py --help` para ver parametros. Usar el script para la parte determinista y dejar al modelo la interpretacion, priorizacion y redaccion.

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
