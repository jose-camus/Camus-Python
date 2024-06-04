from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.controllers import ingredient as crud_ingredient
from app.schemas import ingredient as schema_ingredient
from app.database import get_db

router = APIRouter()

@router.get("/")
def read_root():
    return {"Hello": "World"}