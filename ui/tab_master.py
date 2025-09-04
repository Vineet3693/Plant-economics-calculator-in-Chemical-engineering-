# ui/tab_master.py
import streamlit as st
from calculations.interest import future_value, annuity_present_worth
from calculations.depreciation import straight_line
from calculations.profitability import npv, irr, roi, payback_period
from calculations.cost_estimation import scaling_cost, lang_factor_total
from calculations.breakeven import bep_units
from calculations.replacement import economic_life_min_pw
from utils.ai_helper import summarize_all

def render_master_tab():
    st.header("Master Dashboard (All Sections Together)")

    with st.expander("Global Inputs", expanded=True):
        c = st.columns(6)
        P = c[0].number_input("Principal P", value=100000.0, min_value=0.0, step=1000.0)
        i = c[1].number_input("Interest i", value=0.1, min_value=0.0, step=0.01)
        n = int(c[2].number_input("Years n", value=5, min_value=1, step=1))
        A = c[3].number_input("Annuity A", value=0.0, min_value=0.0, step=100.0)
        invest = c[4].number_input("Investment C0", value=250000.0, min_value=0.0, step=1000.0)
        cash = c[5].number_input("Uniform Cash Rt", value=60000.0, min_value=0.0, step=1000.0)

    cc = st.columns(6)
    S_val = cc[0].number_input("Salvage S", value=10000.0, min_value=0.0, step=500.0)
    C1 = cc[1].number_input("Known Cost C1", value=50000.0, min_value=0.0, step=1000.0)
    Q1 = cc[2].number_input("Capacity Q1", value=10.0, min_value=0.0001, step=0.1)
    Q2 = cc[3].number_input("Capacity Q2", value=20.0, min_value=0.0001, step=0.1)
    n_scale = cc[4].number_input("Scaling exponent n_s", value=0.6, min_value=0.1, max_value=1.0, step=0.05)
    f_lang = cc[5].number_input("Lang factor f", value=4.3, min_value=1.0, step=0.1)

    st.divider()
    if st.button("Calculate All"):
        # Interest/TVM
        F = future_value(P, i, n)
        PW_ann = annuity_present_worth(A, i, n)

        # Depreciation (show just straight line summary here)
        _, _, sl_bv = straight_line(P, S_val, n)

        # Profitability
        cashflows = [-invest] + [cash] * n
        npv_val = npv(cashflows, i)
        irr_val = irr(cashflows)
        roi_val = roi(annual_profit=cash, total_investment=invest)
        pbp = payback_period(invest, cash)

        # Cost estimation
        scaled_cost = scaling_cost(C1, Q1, Q2, n_scale)
        fixed_capital = lang_factor_total([C1, scaled_cost], f_lang)

        # Break-even (simple illustrative values)
        # Assume user maps: F_fixed -> invest, S_price -> 50, V_var -> 35
        q_bep = bep_units(F=invest, S=50, V=35)

        # Replacement (toy annual costs)
        annual_costs = [30000, 32000, 35000, 39000, 44000, 50000, 57000]
        opt_year, pws = economic_life_min_pw(annual_costs, i)

        c1, c2, c3 = st.columns(3)
        c1.metric("Future Value (TVM)", f"{F:,.2f}")
        c2.metric("NPV", f"{npv_val:,.2f}")
        c3.metric("IRR (%)", f"{(irr_val*100 if irr_val else float('nan')):,.2f}")

        c4, c5, c6 = st.columns(3)
        c4.metric("ROI (%)", f"{roi_val:,.2f}")
        c5.metric("Payback (yrs)", f"{pbp:,.2f}")
        c6.metric("Scaled Cost C2", f"{scaled_cost:,.2f}")

        c7, c8, c9 = st.columns(3)
        c7.metric("Fixed Capital (Lang)", f"{fixed_capital:,.2f}")
        c8.metric("BEP (units)", f"{q_bep:,.2f}")
        c9.metric("Optimal Replacement Year", f"{opt_year}")

        summarize_all(
            inputs={
                "TVM": {"P": P, "i": i, "n": n, "A": A},
                "Depreciation": {"P": P, "S": S_val, "n": n},
                "Profitability": {"C0": invest, "Rt": cash, "n": n, "i": i},
                "CostEst": {"C1": C1, "Q1": Q1, "Q2": Q2, "n": n_scale, "f": f_lang},
                "BreakEven": {"F": invest, "S": 50, "V": 35},
                "Replacement": {"annual_costs": annual_costs, "i": i}
            },
            results={
                "F": F, "PW_ann": PW_ann, "NPV": npv_val, "IRR": irr_val,
                "ROI": roi_val, "Payback": pbp, "Scaled": scaled_cost,
                "FixedCapital": fixed_capital, "BEP_units": q_bep, "OptYear": opt_year
            }
        )
