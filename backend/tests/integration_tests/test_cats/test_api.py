import pytest
from httpx import AsyncClient


@pytest.mark.parametrize("name,breed,age,color,description,status_code", [
    ("Барсик", "Мейн-кун", 4, "Черный", "Любит играть с игрушками", 200),
    ("Шарик", "Абиссинская", -2, "Белый", "Любит молоко", 422),
    ("Мурзик", "Сиамский", 2, "Белый", "Спокойный и ласковый", 200)
])
async def test_add_cats(name, breed, age, color, description, status_code, ac: AsyncClient):
    response = await ac.post("/cats/add", json={
        "name": name,
        "breed": breed,
        "age": age,
        "color": color,
        "description": description
    })
    
    assert response.status_code == status_code

@pytest.mark.parametrize("id,status_code", [
    (1, 200),
    (20, 404),
])
async def test_del_cats(id, status_code, ac: AsyncClient):
    response = await ac.delete("/cats/delete", params={"id": id})
    assert response.status_code == status_code