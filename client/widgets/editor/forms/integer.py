import models as m
import widgets
from gui.widgets.editor import forms

from .base import BaseForm


class IntegerForm(BaseForm[forms.integer.Ui_Integer, m.IntegerForm]):
    def __init__(self, parent: "widgets.editor.form.Form", model: m.IntegerForm) -> None:
        super().__init__(parent, model, forms.integer.Ui_Integer)

        self.ui.minValueField.valueChanged.connect(self.ui.defaultField.setMinimum)
        self.ui.maxValueField.valueChanged.connect(self.ui.defaultField.setMaximum)
        self.ui.minValueField.valueChanged.connect(self.ui.maxValueField.setMinimum)
        self.ui.maxValueField.valueChanged.connect(self.ui.minValueField.setMaximum)
        self.ui.maxValueField.valueChanged.connect(self.ui.stepField.setMaximum)

        self.ui.defaultField.setValue(self.model.default)
        self.ui.minValueField.setValue(self.model.min)
        self.ui.maxValueField.setValue(self.model.max)
        self.ui.stepField.setValue(self.model.step)
        self.ui.increaseButtonsCheckbox.setChecked(self.model.increase_buttons)

        self.ui.defaultField.editingFinished.connect(self.default_updated)
        self.ui.minValueField.editingFinished.connect(self.min_updated)
        self.ui.maxValueField.editingFinished.connect(self.max_updated)
        self.ui.stepField.editingFinished.connect(self.step_updated)
        self.ui.increaseButtonsCheckbox.toggled.connect(self.increase_buttons_updates)

    def default_updated(self) -> None:
        self.model.default = self.ui.defaultField.value()

    def min_updated(self) -> None:
        self.model.min = self.ui.minValueField.value()

    def max_updated(self) -> None:
        self.model.max = self.ui.maxValueField.value()

    def step_updated(self) -> None:
        self.model.step = self.ui.stepField.value()

    def increase_buttons_updates(self, status: bool) -> None:
        self.model.increase_buttons = status
