from typing import Callable, Generic, TypeVar

from PyQt5 import QtWidgets

import models as m
import widgets
from gui.widgets.editor import forms

UI = TypeVar(
    "UI",
    forms.text.Ui_Text,
    forms.integer.Ui_Integer,
    forms.float.Ui_Float,
    forms.time.Ui_Time,
    forms.date.Ui_Date,
    forms.datetime.Ui_Datetime,
    forms.checkbox.Ui_Checkbox,
    forms.radio.Ui_Radio,
)


M = TypeVar(
    "M",
    m.TextForm,
    m.IntegerForm,
    m.FloatForm,
    m.TimeForm,
    m.DateForm,
    m.DatetimeForm,
    m.CheckboxForm,
    m.RadioForm,
)


class BaseForm(QtWidgets.QWidget, Generic[UI, M]):
    ui: UI
    model: M
    context: "widgets.editor.form.Form"

    def __init__(
        self,
        parent: "widgets.editor.form.Form",
        model: M,
        ui: type[UI],
    ) -> None:
        super().__init__(parent)
        self.ui = ui()
        self.ui.setupUi(self)
        self.model = model
        self.context = parent
