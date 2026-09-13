---
name: flask-functional-testing
description: Crear tests funcionales para aplicaciones Flask usando pytest y Flask test client. Usar para rutas GET/POST, formularios, sesiones, redirects, mensajes flash, errores HTTP y flujos web de extremo a extremo dentro del proceso, sin navegador ni red real.
---

# Flask Functional Testing

## Purpose
Validar flujos web observables con el cliente de pruebas de Flask.

## Inputs
- `create_app` o instancia Flask.
- Rutas y servicios involucrados.
- `.github/reference-standards/flask-functional-testing-reference.md`.

## Workflow & Instructions
1. Crear fixture `app` con `TESTING=True`.
2. Crear fixture `client = app.test_client()`.
3. Probar GET principal: 200 y contenido clave.
4. Probar POST válido: redirect/respuesta + cambio de estado.
5. Probar POST inválido: 4xx o mensaje esperado.
6. Probar recursos inexistentes con 404 cuando aplique.
7. Verificar sesión o flash solo si son parte del comportamiento observable.
8. Evitar arrancar servidor real.
9. Ejecutar suite focalizada y luego quality gate.

## Expected Output
Tests de rutas y flujos Flask deterministas y rápidos.

## Validation
- Sin red real.
- Status codes afirmados.
- Resultado funcional afirmado.
- Estado persistente en memoria restaurado por fixture.
