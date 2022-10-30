
from fastapi import HTTPException
from fastapi import APIRouter
from src.models.google import GoogleCoordinates
import validators
import src.lib.get_gps_data as get_gps_data


router = APIRouter(
    prefix="/geojson",
    tags=["Google Geojson"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def read_root():
    return {"Geojson Endpoint"}


@router.get("/raw")
async def read_root(googleCoordinates: GoogleCoordinates):
    modelInput = googleCoordinates.dict()

    if validators.url(modelInput['coord_link'].strip()) != True:
        raise HTTPException(
            status_code=404, detail="Coordinates URL is not valid.")

    response = get_gps_data.get_raw_gps_data_from_coords_file(
        modelInput['coord_link'])
    return response


@router.get("/clean")
async def read_root(googleCoordinates: GoogleCoordinates):
    modelInput = googleCoordinates.dict()

    if validators.url(modelInput['coord_link'].strip()) != True:
        raise HTTPException(
            status_code=404, detail="Coordinates URL is not valid.")

    response = get_gps_data.get_gps_data_from_coords_file(
        modelInput['coord_link'])
    return response
