import pytest

from backend.cats.dao import CatsDAO


@pytest.mark.parametrize("name,age,breed,color,description", [
    ("Тимофей", 2, "Британец", "Серый", "Обожает спать на подушках"),
    ("Лео",  1, "Абиссинец", "Рыжий", "Любознательный и активный"),
    ("Василий", 3, "Экзот", "Коричневый", "Умеет выполнять команды")
])
async def test_add_cats(name, age, breed, color, description):
    new_cat = await CatsDAO.add(
        name=name, 
        age=age, 
        breed=breed,
		color=color,
		description=description
    )

    new_cat_id = await CatsDAO.find_by_id(new_cat.id)
    
    assert new_cat_id is not None
    
@pytest.mark.parametrize("id,name,age,breed,color,description", [
    (6, "Тимофей", 2, "Британец", "Серый", "Обожает спать на подушках"),
    (2, "Лео",  1, "Абиссинец", "Рыжий", "Любознательный и активный"),
    (3, "Василий", 3, "Экзот", "Коричневый", "Умеет выполнять команды")
])
async def test_edit_cats(id, name, age, breed, color, description):
    edit_cat = await CatsDAO.edit_cats_from_id(
        id=id,
        name=name, 
        age=age, 
        breed=breed,
		color=color,
		description=description
    )

    edit_cat = await CatsDAO.find_by_id(id)
    
    assert edit_cat.id == id
    assert edit_cat.name == name 
    assert edit_cat.age == age 
    assert edit_cat.breed == breed
    assert edit_cat.color == color
    assert edit_cat.description == description