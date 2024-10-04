from sqlalchemy import delete, select, update

from backend.cats.models import Cats
from backend.dao.base import BaseDAO
from backend.database import async_session_maker


class CatsDAO(BaseDAO):
    model = Cats
        
    @classmethod
    async def find_all_breed_cats(cls):
        async with async_session_maker() as session:
            query = select(cls.model.breed)
            result = await session.execute(query)
            return result.scalars().all()
        
    @classmethod
    async def find_cats_by_breed(cls, breed: str):
        async with async_session_maker() as session:
            query = select(cls.model.name).filter(cls.model.breed.ilike(f"%{breed}%"))
            result = await session.execute(query)
            return result.scalars().all()
    
    @classmethod
    async def edit_cats_from_id(
            cls, 
            id: int, 
            name: str, 
            breed: str, 
            age: int, 
            color: str, 
            description: str
        ):
        async with async_session_maker() as session:
            stmt = update(cls.model).where(cls.model.id == id).values(
				name=name,
				breed=breed,
				age=age,
				color=color,
				description=description
			)
            await session.execute(stmt)
            await session.commit()
    
    @classmethod
    async def del_cats(cls, id: int):
        async with async_session_maker() as session:
            stmt = delete(cls.model).where(cls.model.id == id)
            await session.execute(stmt)
            await session.commit()