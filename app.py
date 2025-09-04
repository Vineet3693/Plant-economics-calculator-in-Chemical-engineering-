# app.py
import streamlit as st
from ui.tab_interest import render_interest_tab
from ui.tab_depreciation import render_depreciation_tab
from ui.tab_profitability import render_profitability_tab
from ui.tab_cost_estimation import render_cost_tab
from ui.tab_breakeven import render_breakeven_tab
from ui.tab_replacement import render_replacement_tab
from ui.tab_master import render_master_tab
from utils.styling import apply_theme

st.set_page_config(page_title="Plant Economics Calculator", page_icon="💹", layout="wide")
apply_theme()

st.sidebar.image("assets/logo.png", use_container_width=True)
st.sidebar.markdown("### Plant Economics Calculator")
st.sidebar.markdown("Use the tabs above to calculate each section or the Master tab for all at once.")

tabs = st.tabs([
    "1) Interest & TVM", "2) Depreciation", "3) Profitability",
    "4) Cost Estimation", "5) Break-even", "6) Replacement", "7) Master (All-in-One)"
])

with tabs[0]: render_interest_tab()
with tabs[1]: render_depreciation_tab()
with tabs[2]: render_profitability_tab()
with tabs[3]: render_cost_tab()
with tabs[4]: render_breakeven_tab()
with tabs[5]: render_replacement_tab()
with tabs[6]: render_master_tab()
