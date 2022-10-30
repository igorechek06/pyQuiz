import sys
from math import ceil

from PyQt5 import QtCore, QtWidgets

import dialogs
import gui
import models as m
import widgets
from api import quiz


class MainWindow(QtWidgets.QMainWindow):
    ui: gui.main_menu.Ui_MainMenu
    quizzes: list[m.Quiz]
    token: str
    user: m.User

    update_ui = QtCore.pyqtSignal()

    def __init__(self) -> None:
        super().__init__()
        self.ui = gui.main_menu.Ui_MainMenu()
        self.ui.setupUi(self)
        self.quizzes = []

        self.ui.authButton.clicked.connect(self.account)
        self.ui.searchButton.clicked.connect(self.search)
        self.ui.pageSelectorField.valueChanged.connect(self.page)
        self.update_ui.connect(self._update_ui)

    def account(self) -> None:
        login = dialogs.login.AuthDialog(self)
        login.exec()

        if login.token is not None and login.user is not None:
            self.token = login.token
            self.user = login.user

    def search(self) -> None:
        self.ui.pageSelectorField.setValue(1)
        self.page()

    def page(self) -> None:
        def _page() -> None:
            search = self.ui.searchField.text()

            self.ui.pageSelectorField.setMaximum(ceil((quiz.count(search) + 1) / 10))
            self.ui.pageSelectorField.setSuffix(f"/{self.ui.pageSelectorField.maximum()}")

            self.quizzes = quiz.find(
                search,
                (self.ui.pageSelectorField.value() - 1) * 10,
                10,
            )

            self.update_ui.emit()

        QtCore.QThreadPool.globalInstance().start(_page)

    def _update_ui(self) -> None:
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
