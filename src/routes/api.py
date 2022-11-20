from fastapi import APIRouter
from src.endpoints import google

router = APIRouter()
router.include_router(google.router)