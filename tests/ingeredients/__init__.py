import os
from fastapi.testclient import TestClient
from app.main import app
from dotenv import load_dotenv

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "..", "..", ".env"))

client = TestClient(app)


def test_create_ingredient():
    ingredient_data = {"name": "Test Ingredient", "quantity": 10}

    response = client.post("/ingredients/", json=ingredient_data)
    assert response.status_code == 200
    assert response.json()["name"] == "Test Ingredient"
    assert response.json()["quantity"] == 10


def test_read_ingredient():
    response = client.get("/ingredients/1")
    assert response.status_code == 200
    assert response.json()["name"] == "Test Ingredient"
    assert response.json()["quantity"] == 10


def test_update_ingredient():
    updated_ingredient_data = {"name": "Updated Ingredient", "quantity": 20}
    response = client.put("/ingredients/1", json=updated_ingredient_data)
    assert response.status_code == 200
    assert response.json()["name"] == "Updated Ingredient"
    assert response.json()["quantity"] == 20


def test_delete_ingredient():
    response = client.delete("/ingredients/1")
    assert response.status_code == 200
    assert response.json() == {"message": "Ingredient deleted"}
