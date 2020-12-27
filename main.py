from fastapi import FastAPI
from leela import core

app = FastAPI()


@app.on_event("startup")
async def startup():
    await core.main()