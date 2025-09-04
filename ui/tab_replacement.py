# ui/tab_replacement.py
import streamlit as st
import numpy as np
import plotly.express as px
from calculations.replacement import economic_life_min_pw
from utils.ai_helper import maybe_explain

def render_replacement_tab():
    st.header("Replacement & Economic Life")
    st.caption("Enter expected annual costs (comma-separated) to find the economic life that minimizes present worth of costs.")
    cols = st.columns(2)
    costs_str = cols[0].text_input("Annual Costs (Year 1..N, comma-separated)", value="30000,32000,35000,39000,44000,50000,57000")
    discount = cols[1].number_input("Discount Rate i", value=0.1, min_value=0.0, step=0.01)

    try:
        annual_costs = [float(x.strip()) for x in costs_str.split(",") if x.strip()]
    except:
        annual_costs = []

    if annual_costs:
        year, pws = economic_life_min_pw(annual_costs, discount)
        st.metric("Optimal Replacement Year", f"{year}")
        fig = px.line(x=list(range(1, len(pws)+1)), y=pws, labels={"x":"Year","y":"Present Worth of Costs"}, title="PW of Costs vs Year")
        st.plotly_chart(fig, use_container_width=True)
        maybe_explain("Replacement", {"annual_costs": annual_costs, "i": discount}, {"optimal_year": year})
    else:
        st.info("Enter at least one annual cost value.")
