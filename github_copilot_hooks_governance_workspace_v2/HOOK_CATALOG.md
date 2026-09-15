# Catalogo de hooks - laboratorio carrito

| Evento | Familia | Uso en la demo |
|---|---|---|
| `sessionStart` | Sesion | Inicializa contexto y auditoria |
| `userPromptSubmitted` | Sesion | Registra el prompt sin ejecutar acciones |
| `preToolUse` | Tools | Bloquea comandos destructivos, secretos y escrituras fuera del repo |
| `postToolUse` | Tools | Si hubo una edicion, recuerda ejecutar tests focalizados |
| `postToolUseFailure` | Tools | Orienta una recuperacion sin reintentos ciegos |
| `permissionRequest` | Tools | Demuestra allow/deny programatico |
| `subagentStart` | Agentes | Limita el alcance de una tarea delegada |
| `subagentStop` | Agentes | Inspecciona/redacta la respuesta de un subagente |
| `agentStop` | Agentes | Ejecuta tests del carrito y puede impedir terminar |
| `errorOccurred` | Agentes | Registra errores |
| `sessionEnd` | Sesion | Registra cierre |
| `notification` | Sesion | Audita notificaciones |
| `preCompact` | Sesion | Pide preservar checks y decisiones antes de compactar |

## Regla didactica

Separar siempre:

- **Agent**: decide como resolver la tarea.
- **Hook**: intercepta eventos y aplica reglas deterministas.
- **Demo carrito**: sistema sobre el que se observa el efecto.
