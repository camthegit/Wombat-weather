from beanie import init_beanie
import motor.motor_asyncio

from app.server.models.ts_test import WeatherTS
from app.configs import cnf as configs
"""Imports configs from .env and environment, creates connect string and connects to Mongodb weather dbase"""


async def init_db():
    if configs.MONGO_USER:
        mongo_connect = f"mongodb://{configs.MONGO_USER}:{configs.MONGO_PW}@" \
                        f"{configs.MONGO_HOST}:{configs.MONGO_PORT}/weather" \
                        f"?authSource=admin&tls=true&AllowInvalidCertificates=true"
    else:
        mongo_connect = f"mongodb://{configs.MONGO_HOST}:{configs.MONGO_PORT}/weather"

    # Todo: remove following debug print
    print(f"DB Connect string: {mongo_connect}")
    client = motor.motor_asyncio.AsyncIOMotorClient(mongo_connect)
    await init_beanie(database=client.weather, document_models=[WeatherTS])
