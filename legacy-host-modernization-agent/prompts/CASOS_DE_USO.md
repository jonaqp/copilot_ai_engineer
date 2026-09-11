# Casos de uso y prompts - Legacy / Host Modernization

## Caso 1 - Impacto antes de tocar una rutina online

**Prompt**

> Analiza `examples/sample_online.cbl` con `host-code-analysis`. Construye inventario de CICS, CALL, COPY, SQL y COMMAREA. Luego usa `cobol-modernization-assessment`. No propongas reescritura total: indica acoplamientos, riesgos y pruebas de caracterización.

## Caso 2 - Online a Batch

> Evalúa si la lógica del programa puede extraerse a un job batch. Usa `online-to-batch-conversion` y separa: bloqueantes CICS, contrato de entrada/salida, commit/restart, idempotencia y regresión.

## Caso 3 - Release Host Perú

> Valida `examples/host_release.json` con `host-release-readiness`. Comprueba paquetes listos, plan de retorno, Jira/evidencia y marca todo dato que requiera procedimiento vigente DQA/Host.
