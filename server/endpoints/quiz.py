from json import loads

from fastapi import APIRouter, Header, HTTPException
from pydantic import BaseModel
from sqlalchemy import and_, or_
from sqlalchemy.orm import Session

import database as db
import models as m
import utils

root = APIRouter(prefix="/quiz")


class Quiz(BaseModel):
    label: str
    image_url: str | None = None
    questions: list[m.Question] = []


def has_answers(session: Session, user_id: int, quiz_id: int) -> bool:
    return (
        session.query(db.Answers)
        .filter(
            and_(
                db.Answers.quiz_id == quiz_id,
                or_(
                    db.Answers.answerer_id == user_id,
                    db.Answers.quiz.has(db.Quiz.owner_id == user_id),
                ),
            )
        )
        .count()
        >= 1
    )


@root.get("/get/{id}")
async def get(id: int, x_token: str | None = Header(None)) -> m.Quiz | None:
    if x_token is not None:
        user = utils.auth(x_token)
    else:
        user = None

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
                has_answers=has_answers(session, user.id, quiz.id)
                if user is not None
                else False,
                questions=quiz.questions,
            )
        else:
            return None


@root.get("/answers/{id}")
async def answers(id: int, x_token: str | None = Header(None)) -> list[m.QuizAnswers]:
    user = utils.auth(x_token)

    with db.session.begin() as session:
        quiz = session.get(db.Quiz, id)

        query = session.query(db.Answers).filter(db.Answers.quiz_id == id)
        my_answers = query.filter(db.Answers.answerer_id == user.id)
        other_answers = query.filter(
            and_(
                db.Answers.quiz.has(db.Quiz.owner_id == user.id),
                db.Answers.answerer_id != user.id,
            )
        )

        if quiz is None:
            raise HTTPException(404, "Опрос не найден")

        return [
            m.QuizAnswers(
                id=a.id,
                quiz_id=a.quiz_id,
                answerer=m.User(
                    id=a.answerer_id,
                    username=a.answerer.username,
                ),
                questions=a.questions,
            )
            for a in my_answers.all() + other_answers.all()
        ]


@root.get("/find")
async def find(
    offset: int = 0,
    limit: int = 10,
    label: str | None = None,
    x_token: str | None = Header(None),
) -> list[m.Quiz]:
    if x_token is not None:
        user = utils.auth(x_token)
    else:
        user = None

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
                has_answers=has_answers(session, user.id, quiz.id)
                if user is not None
                else False,
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
        raise HTTPException(400, "Имя опроса не может быть пустым")

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
            has_answers=has_answers(session, user.id, quiz.id),
            questions=quiz.questions,
        )


@root.put("/update")
async def update(id: int, update: Quiz, x_token: str | None = Header(None)) -> m.Quiz:
    user = utils.auth(x_token)

    if not update.label:
        raise HTTPException(400, "Имя опроса не может быть пустым")

    with db.session() as session:
        quiz = session.get(db.Quiz, id)

        if quiz is None:
            raise HTTPException(404, "Опрос не найден")
        if quiz.owner_id != user.id:
            raise HTTPException(405, "Вы не владеете данным опросом")

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
            has_answers=has_answers(session, user.id, quiz.id),
            questions=quiz.questions,
        )


@root.delete("/delete")
async def delete(id: int, x_token: str | None = Header(None)) -> None:
    user = utils.auth(x_token)
    with db.session.begin() as session:
        quiz = session.get(db.Quiz, id)

        if quiz is None:
            raise HTTPException(404, "Опрос не найден")
        if quiz.owner_id != user.id:
            raise HTTPException(405, "Вы не владеете данным опросом")

        session.delete(quiz)
