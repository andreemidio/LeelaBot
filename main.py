from fastapi import FastAPI
from leela import core

app = FastAPI()


@app.get("/")
async def root():
    return core.main()