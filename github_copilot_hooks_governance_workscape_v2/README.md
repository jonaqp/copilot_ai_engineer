# GitHub Copilot Hooks Governance Agent

Laboratorio sin MCP para aprender y demostrar hooks de GitHub Copilot.

## Objetivo

Mostrar de forma práctica cómo los hooks aportan control determinista alrededor del agente:

- seguridad antes de ejecutar herramientas;
- auditoría de prompts y tools;
- validación después de cambios;
- control de subagentes;
- quality gate al terminar;
- manejo de errores y cierre de sesión.

## Quick start

```bash
python scripts/validate_workspace.py
python scripts/simulate_hooks.py --all
python scripts/run_demo_scenarios.py
```

Los logs quedan en `.github/hooks/logs/audit.jsonl` y están ignorados por Git.

No hay MCP, Jira, GitHub API ni credenciales.
