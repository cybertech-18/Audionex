from pydantic import BaseModel
from typing import Optional

# Shared properties
class AgentBase(BaseModel):
    name: str
    prompt: str
    voice: Optional[str] = "alloy"

# Properties to receive on item creation
class AgentCreate(AgentBase):
    pass

# Properties to receive on item update
class AgentUpdate(AgentBase):
    pass

# Properties shared by models stored in DB
class AgentInDBBase(AgentBase):
    id: int
    
    class Config:
        orm_mode = True

# Properties to return to client
class Agent(AgentInDBBase):
    pass

# Properties stored in DB
class AgentInDB(AgentInDBBase):
    pass
