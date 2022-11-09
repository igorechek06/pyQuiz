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
    has_answers: bool = False
    questions: list[Question] = []


class BaseAnswer(BaseModel):
    form: Form


class TextAnswer(BaseAnswer):
    form: TextForm
    value: str | None


class IntegerAnswer(BaseAnswer):
    form: IntegerForm
    value: int


class FloatAnswer(BaseAnswer):
    form: FloatForm
    value: float


class TimeAnswer(BaseAnswer):
    form: TimeForm
    value: time


class DateAnswer(BaseAnswer):
    form: DateForm
    value: date


class DatetimeAnswer(BaseAnswer):
    form: DatetimeForm
    value: datetime


class CheckboxAnswer(BaseAnswer):
    form: CheckboxForm
    value: bool


class RadioAnswer(BaseAnswer):
    form: RadioForm
    value: bool


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


class QuestionAnswers(BaseModel):
    title: str
    answers: list[Answer] = []


class QuizAnswers(BaseModel):
    id: int
    quiz_id: int
    answerer: User
    questions: list[QuestionAnswers] = []
