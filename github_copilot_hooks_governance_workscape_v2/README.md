# Agente de Gobernanza de Hooks para GitHub Copilot

Laboratorio **sin MCP** para aprender y demostrar hooks de GitHub Copilot completamente en espanol.

## Objetivo

Mostrar de forma practica como los hooks aportan control determinista alrededor de un agente:

- seguridad antes de ejecutar herramientas;
- auditoria de prompts y tools;
- validacion despues de cambios;
- control de subagentes;
- quality gate antes de terminar;
- manejo de errores;
- trazabilidad del ciclo de vida.

## Inicio rapido

```bash
python scripts/validate_workspace.py
python scripts/simulate_hooks.py --all
python scripts/run_demo_scenarios.py
```

Los logs quedan en `.github/hooks/logs/audit.jsonl` y estan ignorados por Git.

Este proyecto no usa MCP, Jira, GitHub API, tokens ni credenciales.
