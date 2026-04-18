from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from schemas import BowlerMomentumRequest, BowlerMomentumResponse, ErrorResponse
from services import bowler_momentum_summary

app = FastAPI(
    title="Khel AI Bowler Momentum API",
    version="2.0.0",
    description="Payload-based bowler momentum calculation API for Khel AI integration."
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

@app.post(
    "/api/bowler-momentum/",
    response_model=BowlerMomentumResponse,
    responses={404: {"model": ErrorResponse}},
)
def calculate_momentum(payload: BowlerMomentumRequest):
    result = bowler_momentum_summary(payload.model_dump())

    if result is None:
        raise HTTPException(status_code=404, detail="No ball events provided")

    return result