from cart import CheckoutService, Product, ShoppingCart

keyboard = Product.create('KB-01', 'Teclado mecanico', '80.00', 10)
mouse = Product.create('MS-01', 'Mouse ergonomico', '40.00', 5)
cart = ShoppingCart()
cart.add(keyboard, 1)
cart.add(mouse, 2)
cart.apply_discount(10)

print('=== CARRITO DEMO ===')
for item in cart.items:
    print(f'- {item.product.name}: {item.quantity} x {item.product.price} = {item.subtotal}')
print('Subtotal:', cart.subtotal())
print('Descuento:', cart.discount_amount())
print('Total:', cart.total())
print('Checkout:', CheckoutService().checkout(cart, 'tok_demo'))
