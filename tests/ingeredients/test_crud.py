import pytest
from pytest import raises
from pydantic import ValidationError
from app.schemas.ingredient import IngredientCreate
from app.controllers.ingredient import (
    get_ingredient,
    get_ingredients,
    create_ingredient,
)


def test_create_ingredient(client, db):
    ingredient_data = IngredientCreate(
        name="Tomato", calories=15, protein=1, carbohydrates=5, fats=0.5
    )
    ingredient = create_ingredient(db, ingredient_data)
    assert ingredient.name == "Tomato"
    assert ingredient.calories == 15
    assert ingredient.protein == 1
    assert ingredient.carbohydrates == 5
    assert ingredient.fats == 0.5


def test_create_ingredient_invalid_data(client, db):
    with pytest.raises(ValidationError):
        ingredient_data = IngredientCreate(
            name="", calories=-10, protein=-1, carbohydrates=-5, fats=-0.5
        )
        create_ingredient(db, ingredient_data)


def test_name_must_not_be_empty():
    with raises(ValueError):
        IngredientCreate(name="")
        assert IngredientCreate(name="Non-empty name").name == "Non-empty name"


def test_get_ingredient(client, db):
    ingredient_data = IngredientCreate(
        name="Tomato", calories=15, protein=1, carbohydrates=5, fats=0.5
    )
    created_ingredient = create_ingredient(db, ingredient_data)
    fetched_ingredient = get_ingredient(db, created_ingredient.id)
    assert fetched_ingredient.id == created_ingredient.id
    assert fetched_ingredient.name == created_ingredient.name


def test_get_ingredient_not_found(client, db):
    fetched_ingredient = get_ingredient(db, 9999)
    assert fetched_ingredient is None


def test_get_ingredients(client, db):
    ingredient_data1 = IngredientCreate(
        name="Tomato", calories=15, protein=1, carbohydrates=5, fats=0.5
    )
    ingredient_data2 = IngredientCreate(
        name="Potato", calories=75, protein=1, carbohydrates=17, fats=0.1
    )
    create_ingredient(db, ingredient_data1)
    create_ingredient(db, ingredient_data2)
    ingredients = get_ingredients(db)
    assert len(ingredients) >= 2
    assert any(ingredient.name == "Tomato" for ingredient in ingredients)
    assert any(ingredient.name == "Potato" for ingredient in ingredients)


def test_get_ingredients_with_pagination(client, db):
    ingredient_data1 = IngredientCreate(
        name="Tomato", calories=15, protein=1, carbohydrates=5, fats=0.5
    )
    ingredient_data2 = IngredientCreate(
        name="Potato", calories=75, protein=1, carbohydrates=17, fats=0.1
    )
    create_ingredient(db, ingredient_data1)
    create_ingredient(db, ingredient_data2)
    ingredients = get_ingredients(db, skip=1, limit=1)
    assert len(ingredients) == 1


def test_create_and_get_ingredient(client, db):
    ingredient_data = IngredientCreate(
        name="Tomato", calories=15, protein=1, carbohydrates=5, fats=0.5
    )
    created_ingredient = create_ingredient(db, ingredient_data)
    fetched_ingredient = get_ingredient(db, created_ingredient.id)
    assert fetched_ingredient.id == created_ingredient.id
    assert fetched_ingredient.name == created_ingredient.name
    assert fetched_ingredient.calories == created_ingredient.calories
    assert fetched_ingredient.protein == created_ingredient.protein
    assert fetched_ingredient.carbohydrates == created_ingredient.carbohydrates
    assert fetched_ingredient.fats == created_ingredient.fats
