import models as m
import widgets
from gui.widgets.editor import forms

from .base import BaseForm


class DateForm(BaseForm[forms.date.Ui_Date, m.DateForm]):
    def __init__(self, parent: "widgets.editor.form.Form", model: m.DateForm) -> None:
        super().__init__(parent, model, forms.date.Ui_Date)

        self.ui.minValueField.dateChanged.connect(self.ui.defaultField.setMinimumDate)
        self.ui.maxValueField.dateChanged.connect(self.ui.defaultField.setMaximumDate)
        self.ui.minValueField.dateChanged.connect(self.ui.maxValueField.setMinimumDate)
        self.ui.maxValueField.dateChanged.connect(self.ui.minValueField.setMaximumDate)

        self.ui.defaultField.setDate(self.model.default)
        self.ui.minValueField.setDate(self.model.min)
        self.ui.maxValueField.setDate(self.model.max)
        self.ui.increaseButtonsCheckbox.setChecked(self.model.increase_buttons)
        self.ui.calendarButtonCheckbox.setChecked(self.model.calendar_button)

        self.ui.defaultField.editingFinished.connect(self.default_updated)
        self.ui.minValueField.editingFinished.connect(self.min_updated)
        self.ui.maxValueField.editingFinished.connect(self.max_updated)
        self.ui.increaseButtonsCheckbox.toggled.connect(self.increase_buttons_updates)
        self.ui.calendarButtonCheckbox.toggled.connect(self.calendar_button_updates)

    def default_updated(self) -> None:
        self.model.default = self.ui.defaultField.date().toPyDate()

    def min_updated(self) -> None:
        self.model.min = self.ui.minValueField.date().toPyDate()

    def max_updated(self) -> None:
        self.model.max = self.ui.maxValueField.date().toPyDate()

    def increase_buttons_updates(self, status: bool) -> None:
        self.model.increase_buttons = status

    def calendar_button_updates(self, status: bool) -> None:
        self.model.calendar_button = status
