from urllib.parse import urljoin

import requests

import models as m
from settings import settings


def register(username: str, password: str) -> None:
    return requests.post(
        urljoin(settings.url, "/user/register"),
        json={
            "username": username,
            "password": password,
        },
    ).json()


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


def delete(token: str) -> None:
    requests.delete(
        urljoin(settings.url, "/user/delete"),
        headers={
            "x-token": token,
        },
    )


def username(token: str, username: str) -> None:
    requests.put(
        urljoin(settings.url, "/user/username"),
        headers={
            "x-token": token,
        },
        json={
            "username": username,
        },
    ),


def password(token: str, password: str) -> None:
    requests.put(
        urljoin(settings.url, "/user/password"),
        headers={
            "x-token": token,
        },
        json={
            "password": password,
        },
    ),
