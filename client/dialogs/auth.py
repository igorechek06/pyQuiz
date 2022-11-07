from typing import Callable

import keyring
from PyQt5 import QtWidgets

import gui
import models as m
import windows
from api import user as u


class AuthDialog(QtWidgets.QDialog):
    ui: gui.dialogs.auth.Ui_AuthDialog
    context: "windows.main.MainWindow"

    def __init__(self, parent: "windows.main.MainWindow") -> None:
        super().__init__(parent)
        self.ui = gui.dialogs.auth.Ui_AuthDialog()
        self.ui.setupUi(self)
        self.context = parent

        # LOGIN
        self.ui.loginShowPasswordCheckbox.toggled.connect(
            self.show_password(
                [
                    self.ui.loginPasswordField,
                ]
            )
        )
        self.ui.loginButton.clicked.connect(self.login_button)

        # REGISTER
        self.ui.registerShowPasswordCheckbox.toggled.connect(
            self.show_password(
                [
                    self.ui.registerPasswordField,
                    self.ui.registerRepeatPasswordField,
                ]
            )
        )
        self.ui.registerButton.clicked.connect(self.register_button)

    def login_button(self) -> None:
        username = self.ui.loginUsernameField.text()
        password = self.ui.loginPasswordField.text()

        self.context.token = u.login(u.User(username=username, password=password))
        self.context.user = u.me(self.context.token)
        self.context.update_ui.emit()
        keyring.set_password("pyquiz", "token", self.context.token)
        self.close()

    def register_button(self) -> None:
        username = self.ui.registerUsernameField.text()
        password = self.ui.registerPasswordField.text()

        if password != self.ui.registerRepeatPasswordField.text():
            QtWidgets.QMessageBox(
                QtWidgets.QMessageBox.Icon.Critical,
                "Ошибка авторизации",
                "Пароли не совпадают",
                QtWidgets.QMessageBox.Close,
            ).exec()
        else:
            u.register(u.User(username=username, password=password))
            self.ui.registerUsernameField.clear()
            self.ui.registerPasswordField.clear()
            self.ui.registerRepeatPasswordField.clear()
            self.ui.registerShowPasswordCheckbox.setChecked(False)
            self.ui.authTabWidget.setCurrentIndex(0)

    def show_password(self, fields: list[QtWidgets.QLineEdit]) -> Callable[[bool], None]:
        def _show_password(show: bool) -> None:
            for field in fields:
                field.setEchoMode(
                    QtWidgets.QLineEdit.EchoMode.Normal
                    if show
                    else QtWidgets.QLineEdit.EchoMode.Password
                )

        return _show_password
