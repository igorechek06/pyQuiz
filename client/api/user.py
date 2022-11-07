from urllib.parse import urljoin

import httpx
from pydantic import BaseModel

import models as m
from settings import settings

from .base import response


class User(BaseModel):
    username: str
    password: str


class Username(BaseModel):
    username: str


class Password(BaseModel):
    password: str


def register(user: User) -> None:
    url = urljoin(settings.url, "/user/register")
    response(httpx.post(url, json=user.dict()))


def login(user: User) -> str:
    url = urljoin(settings.url, "/user/login")
    return str(response(httpx.post(url, json=user.dict())))


def get(id: int) -> m.User:
    url = urljoin(settings.url, f"/user/get/{id}")
    return m.User.parse_obj(response(httpx.get(url)))


def me(token: str) -> m.User:
    url = urljoin(settings.url, "/user/me")
    headers = {"x-token": token}
    return m.User.parse_obj(response(httpx.get(url, headers=headers)))


def delete(token: str) -> None:
    url = urljoin(settings.url, "/user/delete")
    headers = {"x-token": token}
    response(httpx.delete(url, headers=headers))


def update_username(token: str, username: Username) -> None:
    headers = {"x-token": token}
    url = urljoin(settings.url, f"/user/update/username")
    response(httpx.put(url, json=username.dict(), headers=headers))


def update_password(token: str, password: Password) -> None:
    headers = {"x-token": token}
    url = urljoin(settings.url, f"/user/update/password")
    response(httpx.put(url, json=password.dict(), headers=headers))
