from beanie import PydanticObjectId
from fastapi import APIRouter, HTTPException
from typing import List

from app.server.models.ts_test import WeatherTS

router = APIRouter()


@router.post("/", response_description="Observations added to the database")
async def add_product_review(data: WeatherTS) -> dict:
    await data.create()
    return {"message": "Data added successfully"}
