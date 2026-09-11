---
name: cobol-modernization-assessment
description: "Evaluar complejidad y riesgo de modernizacion de programas COBOL usando inventario tecnico, dependencias y patrones legacy. Usar para priorizar refactor, wrapping, replatform o reescritura controlada."
---

# cobol-modernization-assessment

## Objetivo

Aplicar un flujo repetible y auditable para esta capacidad dentro de GitHub Copilot. Usar evidencia del repositorio, parametros del usuario y referencias aprobadas; no completar datos corporativos por suposicion.

## Flujo

1. Obtener inventario con host-code-analysis.
2. Ejecutar `scripts/assess_modernization.py` con el JSON del inventario.
3. Separar quick wins de acoplamientos de alto riesgo.
4. Proponer estrategia incremental y pruebas de caracterizacion.

## Script ejecutable

Ejecutar `python scripts/assess_modernization.py --help` para ver parametros. Usar el script para la parte determinista y dejar al modelo la interpretacion, priorizacion y redaccion.

## Referencias

Consultar `references/bbva_peru_rules.md` antes de emitir una conclusion de cumplimiento. Si el documento interno vigente contradice esta Skill, prevalece el documento vigente.

## Salida esperada

Entregar: objetivo, entradas utilizadas, evidencia, hallazgos clasificados, riesgos, acciones propuestas, validaciones pendientes y cualquier aprobacion humana requerida.

## Guardrails

- No inventar IDs Jira, nombres de UUAA, endpoints, credenciales, APIs propietarias o resultados de pipeline.
- Diferenciar hecho observado, inferencia y dato pendiente.
- No afirmar que tests/quality gates pasaron sin evidencia de ejecucion.
- No ejecutar acciones productivas o destructivas desde esta Skill.

## Composición con otras Skills

Para un análisis end-to-end ejecutar:

```bash
python scripts/run_host_assessment.py <fuente.cbl> --out-dir output_host_assessment
```

Este wrapper invoca primero `host-code-analysis`, luego esta Skill y finalmente `online-to-batch-conversion`. No elimina la revisión humana del mapa de dependencias.

## Prompts de referencia

Consultar `references/prompts_es.md` para ejemplos en español orientados a BBVA Perú.
