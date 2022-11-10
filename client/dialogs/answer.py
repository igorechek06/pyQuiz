from copy import deepcopy
from typing import Union

from PyQt5 import QtCore, QtGui, QtWidgets

import gui
import models as m
import widgets
from api import answers as a

MODELS = (
    m.TextAnswer,
    m.IntegerAnswer,
    m.FloatAnswer,
    m.TimeAnswer,
    m.DateAnswer,
    m.DatetimeAnswer,
    m.CheckboxAnswer,
    m.RadioAnswer,
)


class QuizAnswer(QtWidgets.QDialog):
    ui: gui.dialogs.answer.Ui_QuizAnswer
    context: QtWidgets.QWidget
    token: str
    read_only: bool
    answers_id: int | None
    answers: a.Answers

    update_ui = QtCore.pyqtSignal()

    def __init__(
        self,
        parent: QtWidgets.QWidget,
        token: str,
        quiz: m.Quiz,
        answers: m.QuizAnswers | None = None,
        pixmap: QtGui.QPixmap | None = None,
        image_updated: QtCore.pyqtBoundSignal | None = None,
        read_only: bool = False,
    ) -> None:
        super().__init__(parent)
        self.ui = gui.dialogs.answer.Ui_QuizAnswer()
        self.ui.setupUi(self)
        self.context = parent
        self.token = token
        self.read_only = read_only

        quiz = deepcopy(quiz)
        if answers is not None:
            answers = deepcopy(answers)
            self.answers_id = answers.id
            self.answers = a.Answers(
                quiz_id=quiz.id,
                questions=answers.questions,
            )
        else:
            self.answers_id = None
            self.answers = a.Answers(
                quiz_id=quiz.id,
                questions=[
                    m.QuestionAnswers(
                        title=question.title,
                        answers=[
                            MODELS[form.type.value - 1](
                                form=form,
                                value=form.default,
                            )
                            for form in question.forms
                        ],
                    )
                    for question in quiz.questions
                ],
            )

        if pixmap is not None:
            self.ui.image.setPixmap(pixmap)
        if image_updated is not None:
            image_updated.connect(self.ui.image.setPixmap)

        self.ui.label.setText(quiz.label)
        if self.read_only:
            self.ui.cancelButton.hide()
            self.ui.saveButton.hide()
        else:
            self.ui.closeButton.hide()
            self.ui.cancelButton.clicked.connect(self.cancel_button)
            self.ui.saveButton.clicked.connect(self.save_button)

        self.update_ui.connect(self._update_ui)
        self.update_ui.emit()

    def cancel_button(self) -> None:
        if (
            QtWidgets.QMessageBox(
                QtWidgets.QMessageBox.Icon.Critical,
                "Confirmation",
                "Вы хотите отменить изменения ?",
                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
            ).exec()
            == QtWidgets.QMessageBox.Yes
        ):
            self.close()

    def save_button(self) -> None:
        if self.answers_id is None:
            a.add(self.token, self.answers)
            if isinstance(self.context, widgets.quiz.Quiz):
                self.context.quiz.has_answers = True
                self.context.update_ui.emit()
        else:
            answer = a.update(self.token, self.answers_id, self.answers)
            if isinstance(self.context, widgets.answer_view.answer.Answer):
                self.context.answer = answer

        self.close()

    def _update_ui(self) -> None:
        for i in reversed(range(self.ui.questionLayout.layout().count())):
            self.ui.questionLayout.layout().itemAt(i).widget().deleteLater()

        for question in self.answers.questions:
            self.ui.questionLayout.layout().addWidget(
                widgets.answer.question.Question(self, question)
            )
