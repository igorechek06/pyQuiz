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


class Question(BaseModel):
    title: str
    forms: list[BaseForm]


class Quiz(BaseModel):
    id: int | None
    label: str
    hidden: bool = False
    image_url: str | None = None
    questions: list[Question] = []
