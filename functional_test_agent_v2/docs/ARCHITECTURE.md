# Arquitectura del demo

## Capas
- `demo_shop/domain.py`: entidades y servicios de negocio.
- `demo_shop/app.py`: factory Flask y rutas.
- `templates/`: interfaz del catálogo, carrito y checkout.
- `tests/test_domain.py`: clases, funciones, errores y reglas de negocio.
- `tests/test_flask_functional.py`: flujos funcionales con Flask test client.

## Clases clave
- `Product`: validación de producto.
- `CartItem`: cantidad y subtotal.
- `Cart`: estado del carrito y transiciones.
- `DiscountPolicy`: regla de descuento.
- `PricingService`: subtotal, descuento, impuesto y total.
- `Catalog`: consulta de productos.
- `CheckoutService`: validación y cierre de compra.

La separación permite que el agente encuentre con claridad clases, métodos, funciones y rutas que necesitan cobertura.
