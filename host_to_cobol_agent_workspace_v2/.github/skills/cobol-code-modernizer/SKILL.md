---
name: cobol-code-modernizer
description: Generar y refactorizar COBOL destino durante una migracion HOST/Mainframe preservando comportamiento y contratos. Usar cuando exista un plan aprobado y se necesite producir COBOL limpio, modular, legible, con nombres descriptivos, paragraphs cohesionados, COPYBOOKS reutilizables y manejo explicito de errores sin traducir mecanicamente linea por linea.
---
# Purpose
Implementar COBOL mantenible sin alterar silenciosamente la semantica legacy.

# Workflow
1. Leer solo la unidad fuente y contratos relacionados.
2. Mantener trazabilidad de reglas de negocio.
3. Generar divisiones COBOL consistentes.
4. Preferir nombres descriptivos y paragraphs pequenos.
5. Usar EVALUATE, PERFORM y 88-level cuando mejoren claridad.
6. Centralizar codigos de retorno y mensajes.
7. Mantener COPYBOOKS para records compartidos.
8. Comentar solo decisiones no obvias.

Consultar `references/cobol-clean-code.md`.

# Guardrails
Evitar GOTO nuevo, paragraphs de multiples responsabilidades, conversiones ocultas y funcionalidad no sustentada por source/plan.

# Validation
Ejecutar quality gate y compilar si `cobc` esta disponible. No declarar equivalencia funcional solo por sintaxis.
