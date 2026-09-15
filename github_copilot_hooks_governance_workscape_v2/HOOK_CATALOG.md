# GitHub Copilot Hooks Catalog - Demo sin MCP

Este laboratorio separa el **agente** de los **hooks**. El agente razona; los hooks ejecutan reglas deterministas en puntos concretos del ciclo de vida.

| Hook | Momento | Utilidad demostrada | ¿Puede bloquear? |
|---|---|---|---|
| `sessionStart` | Inicio/reanudación | inicializar auditoría y contexto | No |
| `userPromptSubmitted` | al enviar prompt | auditoría de solicitudes | No en config-file |
| `userPromptTransformed` | después de transformar prompt | modificación del contenido que verá el modelo | Mutación |
| `preToolUse` | antes de una tool | seguridad, allow/deny/ask, validación y modificación de args | Sí |
| `postToolUse` | después de tool exitosa | logging, contexto adicional, transformación de resultado | No bloqueo previo |
| `postToolUseFailure` | después de tool fallida | diagnóstico y guía de recuperación | No |
| `subagentStart` | nace un subagente | contexto y trazabilidad | No |
| `subagentStop` | termina subagente | validación, redacción, continuación | Sí |
| `agentStop` | agente termina turno | quality gate final | Sí |
| `errorOccurred` | error de ejecución | auditoría y métricas | No |
| `sessionEnd` | termina sesión | cierre y reporte | No |
| `notification` | notificación CLI | observabilidad asíncrona | No |
| `preCompact` | antes de compactar contexto | preservar estado crítico | No |
| `permissionRequest` | antes del permiso CLI | política centralizada allow/deny | Sí (CLI) |

## Ideas prácticas

1. **Seguridad:** bloquear `rm -rf`, exposición de credenciales y escrituras fuera del repo.
2. **Calidad:** ejecutar tests en `agentStop` y forzar una corrección si fallan.
3. **Auditoría:** registrar prompts, tools, errores y sesiones en JSONL.
4. **Subagentes:** inyectar alcance al iniciar y redactar secretos al terminar.
5. **Contexto:** tras editar, `postToolUse` recuerda al agente ejecutar tests.
6. **Operación:** `sessionEnd` permite cerrar métricas o generar reportes.
7. **CLI:** `permissionRequest` puede automatizar políticas de permisos.
8. **Prompt hooks:** `sessionStart` puede auto-enviar una instrucción en sesiones CLI interactivas.

## Nota de superficie

Este workspace está diseñado para Copilot CLI y Copilot cloud agent. El simulador local permite aprender los eventos sin depender de una sesión real. Si el IDE no ejecuta `.github/hooks/*.json`, usa el simulador o Copilot CLI para observar el comportamiento real de hooks.
