# calculations/depreciation.py
import numpy as np

def straight_line(P: float, S: float, n: int):
    D = (P - S) / n
    years = np.arange(1, n + 1)
    dep = np.full_like(years, fill_value=D, dtype=float)
    bv = P - D * np.arange(1, n + 1)
    return years, dep, bv

def declining_balance(P: float, S: float, n: int, d: float):
    years = np.arange(1, n + 1)
    bv = np.zeros(n + 1)
    dep = np.zeros(n)
    bv[0] = P
    for t in range(1, n + 1):
        dep[t-1] = bv[t-1] * d
        bv[t] = bv[t-1] - dep[t-1]
    # force final BV not below salvage
    if bv[-1] < S:
        adj = S - bv[-1]
        dep[-1] -= adj
        bv[-1] = S
    return years, dep, bv[1:]

def sum_of_years_digits(P: float, S: float, n: int):
    SYD = n * (n + 1) / 2
    years = np.arange(1, n + 1)
    dep = ((n - years + 1) / SYD) * (P - S)
    bv = P - np.cumsum(dep)
    return years, dep, bv

def sinking_fund(P: float, S: float, n: int, i: float):
    A = (P - S) * (i / ((1 + i) ** n - 1)) if i != 0 else (P - S) / n
    years = np.arange(1, n + 1)
    dep = np.full(n, A)
    bv = P - np.cumsum(dep)
    return years, dep, bv
