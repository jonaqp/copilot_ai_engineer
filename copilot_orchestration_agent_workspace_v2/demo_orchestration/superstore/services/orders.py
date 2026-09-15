from .catalog import get_product
from .inventory import reserve
from .payment import authorize

def checkout(sku: str, qty: int, payment_token: str) -> dict:
    product = get_product(sku)
    stock = reserve(sku, qty)
    if not stock["reserved"]:
        return {"status": "REJECTED", "reason": stock["reason"]}
    total = round(product.price * qty, 2)
    payment = authorize(total, payment_token)
    if not payment["authorized"]:
        return {"status": "REJECTED", "reason": payment["reason"]}
    return {"status": "CONFIRMED", "sku": sku, "qty": qty, "total": total, "authorization_id": payment["authorization_id"]}
