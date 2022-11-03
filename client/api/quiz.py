from urllib.parse import urlencode, urljoin

import requests

import models as m
from settings import settings

from .base import response


def get(id: int) -> m.Quiz:
    url = urljoin(settings.url, f"/quiz/get/{id}")
    return m.Quiz.parse_obj(response(requests.get(url)))


def add(
    token: str,
    label: str,
    image_url: str | None = None,
    questions: list[m.Question] = [],
) -> None:
    data = urlencode(
        dict(
            label=label,
            image_url=image_url,
            questions=[q.dict() for q in questions],
        )
    )
    headers = {"x-token": token}
    url = urljoin(settings.url, f"/quiz/add?{data}")
    response(requests.post(url, headers=headers))


def delete(token: str, id: int) -> None:
    data = urlencode(dict(id=id))
    headers = {"x-token": token}
    url = urljoin(settings.url, f"/quiz/delete?{data}")
    response(requests.delete(url, headers=headers))


def find(
    label: str = "",
    offset: int = 0,
    limit: int = 10,
) -> list[m.Quiz]:
    data = urlencode(
        dict(
            label=label,
            offset=offset,
            limit=limit,
        )
    )
    url = urljoin(settings.url, f"/quiz/find?{data}")
    return [m.Quiz.parse_obj(q) for q in list(response(requests.get(url)))]


def count(label: str = "") -> int:
    data = urlencode(dict(label=label))
    url = urljoin(settings.url, f"/quiz/count?{data}")
    return int(response(requests.get(url)))
