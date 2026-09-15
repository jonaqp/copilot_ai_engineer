# Catalogo de Hooks de GitHub Copilot - Demo sin MCP

Este laboratorio separa el **agente** de los **hooks**. El agente razona; los hooks ejecutan reglas deterministas en puntos concretos del ciclo de vida.

| Hook | Momento | Utilidad demostrada | Puede bloquear |
|---|---|---|---|
| `sessionStart` | Inicio/reanudacion | inicializar auditoria y contexto | No |
| `userPromptSubmitted` | al enviar prompt | auditoria de solicitudes | No en esta demo |
| `userPromptTransformed` | tras transformar prompt | modificar el contenido que recibira el modelo | Puede mutar |
| `preToolUse` | antes de una tool | seguridad, allow/deny/ask, validacion de argumentos | Si |
| `postToolUse` | despues de una tool exitosa | logging y contexto adicional | No bloquea la tool ya ejecutada |
| `postToolUseFailure` | despues de una tool fallida | diagnostico y guia de recuperacion | No |
| `subagentStart` | inicio de subagente | contexto y trazabilidad | No |
| `subagentStop` | fin de subagente | validacion, redaccion y control de salida | Si, segun implementacion |
| `agentStop` | antes de terminar turno | quality gate final | Si |
| `errorOccurred` | error de ejecucion | auditoria y metricas | No |
| `sessionEnd` | fin de sesion | cierre y reporte | No |
| `notification` | notificacion CLI | observabilidad asincrona | No |
| `preCompact` | antes de compactar contexto | preservar estado critico | No |
| `permissionRequest` | antes de conceder permiso | politica centralizada de permisos | Si |

## Utilidades practicas

1. **Seguridad:** bloquear `rm -rf`, acceso a secretos y escrituras fuera del repo.
2. **Calidad:** ejecutar tests en `agentStop` y exigir correccion si fallan.
3. **Auditoria:** registrar prompts, tools, errores y sesiones en JSONL.
4. **Subagentes:** inyectar alcance al iniciar y redactar secretos al terminar.
5. **Contexto:** despues de editar, `postToolUse` recuerda ejecutar tests.
6. **Operacion:** `sessionEnd` puede cerrar metricas o generar reportes.
7. **Permisos:** `permissionRequest` puede automatizar politicas de autorizacion.
8. **Prompts de sesion:** `sessionStart` puede inyectar una instruccion inicial cuando el entorno lo soporte.

## Regla pedagogica

Cuando expliques un hook, mostrar siempre:

```text
EVENTO
  -> ENTRADA
  -> REGLA
  -> DECISION / SALIDA
  -> EFECTO SOBRE EL AGENTE
```
