from typing import NewType

from fastapi import APIRouter, HTTPException, Request

import database as db
import models as m
import utils

root = APIRouter(prefix="/quiz")


@root.get("/get/{id}")
async def get(id: int) -> m.Quiz | None:
    with db.session.begin() as session:
        quiz = session.get(db.Quiz, id)
        if quiz is not None:
            return m.Quiz(
                id=quiz.id,
                owner=m.User(
                    id=quiz.owner.id,
                    username=quiz.owner.username,
                ),
                label=quiz.label,
                image_url=quiz.image_url,
                questions=quiz.questions,
            )
        else:
            return None


@root.post("/add")
async def add(
    request: Request,
    label: str,
    image_url: str | None = None,
    questions: list[m.Question] = [],
) -> None:
    user = utils.auth(request)
    with db.session.begin() as session:
        session.add(
            db.Quiz(
                owner_id=user.id,
                label=label,
                image_url=image_url,
                questions=questions,
            )
        )


@root.delete("/delete")
async def delete(request: Request, id: int) -> None:
    user = utils.auth(request)
    with db.session.begin() as session:
        quiz = session.get(db.Quiz, id)
        if quiz is None:
            raise HTTPException(404, "Тест не найден")
        if quiz.owner.id != user.id:
            raise HTTPException(405, "Ты не владеешь данным тестом")
        session.delete(quiz)


# TODO: /update/*


@root.get("/find")
async def find(
    label: str = "",
    offset: int = 0,
    limit: int = 10,
) -> list[m.Quiz]:
    with db.session.begin() as session:
        return [
            m.Quiz(
                id=quiz.id,
                owner=m.User(
                    id=quiz.owner.id,
                    username=quiz.owner.username,
                ),
                label=quiz.label,
                image_url=quiz.image_url,
                questions=quiz.questions,
            )
            for quiz in session.query(db.Quiz)
            .filter(db.Quiz.label.like(f"%{label}%"))
            .offset(offset)
            .limit(limit)
            .all()
        ]


@root.get("/count")
async def count(label: str = "") -> int:
    with db.session.begin() as session:
        return session.query(db.Quiz).filter(db.Quiz.label.like(f"%{label}%")).count()
