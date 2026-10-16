from fastapi import FastAPI
from .endpoints.gyms import router as gym_router

app = FastAPI()
app.include_router(router=gym_router)

@app.head("/")
def get_head():
    return

@app.get("/")
def get_router():
    return {"status": "OK"}