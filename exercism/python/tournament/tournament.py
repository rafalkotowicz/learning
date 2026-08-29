"""Tournament exercise implementation."""

HEADER = "Team                           | MP |  W |  D |  L |  P"
WIN = "win"
LOSS = "loss"
DRAW = "draw"
POINTS_PER_WIN = 3
POINTS_PER_DRAW = 1


def _empty_stats():
    """Return empty stats structure for a team."""
    return {"mp": 0, "w": 0, "d": 0, "l": 0, "p": 0}


def tally(rows):
    """Return formatted tournament table sorted by points then team name."""
    standings = {}

    for row in rows:
        team_a, team_b, outcome = row.split(";")
        stats_a = standings.setdefault(team_a, _empty_stats())
        stats_b = standings.setdefault(team_b, _empty_stats())

        stats_a["mp"] += 1
        stats_b["mp"] += 1

        if outcome == WIN:
            stats_a["w"] += 1
            stats_b["l"] += 1
            stats_a["p"] += POINTS_PER_WIN
        elif outcome == LOSS:
            stats_a["l"] += 1
            stats_b["w"] += 1
            stats_b["p"] += POINTS_PER_WIN
        elif outcome == DRAW:
            stats_a["d"] += 1
            stats_b["d"] += 1
            stats_a["p"] += POINTS_PER_DRAW
            stats_b["p"] += POINTS_PER_DRAW

    ordered_teams = sorted(standings.items(), key=lambda item: (-item[1]["p"], item[0]))
    table = [HEADER]

    for team_name, stats in ordered_teams:
        table.append(
            f'{team_name:<31}| {stats["mp"]:>2} | {stats["w"]:>2} | '
            f'{stats["d"]:>2} | {stats["l"]:>2} | {stats["p"]:>2}'
        )

    return table
