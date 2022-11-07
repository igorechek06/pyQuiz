import models as m
import widgets
from gui.widgets.editor import forms

from .base import BaseForm


class TimeForm(BaseForm[forms.time.Ui_Time, m.TimeForm]):
    def __init__(self, parent: "widgets.editor.form.Form", model: m.TimeForm) -> None:
        super().__init__(parent, model, forms.time.Ui_Time)

        self.ui.minValueField.timeChanged.connect(self.ui.defaultField.setMinimumTime)
        self.ui.maxValueField.timeChanged.connect(self.ui.defaultField.setMaximumTime)
        self.ui.minValueField.timeChanged.connect(self.ui.maxValueField.setMinimumTime)
        self.ui.maxValueField.timeChanged.connect(self.ui.minValueField.setMaximumTime)

        self.ui.defaultField.setTime(self.model.default)
        self.ui.minValueField.setTime(self.model.min)
        self.ui.maxValueField.setTime(self.model.max)
        self.ui.increaseButtonsCheckbox.setChecked(self.model.increase_buttons)

        self.ui.defaultField.editingFinished.connect(self.default_updated)
        self.ui.minValueField.editingFinished.connect(self.min_updated)
        self.ui.maxValueField.editingFinished.connect(self.max_updated)
        self.ui.increaseButtonsCheckbox.toggled.connect(self.increase_buttons_updates)

    def default_updated(self) -> None:
        self.model.default = self.ui.defaultField.time().toPyTime()

    def min_updated(self) -> None:
        self.model.min = self.ui.minValueField.time().toPyTime()

    def max_updated(self) -> None:
        self.model.max = self.ui.maxValueField.time().toPyTime()

    def increase_buttons_updates(self, status: bool) -> None:
        self.model.increase_buttons = status
