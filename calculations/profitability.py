# calculations/profitability.py
import numpy as np

def roi(annual_profit: float, total_investment: float) -> float:
    return (annual_profit / total_investment) * 100 if total_investment else 0.0

def payback_period(investment: float, annual_cash_inflow: float) -> float:
    return investment / annual_cash_inflow if annual_cash_inflow else float('inf')

def npv(cashflows: list[float], i: float) -> float:
    # cashflows: [C0, C1, C2, ..., Cn] where C0 is negative (investment)
    return sum(cf / ((1 + i) ** t) for t, cf in enumerate(cashflows))

def irr(cashflows: list[float], guess: float = 0.1, max_iter: int = 200, tol: float = 1e-7):
    # Newton-Raphson
    r = guess
    for _ in range(max_iter):
        f = sum(cf / ((1 + r) ** t) for t, cf in enumerate(cashflows))
        df = sum(-t * cf / ((1 + r) ** (t + 1)) for t, cf in enumerate(cashflows) if t > 0)
        if abs(df) < 1e-12:
            break
        r_new = r - f / df
        if abs(r_new - r) < tol:
            return r_new
        r = r_new
    return None  # could not converge
