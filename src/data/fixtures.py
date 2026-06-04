"""
WC 2026 group stage fixtures and knockout bracket template.

Format: 12 groups (A–L), 4 teams each.
Top 2 from each group + 8 best third-place teams advance to Round of 32.
"""

from itertools import combinations
from src.data.teams import get_group_teams, all_groups

# All group-stage matchups per group (each pair plays once)
def group_fixtures(group: str) -> list[tuple[str, str]]:
    teams = get_group_teams(group)
    return list(combinations(teams, 2))


def all_group_fixtures() -> list[tuple[str, str, str]]:
    """Returns list of (group, team_a, team_b) for every group match."""
    fixtures = []
    for g in all_groups():
        for a, b in group_fixtures(g):
            fixtures.append((g, a, b))
    return fixtures


# Third-place ranking tie-breaker groups
# Per FIFA rules, the 8 best third-placed teams advance.
# These are the 4 groups whose third-place teams are compared.
THIRD_PLACE_SLOTS = 8  # 12 groups → 12 third-place teams → 8 advance

KNOCKOUT_ROUND_LABELS = {
    32: "Round of 32",
    16: "Round of 16",
    8: "Quarter-finals",
    4: "Semi-finals",
    2: "Final",
}

# WC 2026 host cities (for display only)
HOST_VENUES = {
    "USA": ["New York/New Jersey", "Los Angeles", "Dallas", "San Francisco",
            "Seattle", "Miami", "Boston", "Atlanta", "Kansas City", "Philadelphia"],
    "MEX": ["Mexico City", "Guadalajara", "Monterrey"],
    "CAN": ["Toronto", "Vancouver"],
}
