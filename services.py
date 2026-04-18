from typing import Optional


def calculate_balls_bowled(events) -> int:
    return sum(1 for event in events if event["is_legal_delivery"])


def calculate_dot_balls(events) -> int:
    return sum(
        1 for event in events
        if event["is_legal_delivery"] and (event["runs_off_bat"] + event["extras"]) == 0
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


def bowler_momentum_summary(payload: dict) -> Optional[dict]:
    events = payload["ball_events"]

    if not events:
        return None

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
        "innings_id": payload["innings_id"],
        "bowler_id": payload["player_id"],
        "bowler_name": payload["bowler_name"],
        "balls_bowled": balls_bowled,
        "dot_balls": dot_balls,
        "wickets": wickets,
        "runs_conceded": runs_conceded,
        "boundary_balls": boundary_balls,
        "momentum_score": momentum_score,
    }