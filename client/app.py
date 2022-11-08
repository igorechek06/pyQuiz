from sys import argv

import keyring
from PyQt5 import QtWidgets

import dialogs
import widgets
import windows

if __name__ == "__main__":
    app = QtWidgets.QApplication(argv)
    window = windows.main.MainWindow(keyring.get_password("pyquiz", "token"))
    window.show()
    window.update_page()
    app.exec()
