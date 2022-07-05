from beanie import init_beanie
import motor.motor_asyncio

from app.server.models.ts_test import WeatherTS


async def init_db():
    client = motor.motor_asyncio.AsyncIOMotorClient(
        "mongodb://localhost:27017/weather"
    )

    await init_beanie(database=client.weather, document_models=[WeatherTS])
