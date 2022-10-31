import requests
from PIL import Image
from PyQt5 import QtCore, QtGui, QtWidgets

import gui
import models as m


class Quiz(QtWidgets.QWidget):
    ui: gui.widgets.quiz.Ui_Quiz
    quiz: m.Quiz
    user: m.User | None

    def __init__(
        self,
        parent: QtWidgets.QWidget,
        quiz: m.Quiz,
        user: m.User | None,
    ) -> None:
        super().__init__(parent)
        self.ui = gui.widgets.quiz.Ui_Quiz()
        self.ui.setupUi(self)
        self.quiz = quiz
        self.user = user

        self.ui.label.setText(self.quiz.label)
        if self.quiz.image_url is not None:
            self.ui.image.setPixmap(QtGui.QPixmap(":/src/src/wait-file.png"))
            QtCore.QThreadPool.globalInstance().start(self._load_image)
        if user is None or quiz.owner.id != user.id:
            self.ui.editButton.hide()

    def _load_image(self) -> None:
        assert self.quiz.image_url is not None
        try:
            image = Image.open(requests.get(self.quiz.image_url, stream=True).raw)
            self.ui.image.setPixmap(image.toqpixmap())
        except Exception:
            pass
