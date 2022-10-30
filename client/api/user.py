from urllib.parse import urljoin

import requests

import models as m
from settings import settings


def login(username: str, password: str) -> str:
    return requests.get(
        urljoin(settings.url, "/user/login"),
        json={
            "username": username,
            "password": password,
        },
    ).json()


def me(token: str) -> m.User:
    return m.User.parse_obj(
        requests.get(
            urljoin(settings.url, "/user/me"),
            headers={
                "x-token": token,
            },
        ).json(),
    )
