STOCK = {"KB-01": 8, "MS-02": 15}

def reserve(sku: str, qty: int) -> dict:
    if qty <= 0:
        raise ValueError("qty must be positive")
    available = STOCK.get(sku, 0)
    if available < qty:
        return {"reserved": False, "reason": "insufficient_stock", "available": available}
    return {"reserved": True, "sku": sku, "qty": qty}
