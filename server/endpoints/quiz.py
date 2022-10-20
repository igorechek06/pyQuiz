from server import app
from models import Quiz
from fastapi import APIRouter

root = APIRouter(prefix="/quiz")


@root.get("/get")
async def get(id: int) -> Quiz:
    pass


@root.get("/find")
async def find(label: str) -> list[Quiz]:
    pass


@root.get("/count")
async def count() -> int:
    pass


@root.get("/all")
async def all(count: int, offset: int = 0) -> list[Quiz]:
    pass
