from pydantic import BaseModel
from datetime import time, date, datetime
from enum import Enum, auto


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
    default: str | None
    hint: str | None
    clear_button: bool = False


class IntegerForm(BaseForm):
    default: int = 0
    min: int = 0
    max: int = 100
    step: int = 1
    icrese_buttons: bool = True


class FloatForm(BaseForm):
    default: float = 0.0
    min: float = 0.0
    max: float = 10.0
    step: float = 0.1
    icrese_buttons: bool = True


class TimeForm(BaseForm):
    default: time = time(0, 0, 0)
    min: time = time(0, 0, 0)
    max: time = time(23, 59, 59)
    icrese_buttons: bool = True


class DateForm(BaseForm):
    default: date = date(1, 1, 1)
    min: date = date(1, 1, 1)
    max: date = date(9999, 12, 31)
    icrese_buttons: bool = True
    calendar_button: bool = False


class DatetimeForm(BaseForm):
    default: datetime = datetime(1, 1, 1, 0, 0, 0)
    min: datetime = datetime(1, 1, 1, 0, 0, 0)
    max: datetime = datetime(9999, 12, 31, 23, 59, 59)
    icrese_buttons: bool = True
    calendar_button: bool = False


class CheckboxForm(BaseForm):
    default: bool = False


class RadioForm(BaseForm):
    default: bool = False


class Question(BaseForm):
    title: str
    forms: list[BaseForm]


class Quiz(BaseModel):
    id: int
    label: str
    hidden: bool = False
    image: str | None = None
    questions: list[Question] = []
