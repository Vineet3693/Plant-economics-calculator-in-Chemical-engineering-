"""
Interest and Time Value of Money Calculations
"""
import numpy as np
import pandas as pd

def simple_interest(P, i, n):
    """Calculate simple interest"""
    return P * i * n

def future_value(P, i, n):
    """Calculate future value with compound interest"""
    return P * (1 + i) ** n

def present_worth(F, i, n):
    """Calculate present worth"""
    return F / (1 + i) ** n

def annuity_present_worth(A, i, n):
    """Calculate present worth of annuity"""
    if i == 0:
        return A * n
    return A * ((1 + i) ** n - 1) / (i * (1 + i) ** n)

def annuity_future_worth(A, i, n):
    """Calculate future worth of annuity"""
    if i == 0:
        return A * n
    return A * ((1 + i) ** n - 1) / i

def cashflow_curve(P, i, n):
    """Generate cashflow data for plotting"""
    years = list(range(n + 1))
    values = [P * (1 + i) ** year for year in years]
    return pd.DataFrame({'Year': years, 'Value': values})
