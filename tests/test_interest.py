# tests/test_interest.py
from calculations.interest import future_value, present_worth

def test_future_present_roundtrip():
    P = 1000; i = 0.1; n = 5
    F = future_value(P, i, n)
    P2 = present_worth(F, i, n)
    assert abs(P - P2) < 1e-6
