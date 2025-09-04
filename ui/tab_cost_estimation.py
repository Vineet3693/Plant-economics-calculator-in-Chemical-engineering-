# ui/tab_cost_estimation.py
import streamlit as st
from calculations.cost_estimation import scaling_cost, lang_factor_total, total_product_cost
from utils.ai_helper import maybe_explain

def render_cost_tab():
    st.header("Cost Estimation")
    st.subheader("Scaling Law (Six-tenths Rule)")
    c = st.columns(4)
    C1 = c[0].number_input("Known Cost C1", value=50000.0, min_value=0.0, step=1000.0)
    Q1 = c[1].number_input("Known Capacity Q1", value=10.0, min_value=0.0001, step=0.1)
    Q2 = c[2].number_input("Target Capacity Q2", value=20.0, min_value=0.0001, step=0.1)
    n = c[3].number_input("Scaling Exponent n", value=0.6, min_value=0.1, max_value=1.0, step=0.05)
    scaled = scaling_cost(C1, Q1, Q2, n)
    st.metric("Scaled Cost C2", f"{scaled:,.2f}")

    st.subheader("Lang Factor Estimate")
    f = st.number_input("Lang Factor f", value=4.3, min_value=1.0, step=0.1)
    equipment_sum = st.text_input("Equipment Costs (comma-separated)", value="12000,24000,33000")
    try:
        eq = [float(x.strip()) for x in equipment_sum.split(",") if x.strip()]
    except:
        eq = []
    lang_total = lang_factor_total(eq, f) if eq else 0.0
    st.metric("Fixed Capital (Lang)", f"{lang_total:,.2f}")

    st.subheader("Total Product Cost")
    C_raw = st.number_input("Raw Materials", value=50000.0, min_value=0.0, step=1000.0)
    C_util = st.number_input("Utilities", value=15000.0, min_value=0.0, step=500.0)
    C_labor = st.number_input("Labor", value=30000.0, min_value=0.0, step=1000.0)
    C_over = st.number_input("Overheads", value=20000.0, min_value=0.0, step=1000.0)
    total_prod = total_product_cost(C_raw, C_util, C_labor, C_over)
    st.metric("Total Product Cost", f"{total_prod:,.2f}")

    maybe_explain("Cost Estimation", {
        "C1": C1, "Q1": Q1, "Q2": Q2, "n": n, "f": f, "equipment": eq
    }, {
        "Scaled_Cost": scaled, "Lang_Total": lang_total, "Total_Product_Cost": total_prod
    })
