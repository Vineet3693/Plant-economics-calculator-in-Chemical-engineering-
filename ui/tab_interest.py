# ui/tab_interest.py
import streamlit as st
from calculations.interest import simple_interest, future_value, present_worth, annuity_present_worth, annuity_future_worth, cashflow_curve
import plotly.express as px
from utils.ai_helper import maybe_explain

def render_interest_tab():
    st.header("Interest & Time Value of Money")
    col = st.columns(4)
    P = col[0].number_input("Principal (P)", value=100000.0, min_value=0.0, step=1000.0)
    i_pct = col[1].number_input("Interest Rate i (%)", value=10.0, min_value=0.0, step=0.1)
    n = int(col[2].number_input("Periods (n, years)", value=5, min_value=1, step=1))
    A = col[3].number_input("Annuity (A)", value=0.0, min_value=0.0, step=100.0)

    i = i_pct / 100.0

    st.subheader("Key Results")
    c1, c2, c3, c4, c5 = st.columns(5)
    c1.metric("Simple Interest", f"{simple_interest(P, i, n):,.2f}")
    c2.metric("Future Value F", f"{future_value(P, i, n):,.2f}")
    c3.metric("Present Worth of F", f"{present_worth(future_value(P, i, n), i, n):,.2f}")
    c4.metric("PW of Annuity (A→P)", f"{annuity_present_worth(A, i, n):,.2f}")
    c5.metric("FW of Annuity (A→F)", f"{annuity_future_worth(A, i, n):,.2f}")

    years, values = cashflow_curve(P, i, n)
    fig = px.line(x=years, y=values, labels={"x": "Year", "y": "Value"}, title="Growth of Principal Over Time")
    st.plotly_chart(fig, use_container_width=True)

    maybe_explain("Interest & TVM", {
        "P": P, "i": i, "n": n, "A": A
    }, {
        "Future Value": future_value(P, i, n),
        "PW(Annuity)": annuity_present_worth(A, i, n)
    })
