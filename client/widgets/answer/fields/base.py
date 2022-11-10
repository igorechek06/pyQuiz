from typing import Callable, Generic, TypeVar

from PyQt5 import QtWidgets

import models as m
import widgets
from gui.widgets.answer import fields

UI = TypeVar(
    "UI",
    fields.text.Ui_Text,
    fields.integer.Ui_Integer,
    fields.float.Ui_Float,
    fields.time.Ui_Time,
    fields.date.Ui_Date,
    fields.datetime.Ui_Datetime,
    fields.checkbox.Ui_Checkbox,
    fields.radio.Ui_Radio,
)


M = TypeVar(
    "M",
    m.TextAnswer,
    m.IntegerAnswer,
    m.FloatAnswer,
    m.TimeAnswer,
    m.DateAnswer,
    m.DatetimeAnswer,
    m.CheckboxAnswer,
    m.RadioAnswer,
)


class BaseField(QtWidgets.QWidget, Generic[UI, M]):
    ui: UI
    model: M
    context: "widgets.answer.question.Question"
    read_only: bool

    def __init__(
        self,
        parent: "widgets.answer.question.Question",
        model: M,
        ui: type[UI],
        read_only: bool = False,
    ) -> None:
        super().__init__(parent)
        self.ui = ui()
        self.ui.setupUi(self)
        self.model = model
        self.context = parent
        self.read_only = read_only
