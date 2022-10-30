# isort: skip_file
from fastapi import APIRouter

from . import user
from . import quiz
from . import answer

root = APIRouter()
root.include_router(user.root)
root.include_router(quiz.root)
root.include_router(answer.root)
