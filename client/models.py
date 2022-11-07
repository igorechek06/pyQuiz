from datetime import date, datetime, time
from enum import IntEnum
from typing import Literal

from pydantic import BaseModel


class User(BaseModel):
    id: int
    username: str


class FormType(IntEnum):
    TEXT = 1
    INTEGER = 2
    FLOAT = 3
    TIME = 4
    DATE = 5
    DATETIME = 6
    CHECKBOX = 7
    RADIO = 8


class BaseForm(BaseModel):
    type: FormType
    label: str


class TextForm(BaseForm):
    type: Literal[FormType.TEXT] = FormType.TEXT
    default: str | None
    hint: str | None
    clear_button: bool = False


class IntegerForm(BaseForm):
    type: Literal[FormType.INTEGER] = FormType.INTEGER
    default: int = 0
    min: int = 0
    max: int = 100
    step: int = 1
    increase_buttons: bool = True


class FloatForm(BaseForm):
    type: Literal[FormType.FLOAT] = FormType.FLOAT
    decimals: int = 1
    default: float = 0.0
    min: float = 0.0
    max: float = 10.0
    step: float = 0.1
    increase_buttons: bool = True


class TimeForm(BaseForm):
    type: Literal[FormType.TIME] = FormType.TIME
    default: time = time.min
    min: time = time.min
    max: time = time.max
    increase_buttons: bool = True


class DateForm(BaseForm):
    type: Literal[FormType.DATE] = FormType.DATE
    default: date = date.min
    min: date = date.min
    max: date = date.max
    increase_buttons: bool = True
    calendar_button: bool = False


class DatetimeForm(BaseForm):
    type: Literal[FormType.DATETIME] = FormType.DATETIME
    default: datetime = datetime.min
    min: datetime = datetime.min
    max: datetime = datetime.max
    increase_buttons: bool = True
    calendar_button: bool = False


class CheckboxForm(BaseForm):
    type: Literal[FormType.CHECKBOX] = FormType.CHECKBOX
    default: bool = False


class RadioForm(BaseForm):
    type: Literal[FormType.RADIO] = FormType.RADIO
    default: bool = False


Form = (
    TextForm
    | IntegerForm
    | FloatForm
    | TimeForm
    | DateForm
    | DatetimeForm
    | CheckboxForm
    | RadioForm
)


class Question(BaseModel):
    title: str
    forms: list[Form] = []


class Quiz(BaseModel):
    id: int
    owner: User
    label: str
    image_url: str | None = None
    questions: list[Question] = []


class BaseAnswer(BaseModel):
    type: FormType
    question: int


class TextAnswer(BaseAnswer):
    type: FormType = FormType.TEXT
    value: str


class IntegerAnswer(BaseAnswer):
    type: FormType = FormType.INTEGER
    value: int = 0


class FloatAnswer(BaseAnswer):
    type: FormType = FormType.FLOAT
    value: float = 0.0


class TimeAnswer(BaseAnswer):
    type: FormType = FormType.TIME
    value: time = time(0, 0, 0)


class DateAnswer(BaseAnswer):
    type: FormType = FormType.DATE
    value: date = date(1, 1, 1)


class DatetimeAnswer(BaseAnswer):
    type: FormType = FormType.DATETIME
    value: datetime = datetime(1, 1, 1, 0, 0, 0)


class CheckboxAnswer(BaseAnswer):
    type: FormType = FormType.CHECKBOX
    value: bool = False


class RadioAnswer(BaseAnswer):
    type: FormType = FormType.RADIO
    value: bool = False


Answer = (
    TextAnswer
    | IntegerAnswer
    | FloatAnswer
    | TimeAnswer
    | DateAnswer
    | DatetimeAnswer
    | CheckboxAnswer
    | RadioAnswer
)


class Answers(BaseModel):
    id: int
    quiz: Quiz
    answerer: User
    answers: list[Answer] = []
