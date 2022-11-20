
from fastapi import HTTPException
from fastapi import APIRouter
from src.models.google import GoogleCoordinates, GoogleVideoCoordinates
import validators
import src.utils.get_gps_data as get_gps_data
import src.utils.firebase as firebase
import src.utils.gdownload_util as gdownload

googleFirebase = firebase.GoogleFirebase()

router = APIRouter(
    prefix="/geojson",
    tags=["Google Geojson"],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
async def read_root():
    return {"Geojson Endpoint"}

@router.post("/raw")
async def read_root(googleCoordinates: GoogleCoordinates):
    modelInput = googleCoordinates.dict()
    if validators.url(modelInput['coord_link'].strip()) != True:
        raise HTTPException(
            status_code=404, detail="Coordinates URL is not valid.")
    response = get_gps_data.get_raw_gps_data_from_coords_file(
        modelInput['coord_link'])
    return response


@router.post("/clean")
async def read_root(googleCoordinates: GoogleCoordinates):
    modelInput = googleCoordinates.dict()
    if validators.url(modelInput['coord_link'].strip()) != True:
        raise HTTPException(
            status_code=404, detail="Coordinates URL is not valid.")
    response = get_gps_data.get_gps_data_from_coords_file(
        modelInput['coord_link'])
    return response

@router.post("/machinelearning")
async def read_root(googleVideoCoordinates: GoogleVideoCoordinates):
    modelInput = googleVideoCoordinates.dict()
    if validators.url(modelInput['video_link'].strip()) != True:
        raise HTTPException(
            status_code=404, detail="Video URL is not valid.")
    if validators.url(modelInput['coord_link'].strip()) != True:
        raise HTTPException(
            status_code=404, detail="Coordinates URL is not valid.")
    response = get_gps_data.get_gps_data_from_coords_file(
        modelInput['coord_link'])
    return response


@router.post("/save")
async def read_root(googleCoordinates: GoogleCoordinates):
    modelInput = googleCoordinates.dict()
    if validators.url(modelInput['coord_link'].strip()) != True:
        raise HTTPException(
            status_code=404, detail="Coordinates URL is not valid.")
    response = get_gps_data.get_gps_data_from_coords_file(
        modelInput['coord_link'])
    
    file_id = gdownload.get_file_id_from_raw_url(modelInput['coord_link'])
    googleFirebase.set_user_id(modelInput['user_id'])
    googleFirebase.get_firebase_users_geojson_collection()
    googleFirebase.save_geojson_to_user_collection(file_id, response)
    
    return response