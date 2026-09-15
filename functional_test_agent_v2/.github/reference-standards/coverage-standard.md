# Estándar de Coverage

## Umbrales
- Global: 80% mínimo.
- Módulo crítico: revisar si queda <70%.
- Demo: objetivo >=90%.

## Priorización
1. Dinero, descuentos y checkout.
2. Carrito, cantidades, inventario y estados.
3. Rutas POST y errores.
4. Ramas condicionales.
5. Renderizado y helpers simples.

## Flujo
1. Medir baseline.
2. Leer líneas faltantes.
3. Traducir línea faltante a comportamiento no probado.
4. Añadir test mínimo que cubra ese comportamiento.
5. Repetir hasta >=80%.
6. Ejecutar suite completa.
