import requests
from PIL import Image
from PyQt5 import QtCore, QtGui, QtWidgets

import gui
import models as m
from api import quiz
from windows.main import MainWindow


class Quiz(QtWidgets.QWidget):
    ui: gui.widgets.quiz.Ui_Quiz
    context: MainWindow
    quiz: m.Quiz

    def __init__(
        self,
        parent: MainWindow,
        quiz: m.Quiz,
    ) -> None:
        super().__init__(parent)
        self.ui = gui.widgets.quiz.Ui_Quiz()
        self.ui.setupUi(self)
        self.quiz = quiz
        self.context = parent

        self.ui.label.setText(self.quiz.label)
        if self.quiz.image_url is not None:
            self.ui.image.setPixmap(QtGui.QPixmap(":/src/src/wait-file.png"))
            QtCore.QThreadPool.globalInstance().start(self._load_image)
        if self.context.user is None or quiz.owner.id != self.context.user.id:
            self.ui.editButton.hide()
            self.ui.deleteButton.hide()
        else:
            self.ui.deleteButton.clicked.connect(self.delete_quiz)
            self.ui.editButton.clicked.connect(self.edit_quiz)
        self.ui.startButton.clicked.connect(self.start_quiz)

    def start_quiz(self) -> None:
        pass

    def edit_quiz(self) -> None:
        pass

    def delete_quiz(self) -> None:
        assert self.context.token
        if (
            QtWidgets.QMessageBox(
                QtWidgets.QMessageBox.Icon.Critical,
                "Confirmation",
                "Вы точно хотите удалить опрос ?",
                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
            ).exec()
            == QtWidgets.QMessageBox.Yes
        ):
            quiz.delete(self.context.token, self.quiz.id)
        self.context.page()

    def _load_image(self) -> None:
        assert self.quiz.image_url is not None
        try:
            image = Image.open(requests.get(self.quiz.image_url, stream=True).raw)
            self.ui.image.setPixmap(image.toqpixmap())
        except Exception:
            pass
