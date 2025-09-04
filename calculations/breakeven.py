# calculations/breakeven.py
def bep_units(F: float, S: float, V: float) -> float:
    denom = (S - V)
    return F / denom if denom != 0 else float('inf')

def bep_revenue(F: float, S: float, V: float) -> float:
    q = bep_units(F, S, V)
    return q * S
