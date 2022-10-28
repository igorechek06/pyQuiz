import sys

import requests
from PyQt5 import QtCore, QtWidgets

import gui
import models as m
import widgets
from settings import settings


class MainWindow(QtWidgets.QMainWindow):
    ui: gui.main_menu.Ui_MainMenu
    quizzes: list[m.Quiz]

    def __init__(self) -> None:
        super().__init__()
        self.ui = gui.main_menu.Ui_MainMenu()
        self.ui.setupUi(self)
        self.quizzes = []

        self.ui.pageSelectorField.valueChanged.connect(self.page)

    def page(self) -> None:
        page = self.ui.pageSelectorField.value()
        self.ui.pageSelectorField.setMaximum(
            int(requests.get(f"{settings.url}/quiz/count").json() / 10)
        )

        self.quizzes = [
            m.Quiz.parse_obj(q)
            for q in requests.get(
                f"{settings.url}/quiz/all?count={10}&offset={(page-1)*10}"
            ).json()
        ]

        self.update_ui()

    def update_ui(self) -> None:
        for i in reversed(range(self.ui.quizzesLayout.layout().count())):
            self.ui.quizzesLayout.layout().itemAt(i).widget().deleteLater()

        for quiz in self.quizzes:
            self.ui.quizzesLayout.layout().addWidget(widgets.quiz.Quiz(self, quiz))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    window.page()
    app.exec()
