from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.controllers import ingredient as crud_ingredient
from app.schemas import ingredient as schema_ingredient
from app.database import get_db

router = APIRouter()

@router.post("/ingredients/", response_model=schema_ingredient.Ingredient)
def create_ingredient(ingredient: schema_ingredient.IngredientCreate, db: Session = Depends(get_db)):
    return crud_ingredient.create_ingredient(db=db, ingredient=ingredient)

@router.get("/ingredients/{ingredient_id}", response_model=schema_ingredient.Ingredient)
def read_ingredient(ingredient_id: int, db: Session = Depends(get_db)):
    db_ingredient = crud_ingredient.get_ingredient(db, ingredient_id=ingredient_id)
    if db_ingredient is None:
        raise HTTPException(status_code=404, detail="Ingredient not found")
    return db_ingredient

@router.get("/ingredients/", response_model=list[schema_ingredient.Ingredient])
def read_ingredients(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    ingredients = crud_ingredient.get_ingredients(db, skip=skip, limit=limit)
    return ingredients