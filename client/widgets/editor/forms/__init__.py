# isort: skip_file

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
    text.TextForm,
    integer.IntegerForm,
    float_.FloatForm,
    time.TimeForm,
    date.DateForm,
    datetime.DatetimeForm,
    checkbox.CheckboxForm,
    radio.RadioForm,
)


WIDGETS_TYPE = (
    text.TextForm
    | integer.IntegerForm
    | float_.FloatForm
    | time.TimeForm
    | date.DateForm
    | datetime.DatetimeForm
    | checkbox.CheckboxForm
    | radio.RadioForm
)
