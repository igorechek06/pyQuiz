import sys
from math import ceil
from traceback import print_exception
from types import TracebackType

import keyring
from httpx import RequestError
from PyQt5 import QtCore, QtWidgets

import dialogs
import gui
import models as m
import widgets
from api import quiz as q
from api import user as u


class MainWindow(QtWidgets.QMainWindow):
    ui: gui.main_menu.Ui_MainMenu
    quizzes: list[m.Quiz]
    token: str | None
    user: m.User | None

    update_ui = QtCore.pyqtSignal()

    def __init__(self, token: str | None) -> None:
        sys.excepthook = self.exceptions_handler
        super().__init__()
        self.ui = gui.main_menu.Ui_MainMenu()
        self.ui.setupUi(self)
        self.quizzes = []
        self.token = token
        if self.token is not None:
            try:
                self.user = u.me(self.token)
            except AssertionError:
                self.user = None
                keyring.delete_password("pyquiz", "token")
        else:
            self.user = None

        self.ui.authButton.clicked.connect(self.auth_button)
        self.ui.searchButton.clicked.connect(self.search_button)
        self.ui.createQuizButton.clicked.connect(self.create_button)
        self.ui.pageSelectorField.valueChanged.connect(self.update_page)

        self.update_ui.connect(self._update_ui)
        self.update_ui.emit()

    def exceptions_handler(
        self,
        cls: type[BaseException],
        exception: BaseException,
        traceback: TracebackType | None,
    ) -> None:
        if isinstance(exception, RequestError):
            QtWidgets.QMessageBox(
                QtWidgets.QMessageBox.Icon.Critical,
                "Error",
                "Нет подключения к серверу",
                QtWidgets.QMessageBox.Close,
            ).exec()
        elif isinstance(exception, AssertionError):
            QtWidgets.QMessageBox(
                QtWidgets.QMessageBox.Icon.Critical,
                "Error",
                exception.args[0],
                QtWidgets.QMessageBox.Close,
            ).exec()
            self.update_page()
        else:
            print_exception(exception)

    def auth_button(self) -> None:
        if self.token is not None and self.user is not None:
            account = dialogs.account.AccountDialog(self)
            account.exec()
        else:
            auth = dialogs.auth.AuthDialog(self)
            auth.exec()

    def search_button(self) -> None:
        self.ui.pageSelectorField.setValue(1)
        self.update_page()

    def create_button(self) -> None:
        if self.token is None:
            self.auth_button()
        if self.token is not None:
            editor = dialogs.editor.QuizEditor(self, self.token)
            editor.exec()
            self.update_page()

    def update_page(self) -> None:
        def _page() -> None:
            search = self.ui.searchField.text() or None

            self.ui.pageSelectorField.setMaximum(max(1, ceil(q.count(search) / 10)))
            self.ui.pageSelectorField.setSuffix(f"/{self.ui.pageSelectorField.maximum()}")

            self.quizzes = q.find(
                (self.ui.pageSelectorField.value() - 1) * 10,
                10,
                search,
                self.token,
            )

            self.update_ui.emit()

        QtCore.QThreadPool.globalInstance().start(_page)

    def _update_ui(self) -> None:
        for i in reversed(range(self.ui.quizzesLayout.layout().count())):
            self.ui.quizzesLayout.layout().itemAt(i).widget().deleteLater()

        for quiz in self.quizzes:
            self.ui.quizzesLayout.layout().addWidget(widgets.quiz.Quiz(self, quiz))

        if self.token is not None and self.user is not None:
            self.ui.authButton.setText(self.user.username)
        else:
            self.ui.authButton.setText("Авторизоваться")
