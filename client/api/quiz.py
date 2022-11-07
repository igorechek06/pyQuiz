from json import loads
from urllib.parse import urljoin

import httpx
from pydantic import BaseModel

import models as m
from settings import settings

from .base import encode, response


class Quiz(BaseModel):
    label: str
    image_url: str | None = None
    questions: list[m.Question] = []


def get(id: int) -> m.Quiz:
    url = urljoin(settings.url, f"/quiz/get/{id}")
    return m.Quiz.parse_obj(response(httpx.get(url)))


def find(offset: int = 0, limit: int = 10, label: str | None = None) -> list[m.Quiz]:
    data = encode(
        dict(
            offset=offset,
            limit=limit,
            label=label,
        )
    )
    url = urljoin(settings.url, f"/quiz/find?{data}")
    return [m.Quiz.parse_obj(q) for q in list(response(httpx.get(url)))]


def count(label: str | None = None) -> int:
    data = encode(
        dict(
            label=label,
        )
    )
    url = urljoin(settings.url, f"/quiz/count?{data}")
    return int(response(httpx.get(url)))


def add(token: str, quiz: Quiz) -> m.Quiz:
    headers = {"x-token": token}
    url = urljoin(settings.url, f"/quiz/add")
    return m.Quiz.parse_obj(
        response(httpx.post(url, json=loads(quiz.json()), headers=headers))
    )


def update(token: str, id: int, quiz: Quiz) -> m.Quiz:
    data = encode(
        dict(
            id=id,
        )
    )
    headers = {"x-token": token}
    url = urljoin(settings.url, f"/quiz/update?{data}")
    return m.Quiz.parse_obj(
        response(httpx.put(url, json=loads(quiz.json()), headers=headers))
    )


def delete(token: str, id: int) -> None:
    data = encode(
        dict(
            id=id,
        )
    )
    headers = {"x-token": token}
    url = urljoin(settings.url, f"/quiz/delete?{data}")
    response(httpx.delete(url, headers=headers))
