# Estándar de análisis de impacto

## Propósito
Transformar un cambio técnico en una evaluación trazable de dependencias, propagación y pruebas preventivas.

## Evidencias válidas
Priorizar, en este orden:
1. Grafo/metadata de arquitectura versionado.
2. Imports y llamadas observables en código.
3. Contratos API, eventos, esquemas y clientes.
4. Configuración de runtime/deploy.
5. Tests existentes.
6. Documentación humana.

## Tipos de dependencia
- `sync-api`: llamada HTTP/RPC síncrona.
- `async-event`: productor/consumidor de evento.
- `database`: lectura/escritura sobre esquema o tabla compartida.
- `library`: dependencia de paquete o módulo.
- `config`: contrato por configuración/feature flag.
- `ui-contract`: frontend que consume un contrato backend.

## Profundidad
- Nivel 0: componente modificado.
- Nivel 1: dependiente directo.
- Nivel 2+: dependiente transitivo/indirecto.

Las dependencias de nivel 2+ son candidatas a "conexión oculta" cuando no están explícitamente documentadas.

## Resultado mínimo
Por cada impacto reportar: componente, profundidad, ruta, tipo de dependencia, criticidad, evidencia y validación recomendada.
