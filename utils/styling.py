# utils/styling.py
import streamlit as st

def apply_theme():
    css = """
    <style>
    .metric { text-align: center; }
    .stMetric { background: #0e1117; border-radius: 16px; padding: 12px; }
    .stTabs [role="tab"] { padding: 10px 16px; font-weight: 600; }
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)
