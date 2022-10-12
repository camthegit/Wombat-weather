import os, sys
from fastapi import FastAPI

folder = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.insert(0, folder)

from src.server.database import init_db
from src.server.routes.past_weather import router as Router
"""Runs the Weather data api and initialised the Mongodb connection using start_db.init_db
example application from https://testdriven.io/blog/fastapi-beanie/"""


app = FastAPI()
app.include_router(Router, tags=["Weather data"], prefix="/obs")


@app.on_event("startup")
async def start_db():
    await init_db()


@app.get("/", tags=["Root"])
async def read_root() -> dict:
    return {"message": "Welcome to your beanie powered app!"}
