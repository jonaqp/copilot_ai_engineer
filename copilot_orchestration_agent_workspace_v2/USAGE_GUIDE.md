# Guía de uso

1. En GitHub Copilot seleccionar `orchestration-engineer`.
2. Prompt inicial: `Analiza la demo SuperStore y prepara un plan multiagente. Ejecuta en paralelo validación de contratos, integración y testing. Después realiza fan-in con validation-specialist y actualiza el dashboard HTML.`
3. Demo local: `python scripts/run_orchestration.py` y `python scripts/validate_workspace.py`.
4. Abrir `demo_orchestration/orchestration-report.html`.
5. Modificar un contrato o test y repetir para ver cómo cambia el gate.
