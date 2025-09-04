# tests/test_cost_estimation.py
from calculations.cost_estimation import scaling_cost

def test_scaling_monotonic():
    C1, Q1, Q2 = 100, 10, 20
    C2 = scaling_cost(C1, Q1, Q2, 0.6)
    assert C2 > C1
