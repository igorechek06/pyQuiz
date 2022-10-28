import typing

import requests
from PIL import Image
from PyQt5 import QtCore, QtGui, QtWidgets

import gui
import models as m
import tasks


class Quiz(QtWidgets.QWidget):
    ui: gui.widgets.quiz_widget.Ui_Quiz
    quiz: m.Quiz

    def __init__(self, parent: QtWidgets.QWidget, quiz: m.Quiz) -> None:
        super().__init__(parent)
        self.ui = gui.widgets.quiz_widget.Ui_Quiz()
        self.ui.setupUi(self)
        self.quiz = quiz

        self.ui.label.setText(self.quiz.label)
        if self.quiz.image_url is not None:
            QtCore.QThreadPool.globalInstance().start(self._load_image)

    def _load_image(self) -> None:
        assert self.quiz.image_url is not None
        self.ui.image.setPixmap(QtGui.QPixmap(":/src/src/wait-file.png"))
        image = Image.open(requests.get(self.quiz.image_url, stream=True).raw)
        self.ui.image.setPixmap(image.toqpixmap())
