from typing import Optional

# demo data for one innings and one bowler
DEMO_BALL_EVENTS = [
    {"innings_id": 1, "bowler_id": 101, "bowler_name": "Jasprit Bumrah", "is_legal_delivery": True,  "runs_off_bat": 0, "extras": 0, "extra_type": "",       "wicket_fell": False, "wicket_type": ""},
    {"innings_id": 1, "bowler_id": 101, "bowler_name": "Jasprit Bumrah", "is_legal_delivery": True,  "runs_off_bat": 0, "extras": 0, "extra_type": "",       "wicket_fell": False, "wicket_type": ""},
    {"innings_id": 1, "bowler_id": 101, "bowler_name": "Jasprit Bumrah", "is_legal_delivery": True,  "runs_off_bat": 4, "extras": 0, "extra_type": "",       "wicket_fell": False, "wicket_type": ""},
    {"innings_id": 1, "bowler_id": 101, "bowler_name": "Jasprit Bumrah", "is_legal_delivery": True,  "runs_off_bat": 0, "extras": 0, "extra_type": "",       "wicket_fell": True,  "wicket_type": "bowled"},
    {"innings_id": 1, "bowler_id": 101, "bowler_name": "Jasprit Bumrah", "is_legal_delivery": True,  "runs_off_bat": 1, "extras": 0, "extra_type": "",       "wicket_fell": False, "wicket_type": ""},
    {"innings_id": 1, "bowler_id": 101, "bowler_name": "Jasprit Bumrah", "is_legal_delivery": False, "runs_off_bat": 0, "extras": 1, "extra_type": "wide",   "wicket_fell": False, "wicket_type": ""},
    {"innings_id": 1, "bowler_id": 101, "bowler_name": "Jasprit Bumrah", "is_legal_delivery": True,  "runs_off_bat": 0, "extras": 0, "extra_type": "",       "wicket_fell": False, "wicket_type": ""},
]


def get_bowler_events(innings_id: int, player_id: int):
    return [
        event for event in DEMO_BALL_EVENTS
        if event["innings_id"] == innings_id and event["bowler_id"] == player_id
    ]


def calculate_balls_bowled(events) -> int:
    return sum(1 for event in events if event["is_legal_delivery"])


def calculate_dot_balls(events) -> int:
    return sum(
        1 for event in events
        if event["is_legal_delivery"]
        and (event["runs_off_bat"] + event["extras"]) == 0
    )


def calculate_wickets(events) -> int:
    return sum(
        1 for event in events
        if event["wicket_fell"] and event["wicket_type"] not in {"run_out", "retired_out"}
    )


def calculate_runs_conceded(events) -> int:
    runs_conceded = 0
    for event in events:
        runs_conceded += event["runs_off_bat"]
        if event["extra_type"] in {"wide", "no_ball"}:
            runs_conceded += event["extras"]
    return runs_conceded


def calculate_boundary_balls(events) -> int:
    return sum(1 for event in events if event["runs_off_bat"] in {4, 6})


def calculate_momentum_score(
    balls_bowled: int,
    dot_balls: int,
    wickets: int,
    runs_conceded: int,
    boundary_balls: int,
) -> float:
    numerator = (balls_bowled + 1) * (dot_balls + 1) * (wickets + 1)
    denominator = (runs_conceded + 1) * (boundary_balls + 1)
    return round(numerator / denominator, 2)


def bowler_momentum_summary(innings_id: int, player_id: int) -> Optional[dict]:
    events = get_bowler_events(innings_id, player_id)

    if not events:
        return None

    bowler_name = events[0]["bowler_name"]
    balls_bowled = calculate_balls_bowled(events)
    dot_balls = calculate_dot_balls(events)
    wickets = calculate_wickets(events)
    runs_conceded = calculate_runs_conceded(events)
    boundary_balls = calculate_boundary_balls(events)

    momentum_score = calculate_momentum_score(
        balls_bowled=balls_bowled,
        dot_balls=dot_balls,
        wickets=wickets,
        runs_conceded=runs_conceded,
        boundary_balls=boundary_balls,
    )

    return {
        "innings_id": innings_id,
        "bowler_id": player_id,
        "bowler_name": bowler_name,
        "balls_bowled": balls_bowled,
        "dot_balls": dot_balls,
        "wickets": wickets,
        "runs_conceded": runs_conceded,
        "boundary_balls": boundary_balls,
        "momentum_score": momentum_score,
    }