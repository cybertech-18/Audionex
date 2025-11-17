from sqlalchemy import Column, Integer, String, JSON
from app.db.session import Base

class Agent(Base):
    __tablename__ = "agents"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    prompt = Column(String)
    voice = Column(String, default="alloy")
    config_json = Column(JSON)
