from PyQt5 import QtCore, QtWidgets

import dialogs
import gui
import models as m
import widgets


class Question(QtWidgets.QWidget):
    ui: gui.widgets.editor.question.Ui_Question
    context: "dialogs.editor.QuizEditor"
    question: m.Question

    update_ui = QtCore.pyqtSignal()

    def __init__(self, parent: "dialogs.editor.QuizEditor", question: m.Question) -> None:
        super().__init__(parent)
        self.ui = gui.widgets.editor.question.Ui_Question()
        self.ui.setupUi(self)
        self.context = parent
        self.question = question

        self.ui.titleField.setText(self.question.title)

        self.ui.addButton.clicked.connect(self.add_button)
        self.ui.titleField.textChanged.connect(self.title_edited)
        self.context.ui.questionTabs.tabBar().tabMoved.connect(self.question_moved)
        self.ui.deleteButton.clicked.connect(self.delete_button)

        self.update_ui.connect(self._update_ui)
        self.update_ui.emit()

    def add_button(self) -> None:
        form = m.TextForm(label="")
        self.question.forms.append(form)
        self.ui.formTabs.setCurrentIndex(
            self.ui.formTabs.addTab(
                widgets.editor.form.Form(self, form),
                form.label,
            )
        )

    def title_edited(self) -> None:
        self.question.title = self.ui.titleField.text()
        self.context.ui.questionTabs.setTabText(
            self.context.ui.questionTabs.indexOf(self),
            self.question.title,
        )

    def question_moved(self, from_: int, to: int) -> None:
        if self.context.ui.questionTabs.widget(from_) == self:
            self.context.quiz.questions[from_], self.context.quiz.questions[to] = (
                self.context.quiz.questions[to],
                self.context.quiz.questions[from_],
            )

    def delete_button(self) -> None:
        if (
            QtWidgets.QMessageBox(
                QtWidgets.QMessageBox.Icon.Critical,
                "Confirmation",
                "Вы точно хотите удалить вопрос ?",
                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
            ).exec()
            == QtWidgets.QMessageBox.Yes
        ):
            self.context.quiz.questions.remove(self.question)
            self.deleteLater()

    def _update_ui(self) -> None:
        for i in range(self.ui.formTabs.count()):
            self.ui.formTabs.widget(i).deleteLater()

        for form in self.question.forms:
            self.ui.formTabs.addTab(widgets.editor.form.Form(self, form), form.label)
