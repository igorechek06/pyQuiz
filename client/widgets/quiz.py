import httpx
from PyQt5 import QtCore, QtGui, QtWidgets

import dialogs
import gui
import models as m
import windows


class Quiz(QtWidgets.QWidget):
    ui: gui.widgets.quiz.Ui_Quiz
    context: "windows.main.MainWindow"
    quiz: m.Quiz

    update_ui = QtCore.pyqtSignal()
    image_updated = QtCore.pyqtSignal(QtGui.QPixmap)

    def __init__(self, parent: "windows.main.MainWindow", quiz: m.Quiz) -> None:
        super().__init__(parent)
        self.ui = gui.widgets.quiz.Ui_Quiz()
        self.ui.setupUi(self)
        self.quiz = quiz
        self.context = parent

        self.ui.editButton.clicked.connect(self.edit_button)
        self.ui.startButton.clicked.connect(self.start_button)
        self.ui.answersButton.clicked.connect(self.answers_button)
        self.image_updated.connect(self.ui.image.setPixmap)

        self.update_ui.connect(self._update_ui)
        self.update_ui.emit()

    def start_button(self) -> None:
        if self.context.token is None:
            self.context.auth_button()
        else:
            answer = dialogs.answer.QuizAnswer(
                self,
                self.context.token,
                self.quiz,
                pixmap=self.ui.image.pixmap(),
                image_updated=self.image_updated,
            )
            answer.exec()

    def edit_button(self) -> None:
        assert self.context.token
        editor = dialogs.editor.QuizEditor(
            self,
            self.context.token,
            self.quiz,
            self.ui.image.pixmap(),
            self.image_updated,
        )
        editor.exec()

    def answers_button(self) -> None:
        view = dialogs.answers_view.AnswersView(self)
        view.exec()

    def _update_ui(self) -> None:
        self.ui.label.setText(self.quiz.label)
        if self.quiz.image_url is not None:
            self.image_updated.emit(QtGui.QPixmap(":/src/src/wait-file.png"))
            QtCore.QThreadPool.globalInstance().start(self._load_image)
        else:
            self.image_updated.emit(QtGui.QPixmap(":/src/src/no-file.png"))

        owner = (
            self.context.user is not None and self.quiz.owner.id == self.context.user.id
        )
        self.ui.editButton.setHidden(not owner)
        self.ui.answersButton.setHidden(not self.quiz.has_answers)

    def _load_image(self) -> None:
        assert self.quiz.image_url is not None
        image = QtGui.QPixmap()
        image.loadFromData(httpx.get(self.quiz.image_url).content)
        self.image_updated.emit(image)
