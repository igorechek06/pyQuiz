from urllib.parse import urlencode, urljoin

import requests

import models as m
from settings import settings


def find(label: str = "", offset: int = 0, count: int = 10) -> list[m.Quiz]:
    data = urlencode(
        dict(
            label=label,
            offset=offset,
            count=count,
        )
    )
    return [
        m.Quiz.parse_obj(obj)
        for obj in requests.get(
            urljoin(
                settings.url,
                f"/quiz/find?{data}",
            )
        ).json()
    ]


def count(label: str = "") -> int:
    data = urlencode(
        dict(
            label=label,
        )
    )
    return requests.get(
        urljoin(
            settings.url,
            f"/quiz/count?{data}",
        )
    ).json()
