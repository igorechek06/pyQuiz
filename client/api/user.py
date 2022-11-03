from urllib.parse import urljoin

import requests

import models as m
from settings import settings

from .base import response


def register(username: str, password: str) -> None:
    data = dict(
        username=username,
        password=password,
    )
    url = urljoin(settings.url, "/user/register")
    response(requests.post(url, json=data))


def login(username: str, password: str) -> str:
    data = dict(
        username=username,
        password=password,
    )
    url = urljoin(settings.url, "/user/login")
    return str(response(requests.get(url, json=data)))


def get(id: int) -> m.User:
    url = urljoin(settings.url, f"/user/get/{id}")
    return m.User.parse_obj(response(requests.get(url)))


def me(token: str) -> m.User:
    url = urljoin(settings.url, "/user/me")
    headers = {"x-token": token}
    return m.User.parse_obj(response(requests.get(url, headers=headers)))


def delete(token: str) -> None:
    url = urljoin(settings.url, "/user/delete")
    headers = {"x-token": token}
    response(requests.delete(url, headers=headers))


def username(token: str, username: str) -> None:
    data = dict(username=username)
    headers = {"x-token": token}
    url = urljoin(settings.url, f"/user/username")
    response(requests.put(url, json=data, headers=headers))


def password(token: str, password: str) -> None:
    data = dict(password=password)
    headers = {"x-token": token}
    url = urljoin(settings.url, f"/user/password")
    response(requests.put(url, json=data, headers=headers))
