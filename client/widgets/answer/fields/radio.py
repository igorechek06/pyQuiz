from PyQt5 import QtCore

import models as m
import widgets
from gui.widgets.answer import fields

from .base import BaseField


class RadioField(BaseField[fields.radio.Ui_Radio, m.RadioAnswer]):
    def __init__(
        self,
        parent: "widgets.answer.question.Question",
        model: m.RadioAnswer,
        read_only: bool = False,
    ) -> None:
        super().__init__(parent, model, fields.radio.Ui_Radio, read_only)

        self.ui.field.setText(self.model.form.label)
        self.ui.field.setChecked(self.model.value)

        if self.read_only:
            self.ui.field.setAttribute(QtCore.Qt.WA_TransparentForMouseEvents)
            self.ui.field.setFocusPolicy(QtCore.Qt.NoFocus)

        self.ui.field.toggled.connect(self.value_updated)

    def value_updated(self, status: bool) -> None:
        self.model.value = status

        if status:
            for i in range(self.context.ui.fieldsLayout.count()):
                widget: BaseField = self.context.ui.fieldsLayout.itemAt(i).widget()
                if isinstance(widget, RadioField) and widget != self:
                    widget.ui.field.setChecked(False)
