---
name: validation-fan-in
description: Aplica un quality gate al finalizar varios workstreams. Usar después de integrar resultados de subagentes para verificar evidencia, conflictos, checks obligatorios y emitir PASS, PASS WITH CONDITIONS o FAIL.
---


# Validation Fan-In
## Purpose
Cerrar el DAG con un gate independiente.
## Workflow
1. Reunir todos los Evidence Packets obligatorios.
2. Rechazar packets de otro run id.
3. FAIL si cualquier gate crítico falla.
4. PASS WITH CONDITIONS si existe BLOCKED/UNKNOWN no crítico o evidencia incompleta.
5. PASS solo con todos los gates críticos verdes.
## Validation
Registrar razones de la decisión y los checks faltantes.
