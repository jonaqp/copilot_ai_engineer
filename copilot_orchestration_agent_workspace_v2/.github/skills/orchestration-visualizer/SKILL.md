---
name: orchestration-visualizer
description: Genera un dashboard HTML local del run multiagente. Usar cuando se requiera visualizar DAG, subagentes paralelos, estados, tiempos, evidencias y fan-in gate. El HTML debe derivarse del JSON real del run y funcionar sin CDN.
---


# Orchestration Visualizer
## Purpose
Convertir el estado real del run en una visualización entendible.
## Workflow
1. Leer `demo_orchestration/run/result.json`.
2. Generar `demo_orchestration/orchestration-report.html`.
3. Mostrar waves paralelas, agentes, estados, duración, evidencia y gate.
4. Mantener HTML/CSS/JS autocontenido y sin CDN.
5. Sobrescribir el reporte en cada ejecución.
## Validation
El número, nombre y estado de agentes en HTML debe coincidir con `result.json`.
