import pytest

from backend.cats.dao import CatsDAO


@pytest.mark.parametrize("id,name,exists", [
    (4, "Снежок", True),
    (5, "Лео", True),
    (10, "...", False)
])
async def test_find_cats_by_id(id, name, exists):
    cat = await CatsDAO.find_by_id(id)
    
    if exists:
        assert cat
        assert cat.id == id
        assert cat.name == name
    else:
        assert not cat