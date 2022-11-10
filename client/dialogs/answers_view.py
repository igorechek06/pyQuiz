import csv
from os.path import expanduser

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
        file_name = QtWidgets.QFileDialog.getSaveFileName(
            self, "Export", expanduser("~"), "CSV таблица (*.csv)"
        )[0].removesuffix(".csv")

        if len(file_name) > 0:
            with open(f"{file_name}.csv", "w") as file:
                writer = csv.writer(file)

                header = ["username"]
                for q in self.context.quiz.questions:
                    for f in q.forms:
                        header.append(f"{q.title}: {f.label}")
                writer.writerow(header)

                for a in self.answers:
                    for qa in a.questions:
                        writer.writerow(
                            [a.answerer.username] + [str(fa.value) for fa in qa.answers]
                        )

    def remove(self, answer: m.QuizAnswers) -> None:
        self.answers.remove(answer)
        self.context.quiz.has_answers = len(self.answers) > 0
        if not self.context.quiz.has_answers:
            self.context.update_ui.emit()
            self.ui.cancelButton.click()

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
