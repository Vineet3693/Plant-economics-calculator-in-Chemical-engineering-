# ui/tab_profitability.py
import streamlit as st
import numpy as np
from calculations.profitability import roi, payback_period, npv, irr
from utils.ai_helper import maybe_explain

def render_profitability_tab():
    st.header("Profitability (ROI, Payback, NPV, IRR)")
    c = st.columns(5)
    total_investment = c[0].number_input("Total Investment", value=250000.0, min_value=0.0, step=1000.0)
    annual_profit = c[1].number_input("Annual Profit", value=45000.0, min_value=0.0, step=1000.0)
    n = int(c[2].number_input("Years (n)", value=8, min_value=1, step=1))
    discount = c[3].number_input("Discount Rate i (%)", value=10.0, min_value=0.0, step=0.1) / 100
    uniform_cash = c[4].number_input("Annual Cashflow (uniform)", value=60000.0, min_value=0.0, step=1000.0)

    pbp = payback_period(total_investment, uniform_cash)
    roi_val = roi(annual_profit, total_investment)
    cashflows = [-total_investment] + [uniform_cash] * n
    npv_val = npv(cashflows, discount)
    irr_val = irr(cashflows)

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("ROI (%)", f"{roi_val:,.2f}")
    c2.metric("Payback Period (yrs)", f"{pbp:,.2f}")
    c3.metric("NPV", f"{npv_val:,.2f}")
    c4.metric("IRR (%)", f"{(irr_val*100 if irr_val is not None else float('nan')):,.2f}")

    maybe_explain("Profitability", {
        "Investment": total_investment, "Annual Profit": annual_profit,
        "n": n, "discount": discount, "uniform_cash": uniform_cash
    }, {
        "ROI_%": roi_val, "Payback": pbp, "NPV": npv_val, "IRR": irr_val
    })
