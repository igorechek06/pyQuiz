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
    salt = secrets.token_hex(8)
    password = utils.hash(data["password"], salt)

    with db.session.begin() as session:
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
            raise HTTPException(401, "Wrong username or password")

        if user.password == utils.hash(data["password"], user.salt):
            return jwt.encode({"sub": user.id}, settings.secret + user.password)
        else:
            raise HTTPException(401, "Wrong username or password")


@root.get("/me")
async def me(request: Request) -> m.User:
    user = utils.auth(request)
    return m.User(
        id=user.id,
        username=user.username,
    )


@root.put("/password")
async def password(request: Request) -> None:
    user = utils.auth(request)
    data = await request.json()
    salt = secrets.token_hex(8)

    with db.session.begin() as session:
        session.add(user)
        user.salt = salt
        user.password = utils.hash(data["password"], salt)


@root.put("/username")
async def username(request: Request) -> None:
    user = utils.auth(request)
    data = await request.json()

    with db.session.begin() as session:
        session.add(user)
        user.username = data["username"]
