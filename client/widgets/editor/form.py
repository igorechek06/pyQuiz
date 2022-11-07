from PyQt5 import QtCore, QtWidgets

import gui
import models as m
import widgets
from widgets.editor import forms

MODELS = (
    m.TextForm,
    m.IntegerForm,
    m.FloatForm,
    m.TimeForm,
    m.DateForm,
    m.DatetimeForm,
    m.CheckboxForm,
    m.RadioForm,
)


class Form(QtWidgets.QWidget):
    ui: gui.widgets.editor.form.Ui_Form
    context: "widgets.editor.question.Question"
    form: m.Form
    form_widget: type["widgets.editor.forms.WIDGETS_TYPE"]
    old_forms: dict[m.FormType, m.Form]

    update_ui = QtCore.pyqtSignal()

    def __init__(self, parent: "widgets.editor.question.Question", form: m.Form) -> None:
        super().__init__(parent)
        self.ui = gui.widgets.editor.form.Ui_Form()
        self.ui.setupUi(self)
        self.context = parent
        self.form = form
        self.form_widget = forms.WIDGETS[self.form.type.value - 1]
        self.old_forms = {}

        self.ui.labelField.setText(self.form.label)
        self.ui.typeEnum.setCurrentIndex(self.form.type.value - 1)

        self.ui.labelField.textChanged.connect(self.label_changed)
        self.context.ui.formTabs.tabBar().tabMoved.connect(self.form_moved)
        self.ui.typeEnum.activated.connect(self.type_changed)
        self.ui.deleteButton.clicked.connect(self.delete_button)

        self.update_ui.connect(self._update_ui)
        self.update_ui.emit()

    def label_changed(self) -> None:
        self.form.label = self.ui.labelField.text()
        self.context.ui.formTabs.setTabText(
            self.context.ui.formTabs.indexOf(self),
            self.form.label,
        )

    def form_moved(self, from_: int, to: int) -> None:
        if self.context.ui.formTabs.widget(from_) == self:
            self.context.question.forms[from_], self.context.question.forms[to] = (
                self.context.question.forms[to],
                self.context.question.forms[from_],
            )

    def type_changed(self, type_: int) -> None:
        if self.form.type not in self.old_forms:
            self.old_forms[self.form.type] = self.form

        if m.FormType(type_ + 1) in self.old_forms:
            new_form = self.old_forms[m.FormType(type_ + 1)]
        else:
            new_form = MODELS[type_](label=self.form.label)

        self.context.question.forms[
            self.context.question.forms.index(self.form)
        ] = new_form

        self.form = new_form
        self.form_widget = forms.WIDGETS[type_]
        self.update_ui.emit()

    def delete_button(self) -> None:
        if (
            QtWidgets.QMessageBox(
                QtWidgets.QMessageBox.Icon.Critical,
                "Confirmation",
                "Вы точно хотите удалить поле ?",
                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
            ).exec()
            == QtWidgets.QMessageBox.Yes
        ):
            self.context.question.forms.remove(self.form)
            self.deleteLater()

    def _update_ui(self) -> None:
        for i in reversed(range(self.ui.propertiesLayout.layout().count())):
            self.ui.propertiesLayout.layout().itemAt(i).widget().deleteLater()

        self.ui.propertiesLayout.layout().addWidget(
            self.form_widget(self, self.form),  # type: ignore
        )
