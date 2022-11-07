import models as m
import widgets
from gui.widgets.editor import forms

from .base import BaseForm


class CheckboxForm(BaseForm[forms.checkbox.Ui_Checkbox, m.CheckboxForm]):
    def __init__(self, parent: "widgets.editor.form.Form", model: m.CheckboxForm) -> None:
        super().__init__(parent, model, forms.checkbox.Ui_Checkbox)

        self.ui.defaultValue.setChecked(self.model.default)

        self.ui.defaultValue.toggled.connect(self.default_updated)

    def default_updated(self, status: bool) -> None:
        self.model.default = status
