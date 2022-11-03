from sys import argv

import keyring
from PyQt5.QtWidgets import QApplication

import dialogs
import widgets
import windows

if __name__ == "__main__":
    app = QApplication(argv)
    window = windows.main.MainWindow(keyring.get_password("pyquiz", "token"))
    window.show()
    window.page()
    app.exec()
