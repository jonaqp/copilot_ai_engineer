# Prompts para probar el agente

### Plan sin ejecutar
> Usa orchestration-engineer. Analiza SuperStore y crea un DAG. Separa integración, contratos y testing en workstreams paralelos. No modifiques código todavía.

### Ejecución completa
> Ejecuta el plan. Lanza integration-specialist, contract-specialist y testing-specialist en paralelo. Consolida sus Evidence Packets y delega el fan-in a validation-specialist. Regenera orchestration-report.html.

### Breaking change
> Cambia el contrato de order-request para exigir customer_id, sin modificar el código. Ejecuta la orquestación completa y muéstrame qué subagente detecta el problema y cómo cambia el gate.

### Conflicto
> Si integration-specialist dice PASS pero contract-specialist detecta incompatibilidad, llama a review-specialist. No cierres en PASS mientras exista contradicción.
