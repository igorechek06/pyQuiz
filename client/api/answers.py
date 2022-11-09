from json import loads
from urllib.parse import urljoin

import httpx
from pydantic import BaseModel

import models as m
from api.base import encode, response
from settings import settings


class Answers(BaseModel):
    quiz_id: int
    questions: list[m.QuestionAnswers] = []


def get(token: str, id: int) -> m.QuizAnswers:
    headers = {"x-token": token}
    url = urljoin(settings.url, f"/answers/get/{id}")
    return m.QuizAnswers.parse_obj(response(httpx.get(url, headers=headers)))


def add(token: str, answers: Answers) -> m.QuizAnswers:
    headers = {"x-token": token}
    url = urljoin(settings.url, f"/answers/add")
    return m.QuizAnswers.parse_obj(
        response(httpx.post(url, json=loads(answers.json()), headers=headers))
    )


def update(token: str, id: int, answers: Answers) -> m.QuizAnswers:
    data = encode(
        dict(
            id=id,
        )
    )
    headers = {"x-token": token}
    url = urljoin(settings.url, f"/answers/update?{data}")
    return m.QuizAnswers.parse_obj(
        response(httpx.put(url, json=loads(answers.json()), headers=headers))
    )


def delete(token: str, id: int) -> None:
    data = encode(
        dict(
            id=id,
        )
    )
    headers = {"x-token": token}
    url = urljoin(settings.url, f"/answers/delete?{data}")
    response(httpx.delete(url, headers=headers))
