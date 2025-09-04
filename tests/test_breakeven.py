# tests/test_breakeven.py
from calculations.breakeven import bep_units

def test_bep_basic():
    F, S, V = 1000, 50, 40
    assert abs(bep_units(F, S, V) - 100) < 1e-9
