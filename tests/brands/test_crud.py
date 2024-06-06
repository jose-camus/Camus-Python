import pytest
from pytest import raises
from pydantic import ValidationError
from fastapi import HTTPException
from app.schemas.brand import BrandCreate
from app.schemas.brand import BrandUpdate
from app.controllers.brand import (
    get_brand,
    get_brands,
    create_brand,
    update_brand,
    delete_brand,
)


def test_create_brand(client, db):
    brand_data = BrandCreate(name="Camus")
    brand = create_brand(db, brand_data)
    assert brand.name == "Camus"


def test_create_brand_invalid_data(client, db):
    with pytest.raises(ValidationError):
        brand_data = BrandCreate(name="")
        create_brand(db, brand_data)


def test_name_must_not_be_empty():
    with raises(ValueError):
        BrandCreate(name="")
        assert BrandCreate(name="Non-empty name").name == "Non-empty name"


def test_get_brand(client, db):
    brand_data = BrandCreate(name="Camus")
    created_brand = create_brand(db, brand_data)
    fetched_brand = get_brand(db, created_brand.id)
    assert fetched_brand.id == created_brand.id
    assert fetched_brand.name == created_brand.name


def test_get_brand_not_found(client, db):
    fetched_brand = get_brand(db, 9999)
    assert fetched_brand is None


def test_get_brands(client, db):
    brand_data1 = BrandCreate(name="Camus")
    brand_data2 = BrandCreate(name="Godoy")
    create_brand(db, brand_data1)
    create_brand(db, brand_data2)
    brands = get_brands(db)
    assert len(brands) >= 2
    assert any(brand.name == "Camus" for brand in brands)
    assert any(brand.name == "Godoy" for brand in brands)


def test_get_brands_with_pagination(client, db):
    brand_data1 = BrandCreate(name="Camus")
    brand_data2 = BrandCreate(name="Godoy")
    create_brand(db, brand_data1)
    create_brand(db, brand_data2)
    brands = get_brands(db, skip=1, limit=1)
    assert len(brands) == 1


def test_create_and_get_brand(client, db):
    brand_data = BrandCreate(name="Camus")
    created_brand = create_brand(db, brand_data)
    fetched_brand = get_brand(db, created_brand.id)
    assert fetched_brand.id == created_brand.id
    assert fetched_brand.name == created_brand.name


def test_update_brand(client, db):
    initial_brand_data = BrandCreate(name="Camus")
    created_brand = create_brand(db, initial_brand_data)

    updated_brand_data = BrandUpdate(name="Updated Camus")
    updated_brand = update_brand(
        db, brand_id=created_brand.id, brand_update=updated_brand_data
    )

    assert updated_brand.id == created_brand.id
    assert updated_brand.name == updated_brand_data.name


def test_update_brand_not_found(client, db):
    with pytest.raises(HTTPException) as exc_info:
        update_brand(
            db, brand_id=9999, brand_update=BrandUpdate(name="Updated Brand Name")
        )

    assert "Brand not found" in exc_info.value.detail
    assert exc_info.value.status_code == 404


def test_delete_brand(client, db):
    brand_data = BrandCreate(name="Camus")
    created_brand = create_brand(db, brand_data)

    success = delete_brand(db, brand_id=created_brand.id)
    assert success is True

    assert get_brand(db, brand_id=created_brand.id) is None


def test_delete_brand_not_found(client, db):
    success = delete_brand(db, brand_id=9999)
    assert success is False
