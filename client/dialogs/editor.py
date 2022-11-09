from copy import deepcopy
from typing import Union

from PyQt5 import QtCore, QtGui, QtWidgets

import gui
import models as m
import widgets
from api import quiz as q


class QuizEditor(QtWidgets.QDialog):
    ui: gui.dialogs.editor.Ui_QuizEditor
    context: Union[QtWidgets.QWidget, "widgets.quiz.Quiz"]
    token: str
    quiz_id: int | None
    quiz: q.Quiz

    update_ui = QtCore.pyqtSignal()

    def __init__(
        self,
        parent: QtWidgets.QWidget,
        token: str,
        quiz: m.Quiz | None = None,
        pixmap: QtGui.QPixmap | None = None,
        image_updated: QtCore.pyqtBoundSignal | None = None,
    ) -> None:
        super().__init__(parent)
        self.ui = gui.dialogs.editor.Ui_QuizEditor()
        self.ui.setupUi(self)
        self.context = parent
        self.token = token

        if quiz is not None:
            quiz = deepcopy(quiz)
            self.quiz_id = quiz.id
            self.quiz = q.Quiz(
                label=quiz.label,
                image_url=quiz.image_url,
                questions=quiz.questions,
            )
        else:
            self.quiz_id = None
            self.quiz = q.Quiz(label="")

        if pixmap is not None:
            self.ui.image.setPixmap(pixmap)
        if image_updated is not None:
            image_updated.connect(self.ui.image.setPixmap)

        self.ui.labelField.setText(self.quiz.label)
        self.ui.imageURLField.setText(self.quiz.image_url)

        self.ui.saveButton.clicked.connect(self.save_button)
        self.ui.cancelButton.clicked.connect(self.cancel_button)
        self.ui.addFieldButton.clicked.connect(self.add_button)
        self.ui.deleteButton.clicked.connect(self.delete_button)

        self.update_ui.connect(self._update_ui)
        self.update_ui.emit()

    def add_button(self) -> None:
        question = m.Question(title="Заголовок вопроса")
        self.quiz.questions.append(question)
        self.ui.questionTabs.setCurrentIndex(
            self.ui.questionTabs.addTab(
                widgets.editor.question.Question(self, question), question.title
            )
        )

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
        self.quiz.label = self.ui.labelField.text()
        self.quiz.image_url = self.ui.imageURLField.text() or None

        if self.quiz_id is None:
            q.add(self.token, self.quiz)
        else:
            quiz = q.update(self.token, self.quiz_id, self.quiz)
            if isinstance(self.context, widgets.quiz.Quiz):
                self.context.quiz = quiz
                self.context.update_ui.emit()

        self.close()

    def delete_button(self) -> None:
        if (
            QtWidgets.QMessageBox(
                QtWidgets.QMessageBox.Icon.Critical,
                "Confirmation",
                "Вы точно хотите удалить опрос ?",
                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
            ).exec()
            == QtWidgets.QMessageBox.Yes
        ):
            if self.quiz_id is not None and isinstance(self.context, widgets.quiz.Quiz):
                q.delete(self.token, self.quiz_id)
                self.context.context.quizzes.remove(self.context.quiz)
                self.context.deleteLater()
            self.close()

    def _update_ui(self) -> None:
        for i in range(self.ui.questionTabs.count()):
            self.ui.questionTabs.widget(i).deleteLater()

        for question in self.quiz.questions:
            self.ui.questionTabs.addTab(
                widgets.editor.question.Question(self, question), question.title
            )
