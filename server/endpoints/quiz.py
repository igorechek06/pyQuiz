from json import loads

from fastapi import APIRouter, Header, HTTPException
from pydantic import BaseModel

import database as db
import models as m
import utils

root = APIRouter(prefix="/quiz")


class Quiz(BaseModel):
    label: str
    image_url: str | None = None
    questions: list[m.Question] = []


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


@root.get("/find")
async def find(
    offset: int = 0,
    limit: int = 10,
    label: str | None = None,
) -> list[m.Quiz]:
    with db.session.begin() as session:
        query = session.query(db.Quiz)

        if label is not None:
            query = query.filter(db.Quiz.label.like(f"%{label}%"))
        query = query.order_by(db.Quiz.id.desc()).offset(offset).limit(limit)

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
            for quiz in query.all()
        ]


@root.get("/count")
async def count(label: str | None = None) -> int:
    with db.session.begin() as session:
        query = session.query(db.Quiz)

        if label is not None:
            query = query.filter(db.Quiz.label.like(f"%{label}%"))

        return query.count()


@root.post("/add")
async def add(add: Quiz, x_token: str | None = Header(None)) -> m.Quiz:
    user = utils.auth(x_token)

    if not add.label:
        raise HTTPException(400, "Имя теста не может быть пустым")

    with db.session() as session:
        quiz = db.Quiz(
            owner_id=user.id,
            label=add.label,
            image_url=add.image_url,
            questions=[loads(q.json()) for q in add.questions],
        )
        session.add(quiz)

        session.commit()

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


@root.put("/update")
async def update(id: int, update: Quiz, x_token: str | None = Header(None)) -> m.Quiz:
    user = utils.auth(x_token)

    if not update.label:
        raise HTTPException(400, "Имя теста не может быть пустым")

    with db.session() as session:
        quiz = session.get(db.Quiz, id)

        if quiz is None:
            raise HTTPException(404, "Тест не найден")
        if quiz.owner.id != user.id:
            raise HTTPException(405, "Ты не владеешь данным тестом")

        quiz.label = update.label
        quiz.image_url = update.image_url
        quiz.questions = [loads(q.json()) for q in update.questions]

        session.commit()

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


@root.delete("/delete")
async def delete(id: int, x_token: str | None = Header(None)) -> None:
    user = utils.auth(x_token)
    with db.session.begin() as session:
        quiz = session.get(db.Quiz, id)

        if quiz is None:
            raise HTTPException(404, "Тест не найден")
        if quiz.owner.id != user.id:
            raise HTTPException(405, "Ты не владеешь данным тестом")

        session.delete(quiz)
