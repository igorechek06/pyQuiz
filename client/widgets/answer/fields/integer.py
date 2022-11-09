from PyQt5.QtWidgets import QAbstractSpinBox

import models as m
import widgets
from gui.widgets.answer import fields

from .base import BaseField


class IntegerField(BaseField[fields.integer.Ui_Integer, m.IntegerAnswer]):
    def __init__(
        self,
        parent: "widgets.answer.question.Question",
        model: m.IntegerAnswer,
    ) -> None:
        super().__init__(parent, model, fields.integer.Ui_Integer)

        self.ui.label.setText(self.model.form.label)
        self.ui.field.setValue(self.model.value)
        self.ui.field.setMinimum(self.model.form.min)
        self.ui.field.setMaximum(self.model.form.max)
        self.ui.field.setSingleStep(self.model.form.step)
        self.ui.field.setButtonSymbols(
            QAbstractSpinBox.ButtonSymbols.UpDownArrows
            if self.model.form.increase_buttons
            else QAbstractSpinBox.ButtonSymbols.NoButtons
        )

        self.ui.field.editingFinished.connect(self.value_updated)

    def value_updated(self) -> None:
        self.model.value = self.ui.field.value()
