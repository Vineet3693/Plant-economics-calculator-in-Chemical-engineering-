# calculations/cost_estimation.py
def scaling_cost(C1: float, Q1: float, Q2: float, n: float = 0.6) -> float:
    return C1 * (Q2 / Q1) ** n

def lang_factor_total(equipment_costs: list[float], f: float) -> float:
    return f * sum(equipment_costs)

def total_product_cost(C_raw: float, C_util: float, C_labor: float, C_overheads: float) -> float:
    return C_raw + C_util + C_labor + C_overheads
