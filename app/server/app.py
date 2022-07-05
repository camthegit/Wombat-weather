from fastapi import FastAPI
from app.server.database import init_db
from app.server.routes.past_weather import router as Router

"""example application from https://testdriven.io/blog/fastapi-beanie/"""


app = FastAPI()
app.include_router(Router, tags=["Weather data"], prefix="/obs")


@app.on_event("startup")
async def start_db():
    await init_db()


@app.get("/", tags=["Root"])
async def read_root() -> dict:
    return {"message": "Welcome to your beanie powered app!"}
