from sqlalchemy import (
    JSON,
    Boolean,
    Column,
    ForeignKey,
    Integer,
    MetaData,
    Text,
    create_engine,
)
from sqlalchemy.orm import registry
from sqlalchemy.orm.decl_api import DeclarativeMeta
from sqlalchemy.orm.session import sessionmaker

import models as m
from config import config

engine = create_engine(config.database)
meta = MetaData(engine)
session = sessionmaker(engine)
mapper = registry(meta)


class Base(metaclass=DeclarativeMeta):
    __abstract__ = True

    registry = mapper
    metadata = meta

    __init__ = mapper.constructor


class Quiz(Base):
    __tablename__ = "quizzes"
    id = Column(Integer, primary_key=True)
    label = Column(Text)
    hidden = Column(Boolean, default=True)
    image_url = Column(Text, default=None, nullable=True)
    questions = Column(JSON, default=[])


class Answers(Base):
    __tablename__ = "answers"
    id = Column(Integer, primary_key=True)
    quiz_id = ForeignKey(Quiz.id)
    answers = Column(JSON, default=[])


Base.metadata.create_all()
