from PyQt5 import QtCore, QtGui, QtWidgets

import dialogs
import gui
import models as m
from api import answers as a


class Answer(QtWidgets.QWidget):
    ui: gui.widgets.answers_view.answer.Ui_Answer
    context: "dialogs.answers_view.AnswersView"
    answer: m.QuizAnswers

    def __init__(
        self,
        parent: "dialogs.answers_view.AnswersView",
        answer: m.QuizAnswers,
    ) -> None:
        super().__init__(parent)
        self.ui = gui.widgets.answers_view.answer.Ui_Answer()
        self.ui.setupUi(self)
        self.context = parent
        self.answer = answer

        assert self.context.context.context.user is not None

        self.ui.username.setText(self.answer.answerer.username)
        self.ui.editButton.setHidden(
            self.answer.answerer.id != self.context.context.context.user.id
        )

        self.ui.editButton.clicked.connect(self.edit_button)
        self.ui.viewButton.clicked.connect(self.view_button)
        self.ui.deleteButton.clicked.connect(self.delete_button)

    def edit_button(self) -> None:
        assert self.context.context.context.token is not None
        answer = dialogs.answer.QuizAnswer(
            self,
            self.context.context.context.token,
            self.context.context.quiz,
            self.answer,
            self.context.context.ui.image.pixmap(),
            self.context.context.image_updated,
        )
        answer.exec()

    def view_button(self) -> None:
        pass

    def delete_button(self) -> None:
        assert self.context.context.context.token is not None
        if (
            QtWidgets.QMessageBox(
                QtWidgets.QMessageBox.Icon.Critical,
                "Confirmation",
                "Вы точно хотите удалить ответ ?",
                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
            ).exec()
            == QtWidgets.QMessageBox.Yes
        ):
            a.delete(self.context.context.context.token, self.answer.id)
            self.context.answers.remove(self.answer)
            self.deleteLater()
