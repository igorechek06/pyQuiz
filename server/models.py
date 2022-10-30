from datetime import date, datetime, time
from enum import Enum, auto

from pydantic import BaseModel


class User(BaseModel):
    id: int
    username: str


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


class TextForm(BaseForm):
    type: FormType = FormType.TEXT
    default: str | None
    hint: str | None
    clear_button: bool = False


class IntegerForm(BaseForm):
    type: FormType = FormType.INTEGER
    default: int = 0
    min: int = 0
    max: int = 100
    step: int = 1
    increase_buttons: bool = True


class FloatForm(BaseForm):
    type: FormType = FormType.FLOAT
    default: float = 0.0
    min: float = 0.0
    max: float = 10.0
    step: float = 0.1
    increase_buttons: bool = True


class TimeForm(BaseForm):
    type: FormType = FormType.TIME
    default: time = time(0, 0, 0)
    min: time = time(0, 0, 0)
    max: time = time(23, 59, 59)
    increase_buttons: bool = True


class DateForm(BaseForm):
    type: FormType = FormType.DATE
    default: date = date(1, 1, 1)
    min: date = date(1, 1, 1)
    max: date = date(9999, 12, 31)
    increase_buttons: bool = True
    calendar_button: bool = False


class DatetimeForm(BaseForm):
    type: FormType = FormType.DATETIME
    default: datetime = datetime(1, 1, 1, 0, 0, 0)
    min: datetime = datetime(1, 1, 1, 0, 0, 0)
    max: datetime = datetime(9999, 12, 31, 23, 59, 59)
    increase_buttons: bool = True
    calendar_button: bool = False


class CheckboxForm(BaseForm):
    type: FormType = FormType.CHECKBOX
    default: bool = False


class RadioForm(BaseForm):
    type: FormType = FormType.RADIO
    default: bool = False


class Forms(Enum):
    TEXT = TextForm
    INTEGER = IntegerForm
    FLOAT = FloatForm
    TIME = TimeForm
    DATE = DateForm
    DATETIME = DatetimeForm
    CHECKBOX = CheckboxForm
    RADIO = RadioForm


class Question(BaseModel):
    title: str
    forms: list[Forms] = []


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


class Answer(Enum):
    TEXT = TextAnswer
    INTEGER = IntegerAnswer
    FLOAT = FloatAnswer
    TIME = TimeAnswer
    DATE = DateAnswer
    DATETIME = DatetimeAnswer
    CHECKBOX = CheckboxAnswer


class Answers(BaseModel):
    id: int
    quiz: Quiz
    answerer: User
    answers: list[Answer] = []
