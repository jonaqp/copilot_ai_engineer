def authorize(amount: float, token: str) -> dict:
    if amount <= 0:
        raise ValueError("amount must be positive")
    if not token.startswith("tok_"):
        return {"authorized": False, "reason": "invalid_token"}
    return {"authorized": True, "authorization_id": "auth_demo_001", "amount": round(amount, 2)}
