from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import schemas
from app.db import session
from typing import List

router = APIRouter()

@router.post("/", response_model=schemas.agent.Agent)
def create_agent(
    *,
    db: Session = Depends(session.get_db),
    agent_in: schemas.agent.AgentCreate,
):
    """
    Create new agent.
    """
    # In a real app, you'd save this to the DB
    # db_obj = crud.agent.create(db=db, obj_in=agent_in)
    # return db_obj
    print(f"Creating agent: {agent_in.name}")
    # For this starter, we'll just return a dummy response
    return schemas.agent.Agent(id=1, name=agent_in.name, prompt=agent_in.prompt, voice=agent_in.voice)


@router.get("/", response_model=List[schemas.agent.Agent])
def read_agents(
    db: Session = Depends(session.get_db),
    skip: int = 0,
    limit: int = 100,
):
    """
    Retrieve agents.
    """
    # In a real app, you'd fetch this from the DB
    # agents = crud.agent.get_multi(db, skip=skip, limit=limit)
    # return agents
    return [
        schemas.agent.Agent(id=1, name="Support Agent", prompt="You are a helpful support agent.", voice="alloy")
    ]
