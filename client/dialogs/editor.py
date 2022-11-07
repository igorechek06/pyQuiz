from copy import deepcopy

from PyQt5 import QtCore, QtWidgets

import gui
import models as m
import widgets
from api import quiz as q


class QuizEditor(QtWidgets.QDialog):
    ui: gui.dialogs.editor.Ui_QuizEditor
    context: "widgets.quiz.Quiz"
    quiz: m.Quiz

    update_ui = QtCore.pyqtSignal()

    def __init__(self, parent: "widgets.quiz.Quiz") -> None:
        super().__init__(parent)
        self.ui = gui.dialogs.editor.Ui_QuizEditor()
        self.ui.setupUi(self)
        self.context = parent
        self.quiz = deepcopy(self.context.quiz)

        self.ui.image.setPixmap(self.context.ui.image.pixmap())
        self.ui.labelField.setText(self.quiz.label)
        self.ui.imageURLField.setText(self.quiz.image_url)

        self.ui.saveButton.clicked.connect(self.save_button)
        self.ui.cancelButton.clicked.connect(self.cancel_button)
        self.ui.addFieldButton.clicked.connect(self.add_button)
        self.ui.deleteButton.clicked.connect(self.delete_button)
        self.context.image_updated.connect(self.ui.image.setPixmap)

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
        if self.quiz != self.context.quiz:
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
        else:
            self.close()

    def save_button(self) -> None:
        assert (
            self.context.context.token is not None
            and self.context.context.user is not None
        )
        self.quiz.label = self.ui.labelField.text()
        self.quiz.image_url = self.ui.imageURLField.text() or None

        q.update(
            self.context.context.token,
            self.quiz.id,
            q.Quiz(
                label=self.quiz.label,
                image_url=self.quiz.image_url,
                questions=self.quiz.questions,
            ),
        )

        self.context.quiz = self.quiz
        self.context.update_ui.emit()
        self.close()

    def delete_button(self) -> None:
        assert self.context.context.token
        if (
            QtWidgets.QMessageBox(
                QtWidgets.QMessageBox.Icon.Critical,
                "Confirmation",
                "Вы точно хотите удалить опрос ?",
                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
            ).exec()
            == QtWidgets.QMessageBox.Yes
        ):
            q.delete(self.context.context.token, self.context.quiz.id)
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
