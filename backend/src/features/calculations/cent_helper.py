from decimal import Decimal, ROUND_HALF_UP



cent = Decimal("0.01")


def to_cent(amount: Decimal) -> Decimal:
    return amount.quantize(cent, ROUND_HALF_UP)