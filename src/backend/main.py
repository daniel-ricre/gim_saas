from fastapi import FastAPI

app = FastAPI()

@app.head("/")
def get_head():
    return

@app.get("/")
def get_router():
    return {"status": "OK"}