# calculations/replacement.py
import numpy as np
from .profitability import npv

def salvage_after_depreciation(P: float, dep_series: list[float]) -> float:
    return P - sum(dep_series)

def economic_life_min_pw(annual_costs: list[float], i: float) -> int:
    """
    Given annual cost in year 1..N (index 0..N-1), return year that minimizes Present Worth of costs.
    """
    pws = []
    for t in range(1, len(annual_costs) + 1):
        cf = [0.0] + annual_costs[:t]  # assume start at year 1
        pws.append(npv(cf, i))
    return int(np.argmin(pws) + 1), pws
