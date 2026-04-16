# Khel AI Bowler Momentum API

This FastAPI service calculates bowling momentum for a selected bowler in a selected innings using the existing Khel AI Django models.

## Endpoint

GET /api/innings/{innings_id}/bowler/{player_id}/momentum/

## Example

GET /api/innings/3/bowler/14/momentum/

## Response

```json
{
  "innings_id": 3,
  "bowler_id": 14,
  "bowler_name": "Jasprit Bumrah",
  "balls_bowled": 24,
  "dot_balls": 13,
  "wickets": 2,
  "runs_conceded": 18,
  "boundary_balls": 1,
  "momentum_score": 4.42
}