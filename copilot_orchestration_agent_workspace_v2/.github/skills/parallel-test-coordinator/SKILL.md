---
name: parallel-test-coordinator
description: Planifica y ejecuta testing focalizado y de regresión como workstream independiente. Usar cuando el orquestador pueda ejecutar pruebas en paralelo con integración o contratos y necesite resultados reproducibles para el fan-in.
---


# Parallel Test Coordinator
## Purpose
Mantener testing aislado, paralelo y reproducible.
## Workflow
1. Seleccionar tests por cambio.
2. Ejecutar suite focalizada.
3. Ejecutar regresión necesaria.
4. Capturar comando, exit code, duración y fallos.
5. Devolver Evidence Packet.
## Validation
No aceptar PASS con tests omitidos, asserts triviales o comandos no ejecutados.
