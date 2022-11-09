import models as m
import widgets
from gui.widgets.editor import forms

from .base import BaseForm


class TextForm(BaseForm[forms.text.Ui_Text, m.TextForm]):
    def __init__(self, parent: "widgets.editor.form.Form", model: m.TextForm) -> None:
        super().__init__(parent, model, forms.text.Ui_Text)

        self.ui.defaultField.setText(self.model.default)
        self.ui.hintField.setText(self.model.hint)
        self.ui.clearButtonCheckbox.setChecked(self.model.clear_button)

        self.ui.defaultField.editingFinished.connect(self.default_updated)
        self.ui.hintField.editingFinished.connect(self.hint_updated)
        self.ui.clearButtonCheckbox.toggled.connect(self.clear_button_updated)

    def default_updated(self) -> None:
        self.model.default = self.ui.defaultField.text() or None

    def hint_updated(self) -> None:
        self.model.hint = self.ui.hintField.text()

    def clear_button_updated(self, status: bool) -> None:
        self.model.clear_button = status
