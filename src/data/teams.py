"""
All 48 FIFA World Cup 2026 qualified teams.

Elo ratings derived from FIFA rankings + WC 2022 performance + international results
through mid-2025. attack/defense on a 0–10 scale (5 = tournament average).
form = recent 10-match weighted points ratio (0–10).
wc_experience = historical World Cup performance score (0–10).
"""

TEAMS: dict = {
    # ── CONMEBOL ──────────────────────────────────────────────────────────────
    "ARG": {
        "name": "Argentina", "flag": "🇦🇷", "confederation": "CONMEBOL",
        "group": "E", "fifa_ranking": 1, "elo": 2061,
        "attack": 9.2, "defense": 8.8, "form": 9.0, "wc_experience": 9.5,
        "color": "#74ACDF",
    },
    "BRA": {
        "name": "Brazil", "flag": "🇧🇷", "confederation": "CONMEBOL",
        "group": "D", "fifa_ranking": 5, "elo": 1995,
        "attack": 9.3, "defense": 8.2, "form": 7.5, "wc_experience": 10.0,
        "color": "#009C3B",
    },
    "COL": {
        "name": "Colombia", "flag": "🇨🇴", "confederation": "CONMEBOL",
        "group": "B", "fifa_ranking": 9, "elo": 1938,
        "attack": 8.0, "defense": 7.5, "form": 8.0, "wc_experience": 7.0,
        "color": "#FCD116",
    },
    "URU": {
        "name": "Uruguay", "flag": "🇺🇾", "confederation": "CONMEBOL",
        "group": "A", "fifa_ranking": 14, "elo": 1922,
        "attack": 7.5, "defense": 8.5, "form": 7.5, "wc_experience": 8.5,
        "color": "#5EB6E4",
    },
    "ECU": {
        "name": "Ecuador", "flag": "🇪🇨", "confederation": "CONMEBOL",
        "group": "I", "fifa_ranking": 36, "elo": 1868,
        "attack": 7.0, "defense": 7.2, "form": 7.0, "wc_experience": 5.0,
        "color": "#FFD100",
    },
    "PAR": {
        "name": "Paraguay", "flag": "🇵🇾", "confederation": "CONMEBOL",
        "group": "F", "fifa_ranking": 61, "elo": 1805,
        "attack": 6.8, "defense": 7.0, "form": 6.5, "wc_experience": 6.0,
        "color": "#D52B1E",
    },
    # ── UEFA ──────────────────────────────────────────────────────────────────
    "FRA": {
        "name": "France", "flag": "🇫🇷", "confederation": "UEFA",
        "group": "G", "fifa_ranking": 2, "elo": 2022,
        "attack": 9.0, "defense": 9.2, "form": 8.5, "wc_experience": 9.8,
        "color": "#002395",
    },
    "ENG": {
        "name": "England", "flag": "🏴󠁧󠁢󠁥󠁮󠁧󠁿", "confederation": "UEFA",
        "group": "H", "fifa_ranking": 4, "elo": 2008,
        "attack": 8.7, "defense": 8.8, "form": 8.5, "wc_experience": 7.5,
        "color": "#CF081F",
    },
    "ESP": {
        "name": "Spain", "flag": "🇪🇸", "confederation": "UEFA",
        "group": "J", "fifa_ranking": 3, "elo": 2015,
        "attack": 8.8, "defense": 9.0, "form": 9.0, "wc_experience": 9.0,
        "color": "#AA151B",
    },
    "GER": {
        "name": "Germany", "flag": "🇩🇪", "confederation": "UEFA",
        "group": "I", "fifa_ranking": 6, "elo": 1982,
        "attack": 8.5, "defense": 8.3, "form": 8.0, "wc_experience": 10.0,
        "color": "#000000",
    },
    "POR": {
        "name": "Portugal", "flag": "🇵🇹", "confederation": "UEFA",
        "group": "K", "fifa_ranking": 7, "elo": 1988,
        "attack": 8.8, "defense": 8.3, "form": 8.0, "wc_experience": 7.5,
        "color": "#006600",
    },
    "NED": {
        "name": "Netherlands", "flag": "🇳🇱", "confederation": "UEFA",
        "group": "L", "fifa_ranking": 8, "elo": 1975,
        "attack": 8.4, "defense": 8.5, "form": 8.0, "wc_experience": 8.5,
        "color": "#FF6600",
    },
    "BEL": {
        "name": "Belgium", "flag": "🇧🇪", "confederation": "UEFA",
        "group": "I", "fifa_ranking": 10, "elo": 1958,
        "attack": 7.8, "defense": 7.8, "form": 7.0, "wc_experience": 7.5,
        "color": "#000000",
    },
    "ITA": {
        "name": "Italy", "flag": "🇮🇹", "confederation": "UEFA",
        "group": "L", "fifa_ranking": 11, "elo": 1945,
        "attack": 7.2, "defense": 8.8, "form": 7.5, "wc_experience": 9.5,
        "color": "#003399",
    },
    "CRO": {
        "name": "Croatia", "flag": "🇭🇷", "confederation": "UEFA",
        "group": "F", "fifa_ranking": 12, "elo": 1885,
        "attack": 7.5, "defense": 7.8, "form": 7.0, "wc_experience": 7.0,
        "color": "#FF0000",
    },
    "DEN": {
        "name": "Denmark", "flag": "🇩🇰", "confederation": "UEFA",
        "group": "E", "fifa_ranking": 13, "elo": 1878,
        "attack": 7.2, "defense": 8.0, "form": 7.5, "wc_experience": 6.5,
        "color": "#C60C30",
    },
    "SUI": {
        "name": "Switzerland", "flag": "🇨🇭", "confederation": "UEFA",
        "group": "G", "fifa_ranking": 15, "elo": 1858,
        "attack": 7.0, "defense": 7.8, "form": 7.5, "wc_experience": 6.5,
        "color": "#FF0000",
    },
    "TUR": {
        "name": "Turkey", "flag": "🇹🇷", "confederation": "UEFA",
        "group": "D", "fifa_ranking": 17, "elo": 1852,
        "attack": 7.3, "defense": 7.2, "form": 7.5, "wc_experience": 5.5,
        "color": "#E30A17",
    },
    "SRB": {
        "name": "Serbia", "flag": "🇷🇸", "confederation": "UEFA",
        "group": "C", "fifa_ranking": 20, "elo": 1820,
        "attack": 7.3, "defense": 7.0, "form": 7.0, "wc_experience": 5.0,
        "color": "#C6363C",
    },
    "AUT": {
        "name": "Austria", "flag": "🇦🇹", "confederation": "UEFA",
        "group": "H", "fifa_ranking": 22, "elo": 1815,
        "attack": 7.2, "defense": 7.0, "form": 7.5, "wc_experience": 4.5,
        "color": "#ED2939",
    },
    "POL": {
        "name": "Poland", "flag": "🇵🇱", "confederation": "UEFA",
        "group": "J", "fifa_ranking": 24, "elo": 1808,
        "attack": 7.5, "defense": 6.8, "form": 6.5, "wc_experience": 5.5,
        "color": "#DC143C",
    },
    "SVK": {
        "name": "Slovakia", "flag": "🇸🇰", "confederation": "UEFA",
        "group": "K", "fifa_ranking": 30, "elo": 1778,
        "attack": 6.5, "defense": 6.8, "form": 6.5, "wc_experience": 4.0,
        "color": "#FFFFFF",
    },
    # ── CONCACAF ──────────────────────────────────────────────────────────────
    "USA": {
        "name": "United States", "flag": "🇺🇸", "confederation": "CONCACAF",
        "group": "A", "fifa_ranking": 16, "elo": 1838,
        "attack": 7.0, "defense": 7.2, "form": 7.5, "wc_experience": 7.0,
        "color": "#002868",
    },
    "MEX": {
        "name": "Mexico", "flag": "🇲🇽", "confederation": "CONCACAF",
        "group": "B", "fifa_ranking": 18, "elo": 1845,
        "attack": 7.3, "defense": 7.0, "form": 7.0, "wc_experience": 7.5,
        "color": "#006847",
    },
    "CAN": {
        "name": "Canada", "flag": "🇨🇦", "confederation": "CONCACAF",
        "group": "C", "fifa_ranking": 42, "elo": 1832,
        "attack": 7.0, "defense": 7.0, "form": 7.5, "wc_experience": 3.5,
        "color": "#FF0000",
    },
    "PAN": {
        "name": "Panama", "flag": "🇵🇦", "confederation": "CONCACAF",
        "group": "J", "fifa_ranking": 50, "elo": 1745,
        "attack": 6.0, "defense": 6.5, "form": 6.5, "wc_experience": 3.0,
        "color": "#005293",
    },
    "HON": {
        "name": "Honduras", "flag": "🇭🇳", "confederation": "CONCACAF",
        "group": "F", "fifa_ranking": 74, "elo": 1718,
        "attack": 5.8, "defense": 6.0, "form": 6.0, "wc_experience": 4.5,
        "color": "#0073CF",
    },
    "JAM": {
        "name": "Jamaica", "flag": "🇯🇲", "confederation": "CONCACAF",
        "group": "D", "fifa_ranking": 47, "elo": 1698,
        "attack": 5.8, "defense": 5.8, "form": 6.5, "wc_experience": 3.0,
        "color": "#000000",
    },
    # ── CAF ───────────────────────────────────────────────────────────────────
    "MAR": {
        "name": "Morocco", "flag": "🇲🇦", "confederation": "CAF",
        "group": "A", "fifa_ranking": 14, "elo": 1892,
        "attack": 7.3, "defense": 8.0, "form": 8.0, "wc_experience": 6.5,
        "color": "#C1272D",
    },
    "SEN": {
        "name": "Senegal", "flag": "🇸🇳", "confederation": "CAF",
        "group": "G", "fifa_ranking": 19, "elo": 1872,
        "attack": 7.5, "defense": 7.3, "form": 7.5, "wc_experience": 6.0,
        "color": "#00853F",
    },
    "NGA": {
        "name": "Nigeria", "flag": "🇳🇬", "confederation": "CAF",
        "group": "D", "fifa_ranking": 35, "elo": 1792,
        "attack": 7.2, "defense": 6.5, "form": 7.0, "wc_experience": 6.5,
        "color": "#008751",
    },
    "EGY": {
        "name": "Egypt", "flag": "🇪🇬", "confederation": "CAF",
        "group": "F", "fifa_ranking": 37, "elo": 1760,
        "attack": 6.5, "defense": 6.8, "form": 7.0, "wc_experience": 5.0,
        "color": "#CE1126",
    },
    "CMR": {
        "name": "Cameroon", "flag": "🇨🇲", "confederation": "CAF",
        "group": "C", "fifa_ranking": 40, "elo": 1788,
        "attack": 6.8, "defense": 6.5, "form": 6.5, "wc_experience": 6.5,
        "color": "#007A5E",
    },
    "CIV": {
        "name": "Ivory Coast", "flag": "🇨🇮", "confederation": "CAF",
        "group": "E", "fifa_ranking": 43, "elo": 1795,
        "attack": 7.0, "defense": 6.5, "form": 7.5, "wc_experience": 5.5,
        "color": "#F77F00",
    },
    "COD": {
        "name": "DR Congo", "flag": "🇨🇩", "confederation": "CAF",
        "group": "H", "fifa_ranking": 56, "elo": 1705,
        "attack": 6.0, "defense": 5.8, "form": 6.5, "wc_experience": 4.0,
        "color": "#007FFF",
    },
    "ZAF": {
        "name": "South Africa", "flag": "🇿🇦", "confederation": "CAF",
        "group": "I", "fifa_ranking": 57, "elo": 1752,
        "attack": 6.3, "defense": 6.5, "form": 6.5, "wc_experience": 5.5,
        "color": "#007A4D",
    },
    "GHA": {
        "name": "Ghana", "flag": "🇬🇭", "confederation": "CAF",
        "group": "B", "fifa_ranking": 60, "elo": 1798,
        "attack": 7.0, "defense": 6.5, "form": 6.5, "wc_experience": 6.0,
        "color": "#006B3F",
    },
    # ── AFC ───────────────────────────────────────────────────────────────────
    "JPN": {
        "name": "Japan", "flag": "🇯🇵", "confederation": "AFC",
        "group": "B", "fifa_ranking": 21, "elo": 1828,
        "attack": 7.3, "defense": 7.2, "form": 8.0, "wc_experience": 6.5,
        "color": "#BC002D",
    },
    "KOR": {
        "name": "South Korea", "flag": "🇰🇷", "confederation": "AFC",
        "group": "A", "fifa_ranking": 23, "elo": 1862,
        "attack": 7.0, "defense": 7.0, "form": 7.5, "wc_experience": 7.0,
        "color": "#CD2E3A",
    },
    "IRN": {
        "name": "Iran", "flag": "🇮🇷", "confederation": "AFC",
        "group": "G", "fifa_ranking": 25, "elo": 1775,
        "attack": 6.3, "defense": 7.5, "form": 7.0, "wc_experience": 5.5,
        "color": "#239F40",
    },
    "SAU": {
        "name": "Saudi Arabia", "flag": "🇸🇦", "confederation": "AFC",
        "group": "H", "fifa_ranking": 58, "elo": 1695,
        "attack": 6.0, "defense": 6.2, "form": 6.5, "wc_experience": 5.0,
        "color": "#006C35",
    },
    "AUS": {
        "name": "Australia", "flag": "🇦🇺", "confederation": "AFC",
        "group": "C", "fifa_ranking": 27, "elo": 1768,
        "attack": 6.5, "defense": 6.5, "form": 7.0, "wc_experience": 6.0,
        "color": "#FFD700",
    },
    "QAT": {
        "name": "Qatar", "flag": "🇶🇦", "confederation": "AFC",
        "group": "E", "fifa_ranking": 34, "elo": 1680,
        "attack": 5.5, "defense": 6.0, "form": 6.0, "wc_experience": 3.5,
        "color": "#8D1B3D",
    },
    "UZB": {
        "name": "Uzbekistan", "flag": "🇺🇿", "confederation": "AFC",
        "group": "L", "fifa_ranking": 62, "elo": 1645,
        "attack": 5.3, "defense": 5.5, "form": 6.5, "wc_experience": 2.5,
        "color": "#1EB53A",
    },
    "JOR": {
        "name": "Jordan", "flag": "🇯🇴", "confederation": "AFC",
        "group": "J", "fifa_ranking": 68, "elo": 1665,
        "attack": 5.5, "defense": 5.8, "form": 6.5, "wc_experience": 2.0,
        "color": "#007A3D",
    },
    # ── OFC & Playoff ─────────────────────────────────────────────────────────
    "NZL": {
        "name": "New Zealand", "flag": "🇳🇿", "confederation": "OFC",
        "group": "L", "fifa_ranking": 96, "elo": 1652,
        "attack": 5.0, "defense": 5.5, "form": 6.0, "wc_experience": 4.0,
        "color": "#000000",
    },
    "VEN": {
        "name": "Venezuela", "flag": "🇻🇪", "confederation": "CONMEBOL",
        "group": "K", "fifa_ranking": 73, "elo": 1712,
        "attack": 6.0, "defense": 5.8, "form": 6.5, "wc_experience": 2.0,
        "color": "#CF142B",
    },
    "IDN": {
        "name": "Indonesia", "flag": "🇮🇩", "confederation": "AFC",
        "group": "K", "fifa_ranking": 120, "elo": 1598,
        "attack": 4.5, "defense": 4.8, "form": 5.5, "wc_experience": 3.0,
        "color": "#CE1126",
    },
}


def get_team(code: str) -> dict:
    return TEAMS[code.upper()]


def get_group_teams(group: str) -> list[str]:
    return [code for code, t in TEAMS.items() if t["group"] == group.upper()]


def all_groups() -> list[str]:
    return sorted({t["group"] for t in TEAMS.values()})


def elo_win_probability(elo_a: float, elo_b: float) -> float:
    """Expected win probability for team A vs team B (neutral venue)."""
    return 1 / (1 + 10 ** ((elo_b - elo_a) / 400))
