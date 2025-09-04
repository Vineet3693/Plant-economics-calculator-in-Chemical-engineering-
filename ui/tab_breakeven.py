# ui/tab_breakeven.py
import streamlit as st
import numpy as np
import plotly.express as px
from calculations.breakeven import bep_units, bep_revenue
from utils.ai_helper import maybe_explain

def render_breakeven_tab():
    st.header("Break-even Analysis")
    c = st.columns(3)
    F = c[0].number_input("Fixed Cost F", value=100000.0, min_value=0.0, step=1000.0)
    V = c[1].number_input("Variable Cost per unit V", value=35.0, min_value=0.0, step=1.0)
    S = c[2].number_input("Selling Price per unit S", value=50.0, min_value=0.0, step=1.0)

    q_bep = bep_units(F, S, V)
    rev_bep = bep_revenue(F, S, V)
    st.metric("Break-even Quantity (units)", f"{q_bep:,.2f}")
    st.metric("Break-even Revenue", f"{rev_bep:,.2f}")

    q = np.linspace(0, max(q_bep * 1.5, 10), 100)
    revenue = S * q
    total_cost = F + V * q
    fig = px.line(x=q, y=[revenue, total_cost], labels={"x":"Quantity","value":"Amount"}, title="Revenue vs Total Cost")
    fig.update_layout(legend=dict(title=None, itemsizing="trace"), yaxis_tickformat=",")
    st.plotly_chart(fig, use_container_width=True)

    maybe_explain("Break-even", {"F": F, "V": V, "S": S}, {"BEP_units": q_bep, "BEP_revenue": rev_bep})
