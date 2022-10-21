# isort: skip_file
from fastapi import APIRouter

from . import quiz

root = APIRouter()
root.include_router(quiz.root)
