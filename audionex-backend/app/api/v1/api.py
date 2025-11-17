from fastapi import APIRouter
from app.api.v1.endpoints import agents, knowledge, telephony

api_router = APIRouter()
api_router.include_router(agents.router, prefix="/agents", tags=["agents"])
api_router.include_router(knowledge.router, prefix="/knowledge", tags=["knowledge"])
api_router.include_router(telephony.router, prefix="/telephony", tags=["telephony"])
