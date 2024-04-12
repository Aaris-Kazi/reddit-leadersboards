import asyncio
import logging as log
from fastapi import FastAPI

from AppConstants.constants import DEFAULT_OFFSET, LIMIT
from requestmodels import UserSubredditRequest
from utility.database import SessionLocal, ENGINE, BASE
from utility.fetchReddit import deleteData, fetchAllData, fetchData, insertUpdateData
from utility.models import UserBases


status:dict = {"status": "success"}

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

BASE.metadata.create_all(bind=ENGINE)

@app.get("/health")
async def index():
    return status


@app.get("/users/{page_number}")
async def get_users(page_number: int= 1):
    try:
        offset:int = ((page_number * LIMIT) - LIMIT) + DEFAULT_OFFSET
        print(offset)
        result: dict = await fetchData(offset)
        return result
    except Exception as e:
        log.error(e)
        print(e)


@app.get("/users")
async def get_all_users():
    try:
        result: dict = await fetchData()
        return result
    except Exception as e:
        log.error(e)
        print(e)


@app.post("/users")
async def set_user(data: UserSubredditRequest):
    try:
        asyncio.ensure_future(insertUpdateData(data.subreddit))
    except Exception as e:
        log.error(e)
        print(e)
    return status


@app.put("/users/{name}")
async def update_user(name: str):
    try:
        asyncio.ensure_future(insertUpdateData(name))
    except Exception as e:
        log.error(e)
        print(e)
    return status


@app.delete("/users/{id}")
async def update_user(id: str):
    try:
        asyncio.ensure_future(deleteData(id))
    except Exception as e:
        log.error(e)
        print(e)
    return status


@app.get("/users_all/")
async def get_all_users_rank():
    try:
        result: dict = await fetchAllData()
        return result
    except Exception as e:
        log.error(e)
        print(e)