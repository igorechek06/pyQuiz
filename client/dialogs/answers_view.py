from PyQt5 import QtCore, QtWidgets

import gui
import models as m
import widgets
from api import quiz as q


class AnswersView(QtWidgets.QDialog):
    ui: gui.dialogs.answers_view.Ui_AnswersView
    context: "widgets.quiz.Quiz"
    answers: list[m.QuizAnswers]

    update_ui = QtCore.pyqtSignal()

    def __init__(self, parent: "widgets.quiz.Quiz") -> None:
        super().__init__(parent)
        self.ui = gui.dialogs.answers_view.Ui_AnswersView()
        self.ui.setupUi(self)
        self.context = parent
        self.answers = []

        self.ui.exportButton.clicked.connect(self.export_button)

        self.update_page()
        self.update_ui.connect(self._update_ui)
        self.update_ui.emit()

    def export_button(self) -> None:
        pass

    def update_page(self) -> None:
        def _page() -> None:
            assert self.context.context.token is not None
            self.answers = q.answers(self.context.context.token, self.context.quiz.id)
            self.update_ui.emit()

        QtCore.QThreadPool.globalInstance().start(_page)

    def _update_ui(self) -> None:
        for i in reversed(range(self.ui.answersLayout.layout().count())):
            self.ui.answersLayout.layout().itemAt(i).widget().deleteLater()

        for answer in self.answers:
            self.ui.answersLayout.layout().addWidget(
                widgets.answer_view.answer.Answer(self, answer)
            )
