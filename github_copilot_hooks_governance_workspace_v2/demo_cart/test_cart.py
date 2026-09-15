import unittest
from decimal import Decimal

from cart import CheckoutService, Product, ShoppingCart


class ShoppingCartTests(unittest.TestCase):
    def setUp(self):
        self.keyboard = Product.create('KB-01', 'Teclado mecanico', '80.00', 10)
        self.mouse = Product.create('MS-01', 'Mouse ergonomico', '40.00', 5)
        self.cart = ShoppingCart()

    def test_add_product_and_subtotal(self):
        self.cart.add(self.keyboard, 2)
        self.assertEqual(self.cart.subtotal(), Decimal('160.00'))

    def test_add_same_product_accumulates_quantity(self):
        self.cart.add(self.mouse, 1)
        self.cart.add(self.mouse, 2)
        self.assertEqual(self.cart.items[0].quantity, 3)

    def test_rejects_quantity_over_stock(self):
        with self.assertRaises(ValueError):
            self.cart.add(self.mouse, 6)

    def test_update_quantity(self):
        self.cart.add(self.keyboard, 1)
        self.cart.update('KB-01', 3)
        self.assertEqual(self.cart.items[0].quantity, 3)

    def test_update_zero_removes_item(self):
        self.cart.add(self.keyboard, 1)
        self.cart.update('KB-01', 0)
        self.assertEqual(len(self.cart.items), 0)

    def test_apply_discount(self):
        self.cart.add(self.keyboard, 1)
        self.cart.apply_discount(10)
        self.assertEqual(self.cart.discount_amount(), Decimal('8.00'))
        self.assertEqual(self.cart.total(), Decimal('72.00'))

    def test_invalid_discount_is_rejected(self):
        with self.assertRaises(ValueError):
            self.cart.apply_discount(60)

    def test_checkout_success(self):
        self.cart.add(self.keyboard, 1)
        result = CheckoutService().checkout(self.cart, 'tok_demo')
        self.assertEqual(result['status'], 'APPROVED')
        self.assertEqual(result['total'], '80.00')

    def test_checkout_empty_cart_is_rejected(self):
        with self.assertRaises(ValueError):
            CheckoutService().checkout(self.cart, 'tok_demo')

    def test_checkout_invalid_token_is_rejected(self):
        self.cart.add(self.mouse, 1)
        with self.assertRaises(ValueError):
            CheckoutService().checkout(self.cart, 'invalid')


if __name__ == '__main__':
    unittest.main()
