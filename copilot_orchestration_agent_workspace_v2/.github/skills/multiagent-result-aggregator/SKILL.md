---
name: multiagent-result-aggregator
description: Normaliza y consolida resultados de múltiples subagentes sin perder fallos ni contradicciones. Usar en el fan-in para convertir respuestas heterogéneas en un resultado único, trazable y apto para validación.
---


# Multiagent Result Aggregator
## Purpose
Reducir contexto y convertir resultados paralelos en un contrato común.
## Workflow
1. Leer Evidence Packets.
2. Normalizar estados: PASS, FAIL, BLOCKED, UNKNOWN.
3. Deduplicar evidencia por check-id.
4. Detectar contradicciones sobre el mismo check.
5. Emitir `aggregate.json` con resumen y conflictos.
## Validation
Nunca descartar un FAIL. Si hay conflicto, marcarlo explícitamente.
