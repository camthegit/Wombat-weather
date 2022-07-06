from beanie import PydanticObjectId
from fastapi import APIRouter, HTTPException
from typing import List

from app.server.models.ts_test import WeatherTS, WeatherAGG

router = APIRouter()


@router.post("/", response_description="Observations added to the database")
async def add_observation(data: WeatherTS) -> dict:
    await data.create()
    return {"message": "Data added successfully"}


@router.get("/{id}", response_description="Weather record retrieved")
async def get_obs_record(id: PydanticObjectId) -> WeatherTS:
    observation = await WeatherTS.get(id)
    return observation


@router.get("/", response_description="Weather records retrieved")
async def get_obs() -> List[WeatherTS]:
    observations = await WeatherTS.find_all().to_list()
    return observations


@router.get("/agg/", response_description="Summary record retrieved")
async def get_obs_aggregate() -> List[WeatherAGG]:
    observations = await WeatherTS.aggregate([
        {
            "$project": {
                "date": {"$dateToParts": {"date": "$ts"}
                         },
                "temp": 1,
                "humidity": 1,
                "source.location": 1
            }
        },
        {"$group": {
            "_id": {
                "year": "$date.year",
                "month": "$date.month",
                "day": "$date.day",
                "hour": "$date.hour",
                "location": "$source.location"
            },
            "avgTemp": {"$avg": "$temp"},
            "maxTemp": {"$max": "$temp"},
            "avgHumidity": {"$avg": "$humidity"}
        }}
    ]).to_list()
    return observations


