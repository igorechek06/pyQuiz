import hashlib

import jwt
from fastapi import HTTPException, Request

import database as db
from settings import settings


def auth(request: Request) -> db.User:
    token = request.headers.get("x-token", None)
    if not token:
        raise HTTPException(401, "Не авторизованная сессия")
    else:
        data = jwt.decode(token, options={"verify_signature": False})

    with db.session.begin() as session:
        user = session.get(db.User, data["sub"])
        if user is None:
            raise HTTPException(401, "Сессия не действительна")
        else:
            try:
                jwt.decode(token, settings.secret + user.password, algorithms=["HS256"])
            except jwt.exceptions.InvalidSignatureError:
                raise HTTPException(401, "Сессия не действительна")
            session.expunge(user)
            return user


def hash(password: str, salt: str) -> str:
    return hashlib.sha512(str.encode(password + salt, "UTF-8")).hexdigest()
