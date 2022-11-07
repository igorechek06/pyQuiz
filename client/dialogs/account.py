import keyring
from PyQt5 import QtWidgets

import gui
import models as m
import windows
from api import user as u


class AccountDialog(QtWidgets.QDialog):
    ui: gui.dialogs.account.Ui_AccountDialog
    context: "windows.main.MainWindow"

    def __init__(self, parent: "windows.main.MainWindow") -> None:
        super().__init__(parent)
        self.ui = gui.dialogs.account.Ui_AccountDialog()
        self.ui.setupUi(self)
        self.context = parent

        assert self.context.token is not None and self.context.user is not None
        self.ui.usernameLabel.setText(self.context.user.username)

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
            self.context.token = None
            self.context.user = None
            keyring.delete_password("pyquiz", "token")
            self.context.update_ui.emit()
            self.close()

    def delete(self) -> None:
        assert self.context.token is not None and self.context.user is not None
        if (
            QtWidgets.QMessageBox(
                QtWidgets.QMessageBox.Icon.Critical,
                "Confirmation",
                "Вы точно хотите удалить аккаунт ?",
                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
            ).exec()
            == QtWidgets.QMessageBox.Yes
        ):
            u.delete(self.context.token)
            self.context.token = None
            self.context.user = None
            keyring.delete_password("pyquiz", "token")
            self.context.update_page()
            self.close()

    def save(self) -> None:
        assert self.context.token is not None and self.context.user is not None
        username = self.ui.usernameField.text()
        password = self.ui.passwordField.text()

        if username != "":
            u.update_username(self.context.token, u.Username(username=username))
            self.ui.usernameField.clear()
            self.ui.usernameLabel.setText(username)
            self.context.user.username = username
        if password != "" or self.ui.repeatPasswordField.text() != "":
            if password != self.ui.repeatPasswordField.text():
                raise AssertionError("Пароли не совпадают")

            u.update_password(self.context.token, u.Password(password=password))
            self.context.token = None
            self.context.user = None
            keyring.delete_password("pyquiz", "token")

        self.context.update_ui.emit()
        self.close()
