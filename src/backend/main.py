from fastapi import FastAPI

app = FastAPI()

@app.head("/")
def get_head():
    return