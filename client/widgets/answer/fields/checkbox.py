import models as m
import widgets
from gui.widgets.answer import fields

from .base import BaseField


class CheckboxField(BaseField[fields.checkbox.Ui_Checkbox, m.CheckboxAnswer]):
    def __init__(
        self,
        parent: "widgets.answer.question.Question",
        model: m.CheckboxAnswer,
    ) -> None:
        super().__init__(parent, model, fields.checkbox.Ui_Checkbox)

        self.ui.field.setText(self.model.form.label)
        self.ui.field.setChecked(self.model.value)

        self.ui.field.toggled.connect(self.value_updated)

    def value_updated(self, status: bool) -> None:
        self.model.value = status
