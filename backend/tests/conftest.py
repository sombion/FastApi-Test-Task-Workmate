import asyncio
import json

import pytest
from fastapi.testclient import TestClient
from httpx import ASGITransport, AsyncClient
from sqlalchemy import insert

from backend.cats.models import Cats
from backend.config import settings
from backend.database import Base, async_session_maker, engine
from backend.main import app as fastapi_app


@pytest.fixture(scope="session", autouse=True)
async def prepare_database():
    assert settings.MODE == "TEST"
    
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
        
    def open_mock_json(model: str):
        with open(f"backend/tests/mock_{model}.json", "r") as file:
            return json.load(file)
    
    cats = open_mock_json("cats")
    
    async with async_session_maker() as session:
        add_cats = insert(Cats).values(cats)
        await session.execute(add_cats)
        await session.commit()
    

@pytest.mark.asyncio(scope="function")
def event_loop(request):
    """Create an instance of the default event loop for each test case."""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()
    

@pytest.fixture(scope="function")
async def ac():
    transport = ASGITransport(app=fastapi_app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        yield ac
        
