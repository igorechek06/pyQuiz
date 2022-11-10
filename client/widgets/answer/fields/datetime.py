from PyQt5.QtWidgets import QAbstractSpinBox

import models as m
import widgets
from gui.widgets.answer import fields

from .base import BaseField


class DatetimeField(BaseField[fields.datetime.Ui_Datetime, m.DatetimeAnswer]):
    def __init__(
        self,
        parent: "widgets.answer.question.Question",
        model: m.DatetimeAnswer,
        read_only: bool = False,
    ) -> None:
        super().__init__(parent, model, fields.datetime.Ui_Datetime, read_only)

        self.ui.label.setText(self.model.form.label)
        self.ui.field.setDateTime(self.model.value)
        self.ui.field.setMinimumDateTime(self.model.form.min)
        self.ui.field.setMaximumDateTime(self.model.form.max)
        self.ui.field.setButtonSymbols(
            QAbstractSpinBox.ButtonSymbols.UpDownArrows
            if self.model.form.increase_buttons
            else QAbstractSpinBox.ButtonSymbols.NoButtons
        )
        self.ui.field.setCalendarPopup(self.model.form.calendar_button)

        self.ui.field.setReadOnly(self.read_only)

        self.ui.field.editingFinished.connect(self.value_updated)

    def value_updated(self) -> None:
        self.model.value = self.ui.field.dateTime().toPyDateTime()
