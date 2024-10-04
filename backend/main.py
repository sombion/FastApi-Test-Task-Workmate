from fastapi import FastAPI
from fastapi.concurrency import asynccontextmanager

from backend.cats.db_init import init_db_data
from backend.cats.router import router as router_cast


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db_data()
    yield

app = FastAPI(lifespan=lifespan)

app.include_router(router_cast)