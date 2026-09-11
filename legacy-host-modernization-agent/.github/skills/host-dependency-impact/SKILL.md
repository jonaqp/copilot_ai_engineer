---
name: host-dependency-impact
description: "Construir y consultar un grafo simple de dependencias entre programas Host a partir de CALL y COPY. Usar para analisis de impacto antes de modificar o liberar un componente."
---

# host-dependency-impact

## Objetivo

Aplicar un flujo repetible y auditable para esta capacidad dentro de GitHub Copilot. Usar evidencia del repositorio, parametros del usuario y referencias aprobadas; no completar datos corporativos por suposicion.

## Flujo

1. Ejecutar `scripts/build_dependency_graph.py` sobre una carpeta de fuentes.
2. Identificar consumidores/proveedores directos.
3. Enriquecer con catalogos/MCP internos si existen.
4. Entregar impacto confirmado vs impacto por validar.

## Script ejecutable

Ejecutar `python scripts/build_dependency_graph.py --help` para ver parametros. Usar el script para la parte determinista y dejar al modelo la interpretacion, priorizacion y redaccion.

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
