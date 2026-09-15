# Casos de uso y prompts - APX Development

## Caso 1 - Generación segura

> Necesito crear un componente APX. Clasifica primero el recurso y busca componentes equivalentes mediante GitHub MCP. Usa `apx-code-generation` para pedir parámetros y generar un plan. No inventes clases/APIs APX si no aparecen en plantilla o referencia aprobada.

## Caso 2 - Review PR APX

> Revisa el PR actual con `apx-code-review` y `apx-best-practices`. Comprueba estructura, modelo de rama, tests, Sonar/Chimera y dependencias. Separa bloqueantes, warnings y reglas cuya vigencia deba confirmarse.

## Caso 3 - Quality gate local

> Ejecuta `run_apx_quality_gate.py` sobre `examples/apx-demo-repo`, `examples/apx_manifest.json` y `examples/jacoco.xml`. El 80% del ejemplo es cobertura global; no lo declares equivalente a cobertura de nuevo código si el reporte no lo prueba.
