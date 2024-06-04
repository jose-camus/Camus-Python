from pydantic import BaseModel

class IngredientBase(BaseModel):
    name: str
    calories: float
    protein: float
    carbohydrates: float
    fats: float

class IngredientCreate(IngredientBase):
    pass

class Ingredient(IngredientBase):
    id: int

    class Config:
        orm_mode = True