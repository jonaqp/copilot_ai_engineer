# GitHub Copilot - Agente Simple Explicador de Hooks

Demo minima, en espanol y sin MCP, para comprender que ocurre cuando un usuario envia un prompt y GitHub Copilot atraviesa distintos puntos del ciclo de vida.

La demo se centra en siete eventos: `sessionStart`, `userPromptSubmitted`, `preToolUse`, `postToolUse`, `postToolUseFailure`, `agentStop` y `sessionEnd`.

## Prueba rapida

```bash
python scripts/simular_prompt.py "explicame que es una API"
python scripts/ver_traza.py
```

La simulacion no necesita GitHub, red, tokens ni dependencias externas.
