from pydantic import BaseModel, Field, field_validator


class IngredientBase(BaseModel):
    name: str
    calories: float
    protein: float
    carbohydrates: float
    fats: float


class IngredientCreate(IngredientBase):
    name: str = Field(..., min_length=1)
    calories: float = Field(..., ge=0)
    protein: float = Field(..., ge=0)
    carbohydrates: float = Field(..., ge=0)
    fats: float = Field(..., ge=0)

    @field_validator("name")
    def name_must_not_be_empty(cls, v):
        if not v.strip():
            raise ValueError("Name must not be empty")
        return v


class Ingredient(IngredientBase):
    id: int

    class ConfigDict:
        from_attributes = True
