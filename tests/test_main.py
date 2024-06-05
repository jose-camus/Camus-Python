import os
import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.database import Base, get_db, DATABASE_URL
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

engine = create_engine(DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "..", ".env"))

client = TestClient(app)


def test_read_root():
    """Test the root path ('/') response."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}
