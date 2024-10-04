from fastapi import FastAPI

from backend.cats.router import router as router_cast

app = FastAPI()

app.include_router(router_cast)