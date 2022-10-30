from pydantic import BaseModel, validator
from typing import Optional

class GoogleCoordinates(BaseModel):
    user_id: str
    coord_link: str
    
    
    @validator("user_id", pre=True, always=True)
    def check_id(cls, id):
        assert id != '', "ID cannot be empty."
        return id
    
    @validator("coord_link", pre=True, always=True)
    def check_coordinates_link(cls, coordinates_link):
        assert coordinates_link != '', "Coordinates Link cannot be empty."
        return coordinates_link