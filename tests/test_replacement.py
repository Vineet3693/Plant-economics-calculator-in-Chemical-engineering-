# tests/test_replacement.py
from calculations.replacement import economic_life_min_pw

def test_economic_life_returns_year():
    costs = [100,110,130,170]
    year, pws = economic_life_min_pw(costs, 0.1)
    assert 1 <= year <= len(costs)
    assert len(pws) == len(costs)
