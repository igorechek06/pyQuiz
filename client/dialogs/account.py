import keyring
from PyQt5 import QtWidgets

import gui
import models as m
from api import user
from windows.main import MainWindow


class AccountDialog(QtWidgets.QDialog):
    ui: gui.dialogs.account.Ui_AccountDialog
    context: MainWindow

    def __init__(self, parent: MainWindow) -> None:
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
            user.delete(self.context.token)
            self.context.token = None
            self.context.user = None
            keyring.delete_password("pyquiz", "token")
            self.context.update_ui.emit()
            self.close()

    def save(self) -> None:
        assert self.context.token is not None and self.context.user is not None
        username = self.ui.usernameField.text()
        password = self.ui.passwordField.text()

        if username != "":
            user.username(self.context.token, username)
            self.ui.usernameField.clear()
            self.ui.usernameLabel.setText(username)
            self.context.user.username = username
            self.context.update_ui.emit()
        if password != "" or self.ui.repeatPasswordField.text() != "":
            if password != self.ui.repeatPasswordField.text():
                QtWidgets.QMessageBox(
                    QtWidgets.QMessageBox.Icon.Critical,
                    "Error",
                    "Пароли не совпадают",
                    QtWidgets.QMessageBox.Close,
                ).exec()
                return

            user.password(self.context.token, password)
            self.context.token = None
            self.context.user = None
            keyring.delete_password("pyquiz", "token")
            self.context.update_ui.emit()
            self.close()
