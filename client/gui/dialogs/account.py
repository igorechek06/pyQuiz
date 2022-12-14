# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './gui/dialogs/account.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AccountDialog(object):
    def setupUi(self, AccountDialog):
        AccountDialog.setObjectName("AccountDialog")
        AccountDialog.resize(400, 500)
        AccountDialog.setMinimumSize(QtCore.QSize(400, 500))
        AccountDialog.setMaximumSize(QtCore.QSize(400, 500))
        self.verticalLayout = QtWidgets.QVBoxLayout(AccountDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.usernameLabel = QtWidgets.QLabel(AccountDialog)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.usernameLabel.setFont(font)
        self.usernameLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.usernameLabel.setWordWrap(True)
        self.usernameLabel.setObjectName("usernameLabel")
        self.verticalLayout.addWidget(self.usernameLabel)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.eidtUsernameLabel = QtWidgets.QLabel(AccountDialog)
        self.eidtUsernameLabel.setObjectName("eidtUsernameLabel")
        self.verticalLayout.addWidget(self.eidtUsernameLabel)
        self.usernameField = QtWidgets.QLineEdit(AccountDialog)
        self.usernameField.setObjectName("usernameField")
        self.verticalLayout.addWidget(self.usernameField)
        self.editPassowrdLabel = QtWidgets.QLabel(AccountDialog)
        self.editPassowrdLabel.setObjectName("editPassowrdLabel")
        self.verticalLayout.addWidget(self.editPassowrdLabel)
        self.passwordField = QtWidgets.QLineEdit(AccountDialog)
        self.passwordField.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordField.setObjectName("passwordField")
        self.verticalLayout.addWidget(self.passwordField)
        self.repeatPasswordField = QtWidgets.QLineEdit(AccountDialog)
        self.repeatPasswordField.setEchoMode(QtWidgets.QLineEdit.Password)
        self.repeatPasswordField.setObjectName("repeatPasswordField")
        self.verticalLayout.addWidget(self.repeatPasswordField)
        self.showPasswordCheckBox = QtWidgets.QCheckBox(AccountDialog)
        self.showPasswordCheckBox.setObjectName("showPasswordCheckBox")
        self.verticalLayout.addWidget(self.showPasswordCheckBox)
        self.buttonsLayout1 = QtWidgets.QHBoxLayout()
        self.buttonsLayout1.setObjectName("buttonsLayout1")
        self.logoutButton = QtWidgets.QPushButton(AccountDialog)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/src/src/logout.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.logoutButton.setIcon(icon)
        self.logoutButton.setAutoDefault(False)
        self.logoutButton.setObjectName("logoutButton")
        self.buttonsLayout1.addWidget(self.logoutButton)
        self.deleteButton = QtWidgets.QPushButton(AccountDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.deleteButton.sizePolicy().hasHeightForWidth())
        self.deleteButton.setSizePolicy(sizePolicy)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/src/src/delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.deleteButton.setIcon(icon1)
        self.deleteButton.setAutoDefault(False)
        self.deleteButton.setObjectName("deleteButton")
        self.buttonsLayout1.addWidget(self.deleteButton)
        self.verticalLayout.addLayout(self.buttonsLayout1)
        self.saveButton = QtWidgets.QPushButton(AccountDialog)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/src/src/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.saveButton.setIcon(icon2)
        self.saveButton.setAutoDefault(False)
        self.saveButton.setObjectName("saveButton")
        self.verticalLayout.addWidget(self.saveButton)

        self.retranslateUi(AccountDialog)
        self.passwordField.returnPressed.connect(self.repeatPasswordField.setFocus) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(AccountDialog)

    def retranslateUi(self, AccountDialog):
        _translate = QtCore.QCoreApplication.translate
        AccountDialog.setWindowTitle(_translate("AccountDialog", "Account"))
        self.usernameLabel.setText(_translate("AccountDialog", "User name"))
        self.eidtUsernameLabel.setText(_translate("AccountDialog", "???????????????? ?????? ????????????????????????"))
        self.usernameField.setPlaceholderText(_translate("AccountDialog", "?????????? ?????? ????????????????????????"))
        self.editPassowrdLabel.setText(_translate("AccountDialog", "???????????????? ????????????"))
        self.passwordField.setPlaceholderText(_translate("AccountDialog", "?????????? ????????????"))
        self.repeatPasswordField.setPlaceholderText(_translate("AccountDialog", "?????????????????? ?????????? ????????????"))
        self.showPasswordCheckBox.setText(_translate("AccountDialog", "???????????????? ????????????"))
        self.logoutButton.setText(_translate("AccountDialog", "??????????"))
        self.deleteButton.setText(_translate("AccountDialog", "?????????????? ??????????????"))
        self.saveButton.setText(_translate("AccountDialog", "??????????????????"))
import src_rc
