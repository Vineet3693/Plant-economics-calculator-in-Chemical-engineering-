# calculations/interest.py

def simple_interest(P, r, t):
    """Calculate Simple Interest"""
    return P * r * t


def future_value(P, r, n):
    """Calculate Future Value"""
    return P * (1 + r) ** n


def present_worth(F, r, n):
    """Calculate Present Worth"""
    return F / ((1 + r) ** n)


def annuity_present_worth(A, r, n):
    """Calculate Present Worth of Annuity"""
    return A * ((1 - (1 + r) ** -n) / r)


def annuity_future_worth(A, r, n):
    """Calculate Future Worth of Annuity"""
    return A * (((1 + r) ** n - 1) / r)


def cashflow_curve(P, r, n):
    """Generate cashflow values for n years"""
    values = []
    for i in range(1, n + 1):
        values.append(future_value(P, r, i))
    return values
