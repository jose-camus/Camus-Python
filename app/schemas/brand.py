from pydantic import BaseModel, Field, field_validator


class BrandBase(BaseModel):
    name: str


class BrandCreate(BrandBase):
    name: str = Field(..., min_length=1)

    @field_validator("name")
    def name_must_not_be_empty(cls, v):
        if not v.strip():
            raise ValueError("Name must not be empty")
        return v


class BrandUpdate(BrandBase):
    pass


class Brand(BrandBase):
    id: int

    class ConfigDict:
        orm_mode = True
