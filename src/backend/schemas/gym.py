from pydantic import BaseModel, Field, ConfigDict
from typing import Optional

class GymBase(BaseModel):
    name: str = Field(..., min_length=3)
    members: int = Field(..., gt=0)

class GymCreate(GymBase):
    pass

class GymUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=3)
    members: Optional[int] = Field(None, gt=0)
    
class GymResponse(GymBase):
    id: int
    
    model_config = ConfigDict(from_attributes=True)