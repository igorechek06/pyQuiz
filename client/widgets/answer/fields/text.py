import models as m
import widgets
from gui.widgets.answer import fields

from .base import BaseField


class TextField(BaseField[fields.text.Ui_Text, m.TextAnswer]):
    def __init__(
        self, parent: "widgets.answer.question.Question", model: m.TextAnswer
    ) -> None:
        super().__init__(parent, model, fields.text.Ui_Text)

        self.ui.label.setText(self.model.form.label)
        self.ui.field.setText(self.model.value)
        self.ui.field.setPlaceholderText(self.model.form.hint)

        self.ui.field.editingFinished.connect(self.value_updated)

    def value_updated(self) -> None:
        self.model.value = self.ui.field.text() or None
