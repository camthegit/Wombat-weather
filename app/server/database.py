from beanie import init_beanie
import motor.motor_asyncio

from app.server.models.ts_test import WeatherTS
from app.configs import cnf as configs
"""Imports configs from .env and environment, creates connect string and connects to Mongodb weather dbase"""


async def init_db():
    mongo_connect = f"mongodb://{configs.MONGO_HOST}:{configs.MONGO_PORT}/weather"
    client = motor.motor_asyncio.AsyncIOMotorClient(
        mongo_connect
    )

    await init_beanie(database=client.weather, document_models=[WeatherTS])
