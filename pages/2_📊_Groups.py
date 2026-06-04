"""Group stage predictions — standings and advancement probabilities."""

import streamlit as st
import plotly.express as px
import pandas as pd
import sys, os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from app import get_simulation_results
from src.data.teams import TEAMS, all_groups, get_group_teams
from src.data.fixtures import group_fixtures
from src.engine.predictor import match_probabilities

st.set_page_config(page_title="Groups — WC 2026", page_icon="📊", layout="wide")
st.title("📊 Group Stage Predictions")

results = get_simulation_results()
probs = results["probabilities"]
group_avg = results["group_avg"]

groups = all_groups()
selected_group = st.selectbox("Select group", groups, format_func=lambda g: f"Group {g}")

# ── Group standings ───────────────────────────────────────────────────────────
st.subheader(f"Group {selected_group} — Predicted Standings")
codes = get_group_teams(selected_group)

rows = []
for code in codes:
    t = TEAMS[code]
    avg = group_avg[code]
    p = probs[code]
    rows.append({
        "": t["flag"],
        "Team": t["name"],
        "Elo": t["elo"],
        "Avg Pts": round(avg["points"], 2),
        "Avg GD": round(avg["gd"], 2),
        "Avg GF": round(avg["gf"], 2),
        "Advance %": round(p["r32"] * 100, 1),
        "R16 %": round(p["r16"] * 100, 1),
        "QF %": round(p["qf"] * 100, 1),
        "_code": code,
    })

group_df = pd.DataFrame(rows).sort_values("Avg Pts", ascending=False).reset_index(drop=True)
group_df.index += 1

st.dataframe(
    group_df.drop(columns=["_code"]),
    use_container_width=True,
    column_config={
        "Advance %": st.column_config.ProgressColumn(
            "Advance %", format="%.1f%%", min_value=0, max_value=100
        )
    },
)

# ── Group fixtures with match odds ────────────────────────────────────────────
st.subheader(f"Group {selected_group} — Match Probabilities")

fixture_rows = []
for a, b in group_fixtures(selected_group):
    mp = match_probabilities(a, b, n=20_000)
    fixture_rows.append({
        "Match": f"{TEAMS[a]['flag']} {TEAMS[a]['name']} vs {TEAMS[b]['flag']} {TEAMS[b]['name']}",
        "xG (A)": round(mp["xg_a"], 2),
        "Win A %": round(mp["win_a"] * 100, 1),
        "Draw %": round(mp["draw"] * 100, 1),
        "Win B %": round(mp["win_b"] * 100, 1),
        "xG (B)": round(mp["xg_b"], 2),
    })

st.dataframe(pd.DataFrame(fixture_rows), use_container_width=True)

# ── All groups overview bar chart ─────────────────────────────────────────────
st.subheader("Advancement Probability — All Groups")
all_rows = []
for g in groups:
    for code in get_group_teams(g):
        all_rows.append({
            "Group": f"Group {g}",
            "Team": TEAMS[code]["name"],
            "Flag": TEAMS[code]["flag"],
            "Advance %": round(probs[code]["r32"] * 100, 1),
            "Confederation": TEAMS[code]["confederation"],
        })

all_df = pd.DataFrame(all_rows)
selected_groups_filter = st.multiselect(
    "Filter groups", groups, default=groups[:4], format_func=lambda g: f"Group {g}"
)
filtered = all_df[all_df["Group"].isin([f"Group {g}" for g in selected_groups_filter])]
fig = px.bar(
    filtered,
    x="Team",
    y="Advance %",
    color="Group",
    barmode="group",
    text="Advance %",
    height=400,
)
fig.update_traces(texttemplate="%{text}%", textposition="outside")
fig.update_layout(xaxis_tickangle=-35, yaxis_title="Advance from group (%)")
st.plotly_chart(fig, use_container_width=True)
