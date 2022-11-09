from PyQt5 import QtCore, QtWidgets

import dialogs
import gui
import models as m
import widgets


class Question(QtWidgets.QWidget):
    ui: gui.widgets.answer.question.Ui_Question
    context: "dialogs.answer.QuizAnswer"
    answers: m.QuestionAnswers

    update_ui = QtCore.pyqtSignal()

    def __init__(
        self,
        parent: "dialogs.answer.QuizAnswer",
        answers: m.QuestionAnswers,
    ) -> None:
        super().__init__(parent)
        self.ui = gui.widgets.answer.question.Ui_Question()
        self.ui.setupUi(self)
        self.context = parent
        self.answers = answers

        self.ui.questionBox.setTitle(self.answers.title)

        self.update_ui.connect(self._update_ui)
        self.update_ui.emit()

    def _update_ui(self) -> None:
        for i in reversed(range(self.ui.fieldsLayout.layout().count())):
            self.ui.fieldsLayout.layout().itemAt(i).widget().deleteLater()

        for answer in self.answers.answers:
            self.ui.fieldsLayout.layout().addWidget(
                widgets.answer.fields.WIDGETS[answer.form.type.value - 1](self, answer)  # type: ignore
            )
