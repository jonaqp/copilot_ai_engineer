---
name: shift-left-gate
description: Convertir un análisis de impacto en un gate preventivo de calidad antes del deploy. Usar cuando se necesite recomendar tests de contrato, integración, funcionales o regresión, exigir evidencias sobre rutas críticas y emitir GO, GO WITH CONDITIONS o NO-GO.
---

# Purpose
Evitar que un cambio de alto riesgo avance sin validaciones proporcionales al impacto.

# Inputs
- Reporte de impacto.
- Score de riesgo.
- Tests existentes/ejecutados.
- Políticas del repositorio.

# Workflow & Instructions
1. Mapear cada ruta impactada a una validación.
2. Priorizar contrato para APIs, integración para dependencias entre servicios y regresión para consumidores indirectos.
3. Exigir evidencia sobre nodos críticos.
4. Emitir:
   - GO: riesgo bajo/medio y validaciones suficientes.
   - GO WITH CONDITIONS: riesgo alto o evidencia parcial.
   - NO-GO: riesgo crítico sin mitigación suficiente.
5. No ejecutar deploy.
6. No cambiar umbrales para aprobar.

# Expected Output
Decisión, tests requeridos, tests faltantes, condiciones y evidencia.

# Validation
No puede existir GO si una ruta crítica carece de validación relevante.
