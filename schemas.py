from pydantic import BaseModel, Field
from typing import List


class BallEventInput(BaseModel):
    over_number: int
    ball_number: int
    runs_off_bat: int
    extras: int
    extra_type: str
    is_legal_delivery: bool
    wicket_fell: bool
    wicket_type: str


class BowlerMomentumRequest(BaseModel):
    innings_id: int = Field(..., description="Selected innings ID")
    player_id: int = Field(..., description="Selected bowler/player ID")
    bowler_name: str = Field(..., description="Bowler name")
    ball_events: List[BallEventInput] = Field(..., description="Raw ball events for this bowler")


class BowlerMomentumResponse(BaseModel):
    innings_id: int = Field(..., description="Selected innings ID")
    bowler_id: int = Field(..., description="Selected bowler/player ID")
    bowler_name: str = Field(..., description="Bowler name")
    balls_bowled: int = Field(..., description="Legal balls bowled by the bowler")
    dot_balls: int = Field(..., description="Legal dot balls bowled")
    wickets: int = Field(..., description="Bowler-earned wickets")
    runs_conceded: int = Field(..., description="Runs charged to the bowler")
    boundary_balls: int = Field(..., description="Balls on which 4 or 6 was scored off the bat")
    momentum_score: float = Field(..., description="Computed bowling momentum score")


class ErrorResponse(BaseModel):
    detail: str