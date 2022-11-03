# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './gui/dialogs/editor.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_QuizEditor(object):
    def setupUi(self, QuizEditor):
        QuizEditor.setObjectName("QuizEditor")
        QuizEditor.resize(500, 673)
        QuizEditor.setMinimumSize(QtCore.QSize(500, 0))
        QuizEditor.setMaximumSize(QtCore.QSize(500, 16777215))
        self.verticalLayout = QtWidgets.QVBoxLayout(QuizEditor)
        self.verticalLayout.setObjectName("verticalLayout")
        self.inputField = QtWidgets.QHBoxLayout()
        self.inputField.setObjectName("inputField")
        self.label = QtWidgets.QLabel(QuizEditor)
        self.label.setMaximumSize(QtCore.QSize(150, 150))
        self.label.setPixmap(QtGui.QPixmap(":/src/src/no-file.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.inputField.addWidget(self.label)
        self.labelField = QtWidgets.QLineEdit(QuizEditor)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.labelField.setFont(font)
        self.labelField.setFrame(True)
        self.labelField.setObjectName("labelField")
        self.inputField.addWidget(self.labelField)
        self.verticalLayout.addLayout(self.inputField)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.imageURLField = QtWidgets.QLineEdit(QuizEditor)
        self.imageURLField.setMinimumSize(QtCore.QSize(150, 0))
        self.imageURLField.setObjectName("imageURLField")
        self.horizontalLayout_2.addWidget(self.imageURLField)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.scrollArea = QtWidgets.QScrollArea(QuizEditor)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 484, 367))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.pushButton = QtWidgets.QPushButton(QuizEditor)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/src/src/plus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setAutoDefault(False)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(QuizEditor)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/src/src/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setAutoDefault(False)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)

        self.retranslateUi(QuizEditor)
        QtCore.QMetaObject.connectSlotsByName(QuizEditor)

    def retranslateUi(self, QuizEditor):
        _translate = QtCore.QCoreApplication.translate
        QuizEditor.setWindowTitle(_translate("QuizEditor", "Editor"))
        self.labelField.setPlaceholderText(_translate("QuizEditor", "Название теста"))
        self.imageURLField.setPlaceholderText(_translate("QuizEditor", "Ссылка на изображение"))
        self.pushButton.setText(_translate("QuizEditor", "Добавить поле"))
        self.pushButton_2.setText(_translate("QuizEditor", "Сохранить"))
import src_rc
