# ui/tab_interest.py
from calculations.interest import simple_interest, future_value, present_worth, annuity_present_worth, annuity_future_worth, cashflow_curve

def render_interest_tab():
    st.header("📈 Interest and Time Value of Money")

    option = st.selectbox(
        "Select Calculation",
        [
            "Simple Interest",
            "Future Value",
            "Present Worth",
            "Annuity Present Worth",
            "Annuity Future Worth",
            "Cashflow Curve",
        ],
    )

    if option == "Simple Interest":
        P = st.number_input("Principal (P)", value=1000.0)
        r = st.number_input("Rate of Interest (r)", value=0.05)
        t = st.number_input("Time (t)", value=5.0)
        if st.button("Calculate"):
            st.success(f"Simple Interest = {simple_interest(P, r, t):.2f}")

    elif option == "Future Value":
        P = st.number_input("Principal (P)", value=1000.0)
        r = st.number_input("Rate (r)", value=0.05)
        n = st.number_input("Years (n)", value=5)
        if st.button("Calculate"):
            st.success(f"Future Value = {future_value(P, r, n):.2f}")

    elif option == "Present Worth":
        F = st.number_input("Future Value (F)", value=2000.0)
        r = st.number_input("Rate (r)", value=0.05)
        n = st.number_input("Years (n)", value=5)
        if st.button("Calculate"):
            st.success(f"Present Worth = {present_worth(F, r, n):.2f}")

    elif option == "Annuity Present Worth":
        A = st.number_input("Annuity (A)", value=500.0)
        r = st.number_input("Rate (r)", value=0.05)
        n = st.number_input("Years (n)", value=5)
        if st.button("Calculate"):
            st.success(f"Annuity Present Worth = {annuity_present_worth(A, r, n):.2f}")

    elif option == "Annuity Future Worth":
        A = st.number_input("Annuity (A)", value=500.0)
        r = st.number_input("Rate (r)", value=0.05)
        n = st.number_input("Years (n)", value=5)
        if st.button("Calculate"):
            st.success(f"Annuity Future Worth = {annuity_future_worth(A, r, n):.2f}")

    elif option == "Cashflow Curve":
        P = st.number_input("Principal (P)", value=1000.0)
        r = st.number_input("Rate (r)", value=0.05)
        n = st.number_input("Years (n)", value=10)
        if st.button("Generate"):
            values = cashflow_curve(P, r, n)
            st.line_chart(values)
