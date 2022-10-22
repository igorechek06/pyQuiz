from datetime import date, datetime, time
from enum import Enum, auto

from pydantic import BaseModel


class FormType(Enum):
    TEXT = auto()
    INTEGER = auto()
    FLOAT = auto()
    TIME = auto()
    DATE = auto()
    DATETIME = auto()
    CHECKBOX = auto()
    RADIO = auto()


class BaseForm(BaseModel):
    type: FormType
    label: str


class Question(BaseModel):
    title: str
    forms: list[BaseForm]


class Quiz(BaseModel):
    id: int | None
    label: str
    hidden: bool = False
    image_url: str | None = None
    questions: list[Question] = []


class BaseAnswer(BaseModel):
    type: FormType
    question: int


class Answers(BaseModel):
    id: int | None
    quiz_id: int
    answers: list[BaseAnswer] = []
