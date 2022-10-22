# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './gui/main_menu.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainMenu(object):
    def setupUi(self, MainMenu):
        MainMenu.setObjectName("MainMenu")
        MainMenu.resize(575, 690)
        MainMenu.setMinimumSize(QtCore.QSize(575, 0))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/src/src/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainMenu.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainMenu)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.searchLayout = QtWidgets.QHBoxLayout()
        self.searchLayout.setObjectName("searchLayout")
        self.searchField = QtWidgets.QLineEdit(self.centralwidget)
        self.searchField.setClearButtonEnabled(True)
        self.searchField.setObjectName("searchField")
        self.searchLayout.addWidget(self.searchField)
        self.searchButton = QtWidgets.QPushButton(self.centralwidget)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/src/src/search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.searchButton.setIcon(icon1)
        self.searchButton.setObjectName("searchButton")
        self.searchLayout.addWidget(self.searchButton)
        self.verticalLayout_2.addLayout(self.searchLayout)
        self.quizzesArea = QtWidgets.QScrollArea(self.centralwidget)
        self.quizzesArea.setWidgetResizable(True)
        self.quizzesArea.setObjectName("quizzesArea")
        self.quizzesLayout = QtWidgets.QWidget()
        self.quizzesLayout.setGeometry(QtCore.QRect(0, 0, 559, 540))
        self.quizzesLayout.setObjectName("quizzesLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.quizzesLayout)
        self.verticalLayout.setObjectName("verticalLayout")
        self.quizzesArea.setWidget(self.quizzesLayout)
        self.verticalLayout_2.addWidget(self.quizzesArea)
        self.pageSelectorLayout = QtWidgets.QHBoxLayout()
        self.pageSelectorLayout.setObjectName("pageSelectorLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.pageSelectorLayout.addItem(spacerItem)
        self.pageSelectorPrevButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pageSelectorPrevButton.sizePolicy().hasHeightForWidth())
        self.pageSelectorPrevButton.setSizePolicy(sizePolicy)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/src/src/prev.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pageSelectorPrevButton.setIcon(icon2)
        self.pageSelectorPrevButton.setAutoRepeat(True)
        self.pageSelectorPrevButton.setObjectName("pageSelectorPrevButton")
        self.pageSelectorLayout.addWidget(self.pageSelectorPrevButton)
        self.pageSelectorField = QtWidgets.QSpinBox(self.centralwidget)
        self.pageSelectorField.setAlignment(QtCore.Qt.AlignCenter)
        self.pageSelectorField.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.pageSelectorField.setMinimum(1)
        self.pageSelectorField.setMaximum(1)
        self.pageSelectorField.setObjectName("pageSelectorField")
        self.pageSelectorLayout.addWidget(self.pageSelectorField)
        self.pageSelectorNextButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pageSelectorNextButton.sizePolicy().hasHeightForWidth())
        self.pageSelectorNextButton.setSizePolicy(sizePolicy)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/src/src/next.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pageSelectorNextButton.setIcon(icon3)
        self.pageSelectorNextButton.setAutoRepeat(True)
        self.pageSelectorNextButton.setObjectName("pageSelectorNextButton")
        self.pageSelectorLayout.addWidget(self.pageSelectorNextButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.pageSelectorLayout.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.pageSelectorLayout)
        self.createQuizButton = QtWidgets.QPushButton(self.centralwidget)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/src/src/plus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.createQuizButton.setIcon(icon4)
        self.createQuizButton.setObjectName("createQuizButton")
        self.verticalLayout_2.addWidget(self.createQuizButton)
        MainMenu.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainMenu)
        self.pageSelectorNextButton.clicked.connect(self.pageSelectorField.stepUp) # type: ignore
        self.pageSelectorPrevButton.clicked.connect(self.pageSelectorField.stepDown) # type: ignore
        self.searchButton.clicked.connect(self.quizzesArea.setFocus) # type: ignore
        self.searchField.returnPressed.connect(self.searchButton.click) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainMenu)

    def retranslateUi(self, MainMenu):
        _translate = QtCore.QCoreApplication.translate
        MainMenu.setWindowTitle(_translate("MainMenu", "PyQuiz"))
        self.searchField.setPlaceholderText(_translate("MainMenu", "Имя или id"))
        self.searchButton.setText(_translate("MainMenu", "Найти"))
        self.createQuizButton.setText(_translate("MainMenu", "Создать"))
import src_rc