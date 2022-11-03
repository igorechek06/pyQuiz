import secrets

import jwt
from fastapi import APIRouter, HTTPException, Request

import database as db
import models as m
import utils
from settings import settings

root = APIRouter(prefix="/user")


@root.post("/register")
async def register(request: Request) -> None:
    data = await request.json()

    username = data["username"]
    password = data["password"]

    if not username:
        raise HTTPException(400, "Имя не может быть пустым")
    if not password:
        raise HTTPException(403, "Пароль не может быть пустым")

    salt = secrets.token_hex(8)
    password = utils.hash(password, salt)

    with db.session.begin() as session:
        if session.query(db.User).filter(db.User.username == username).count() > 0:
            raise HTTPException(403, "Имя занято другим пользователем")

        session.add(
            db.User(
                username=username,
                password=password,
                salt=salt,
            )
        )


@root.get("/login")
async def login(request: Request) -> str:
    data = await request.json()

    with db.session.begin() as session:
        user = (
            session.query(db.User)
            .filter(db.User.username == data["username"])
            .one_or_none()
        )
        if user is None:
            raise HTTPException(401, "Неверное имя пользователя или пароль")

        if user.password == utils.hash(data["password"], user.salt):
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
async def me(request: Request) -> m.User:
    user = utils.auth(request)
    return m.User(
        id=user.id,
        username=user.username,
    )


@root.delete("/delete")
async def delete(request: Request) -> None:
    user = utils.auth(request)
    with db.session.begin() as session:
        session.add(user)
        session.delete(user)


@root.put("/username")
async def username(request: Request) -> None:
    user = utils.auth(request)
    data = await request.json()
    username = data["username"]

    if not username:
        raise HTTPException(400, "Имя не может быть пустым")

    with db.session.begin() as session:
        if session.query(db.User).filter(db.User.username == username).count() > 0:
            raise HTTPException(403, "Имя занято другим пользователем")

        session.add(user)
        user.username = username


@root.put("/password")
async def password(request: Request) -> None:
    user = utils.auth(request)
    data = await request.json()
    password = data["password"]

    if not password:
        raise HTTPException(400, "Пароль не может быть пустым")

    with db.session.begin() as session:
        session.add(user)
        user.salt = secrets.token_hex(8)
        user.password = utils.hash(password, user.salt)
