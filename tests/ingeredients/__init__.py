import os
from fastapi.testclient import TestClient
from app.main import app

# Cargar las variables de entorno desde el archivo .env
from dotenv import load_dotenv
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '..', '..', '.env'))

client = TestClient(app)

def test_create_ingredient():
    response = client.post("/ingredients/", json={"name": "Test Ingredient", "quantity": 10})
    assert response.status_code == 200
    assert response.json()["name"] == "Test Ingredient"
    assert response.json()["quantity"] == 10

def test_read_ingredient():
    response = client.get("/ingredients/1")
    assert response.status_code == 200
    assert response.json()["name"] == "Test Ingredient"
    assert response.json()["quantity"] == 10


def test_update_ingredient():
    response = client.put("/ingredients/1", json={"name": "Updated Ingredient", "quantity": 20})
    assert response.status_code == 200
    assert response.json()["name"] == "Updated Ingredient"
    assert response.json()["quantity"] == 20

def test_delete_ingredient():
    response = client.delete("/ingredients/1")
    assert response.status_code == 200
    assert response.json() == {"message": "Ingredient deleted"}