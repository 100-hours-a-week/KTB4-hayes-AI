from contextlib import asynccontextmanager

from fastapi import FastAPI

from community_api.database import create_db_and_tables
from community_api.routers import comments, posts


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(posts.router)
app.include_router(comments.router)


@app.get("/")
async def root():
    return {"message": "server is running"}
