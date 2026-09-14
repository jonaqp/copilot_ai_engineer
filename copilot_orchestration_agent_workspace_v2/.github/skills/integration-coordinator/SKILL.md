---
name: integration-coordinator
description: Coordina la validación de integraciones entre servicios, adapters, endpoints y configuración. Usar cuando una tarea requiera verificar comunicación entre componentes y producir smoke checks/evidencias antes del fan-in.
---


# Integration Coordinator
## Purpose
Estandarizar el workstream de integración.
## Workflow
1. Identificar integración afectada.
2. Cargar solo adapters/config relevantes.
3. Ejecutar smoke checks deterministas.
4. Reportar `PASS`, `FAIL` o `BLOCKED` y evidencia.
5. No decidir el resultado global.
## Expected Output
Evidence Packet conforme a `references/evidence-packet.md`.
## Validation
Toda afirmación de integración debe apuntar a un check ejecutado o archivo concreto.
