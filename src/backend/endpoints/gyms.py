from fastapi import APIRouter, Depends
from ..schemas.gym import GymCreate, GymResponse
from sqlalchemy.orm import Session
from ..utils.get_db import get_db
from ..crud.gym import create_gym, get_gyms
from typing import List


router = APIRouter()

@router.post("/new_gym")
def new_gym(gym: GymCreate, db: Session = Depends(get_db)):
    return create_gym(db, gym)


@router.get("/get_gyms", response_model=List[GymResponse])
def all_gyms(skip: int = 0, limit: int = 50, db: Session = Depends(get_db)):
    return get_gyms(db, skip, limit)