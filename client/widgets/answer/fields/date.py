from PyQt5.QtWidgets import QAbstractSpinBox

import models as m
import widgets
from gui.widgets.answer import fields

from .base import BaseField


class DateField(BaseField[fields.date.Ui_Date, m.DateAnswer]):
    def __init__(
        self, parent: "widgets.answer.question.Question", model: m.DateAnswer
    ) -> None:
        super().__init__(parent, model, fields.date.Ui_Date)

        self.ui.label.setText(self.model.form.label)
        self.ui.field.setDate(self.model.value)
        self.ui.field.setMinimumDate(self.model.form.min)
        self.ui.field.setMaximumDate(self.model.form.max)
        self.ui.field.setButtonSymbols(
            QAbstractSpinBox.ButtonSymbols.UpDownArrows
            if self.model.form.increase_buttons
            else QAbstractSpinBox.ButtonSymbols.NoButtons
        )
        self.ui.field.setCalendarPopup(self.model.form.calendar_button)

        self.ui.field.editingFinished.connect(self.value_updated)

    def value_updated(self) -> None:
        self.model.value = self.ui.field.date().toPyDate()
