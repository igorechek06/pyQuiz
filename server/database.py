from sqlalchemy import JSON, ForeignKey, create_engine
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    Session,
    mapped_column,
    relationship,
    sessionmaker,
)

from settings import settings

engine = create_engine(settings.database)
session = sessionmaker(engine, Session)


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str]
    salt: Mapped[str]


class Quiz(Base):
    __tablename__ = "quizzes"
    id: Mapped[int] = mapped_column(primary_key=True)
    owner_id: Mapped[int] = mapped_column(ForeignKey(User.id, ondelete="CASCADE"))
    label: Mapped[str]
    image_url: Mapped[str | None]
    questions: Mapped[list] = mapped_column(JSON)

    owner: Mapped[User] = relationship(User)


class Answer(Base):
    __tablename__ = "answers"
    id: Mapped[int] = mapped_column(primary_key=True)
    quiz_id: Mapped[int] = mapped_column(ForeignKey(Quiz.id, ondelete="CASCADE"))
    answerer_id: Mapped[int] = mapped_column(ForeignKey(User.id, ondelete="CASCADE"))
    answers: Mapped[list] = mapped_column(JSON)

    quiz: Mapped[Quiz] = relationship(Quiz)
    answerer: Mapped[User] = relationship(User)


Base.metadata.create_all(engine)
