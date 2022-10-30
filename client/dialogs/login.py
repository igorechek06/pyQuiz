from typing import Callable

from PyQt5 import QtCore, QtWidgets

import gui
import models as m
from api import user


class AuthDialog(QtWidgets.QDialog):
    ui: gui.dialogs.login.Ui_AuthDialog
    token: str | None
    user: m.User | None

    def __init__(self, parent: QtWidgets.QWidget) -> None:
        super().__init__(parent)
        self.ui = gui.dialogs.login.Ui_AuthDialog()
        self.ui.setupUi(self)
        self.token = None
        self.user = None

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

    def login_button(self) -> None:
        username = self.ui.loginUsernameField.text()
        password = self.ui.loginPasswordField.text()
        try:
            self.token = user.login(username, password)
            self.user = user.me(self.token)
            self.close()
        except Exception:
            QtWidgets.QMessageBox(
                QtWidgets.QMessageBox.Icon.Critical,
                "Ошибка авторизации",
                "Пароль или логин неверные",
                QtWidgets.QMessageBox.Close,
            ).exec()

    def show_password(self, fields: list[QtWidgets.QLineEdit]) -> Callable[[bool], None]:
        def _show_password(show: bool) -> None:
            for field in fields:
                field.setEchoMode(
                    QtWidgets.QLineEdit.EchoMode.Normal
                    if show
                    else QtWidgets.QLineEdit.EchoMode.Password
                )

        return _show_password
