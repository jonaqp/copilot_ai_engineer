---
name: host-code-analysis
description: "Analizar fuentes COBOL/Host y extraer PROGRAM-ID, CALL, COPY, tablas SQL, CICS y archivos para construir un inventario tecnico. Usar ante analisis de codigo Host, discovery, documentacion o preparacion de modernizacion."
---

# host-code-analysis

## Objetivo

Aplicar un flujo repetible y auditable para esta capacidad dentro de GitHub Copilot. Usar evidencia del repositorio, parametros del usuario y referencias aprobadas; no completar datos corporativos por suposicion.

## Flujo

1. Ejecutar `scripts/analyze_cobol.py` sobre el fuente objetivo.
2. Revisar inventario de CALL/COPY/SQL/CICS/archivos.
3. Contrastar dependencias con GitHub MCP o catalogo Host aprobado.
4. Entregar evidencia y preguntas abiertas; no inferir dependencias que no aparezcan.

## Script ejecutable

Ejecutar `python scripts/analyze_cobol.py --help` para ver parametros. Usar el script para la parte determinista y dejar al modelo la interpretacion, priorizacion y redaccion.

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
