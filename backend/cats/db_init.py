from sqlalchemy import select

from backend.cats.dao import CatsDAO
from backend.cats.models import Cats
from backend.database import async_session_maker


async def init_db_data():
    async with async_session_maker() as session:
        result = await session.execute(select(Cats))
        if len(result.scalars().all()) == 0:
            await CatsDAO.add(
                name="Том", 
                age=3, 
                breed="Бурма",
                color="Серый",
                description="Очень игривый"
            )
            