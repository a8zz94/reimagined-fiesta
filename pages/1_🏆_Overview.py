"""Overview page — championship probabilities for all 48 teams."""

import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import sys, os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from app import get_simulation_results
from src.data.teams import TEAMS

st.set_page_config(page_title="Overview — WC 2026", page_icon="🏆", layout="wide")
st.title("🏆 Championship Probabilities")

results = get_simulation_results()
probs = results["probabilities"]

ROUND_LABELS = {
    "r32": "Round of 32",
    "r16": "Round of 16",
    "qf": "Quarter-final",
    "sf": "Semi-final",
    "final": "Final",
    "winner": "Champion",
}

# Build dataframe
rows = []
for code, p in probs.items():
    t = TEAMS[code]
    rows.append({
        "Flag": t["flag"],
        "Team": t["name"],
        "Confederation": t["confederation"],
        "Elo": t["elo"],
        "Champion %": round(p["winner"] * 100, 2),
        "Final %": round(p["final"] * 100, 1),
        "Semi-final %": round(p["sf"] * 100, 1),
        "Quarter-final %": round(p["qf"] * 100, 1),
        "Round of 16 %": round(p["r16"] * 100, 1),
        "Advance %": round(p["r32"] * 100, 1),
        "_code": code,
    })

df = pd.DataFrame(rows).sort_values("Champion %", ascending=False).reset_index(drop=True)
df.index += 1

# ── Top 10 bar chart ─────────────────────────────────────────────────────────
st.subheader("Top 20 — Win the Tournament")
top20 = df.head(20).copy()

fig = px.bar(
    top20,
    x="Team",
    y="Champion %",
    color="Confederation",
    text="Champion %",
    color_discrete_map={
        "UEFA": "#1a73e8",
        "CONMEBOL": "#34a853",
        "CONCACAF": "#fbbc05",
        "CAF": "#ea4335",
        "AFC": "#9c27b0",
        "OFC": "#00bcd4",
    },
    labels={"Champion %": "Probability (%)"},
)
fig.update_traces(texttemplate="%{text:.1f}%", textposition="outside")
fig.update_layout(
    xaxis_tickangle=-35,
    yaxis_title="Win probability (%)",
    showlegend=True,
    height=420,
)
st.plotly_chart(fig, use_container_width=True)

# ── Heatmap — round-by-round ──────────────────────────────────────────────────
st.subheader("Round-by-Round Probabilities — All 48 Teams")

top_n = st.slider("Show top N teams", min_value=10, max_value=48, value=24)
heat_df = df.head(top_n)[
    ["Flag", "Team", "Advance %", "Round of 16 %", "Quarter-final %",
     "Semi-final %", "Final %", "Champion %"]
].set_index("Team")

# Numeric only for heatmap
heat_vals = heat_df.drop(columns=["Flag"])

fig2 = go.Figure(data=go.Heatmap(
    z=heat_vals.values,
    x=heat_vals.columns.tolist(),
    y=heat_vals.index.tolist(),
    colorscale="Blues",
    text=heat_vals.values.round(1),
    texttemplate="%{text}%",
    hovertemplate="%{y} — %{x}: %{z:.1f}%<extra></extra>",
))
fig2.update_layout(
    height=60 + top_n * 22,
    xaxis_title="",
    yaxis_title="",
    margin=dict(l=120),
)
st.plotly_chart(fig2, use_container_width=True)

# ── Full table ────────────────────────────────────────────────────────────────
st.subheader("Full Rankings Table")
display_df = df.drop(columns=["_code"])
st.dataframe(
    display_df,
    use_container_width=True,
    column_config={
        "Champion %": st.column_config.ProgressColumn(
            "Champion %", format="%.2f%%", min_value=0, max_value=float(display_df["Champion %"].max())
        )
    },
)

st.caption(f"Based on {results['n_simulations']:,} Monte Carlo simulations · Elo + Poisson model")
