# routes for text analysis
from fastapi import APIRouter
router = APIRouter()
@router.post("/text")
async def text_route(payload: dict):
    return {"demo": True}
