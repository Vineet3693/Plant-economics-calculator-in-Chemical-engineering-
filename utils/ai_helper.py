# utils/ai_helper.py
import os
import streamlit as st
from dotenv import load_dotenv

# Optional Groq import guarded so app still runs without key
try:
    from groq import Groq
except Exception:
    Groq = None

load_dotenv()
_API = os.getenv("GROQ_API_KEY")

_client = Groq(api_key=_API) if (Groq and _API) else None

def _call_groq(prompt: str, temperature: float = 0.4) -> str:
    if not _client:
        return "⚠️ Groq not configured. Add GROQ_API_KEY in .env to enable AI explanations."
    try:
        resp = _client.chat.completions.create(
            model="llama-3.1-70b-versatile",
            messages=[{"role": "user", "content": prompt}],
            temperature=temperature,
        )
        # groq python SDK returns .choices[0].message.content in recent versions
        return resp.choices[0].message.content
    except Exception as e:
        return f"⚠️ AI error: {e}"

def maybe_explain(topic: str, inputs: dict, results: dict):
    with st.expander("🔎 Explain with AI", expanded=False):
        if st.button(f"Explain {topic}", key=f"ai_{topic}"):
            prompt = f"""
You are a chemical engineering economics tutor.
Topic: {topic}
Inputs: {inputs}
Results: {results}

Explain:
1) What the results mean for decision-making.
2) Assumptions & risks to watch.
3) A short analogy.
Keep it concise (150-220 words), structured, and friendly.
"""
            st.write(_call_groq(prompt))

def summarize_all(inputs: dict, results: dict):
    with st.expander("🧠 AI Executive Summary", expanded=True):
        if st.button("Generate AI Summary"):
            prompt = f"""
You are a senior process economics analyst. Given these inputs and results across TVM, Depreciation, Profitability, Cost Estimation, Break-even, and Replacement, write an executive summary with actionable recommendations.

Inputs: {inputs}
Results: {results}

Deliver:
- 3–5 key takeaways
- Go / No-Go signal with reasoning
- Top 3 risks and mitigations
- One sensitivity worth running next
Tone: crisp, data-aware, no fluff. <300 words.
"""
            st.write(_call_groq(prompt, temperature=0.35))
