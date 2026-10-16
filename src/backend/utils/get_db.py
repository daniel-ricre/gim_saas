from ..database.base import Base
from ..database.session import SessionLocal

def get_db(Base):
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()