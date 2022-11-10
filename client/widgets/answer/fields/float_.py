from PyQt5.QtWidgets import QAbstractSpinBox

import models as m
import widgets
from gui.widgets.answer import fields

from .base import BaseField


class FloatField(BaseField[fields.float.Ui_Float, m.FloatAnswer]):
    def __init__(
        self,
        parent: "widgets.answer.question.Question",
        model: m.FloatAnswer,
        read_only: bool = False,
    ) -> None:
        super().__init__(parent, model, fields.float.Ui_Float, read_only)

        self.ui.label.setText(self.model.form.label)
        self.ui.field.setDecimals(self.model.form.decimals)
        self.ui.field.setValue(self.model.value)
        self.ui.field.setMinimum(self.model.form.min)
        self.ui.field.setMaximum(self.model.form.max)
        self.ui.field.setSingleStep(self.model.form.step)
        self.ui.field.setButtonSymbols(
            QAbstractSpinBox.ButtonSymbols.UpDownArrows
            if self.model.form.increase_buttons
            else QAbstractSpinBox.ButtonSymbols.NoButtons
        )

        self.ui.field.setReadOnly(self.read_only)

        self.ui.field.editingFinished.connect(self.value_updated)

    def value_updated(self) -> None:
        self.model.value = self.ui.field.value()
