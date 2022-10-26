import validators
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Header, HTTPException
import src.get_gps_data as get_gps_data
from dotenv import load_dotenv
load_dotenv()

class CoordInput(BaseModel):
    key: int
    user_id: str
    coord_link: str

app = FastAPI(
    title="Custom YOLOV5 Machine Learning API",
    description="""Obtain object value out of image
    and return image and json result""",
    version="0.0.2",
)

origins = [
    "http://localhost",
    "http://localhost:8000",
    "https://amdcapstone.netlify.app/",
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"Geojson Utility API"}

@app.post("/fetchGPSData")
async def read_root(coordInput : CoordInput):
    modelInput = coordInput.dict()

    if modelInput['user_id'] == "":
        raise HTTPException(status_code=404, detail="User ID not found.")

    if modelInput['coord_link'] == "":
        raise HTTPException(status_code=404, detail="Video link and Coordinates link not found.")

    if validators.url(modelInput['coord_link'].strip()) != True:
            raise HTTPException(status_code=404, detail="Video link and Coordinates URL is not valid.")

    response = get_gps_data.get_gps_data_from_coords_file(modelInput['coord_link'])
    return response;