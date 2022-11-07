import models as m
import widgets
from gui.widgets.editor import forms

from .base import BaseForm


class RadioForm(BaseForm[forms.radio.Ui_Radio, m.RadioForm]):
    def __init__(self, parent: "widgets.editor.form.Form", model: m.RadioForm) -> None:
        super().__init__(parent, model, forms.radio.Ui_Radio)

        self.ui.defaultValue.setChecked(self.model.default)

        self.ui.defaultValue.toggled.connect(self.default_updated)

    def default_updated(self, status: bool) -> None:
        self.model.default = status

        if status:
            for i in range(self.context.context.ui.formTabs.count()):
                widget: widgets.editor.form.Form = (
                    self.context.context.ui.formTabs.widget(i)
                )
                form_widget: BaseForm = widget.ui.propertiesLayout.itemAt(0).widget()

                if isinstance(form_widget, RadioForm) and form_widget != self:
                    form_widget.ui.defaultValue.setChecked(False)
