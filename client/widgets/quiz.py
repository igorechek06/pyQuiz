import typing

import requests
from PIL import Image
from PyQt5 import QtCore, QtGui, QtWidgets

import gui
import models as m
import tasks


class Quiz(QtWidgets.QWidget):
    ui: gui.widgets.quiz_widget.Ui_Quiz

    def __init__(self, parent: QtWidgets.QWidget, quiz: m.Quiz) -> None:
        super().__init__(parent)
        self.ui = gui.widgets.quiz_widget.Ui_Quiz()
        self.ui.setupUi(self)

        self.ui.label.setText(quiz.label)
        if quiz.image_url is not None:
            self.ui.image.setPixmap(QtGui.QPixmap(":/src/src/wait-file.png"))
            task = tasks.DownloadImage(self.ui.image, quiz.image_url)
            QtCore.QThreadPool.globalInstance().start(task)
