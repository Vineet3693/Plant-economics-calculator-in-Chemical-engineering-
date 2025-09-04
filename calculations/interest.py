# calculations/interest.py
import numpy as np

def simple_interest(P: float, i: float, n: float) -> float:
    return P * i * n

def future_value(P: float, i: float, n: int) -> float:
    return P * (1 + i) ** n

def present_worth(F: float, i: float, n: int) -> float:
    return F / ((1 + i) ** n)

def annuity_present_worth(A: float, i: float, n: int) -> float:
    return A * ((1 + i) ** n - 1) / (i * (1 + i) ** n) if i != 0 else A * n

def annuity_future_worth(A: float, i: float, n: int) -> float:
    return A * (((1 + i) ** n - 1) / i) if i != 0 else A * n

def cashflow_curve(P: float, i: float, n: int):
    years = np.arange(0, n + 1)
    values = P * (1 + i) ** years
    return years, values
