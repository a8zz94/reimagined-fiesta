"""Head-to-head match simulator and custom strength adjustment."""

import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import pandas as pd
import sys, os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from src.data.teams import TEAMS
from src.engine.predictor import match_probabilities, expected_goals, simulate_match

st.set_page_config(page_title="Simulator — WC 2026", page_icon="⚔️", layout="wide")
st.title("⚔️ Head-to-Head Match Simulator")

team_options = sorted(TEAMS.keys(), key=lambda c: TEAMS[c]["name"])
display_names = {c: f"{TEAMS[c]['flag']} {TEAMS[c]['name']}" for c in team_options}

col1, col2 = st.columns(2)
with col1:
    team_a = st.selectbox("Team A", team_options, index=0, format_func=lambda c: display_names[c])
with col2:
    team_b = st.selectbox("Team B", team_options, index=1, format_func=lambda c: display_names[c])

match_type = st.radio("Match type", ["Group stage (draws allowed)", "Knockout (no draws)"], horizontal=True)
knockout = "Knockout" in match_type

if team_a == team_b:
    st.warning("Please select two different teams.")
    st.stop()

# ── Stats comparison ──────────────────────────────────────────────────────────
ta, tb = TEAMS[team_a], TEAMS[team_b]
st.subheader("Team Comparison")

metrics = ["Elo", "Attack", "Defense", "Form", "WC Experience"]
vals_a = [ta["elo"], ta["attack"] * 10, ta["defense"] * 10, ta["form"] * 10, ta["wc_experience"] * 10]
vals_b = [tb["elo"], tb["attack"] * 10, tb["defense"] * 10, tb["form"] * 10, tb["wc_experience"] * 10]

comp_fig = go.Figure()
comp_fig.add_trace(go.Bar(
    name=ta["name"], x=metrics, y=vals_a,
    marker_color="#1a73e8", text=[f"{v:.0f}" for v in vals_a],
    textposition="outside",
))
comp_fig.add_trace(go.Bar(
    name=tb["name"], x=metrics, y=vals_b,
    marker_color="#ea4335", text=[f"{v:.0f}" for v in vals_b],
    textposition="outside",
))
comp_fig.update_layout(barmode="group", height=320, yaxis_title="Score",
                        legend=dict(orientation="h"))
st.plotly_chart(comp_fig, use_container_width=True)

# ── Match probabilities ───────────────────────────────────────────────────────
st.subheader("Match Outcome Probabilities")

with st.spinner("Simulating 50,000 matches…"):
    mp = match_probabilities(team_a, team_b, n=50_000)

c1, c2, c3 = st.columns(3)
c1.metric(f"{ta['flag']} {ta['name']} Win", f"{mp['win_a']*100:.1f}%")
c2.metric("Draw", f"{mp['draw']*100:.1f}%" if not knockout else "N/A (knockout)")
c3.metric(f"{tb['flag']} {tb['name']} Win", f"{mp['win_b']*100:.1f}%")

la, lb = expected_goals(team_a, team_b)
col_a, col_b = st.columns(2)
col_a.metric(f"Expected Goals — {ta['name']}", f"{la:.2f}")
col_b.metric(f"Expected Goals — {tb['name']}", f"{lb:.2f}")

# Donut chart
if not knockout:
    labels = [f"{ta['name']} Win", "Draw", f"{tb['name']} Win"]
    values = [mp["win_a"], mp["draw"], mp["win_b"]]
else:
    labels = [f"{ta['name']} Win", f"{tb['name']} Win"]
    values = [mp["win_a"] / (mp["win_a"] + mp["win_b"]),
              mp["win_b"] / (mp["win_a"] + mp["win_b"])]

donut = go.Figure(go.Pie(labels=labels, values=values, hole=0.5,
                          marker_colors=["#1a73e8", "#fbbc05", "#ea4335"][:len(labels)]))
donut.update_layout(height=300, showlegend=True)
st.plotly_chart(donut, use_container_width=True)

# ── Score distribution ────────────────────────────────────────────────────────
st.subheader("Scoreline Distribution (top 15 most likely)")

rng = np.random.default_rng(seed=42)
n_samples = 100_000
goals_a_samples = rng.poisson(la, n_samples)
goals_b_samples = rng.poisson(lb, n_samples)

from collections import Counter
score_counts = Counter(zip(goals_a_samples.tolist(), goals_b_samples.tolist()))
top_scores = score_counts.most_common(15)

score_df = pd.DataFrame(
    [(f"{a}–{b}", cnt / n_samples * 100) for (a, b), cnt in top_scores],
    columns=["Scoreline", "Probability %"],
)
score_df = score_df.sort_values("Probability %", ascending=False)

fig_scores = px.bar(
    score_df, x="Scoreline", y="Probability %",
    text="Probability %", color="Probability %", color_continuous_scale="Blues",
)
fig_scores.update_traces(texttemplate="%{text:.1f}%", textposition="outside")
fig_scores.update_layout(height=380, coloraxis_showscale=False)
st.plotly_chart(fig_scores, use_container_width=True)

# ── Live single match simulation ──────────────────────────────────────────────
st.subheader("Simulate a Single Match")
if st.button("⚽ Kick off!"):
    sim_rng = np.random.default_rng()
    ga, gb, pen = simulate_match(team_a, team_b, knockout=knockout, rng=sim_rng)
    if pen:
        st.success(
            f"**{ta['flag']} {ta['name']} {ga} — {gb} {tb['flag']} {tb['name']}** "
            f"(after extra time → {TEAMS[pen]['name']} win on penalties)"
        )
    elif ga > gb:
        st.success(f"**{ta['flag']} {ta['name']} {ga} — {gb} {tb['flag']} {tb['name']}** — {ta['name']} win!")
    elif ga < gb:
        st.success(f"**{ta['flag']} {ta['name']} {ga} — {gb} {tb['flag']} {tb['name']}** — {tb['name']} win!")
    else:
        st.info(f"**{ta['flag']} {ta['name']} {ga} — {gb} {tb['flag']} {tb['name']}** — Draw!")
