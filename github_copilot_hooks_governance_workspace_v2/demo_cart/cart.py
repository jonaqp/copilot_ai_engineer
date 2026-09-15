from dataclasses import dataclass
from decimal import Decimal, ROUND_HALF_UP


MONEY = Decimal('0.01')


def money(value) -> Decimal:
    return Decimal(str(value)).quantize(MONEY, rounding=ROUND_HALF_UP)


@dataclass(frozen=True)
class Product:
    sku: str
    name: str
    price: Decimal
    stock: int

    @classmethod
    def create(cls, sku: str, name: str, price, stock: int):
        if not sku or not name:
            raise ValueError('sku y nombre son obligatorios')
        if money(price) < 0:
            raise ValueError('el precio no puede ser negativo')
        if stock < 0:
            raise ValueError('el stock no puede ser negativo')
        return cls(sku=sku, name=name, price=money(price), stock=stock)


@dataclass
class CartItem:
    product: Product
    quantity: int

    @property
    def subtotal(self) -> Decimal:
        return money(self.product.price * self.quantity)


class ShoppingCart:
    def __init__(self):
        self._items: dict[str, CartItem] = {}
        self._discount_percent = Decimal('0')

    @property
    def items(self):
        return tuple(self._items.values())

    def add(self, product: Product, quantity: int = 1):
        if quantity <= 0:
            raise ValueError('la cantidad debe ser mayor que cero')
        current = self._items.get(product.sku)
        new_quantity = quantity + (current.quantity if current else 0)
        if new_quantity > product.stock:
            raise ValueError('stock insuficiente')
        self._items[product.sku] = CartItem(product, new_quantity)

    def update(self, sku: str, quantity: int):
        if sku not in self._items:
            raise KeyError('producto no encontrado en el carrito')
        if quantity <= 0:
            self.remove(sku)
            return
        item = self._items[sku]
        if quantity > item.product.stock:
            raise ValueError('stock insuficiente')
        item.quantity = quantity

    def remove(self, sku: str):
        if sku not in self._items:
            raise KeyError('producto no encontrado en el carrito')
        del self._items[sku]

    def apply_discount(self, percent):
        percent = Decimal(str(percent))
        if percent < 0 or percent > 50:
            raise ValueError('el descuento permitido debe estar entre 0 y 50')
        self._discount_percent = percent

    def subtotal(self) -> Decimal:
        return money(sum((item.subtotal for item in self._items.values()), Decimal('0')))

    def discount_amount(self) -> Decimal:
        return money(self.subtotal() * self._discount_percent / Decimal('100'))

    def total(self) -> Decimal:
        return money(self.subtotal() - self.discount_amount())


class CheckoutService:
    def checkout(self, cart: ShoppingCart, payment_token: str) -> dict:
        if not cart.items:
            raise ValueError('no se puede pagar un carrito vacio')
        if not payment_token or not payment_token.startswith('tok_'):
            raise ValueError('token de pago invalido')
        return {
            'status': 'APPROVED',
            'items': sum(item.quantity for item in cart.items),
            'total': str(cart.total()),
        }
