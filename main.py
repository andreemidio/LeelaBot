from fastapi import FastAPI

import core

app = FastAPI()


@app.on_event("startup")
async def startup():
    await core.main()