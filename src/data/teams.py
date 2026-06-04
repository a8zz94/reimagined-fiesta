"""
All 48 FIFA World Cup 2026 qualified teams.

Elo ratings derived from FIFA rankings + WC 2022 performance + international results
through mid-2025. attack/defense on a 0–10 scale (5 = tournament average).
form = recent 10-match weighted points ratio (0–10).
wc_experience = historical World Cup performance score (0–10).
"""

TEAMS: dict = {
    # ── GROUP A: Mexico, South Africa, South Korea, Czech Republic ────────────
    "MEX": {
        "name": "Mexico", "flag": "🇲🇽", "confederation": "CONCACAF",
        "group": "A", "fifa_ranking": 16, "elo": 1845,
        "attack": 7.3, "defense": 7.0, "form": 7.0, "wc_experience": 7.5,
        "color": "#006847",
    },
    "ZAF": {
        "name": "South Africa", "flag": "🇿🇦", "confederation": "CAF",
        "group": "A", "fifa_ranking": 57, "elo": 1752,
        "attack": 6.3, "defense": 6.5, "form": 6.5, "wc_experience": 5.5,
        "color": "#007A4D",
    },
    "KOR": {
        "name": "South Korea", "flag": "🇰🇷", "confederation": "AFC",
        "group": "A", "fifa_ranking": 23, "elo": 1862,
        "attack": 7.0, "defense": 7.0, "form": 7.5, "wc_experience": 7.0,
        "color": "#CD2E3A",
    },
    "CZE": {
        "name": "Czech Republic", "flag": "🇨🇿", "confederation": "UEFA",
        "group": "A", "fifa_ranking": 40, "elo": 1810,
        "attack": 7.0, "defense": 7.2, "form": 7.5, "wc_experience": 6.5,
        "color": "#D7141A",
    },
    # ── GROUP B: Canada, Bosnia and Herzegovina, Qatar, Switzerland ───────────
    "CAN": {
        "name": "Canada", "flag": "🇨🇦", "confederation": "CONCACAF",
        "group": "B", "fifa_ranking": 42, "elo": 1832,
        "attack": 7.0, "defense": 7.0, "form": 7.5, "wc_experience": 3.5,
        "color": "#FF0000",
    },
    "BIH": {
        "name": "Bosnia and Herzegovina", "flag": "🇧🇦", "confederation": "UEFA",
        "group": "B", "fifa_ranking": 65, "elo": 1760,
        "attack": 7.0, "defense": 6.5, "form": 7.0, "wc_experience": 4.0,
        "color": "#002395",
    },
    "QAT": {
        "name": "Qatar", "flag": "🇶🇦", "confederation": "AFC",
        "group": "B", "fifa_ranking": 34, "elo": 1680,
        "attack": 5.5, "defense": 6.0, "form": 6.0, "wc_experience": 3.5,
        "color": "#8D1B3D",
    },
    "SUI": {
        "name": "Switzerland", "flag": "🇨🇭", "confederation": "UEFA",
        "group": "B", "fifa_ranking": 15, "elo": 1858,
        "attack": 7.0, "defense": 7.8, "form": 7.5, "wc_experience": 6.5,
        "color": "#FF0000",
    },
    # ── GROUP C: Brazil, Morocco, Haiti, Scotland ─────────────────────────────
    "BRA": {
        "name": "Brazil", "flag": "🇧🇷", "confederation": "CONMEBOL",
        "group": "C", "fifa_ranking": 5, "elo": 1995,
        "attack": 9.3, "defense": 8.2, "form": 8.0, "wc_experience": 10.0,
        "color": "#009C3B",
    },
    "MAR": {
        "name": "Morocco", "flag": "🇲🇦", "confederation": "CAF",
        "group": "C", "fifa_ranking": 14, "elo": 1892,
        "attack": 7.3, "defense": 8.0, "form": 8.0, "wc_experience": 6.5,
        "color": "#C1272D",
    },
    "HAI": {
        "name": "Haiti", "flag": "🇭🇹", "confederation": "CONCACAF",
        "group": "C", "fifa_ranking": 110, "elo": 1630,
        "attack": 5.0, "defense": 5.2, "form": 6.0, "wc_experience": 3.5,
        "color": "#00209F",
    },
    "SCO": {
        "name": "Scotland", "flag": "🏴󠁧󠁢󠁳󠁣󠁴󠁿", "confederation": "UEFA",
        "group": "C", "fifa_ranking": 38, "elo": 1790,
        "attack": 7.0, "defense": 7.0, "form": 7.0, "wc_experience": 5.5,
        "color": "#003078",
    },
    # ── GROUP D: United States, Paraguay, Australia, Turkey ───────────────────
    "USA": {
        "name": "United States", "flag": "🇺🇸", "confederation": "CONCACAF",
        "group": "D", "fifa_ranking": 16, "elo": 1838,
        "attack": 7.0, "defense": 7.2, "form": 7.5, "wc_experience": 7.0,
        "color": "#002868",
    },
    "PAR": {
        "name": "Paraguay", "flag": "🇵🇾", "confederation": "CONMEBOL",
        "group": "D", "fifa_ranking": 61, "elo": 1805,
        "attack": 6.8, "defense": 7.0, "form": 6.5, "wc_experience": 6.0,
        "color": "#D52B1E",
    },
    "AUS": {
        "name": "Australia", "flag": "🇦🇺", "confederation": "AFC",
        "group": "D", "fifa_ranking": 27, "elo": 1768,
        "attack": 6.5, "defense": 6.5, "form": 7.0, "wc_experience": 6.0,
        "color": "#FFD700",
    },
    "TUR": {
        "name": "Turkey", "flag": "🇹🇷", "confederation": "UEFA",
        "group": "D", "fifa_ranking": 17, "elo": 1852,
        "attack": 7.3, "defense": 7.2, "form": 7.5, "wc_experience": 5.5,
        "color": "#E30A17",
    },
    # ── GROUP E: Germany, Curaçao, Ivory Coast, Ecuador ──────────────────────
    "GER": {
        "name": "Germany", "flag": "🇩🇪", "confederation": "UEFA",
        "group": "E", "fifa_ranking": 6, "elo": 1982,
        "attack": 8.5, "defense": 8.3, "form": 8.0, "wc_experience": 10.0,
        "color": "#000000",
    },
    "CUW": {
        "name": "Curaçao", "flag": "🇨🇼", "confederation": "CONCACAF",
        "group": "E", "fifa_ranking": 85, "elo": 1570,
        "attack": 4.8, "defense": 4.5, "form": 6.0, "wc_experience": 2.0,
        "color": "#002B7F",
    },
    "CIV": {
        "name": "Ivory Coast", "flag": "🇨🇮", "confederation": "CAF",
        "group": "E", "fifa_ranking": 43, "elo": 1795,
        "attack": 7.0, "defense": 6.5, "form": 7.5, "wc_experience": 5.5,
        "color": "#F77F00",
    },
    "ECU": {
        "name": "Ecuador", "flag": "🇪🇨", "confederation": "CONMEBOL",
        "group": "E", "fifa_ranking": 36, "elo": 1868,
        "attack": 7.0, "defense": 7.2, "form": 7.0, "wc_experience": 5.0,
        "color": "#FFD100",
    },
    # ── GROUP F: Netherlands, Japan, Sweden, Tunisia ──────────────────────────
    "NED": {
        "name": "Netherlands", "flag": "🇳🇱", "confederation": "UEFA",
        "group": "F", "fifa_ranking": 8, "elo": 1975,
        "attack": 8.4, "defense": 8.5, "form": 8.0, "wc_experience": 8.5,
        "color": "#FF6600",
    },
    "JPN": {
        "name": "Japan", "flag": "🇯🇵", "confederation": "AFC",
        "group": "F", "fifa_ranking": 21, "elo": 1828,
        "attack": 7.3, "defense": 7.2, "form": 8.0, "wc_experience": 6.5,
        "color": "#BC002D",
    },
    "SWE": {
        "name": "Sweden", "flag": "🇸🇪", "confederation": "UEFA",
        "group": "F", "fifa_ranking": 22, "elo": 1865,
        "attack": 8.5, "defense": 7.5, "form": 8.0, "wc_experience": 7.0,
        "color": "#006AA7",
    },
    "TUN": {
        "name": "Tunisia", "flag": "🇹🇳", "confederation": "CAF",
        "group": "F", "fifa_ranking": 30, "elo": 1745,
        "attack": 6.0, "defense": 6.8, "form": 6.5, "wc_experience": 5.5,
        "color": "#E70013",
    },
    # ── GROUP G: Belgium, Egypt, Iran, New Zealand ────────────────────────────
    "BEL": {
        "name": "Belgium", "flag": "🇧🇪", "confederation": "UEFA",
        "group": "G", "fifa_ranking": 10, "elo": 1958,
        "attack": 7.8, "defense": 7.8, "form": 7.0, "wc_experience": 7.5,
        "color": "#000000",
    },
    "EGY": {
        "name": "Egypt", "flag": "🇪🇬", "confederation": "CAF",
        "group": "G", "fifa_ranking": 37, "elo": 1760,
        "attack": 6.5, "defense": 6.8, "form": 7.0, "wc_experience": 5.0,
        "color": "#CE1126",
    },
    "IRN": {
        "name": "Iran", "flag": "🇮🇷", "confederation": "AFC",
        "group": "G", "fifa_ranking": 25, "elo": 1775,
        "attack": 6.3, "defense": 7.5, "form": 7.0, "wc_experience": 5.5,
        "color": "#239F40",
    },
    "NZL": {
        "name": "New Zealand", "flag": "🇳🇿", "confederation": "OFC",
        "group": "G", "fifa_ranking": 96, "elo": 1652,
        "attack": 5.0, "defense": 5.5, "form": 6.0, "wc_experience": 4.0,
        "color": "#000000",
    },
    # ── GROUP H: Spain, Cape Verde, Saudi Arabia, Uruguay ────────────────────
    "ESP": {
        "name": "Spain", "flag": "🇪🇸", "confederation": "UEFA",
        "group": "H", "fifa_ranking": 3, "elo": 2015,
        "attack": 8.8, "defense": 9.0, "form": 9.0, "wc_experience": 9.0,
        "color": "#AA151B",
    },
    "CPV": {
        "name": "Cape Verde", "flag": "🇨🇻", "confederation": "CAF",
        "group": "H", "fifa_ranking": 72, "elo": 1700,
        "attack": 5.8, "defense": 6.0, "form": 7.0, "wc_experience": 3.0,
        "color": "#003893",
    },
    "SAU": {
        "name": "Saudi Arabia", "flag": "🇸🇦", "confederation": "AFC",
        "group": "H", "fifa_ranking": 58, "elo": 1695,
        "attack": 6.0, "defense": 6.2, "form": 6.5, "wc_experience": 5.0,
        "color": "#006C35",
    },
    "URU": {
        "name": "Uruguay", "flag": "🇺🇾", "confederation": "CONMEBOL",
        "group": "H", "fifa_ranking": 14, "elo": 1922,
        "attack": 7.5, "defense": 8.5, "form": 7.5, "wc_experience": 8.5,
        "color": "#5EB6E4",
    },
    # ── GROUP I: France, Senegal, Iraq, Norway ────────────────────────────────
    "FRA": {
        "name": "France", "flag": "🇫🇷", "confederation": "UEFA",
        "group": "I", "fifa_ranking": 2, "elo": 2022,
        "attack": 9.0, "defense": 9.2, "form": 8.5, "wc_experience": 9.8,
        "color": "#002395",
    },
    "SEN": {
        "name": "Senegal", "flag": "🇸🇳", "confederation": "CAF",
        "group": "I", "fifa_ranking": 19, "elo": 1872,
        "attack": 7.5, "defense": 7.3, "form": 7.5, "wc_experience": 6.0,
        "color": "#00853F",
    },
    "IRQ": {
        "name": "Iraq", "flag": "🇮🇶", "confederation": "AFC",
        "group": "I", "fifa_ranking": 68, "elo": 1660,
        "attack": 5.5, "defense": 5.8, "form": 6.5, "wc_experience": 4.5,
        "color": "#007A3D",
    },
    "NOR": {
        "name": "Norway", "flag": "🇳🇴", "confederation": "UEFA",
        "group": "I", "fifa_ranking": 13, "elo": 1890,
        "attack": 8.5, "defense": 7.5, "form": 8.0, "wc_experience": 5.5,
        "color": "#EF2B2D",
    },
    # ── GROUP J: Argentina, Algeria, Austria, Jordan ──────────────────────────
    "ARG": {
        "name": "Argentina", "flag": "🇦🇷", "confederation": "CONMEBOL",
        "group": "J", "fifa_ranking": 1, "elo": 2061,
        "attack": 9.2, "defense": 8.8, "form": 9.0, "wc_experience": 9.5,
        "color": "#74ACDF",
    },
    "ALG": {
        "name": "Algeria", "flag": "🇩🇿", "confederation": "CAF",
        "group": "J", "fifa_ranking": 32, "elo": 1840,
        "attack": 7.3, "defense": 7.0, "form": 7.5, "wc_experience": 5.5,
        "color": "#006233",
    },
    "AUT": {
        "name": "Austria", "flag": "🇦🇹", "confederation": "UEFA",
        "group": "J", "fifa_ranking": 22, "elo": 1815,
        "attack": 7.2, "defense": 7.0, "form": 7.5, "wc_experience": 4.5,
        "color": "#ED2939",
    },
    "JOR": {
        "name": "Jordan", "flag": "🇯🇴", "confederation": "AFC",
        "group": "J", "fifa_ranking": 68, "elo": 1665,
        "attack": 5.5, "defense": 5.8, "form": 6.5, "wc_experience": 2.0,
        "color": "#007A3D",
    },
    # ── GROUP K: Portugal, DR Congo, Uzbekistan, Colombia ─────────────────────
    "POR": {
        "name": "Portugal", "flag": "🇵🇹", "confederation": "UEFA",
        "group": "K", "fifa_ranking": 7, "elo": 1988,
        "attack": 8.8, "defense": 8.3, "form": 8.0, "wc_experience": 7.5,
        "color": "#006600",
    },
    "COD": {
        "name": "DR Congo", "flag": "🇨🇩", "confederation": "CAF",
        "group": "K", "fifa_ranking": 56, "elo": 1705,
        "attack": 6.0, "defense": 5.8, "form": 6.5, "wc_experience": 4.0,
        "color": "#007FFF",
    },
    "UZB": {
        "name": "Uzbekistan", "flag": "🇺🇿", "confederation": "AFC",
        "group": "K", "fifa_ranking": 62, "elo": 1645,
        "attack": 5.3, "defense": 5.5, "form": 6.5, "wc_experience": 2.5,
        "color": "#1EB53A",
    },
    "COL": {
        "name": "Colombia", "flag": "🇨🇴", "confederation": "CONMEBOL",
        "group": "K", "fifa_ranking": 9, "elo": 1938,
        "attack": 8.0, "defense": 7.5, "form": 8.5, "wc_experience": 7.0,
        "color": "#FCD116",
    },
    # ── GROUP L: England, Croatia, Ghana, Panama ──────────────────────────────
    "ENG": {
        "name": "England", "flag": "🏴󠁧󠁢󠁥󠁮󠁧󠁿", "confederation": "UEFA",
        "group": "L", "fifa_ranking": 4, "elo": 2008,
        "attack": 8.7, "defense": 8.8, "form": 8.5, "wc_experience": 7.5,
        "color": "#CF081F",
    },
    "CRO": {
        "name": "Croatia", "flag": "🇭🇷", "confederation": "UEFA",
        "group": "L", "fifa_ranking": 12, "elo": 1885,
        "attack": 7.5, "defense": 7.8, "form": 7.0, "wc_experience": 7.0,
        "color": "#FF0000",
    },
    "GHA": {
        "name": "Ghana", "flag": "🇬🇭", "confederation": "CAF",
        "group": "L", "fifa_ranking": 60, "elo": 1748,
        "attack": 7.0, "defense": 6.5, "form": 6.5, "wc_experience": 6.0,
        "color": "#006B3F",
    },
    "PAN": {
        "name": "Panama", "flag": "🇵🇦", "confederation": "CONCACAF",
        "group": "L", "fifa_ranking": 50, "elo": 1695,
        "attack": 6.0, "defense": 6.5, "form": 6.5, "wc_experience": 3.0,
        "color": "#005293",
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
