# tests/test_profitability.py
from calculations.profitability import npv

def test_npv_zero_rate():
    cf = [-100, 50, 50, 50]
    assert abs(npv(cf, 0.0) - sum(cf)) < 1e-9
