# Hooks de GitHub Copilot - mapa del laboratorio

La carpeta esta ordenada por **responsabilidad**, no por una sola configuracion gigante.
Los archivos JSON permanecen directamente en `.github/hooks/` para que el repositorio conserve el patron esperado de descubrimiento.

```text
.github/hooks/
├── 01-session-audit.json      # inicio, prompts, cierre, notificaciones y compactacion
├── 02-tool-guardrails.json    # seguridad antes/despues de tools y permisos
├── 03-agent-lifecycle.json    # subagentes, errores y quality gate final
├── scripts/
│   └── hook_handler.py        # implementacion determinista de todos los eventos
├── logs/
│   └── audit.jsonl            # evidencia de ejecucion local
└── README.md                  # este mapa
```

## Como leer el flujo

1. `01-session-audit.json`: observar la sesion.
2. `02-tool-guardrails.json`: gobernar acciones que pueden cambiar el repositorio o ejecutar comandos.
3. `03-agent-lifecycle.json`: gobernar subagentes y bloquear el cierre si los tests del carrito fallan.
4. `scripts/hook_handler.py`: contiene la logica concreta.
5. `logs/audit.jsonl`: deja trazabilidad.

## Demo funcional

El quality gate de `agentStop` ejecuta los tests de `demo_cart/`.
Por eso, si Copilot rompe el carrito, el hook puede impedir que el agente finalice hasta corregirlo.
