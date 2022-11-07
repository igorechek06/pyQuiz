import secrets

import jwt
from fastapi import APIRouter, Header, HTTPException
from pydantic import BaseModel

import database as db
import models as m
import utils
from settings import settings

root = APIRouter(prefix="/user")


class User(BaseModel):
    username: str
    password: str


class Username(BaseModel):
    username: str


class Password(BaseModel):
    password: str


@root.post("/register")
async def register(register: User) -> None:
    if not register.username:
        raise HTTPException(400, "Имя не может быть пустым")
    if not register.password:
        raise HTTPException(403, "Пароль не может быть пустым")

    salt = secrets.token_hex(8)
    password_hash = utils.hash(register.password, salt)

    with db.session.begin() as session:
        if (
            session.query(db.User).filter(db.User.username == register.username).count()
            > 0
        ):
            raise HTTPException(403, "Имя занято другим пользователем")

        session.add(
            db.User(
                username=register.username,
                password=password_hash,
                salt=salt,
            )
        )


@root.post("/login")
async def login(login: User) -> str:
    with db.session.begin() as session:
        user = (
            session.query(db.User)
            .filter(db.User.username == login.username)
            .one_or_none()
        )
        if user is None:
            raise HTTPException(401, "Неверное имя пользователя или пароль")

        if user.password == utils.hash(login.password, user.salt):
            return jwt.encode({"sub": user.id}, settings.secret + user.password)
        else:
            raise HTTPException(401, "Неверное имя пользователя или пароль")


@root.get("/get/{id}")
async def get(id: int) -> m.User | None:
    with db.session.begin() as session:
        user = session.get(db.User, id)
        if user is not None:
            return m.User(
                id=user.id,
                username=user.username,
            )
        else:
            return None


@root.get("/me")
async def me(x_token: str | None = Header(None)) -> m.User:
    user = utils.auth(x_token)
    return m.User(
        id=user.id,
        username=user.username,
    )


@root.put("/update/username")
async def update_username(update: Username, x_token: str | None = Header(None)) -> None:
    user = utils.auth(x_token)

    if not update.username:
        raise HTTPException(400, "Имя не может быть пустым")

    with db.session.begin() as session:
        if session.query(db.User).filter(db.User.username == update.username).count() > 0:
            raise HTTPException(403, "Имя занято другим пользователем")

        session.add(user)
        user.username = update.username


@root.put("/update/password")
async def update_password(update: Password, x_token: str | None = Header(None)) -> None:
    user = utils.auth(x_token)

    if not update.password:
        raise HTTPException(400, "Пароль не может быть пустым")

    with db.session.begin() as session:
        session.add(user)
        user.salt = secrets.token_hex(8)
        user.password = utils.hash(update.password, user.salt)


@root.delete("/delete")
async def delete(x_token: str | None = Header(None)) -> None:
    user = utils.auth(x_token)
    with db.session.begin() as session:
        session.add(user)
        session.delete(user)
