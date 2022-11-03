import sys
from math import ceil
from traceback import print_stack
from types import TracebackType

import keyring
from PyQt5 import QtCore, QtWidgets
from requests import ConnectionError, HTTPError

import gui
import models as m
from api import quiz, user


class MainWindow(QtWidgets.QMainWindow):
    ui: gui.main_menu.Ui_MainMenu
    quizzes: list[m.Quiz]
    token: str | None
    user: m.User | None

    update_ui = QtCore.pyqtSignal()

    def __init__(self, token: str | None) -> None:
        super().__init__()
        sys.excepthook = self.exceptions_handler

        self.ui = gui.main_menu.Ui_MainMenu()
        self.ui.setupUi(self)
        self.quizzes = []
        self.token = token
        if self.token is not None:
            try:
                self.user = user.me(self.token)
            except HTTPError:
                self.user = None
                keyring.delete_password("pyquiz", "token")
            except ConnectionError:
                self.user = None
        else:
            self.user = None

        self.ui.authButton.clicked.connect(self.account)
        self.ui.searchButton.clicked.connect(self.search)
        self.ui.pageSelectorField.valueChanged.connect(self.page)
        self.update_ui.connect(self._update_ui)

    def exceptions_handler(
        self,
        cls: type[BaseException],
        exception: BaseException,
        traceback: TracebackType | None,
    ) -> None:
        if isinstance(exception, HTTPError):
            message = exception.args[1]
            QtWidgets.QMessageBox(
                QtWidgets.QMessageBox.Icon.Critical,
                "Error",
                message,
                QtWidgets.QMessageBox.Close,
            ).exec()
        elif isinstance(exception, ConnectionError):
            QtWidgets.QMessageBox(
                QtWidgets.QMessageBox.Icon.Critical,
                "Error",
                "Нет подключения к серверу",
                QtWidgets.QMessageBox.Close,
            ).exec()
        else:
            print_stack()

    def account(self) -> None:
        import dialogs

        if self.token is not None and self.user is not None:
            account = dialogs.account.AccountDialog(self)
            account.exec()
        else:
            auth = dialogs.auth.AuthDialog(self)
            auth.exec()

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
        import widgets

        for i in reversed(range(self.ui.quizzesLayout.layout().count())):
            self.ui.quizzesLayout.layout().itemAt(i).widget().deleteLater()

        for quiz in self.quizzes:
            self.ui.quizzesLayout.layout().addWidget(
                widgets.quiz.Quiz(
                    parent=self,
                    quiz=quiz,
                )
            )

        if self.user is not None:
            self.ui.authButton.setText(self.user.username)
        else:
            self.ui.authButton.setText("Авторизоваться")
