# ui/tab_depreciation.py
import streamlit as st
import pandas as pd
import plotly.express as px
from calculations.depreciation import straight_line, declining_balance, sum_of_years_digits, sinking_fund
from utils.ai_helper import maybe_explain

def render_depreciation_tab():
    st.header("Depreciation Methods")
    cols = st.columns(5)
    P = cols[0].number_input("Purchase Cost P", value=150000.0, min_value=0.0, step=1000.0)
    S = cols[1].number_input("Salvage Value S", value=10000.0, min_value=0.0, step=500.0)
    n = int(cols[2].number_input("Useful Life n (years)", value=8, min_value=1, step=1))
    d = cols[3].number_input("Declining Rate d", value=0.2, min_value=0.0, max_value=1.0, step=0.01)
    i = cols[4].number_input("Interest i (for Sinking Fund)", value=0.08, min_value=0.0, step=0.01)

    sl_years, sl_dep, sl_bv = straight_line(P, S, n)
    db_years, db_dep, db_bv = declining_balance(P, S, n, d)
    syd_years, syd_dep, syd_bv = sum_of_years_digits(P, S, n)
    sf_years, sf_dep, sf_bv = sinking_fund(P, S, n, i)

    df = pd.DataFrame({
        "Year": sl_years,
        "SL_Dep": sl_dep, "SL_BV": sl_bv,
        "DB_Dep": db_dep, "DB_BV": db_bv,
        "SYD_Dep": syd_dep, "SYD_BV": syd_bv,
        "SF_Dep": sf_dep, "SF_BV": sf_bv
    })
    st.dataframe(df, use_container_width=True)

    fig = px.line(df, x="Year", y=["SL_BV", "DB_BV", "SYD_BV", "SF_BV"], title="Book Value vs Year")
    st.plotly_chart(fig, use_container_width=True)

    maybe_explain("Depreciation", {"P": P, "S": S, "n": n, "d": d, "i": i}, {"SL_last_BV": sl_bv[-1]})
