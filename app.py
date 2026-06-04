"""
FIFA World Cup 2026 Super Computer — main Streamlit entry point.
Run with: streamlit run app.py
"""

import streamlit as st
import sys, os

sys.path.insert(0, os.path.dirname(__file__))

st.set_page_config(
    page_title="WC 2026 Super Computer",
    page_icon="🏆",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Shared simulation cache ──────────────────────────────────────────────────

@st.cache_data(show_spinner="Running 100,000 tournament simulations…")
def get_simulation_results(n: int = 100_000):
    from src.engine.simulator import run_simulation
    return run_simulation(n=n, seed=2026)


# ── Home page ────────────────────────────────────────────────────────────────

st.title("🏆 FIFA World Cup 2026 Super Computer")
st.caption("Monte Carlo + Elo prediction engine — 100,000 tournament simulations")

st.markdown(
    """
    This tool simulates the **FIFA World Cup 2026** using a composite model that accounts for:

    | Factor | Weight |
    |--------|--------|
    | Elo rating (FIFA ranking + historical results) | 40% |
    | Recent international form (last 10 matches) | 25% |
    | Squad quality (player ratings, key players) | 20% |
    | World Cup experience / historical performance | 15% |

    Each match uses a **Poisson goal-scoring model** calibrated by team attack/defense ratings and
    the Elo-derived win probability. The full tournament (group stage → final) is simulated
    **100,000 times** to produce stable probabilities.

    ---
    **Navigate using the sidebar →**
    - 🏆 **Overview** — championship probabilities for all 48 teams
    - 📊 **Groups** — predicted group standings and advancement chances
    - ⚔️ **Simulator** — head-to-head match predictor
    - 👥 **Teams** — squad details and individual team analysis
    """
)

col1, col2, col3 = st.columns(3)
col1.metric("Teams", "48")
col2.metric("Groups", "12")
col3.metric("Simulations", "100,000")
