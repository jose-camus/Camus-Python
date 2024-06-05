from sqlalchemy.orm import Session
from app.models.ingredient import Ingredient
from app.schemas.ingredient import IngredientCreate


def get_ingredient(db: Session, ingredient_id: int):
    return db.query(Ingredient).filter(Ingredient.id == ingredient_id).first()


def get_ingredients(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Ingredient).offset(skip).limit(limit).all()


def create_ingredient(db: Session, ingredient: IngredientCreate):
    db_ingredient = Ingredient(**ingredient.dict())
    db.add(db_ingredient)
    db.commit()
    db.refresh(db_ingredient)
    return db_ingredient
