import models as m
import widgets
from gui.widgets.editor import forms

from .base import BaseForm


class DatetimeForm(BaseForm[forms.datetime.Ui_Datetime, m.DatetimeForm]):
    def __init__(self, parent: "widgets.editor.form.Form", model: m.DatetimeForm) -> None:
        super().__init__(parent, model, forms.datetime.Ui_Datetime)

        self.ui.minValueField.dateTimeChanged.connect(
            self.ui.defaultField.setMinimumDateTime
        )
        self.ui.maxValueField.dateTimeChanged.connect(
            self.ui.defaultField.setMaximumDateTime
        )
        self.ui.minValueField.dateTimeChanged.connect(
            self.ui.maxValueField.setMinimumDateTime
        )
        self.ui.maxValueField.dateTimeChanged.connect(
            self.ui.minValueField.setMaximumDateTime
        )

        self.ui.defaultField.setDateTime(self.model.default)
        self.ui.minValueField.setDateTime(self.model.min)
        self.ui.maxValueField.setDateTime(self.model.max)
        self.ui.increaseButtonsCheckbox.setChecked(self.model.increase_buttons)
        self.ui.calendarButtonCheckbox.setChecked(self.model.calendar_button)

        self.ui.defaultField.editingFinished.connect(self.default_updated)
        self.ui.minValueField.editingFinished.connect(self.min_updated)
        self.ui.maxValueField.editingFinished.connect(self.max_updated)
        self.ui.increaseButtonsCheckbox.toggled.connect(self.increase_buttons_updates)
        self.ui.calendarButtonCheckbox.toggled.connect(self.calendar_button_updates)

    def default_updated(self) -> None:
        self.model.default = self.ui.defaultField.dateTime().toPyDateTime()

    def min_updated(self) -> None:
        self.model.min = self.ui.minValueField.dateTime().toPyDateTime()

    def max_updated(self) -> None:
        self.model.max = self.ui.maxValueField.dateTime().toPyDateTime()

    def increase_buttons_updates(self, status: bool) -> None:
        self.model.increase_buttons = status

    def calendar_button_updates(self, status: bool) -> None:
        self.model.calendar_button = status
