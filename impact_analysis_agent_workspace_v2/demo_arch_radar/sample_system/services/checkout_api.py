from dataclasses import dataclass
from cart_service import Cart, CartService


@dataclass
class CheckoutCommand:
    cart: Cart
    payment_token: str


class InventoryClient:
    def reserve(self, sku: str, quantity: int) -> bool:
        return quantity <= 10


class PaymentAdapter:
    def authorize(self, token: str, amount) -> str:
        if not token:
            raise ValueError("payment token required")
        return "auth-demo-001"


class CheckoutService:
    def __init__(self, carts: CartService, inventory: InventoryClient, payments: PaymentAdapter):
        self.carts = carts
        self.inventory = inventory
        self.payments = payments

    def checkout(self, command: CheckoutCommand) -> dict:
        for line in command.cart.lines:
            if not self.inventory.reserve(line.sku, line.quantity):
                raise RuntimeError(f"inventory unavailable: {line.sku}")
        total = self.carts.total(command.cart)
        authorization = self.payments.authorize(command.payment_token, total)
        return {"status": "accepted", "total": total, "authorization": authorization}
