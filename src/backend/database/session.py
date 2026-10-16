from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise RuntimeError("URL de base de datos no encontrada")

if DATABASE_URL.startswith("postgres://"):
    DATABASE_URL.replace("postgres://", "postgressql+psycopg://", 1)
    
if DATABASE_URL.startswith("postgresql://"):
    DATABASE_URL.replace("postgresql://", "postgresql+psycopg://", 1)

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
