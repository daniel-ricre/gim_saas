from sqlalchemy import Column, String, Integer, Float
from ..database.base import Base

class Gym(Base):
    __tablename__ = "gyms"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    members = Column(Integer)