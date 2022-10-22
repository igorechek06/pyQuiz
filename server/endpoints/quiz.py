from fastapi import APIRouter, Request
from sqlalchemy import and_

import database as db
import models as m

root = APIRouter(prefix="/quiz")


@root.get("/get")
async def get(id: int) -> m.Quiz | None:
    with db.session.begin() as session:
        quiz: db.Quiz = session.query(db.Quiz).get(id)
        if quiz is not None:
            return m.Quiz(
                id=quiz.id,
                label=quiz.label,
                hidden=quiz.hidden,
                image_url=quiz.image_url,
                questions=quiz.questions,
            )


@root.post("/add")
async def add(request: Request) -> None:
    quiz = m.Quiz.parse_obj(await request.json())
    with db.session.begin() as session:
        session.add(db.Quiz(**quiz.dict()))


@root.get("/all")
async def all(count: int, offset: int = 0) -> list[m.Quiz]:
    with db.session.begin() as session:
        quizzes: list[db.Quiz] = (
            session.query(db.Quiz)
            .filter(db.Quiz.hidden.is_(False))
            .limit(count)
            .offset(offset)
            .all()
        )
        return [
            m.Quiz(
                id=quiz.id,
                label=quiz.label,
                hidden=quiz.hidden,
                image_url=quiz.image_url,
                questions=quiz.questions,
            )
            for quiz in quizzes
        ]


@root.get("/find")
async def find(label: str, count: int, offset: int = 0) -> list[m.Quiz]:
    with db.session.begin() as session:
        quizzes: list[db.Quiz] = (
            session.query(db.Quiz)
            .filter(and_(db.Quiz.label.like(f"%{label}%"), db.Quiz.hidden.is_(False)))
            .limit(count)
            .offset(offset)
            .all()
        )
        return [
            m.Quiz(
                id=quiz.id,
                label=quiz.label,
                hidden=quiz.hidden,
                image_url=quiz.image_url,
                questions=quiz.questions,
            )
            for quiz in quizzes
        ]


@root.get("/count")
async def count(label: str | None = None) -> int:
    with db.session.begin() as session:
        if label is None:
            return session.query(db.Quiz).filter(db.Quiz.hidden.is_(False)).count()
        else:
            return (
                session.query(db.Quiz)
                .filter(and_(db.Quiz.label.like(f"%{label}%"), db.Quiz.hidden.is_(False)))
                .count()
            )
