from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from schemas import BowlerMomentumResponse, ErrorResponse
from services import bowler_momentum_summary

app = FastAPI(
    title="Khel AI Bowler Momentum API",
    version="1.0.0",
    description="Standalone demo API for teaching bowling momentum calculation."
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {
        "message": "Bowler Momentum API is live",
        "docs": "/docs",
        "health": "/health"
    }


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get(
    "/api/innings/{innings_id}/bowler/{player_id}/momentum/",
    response_model=BowlerMomentumResponse,
    responses={404: {"model": ErrorResponse}},
)
def get_bowler_momentum(innings_id: int, player_id: int):
    result = bowler_momentum_summary(innings_id=innings_id, player_id=player_id)

    if result is None:
        raise HTTPException(status_code=404, detail="No demo data found for this bowler in this innings")

    return result