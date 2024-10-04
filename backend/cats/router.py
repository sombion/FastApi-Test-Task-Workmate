from fastapi import APIRouter, HTTPException, status

from backend.cats.dao import CatsDAO
from backend.cats.schemas import SCats, SFilterCats
from backend.exceptions import CatInformationNotFoundException

router = APIRouter(
	prefix="/cats",
	tags=["Api работы с котами"]
)


@router.get("/all-name", name="Получение списка всех котят.")
async def all_name_cats() -> list[SCats]:
    result = await CatsDAO.find_all()
    return result

@router.get("/all-breed", name="Получение списка пород.")
async def all_breed_cats() -> list:
    result = await CatsDAO.find_all_breed_cats()
    return set(result)

@router.get("/filter", name="Получение списка котят определенной породы по фильтру.")
async def filter_breed_cats(breed: str) -> list:
    result = await CatsDAO.find_cats_by_breed(breed)
    return result

@router.get("/{id}", name="Получение подробной информации о котенке.")
async def filter_cats_id(id: int) -> dict:
    result = await CatsDAO.find_by_id(id)
    return result

@router.post("/add", name="Добавление информации о котенке.")
async def add_cats(cats_data: SCats) -> dict:
    await CatsDAO.add(
        name=cats_data.name, 
        age=cats_data.age, 
        breed=cats_data.breed,
		color=cats_data.color,
		description=cats_data.description
    )
    return {"message": "Информации о котенке успешна добавлена"}

@router.put("/edit", name="Изменение информации о котенке.")
async def edit_cats(filter_cats: SFilterCats, cats_data: SCats) -> dict:
    if not await CatsDAO.find_by_id(filter_cats.id):
        raise CatInformationNotFoundException
    
    await CatsDAO.edit_cats_from_id(
        filter_cats.id,
        cats_data.name,
        cats_data.breed,
        cats_data.age,
        cats_data.color,
        cats_data.description
    )
    return {"message": "Информации о котенке успешна обновлена"}
    
@router.delete("/delete", name="Удаление информации о котенке.")
async def del_cats(id: int) -> dict:
    if not await CatsDAO.find_by_id(id):
        raise CatInformationNotFoundException
    await CatsDAO.del_cats(id)
    return {"message": "Информации о котенке успешна удалена"}