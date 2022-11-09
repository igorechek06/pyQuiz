# isort:skip_file
from . import base
from . import text
from . import integer
from . import float_
from . import time
from . import date
from . import datetime
from . import checkbox
from . import radio


WIDGETS = (
    text.TextField,
    integer.IntegerField,
    float_.FloatField,
    time.TimeField,
    date.DateField,
    datetime.DatetimeField,
    checkbox.CheckboxField,
    radio.RadioField,
)

WIDGETS_TYPE = (
    text.TextField
    | integer.IntegerField
    | float_.FloatField
    | time.TimeField
    | date.DateField
    | datetime.DatetimeField
    | checkbox.CheckboxField
    | radio.RadioField
)
