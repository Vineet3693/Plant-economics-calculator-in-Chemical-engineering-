# tests/test_depreciation.py
from calculations.depreciation import straight_line

def test_straight_line_sum():
    P, S, n = 10000, 1000, 9
    years, dep, bv = straight_line(P, S, n)
    assert abs(sum(dep) - (P - S)) < 1e-6
    assert abs(bv[-1] - S) < 1e-6
