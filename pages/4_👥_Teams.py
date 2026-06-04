"""Individual team deep-dive — squad, ratings, form, WC history."""

import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import sys, os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from app import get_simulation_results
from src.data.teams import TEAMS
from src.data.players import SQUADS, SQUAD_SUMMARY, squad_avg_rating, squad_form_score

st.set_page_config(page_title="Teams — WC 2026", page_icon="👥", layout="wide")
st.title("👥 Team Analysis")

team_options = sorted(TEAMS.keys(), key=lambda c: TEAMS[c]["name"])
display_names = {c: f"{TEAMS[c]['flag']} {TEAMS[c]['name']}" for c in team_options}

selected = st.selectbox("Select a team", team_options, format_func=lambda c: display_names[c])
team = TEAMS[selected]

results = get_simulation_results()
probs = results["probabilities"][selected]
group_avg = results["group_avg"][selected]

# ── Header ────────────────────────────────────────────────────────────────────
st.header(f"{team['flag']} {team['name']}")
st.caption(f"Group {team['group']} · {team['confederation']} · FIFA Ranking #{team['fifa_ranking']}")

# Key metrics
m1, m2, m3, m4, m5 = st.columns(5)
m1.metric("Elo Rating", f"{team['elo']:,}")
m2.metric("Champion %", f"{probs['winner']*100:.2f}%")
m3.metric("Final %", f"{probs['final']*100:.1f}%")
m4.metric("Semi-final %", f"{probs['sf']*100:.1f}%")
m5.metric("Advance %", f"{probs['r32']*100:.1f}%")

# ── Radar chart ───────────────────────────────────────────────────────────────
st.subheader("Team Profile")
categories = ["Attack", "Defense", "Form", "WC Experience", "Squad Quality"]
values = [
    team["attack"],
    team["defense"],
    team["form"],
    team["wc_experience"],
    squad_avg_rating(selected) / 10,
]
values_closed = values + [values[0]]
categories_closed = categories + [categories[0]]

radar = go.Figure(go.Scatterpolar(
    r=values_closed,
    theta=categories_closed,
    fill="toself",
    line_color=team.get("color", "#1a73e8"),
    fillcolor=team.get("color", "#1a73e8") + "44",
    name=team["name"],
))
radar.update_layout(
    polar=dict(radialaxis=dict(range=[0, 10], tickfont_size=9)),
    showlegend=False,
    height=350,
)
st.plotly_chart(radar, use_container_width=True)

# ── Group predictions ─────────────────────────────────────────────────────────
st.subheader("Group Stage Prediction")
col1, col2, col3 = st.columns(3)
col1.metric("Avg Points", f"{group_avg['points']:.2f}")
col2.metric("Avg Goal Diff", f"{group_avg['gd']:+.2f}")
col3.metric("Avg Goals Scored", f"{group_avg['gf']:.2f}")

# ── Round-by-round probabilities bar ─────────────────────────────────────────
rnd_labels = {
    "r32": "Advance (R32)", "r16": "Round of 16",
    "qf": "Quarter-final", "sf": "Semi-final",
    "final": "Final", "winner": "Champion",
}
rnd_df = pd.DataFrame({
    "Round": list(rnd_labels.values()),
    "Probability %": [probs[k] * 100 for k in rnd_labels],
})
fig_rnd = px.bar(rnd_df, x="Round", y="Probability %", text="Probability %",
                  color="Probability %", color_continuous_scale="Greens")
fig_rnd.update_traces(texttemplate="%{text:.1f}%", textposition="outside")
fig_rnd.update_layout(height=320, coloraxis_showscale=False, xaxis_tickangle=-20)
st.plotly_chart(fig_rnd, use_container_width=True)

# ── Squad ─────────────────────────────────────────────────────────────────────
st.subheader("Squad")

if selected in SQUADS:
    players = SQUADS[selected]
    pos_order = {"GK": 0, "RB": 1, "CB": 1, "LB": 1, "DM": 2, "CM": 2, "AM": 3, "FW": 4}
    players_sorted = sorted(players, key=lambda p: (pos_order.get(p["pos"], 5), -p["rating"]))

    squad_df = pd.DataFrame([{
        "⭐": "⭐" if p["is_key"] else "",
        "Name": p["name"],
        "Pos": p["pos"],
        "Club": p["club"],
        "Age": p["age"],
        "Rating": p["rating"],
        "Form": p["form"],
        "Caps": p["caps"],
        "Int. Goals": p["int_goals"],
    } for p in players_sorted])

    st.dataframe(
        squad_df,
        use_container_width=True,
        column_config={
            "Rating": st.column_config.ProgressColumn(
                "Rating", format="%d", min_value=70, max_value=95
            ),
            "Form": st.column_config.ProgressColumn(
                "Form", format="%.1f", min_value=0, max_value=10
            ),
        },
    )

    # Top scorer chart
    scorers = sorted(players, key=lambda p: -p["int_goals"])[:8]
    scorer_fig = px.bar(
        pd.DataFrame({"Player": [p["name"] for p in scorers],
                       "International Goals": [p["int_goals"] for p in scorers]}),
        x="Player", y="International Goals",
        text="International Goals", color="International Goals",
        color_continuous_scale="Oranges",
    )
    scorer_fig.update_traces(textposition="outside")
    scorer_fig.update_layout(height=320, coloraxis_showscale=False,
                               xaxis_tickangle=-25, title="Top International Scorers in Squad")
    st.plotly_chart(scorer_fig, use_container_width=True)

elif selected in SQUAD_SUMMARY:
    s = SQUAD_SUMMARY[selected]
    st.info(
        f"**Captain / Key Player:** {s['captain']} ({s['captain_club']}) — "
        f"Rating {s['captain_rating']}\n\n"
        f"**Star Player:** {s['star_player']}\n\n"
        f"**Average Squad Rating:** {s['avg_rating']}"
    )
else:
    st.info("Detailed squad data not yet available for this team.")

# ── Contextual stats ──────────────────────────────────────────────────────────
st.subheader("Strength Breakdown")
strength_data = {
    "Attack": team["attack"],
    "Defense": team["defense"],
    "Form (0–10)": team["form"],
    "WC Experience (0–10)": team["wc_experience"],
    "Squad Avg Rating / 10": squad_avg_rating(selected) / 10,
    "Squad Form / 10": squad_form_score(selected),
}
for label, val in strength_data.items():
    st.progress(min(val / 10, 1.0), text=f"{label}: {val:.2f}")
