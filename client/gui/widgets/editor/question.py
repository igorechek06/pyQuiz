# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './gui/widgets/editor/question.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Question(object):
    def setupUi(self, Question):
        Question.setObjectName("Question")
        Question.resize(500, 500)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Question.sizePolicy().hasHeightForWidth())
        Question.setSizePolicy(sizePolicy)
        Question.setMinimumSize(QtCore.QSize(500, 400))
        self.verticalLayout = QtWidgets.QVBoxLayout(Question)
        self.verticalLayout.setObjectName("verticalLayout")
        self.titleField = QtWidgets.QLineEdit(Question)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.titleField.setFont(font)
        self.titleField.setAlignment(QtCore.Qt.AlignCenter)
        self.titleField.setObjectName("titleField")
        self.verticalLayout.addWidget(self.titleField)
        self.addButton = QtWidgets.QPushButton(Question)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/src/src/plus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addButton.setIcon(icon)
        self.addButton.setAutoDefault(False)
        self.addButton.setObjectName("addButton")
        self.verticalLayout.addWidget(self.addButton)
        self.formTabs = QtWidgets.QTabWidget(Question)
        self.formTabs.setMovable(True)
        self.formTabs.setObjectName("formTabs")
        self.verticalLayout.addWidget(self.formTabs)
        self.deleteButton = QtWidgets.QPushButton(Question)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/src/src/delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.deleteButton.setIcon(icon1)
        self.deleteButton.setAutoDefault(False)
        self.deleteButton.setObjectName("deleteButton")
        self.verticalLayout.addWidget(self.deleteButton)

        self.retranslateUi(Question)
        self.formTabs.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(Question)

    def retranslateUi(self, Question):
        _translate = QtCore.QCoreApplication.translate
        Question.setWindowTitle(_translate("Question", "Question"))
        self.titleField.setPlaceholderText(_translate("Question", "Заголовок вопроса"))
        self.addButton.setText(_translate("Question", "Добавить поле"))
        self.deleteButton.setText(_translate("Question", "Удалить"))
import src_rc
