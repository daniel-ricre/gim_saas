from sqlalchemy.orm import Session
from ..models.gym import Gym
from ..schemas.gym import GymCreate


def create_gym(db: Session, gym: GymCreate):
    
    new_gym = Gym(**gym.model_dump())
    
    db.add(new_gym)
    db.commit()
    db.refresh(new_gym)
    
    return True


def get_gyms(db: Session, skip: int = 0, limit: int = 50):
    
    gyms = db.query(Gym).offset(skip).limit(limit).all()
    return gyms
