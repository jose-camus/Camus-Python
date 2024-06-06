from fastapi import FastAPI
from app.routers import router
from app.routers import ingredient
from app.routers import brand
from app.database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(router)
app.include_router(ingredient.router, prefix="/api/v1")
app.include_router(brand.router, prefix="/api/v1")
