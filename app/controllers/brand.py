from sqlalchemy.orm import Session
from app.models.brand import Brand
from app.schemas.brand import BrandCreate
from app.schemas.brand import BrandUpdate


# Create
def create_brand(db: Session, brand: BrandCreate):
    db_brand = Brand(**brand.model_dump())
    db.add(db_brand)
    db.commit()
    db.refresh(db_brand)
    return db_brand


# Read
def get_brand(db: Session, brand_id: int):
    return db.query(Brand).filter(Brand.id == brand_id).first()


# Index
def get_brands(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Brand).offset(skip).limit(limit).all()


# Update
def update_brand(db: Session, brand_id: int, brand_update: BrandUpdate):
    db_brand = db.query(Brand).filter(Brand.id == brand_id).first()
    if db_brand:
        for key, value in brand_update.model_dump().items():
            setattr(db_brand, key, value)
        db.commit()
        db.refresh(db_brand)
    return db_brand


# Delete
def delete_brand(db: Session, brand_id: int):
    db_brand = db.query(Brand).filter(Brand.id == brand_id).first()
    if db_brand:
        db.delete(db_brand)
        db.commit()
        return True
    return False
