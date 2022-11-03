from typing import Callable

from PyQt5 import QtWidgets

import gui
import models as m
from api import user


class AccountDialog(QtWidgets.QDialog):
    ui: gui.dialogs.account.Ui_AccountDialog
    token: str | None
    user: m.User | None

    def __init__(self, parent: QtWidgets.QWidget, token: str, user: m.User) -> None:
        super().__init__(parent)
        self.ui = gui.dialogs.account.Ui_AccountDialog()
        self.ui.setupUi(self)
        self.token = token
        self.user = user

        self.ui.usernameLabel.setText(self.user.username)

        self.ui.showPasswordCheckBox.toggled.connect(self.show_password)
        self.ui.logoutButton.clicked.connect(self.logout)
        self.ui.deleteButton.clicked.connect(self.delete)
        self.ui.saveButton.clicked.connect(self.save)

    def show_password(self, check: bool) -> None:
        mode = (
            QtWidgets.QLineEdit.EchoMode.Normal
            if check
            else QtWidgets.QLineEdit.EchoMode.Password
        )
        self.ui.passwordField.setEchoMode(mode)
        self.ui.repeatPasswordField.setEchoMode(mode)

    def logout(self) -> None:
        if (
            QtWidgets.QMessageBox(
                QtWidgets.QMessageBox.Icon.Information,
                "Confirmation",
                "Вы точно хотите выйти ?",
                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
            ).exec()
            == QtWidgets.QMessageBox.Yes
        ):
            self.token = None
            self.user = None
            self.close()

    def delete(self) -> None:
        assert self.token is not None
        if (
            QtWidgets.QMessageBox(
                QtWidgets.QMessageBox.Icon.Critical,
                "Confirmation",
                "Вы точно хотите удалить аккаунт ?",
                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
            ).exec()
            == QtWidgets.QMessageBox.Yes
        ):
            user.delete(self.token)
            self.token = None
            self.user = None
            self.close()

    def save(self) -> None:
        assert self.token is not None and self.user is not None
        username = self.ui.usernameField.text()
        password = self.ui.passwordField.text()

        if username != "":
            user.username(self.token, username)
            self.ui.usernameField.clear()
            self.user.username = username
            self.ui.usernameLabel.setText(username)
        if password != "" or self.ui.repeatPasswordField.text() != "":
            if password != self.ui.repeatPasswordField.text():
                QtWidgets.QMessageBox(
                    QtWidgets.QMessageBox.Icon.Critical,
                    "Error",
                    "Пароли не совпадают",
                    QtWidgets.QMessageBox.Close,
                ).exec()
                return

            user.password(self.token, password)
            self.token = None
            self.user = None
            self.close()
