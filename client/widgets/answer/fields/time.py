from PyQt5.QtWidgets import QAbstractSpinBox

import models as m
import widgets
from gui.widgets.answer import fields

from .base import BaseField


class TimeField(BaseField[fields.time.Ui_Time, m.TimeAnswer]):
    def __init__(
        self,
        parent: "widgets.answer.question.Question",
        model: m.TimeAnswer,
        read_only: bool = False,
    ) -> None:
        super().__init__(parent, model, fields.time.Ui_Time, read_only)

        self.ui.label.setText(self.model.form.label)
        self.ui.field.setTime(self.model.value)
        self.ui.field.setMinimumTime(self.model.form.min)
        self.ui.field.setMaximumTime(self.model.form.max)
        self.ui.field.setButtonSymbols(
            QAbstractSpinBox.ButtonSymbols.UpDownArrows
            if self.model.form.increase_buttons
            else QAbstractSpinBox.ButtonSymbols.NoButtons
        )

        self.ui.field.setReadOnly(self.read_only)

        self.ui.field.editingFinished.connect(self.value_updated)

    def value_updated(self) -> None:
        self.model.value = self.ui.field.time().toPyTime()
