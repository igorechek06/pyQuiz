from json import loads

from fastapi import APIRouter, Header, HTTPException
from pydantic import BaseModel

import database as db
import models as m
import utils

root = APIRouter(prefix="/answers")


class Answers(BaseModel):
    quiz_id: int
    questions: list[m.QuestionAnswers] = []


def check_compatibility(answer: Answers, quiz: db.Quiz) -> None:
    try:
        assert len(quiz.questions) == len(answer.questions)
        for qa, q in zip(answer.questions, quiz.questions):
            q = m.Question.parse_obj(q)

            assert qa.title == q.title
            assert len(qa.answers) == len(q.forms)
            for af, f in zip(qa.answers, q.forms):
                assert af.form.type == f.type
    except AssertionError:
        raise HTTPException(400, "Ответ не совместим с опросом")


@root.get("/get/{id}")
async def get(id: int, x_token: str | None = Header(None)) -> m.QuizAnswers:
    user = utils.auth(x_token)

    with db.session.begin() as session:
        answers = session.get(db.Answers, id)

        if answers is None:
            raise HTTPException(404, "Ответ не найден")
        if not (answers.answerer_id == user.id or answers.quiz.owner_id == user.id):
            raise HTTPException(405, "У вас нету прав на получение данного ответа")

        return m.QuizAnswers(
            id=answers.id,
            quiz_id=answers.quiz_id,
            answerer=m.User(
                id=answers.answerer_id,
                username=answers.answerer.username,
            ),
            questions=answers.questions,
        )


@root.post("/add")
async def add(add: Answers, x_token: str | None = Header(None)) -> m.QuizAnswers:
    user = utils.auth(x_token)

    with db.session() as session:
        quiz = session.get(db.Quiz, add.quiz_id)

        if quiz is None:
            raise HTTPException(404, "Опрос не найден")
        check_compatibility(add, quiz)

        answers = db.Answers(
            quiz_id=quiz.id,
            answerer_id=user.id,
            questions=[loads(q.json()) for q in add.questions],
        )
        session.add(answers)

        session.commit()

        return m.QuizAnswers(
            id=answers.id,
            quiz_id=answers.quiz_id,
            answerer=m.User(
                id=answers.answerer_id,
                username=answers.answerer.username,
            ),
            questions=answers.questions,
        )


@root.put("/update")
async def update(
    id: int,
    update: Answers,
    x_token: str | None = Header(None),
) -> m.QuizAnswers:
    user = utils.auth(x_token)

    with db.session() as session:
        quiz = session.get(db.Quiz, update.quiz_id)
        answers = session.get(db.Answers, id)

        if quiz is None:
            raise HTTPException(404, "Опрос не найден")
        if answers is None:
            raise HTTPException(404, "Ответ не найден")
        if answers.answerer_id != user.id:
            raise HTTPException(405, "У вас нету прав на удаление данного ответа")
        check_compatibility(update, quiz)

        answers.quiz_id = update.quiz_id
        answers.questions = [loads(q.json()) for q in update.questions]

        session.commit()

        return m.QuizAnswers(
            id=answers.id,
            quiz_id=answers.quiz_id,
            answerer=m.User(
                id=answers.answerer_id,
                username=answers.answerer.username,
            ),
            questions=answers.questions,
        )


@root.delete("/delete")
async def delete(id: int, x_token: str | None = Header(None)) -> None:
    user = utils.auth(x_token)

    with db.session.begin() as session:
        answers = session.get(db.Answers, id)

        if answers is None:
            raise HTTPException(404, "Ответ не найден")
        if not (answers.answerer_id == user.id or answers.quiz.owner_id == user.id):
            print(answers.quiz.owner_id, user.id)
            raise HTTPException(405, "У вас нету прав на удаление данного ответа")

        session.delete(answers)
