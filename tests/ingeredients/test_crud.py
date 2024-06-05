import os
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

from app.main import app
from app.database import Base, get_db, DATABASE_URL
from app.models.ingredient import Ingredient
from app.schemas.ingredient import IngredientCreate
from app.controllers.ingredient import get_ingredient, get_ingredients, create_ingredient


engine = create_engine(DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "..", "..", ".env"))

client = TestClient(app)

# Dependencia de la base de datos para pruebas
def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

@pytest.fixture(scope="module")
def setup_database():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)


@pytest.fixture(scope="function")
def db_session():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


def test_create_ingredient(db_session):
    ingredient_data = IngredientCreate(name="Tomato", calories=15, protein=1, carbohydrates=5, fats=0.5)
    ingredient = create_ingredient(db_session, ingredient_data)
    assert ingredient.name == "Tomato"
    assert ingredient.calories > 0


def test_get_ingredient(db_session):
    ingredient_data = IngredientCreate(name="Tomato", calories=15, protein=1, carbohydrates=5, fats=0.5)
    created_ingredient = create_ingredient(db_session, ingredient_data)
    fetched_ingredient = get_ingredient(db_session, created_ingredient.id)
    assert fetched_ingredient.id == created_ingredient.id
    assert fetched_ingredient.name == created_ingredient.name


def test_get_ingredients(db_session):
    ingredient_data1 = IngredientCreate(name="Tomato", calories=15, protein=1, carbohydrates=5, fats=0.5)
    ingredient_data2 = IngredientCreate(name="Potato", calories=75, protein=1, carbohydrates=17, fats=0.1)
    create_ingredient(db_session, ingredient_data1)
    create_ingredient(db_session, ingredient_data2)
    ingredients = get_ingredients(db_session)
    assert len(ingredients) >= 2
    assert any(ingredient.name == "Tomato" for ingredient in ingredients)
    assert any(ingredient.name == "Potato" for ingredient in ingredients)