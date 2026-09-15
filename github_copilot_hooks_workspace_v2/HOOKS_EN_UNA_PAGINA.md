# Hooks en una pagina

```text
ENVIO PROMPT
    |
    v
userPromptSubmitted
    |
    v
preToolUse --------> puede ALLOW / DENY
    |
    v
  TOOL
    |
    +---- fallo ----> postToolUseFailure
    |
    v
postToolUse
    |
    v
agentStop ----------> puede ALLOW / BLOCK
```

Alrededor de ese flujo existen:
- `sessionStart`: abre/inicializa la sesion.
- `sessionEnd`: cierra la sesion.

La idea principal es:

**Agente = decide que hacer. Hook = intercepta momentos concretos del ciclo para auditar, validar o gobernar.**
