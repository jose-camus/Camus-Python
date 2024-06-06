from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.controllers import brand as crud_brand
from app.schemas import brand as schema_brand
from app.database import get_db

router = APIRouter()


@router.post("/brands/", response_model=schema_brand.Brand)
def create_brand(brand: schema_brand.BrandCreate, db: Session = Depends(get_db)):
    return crud_brand.create_brand(db=db, brand=brand)


@router.get("/brands/{brand_id}", response_model=schema_brand.Brand)
def read_brand(brand_id: int, db: Session = Depends(get_db)):
    db_brand = crud_brand.get_brand(db, brand_id=brand_id)
    if db_brand is None:
        raise HTTPException(status_code=404, detail="Brand not found")
    return db_brand


@router.get("/brands/", response_model=list[schema_brand.Brand])
def read_brands(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    brands = crud_brand.get_brands(db, skip=skip, limit=limit)
    return brands


@router.put("/brands/{brand_id}", response_model=schema_brand.Brand)
def update_brand(
    brand_id: int, brand: schema_brand.BrandUpdate, db: Session = Depends(get_db)
):
    db_brand = crud_brand.update_brand(db, brand_id=brand_id, brand_update=brand)
    if db_brand is None:
        raise HTTPException(status_code=404, detail="Brand not found")
    return db_brand


@router.delete("/brands/{brand_id}", response_model=bool)
def delete_brand(brand_id: int, db: Session = Depends(get_db)):
    success = crud_brand.delete_brand(db, brand_id=brand_id)
    if not success:
        raise HTTPException(status_code=404, detail="Brand not found")
    return True
