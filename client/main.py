import sys

from PyQt5 import QtCore, QtWidgets

import gui
import models as m
import widgets


class MainWindow(QtWidgets.QMainWindow):
    ui: gui.main_menu.Ui_MainMenu
    quizzes: list[m.Quiz]

    def __init__(self) -> None:
        super().__init__()
        self.ui = gui.main_menu.Ui_MainMenu()
        self.ui.setupUi(self)
        self.quizzes = []

        self.ui.searchButton.clicked.connect(self.search)
        self.update_ui()

    def search(self) -> None:
        pass

    def update_ui(self) -> None:
        for quiz in self.quizzes:
            self.ui.quizzesLayout.layout().addWidget(widgets.quiz.Quiz(self, quiz))


if __name__ == "__main__":
    QtCore.QThreadPool.globalInstance().setMaxThreadCount(100)
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
