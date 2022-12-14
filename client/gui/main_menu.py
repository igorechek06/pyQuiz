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
        MainMenu.resize(600, 850)
        MainMenu.setMinimumSize(QtCore.QSize(600, 0))
        MainMenu.setMaximumSize(QtCore.QSize(600, 850))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/src/src/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainMenu.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainMenu)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.topLayout = QtWidgets.QHBoxLayout()
        self.topLayout.setObjectName("topLayout")
        self.authButton = QtWidgets.QPushButton(self.centralwidget)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/src/src/user.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.authButton.setIcon(icon1)
        self.authButton.setAutoDefault(False)
        self.authButton.setObjectName("authButton")
        self.topLayout.addWidget(self.authButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.topLayout.addItem(spacerItem)
        self.searchField = QtWidgets.QLineEdit(self.centralwidget)
        self.searchField.setClearButtonEnabled(True)
        self.searchField.setObjectName("searchField")
        self.topLayout.addWidget(self.searchField)
        self.searchButton = QtWidgets.QPushButton(self.centralwidget)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/src/src/search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.searchButton.setIcon(icon2)
        self.searchButton.setAutoDefault(False)
        self.searchButton.setObjectName("searchButton")
        self.topLayout.addWidget(self.searchButton)
        self.verticalLayout_2.addLayout(self.topLayout)
        self.quizzesArea = QtWidgets.QScrollArea(self.centralwidget)
        self.quizzesArea.setWidgetResizable(True)
        self.quizzesArea.setObjectName("quizzesArea")
        self.quizzesLayout = QtWidgets.QWidget()
        self.quizzesLayout.setGeometry(QtCore.QRect(0, 0, 584, 700))
        self.quizzesLayout.setObjectName("quizzesLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.quizzesLayout)
        self.verticalLayout.setObjectName("verticalLayout")
        self.quizzesArea.setWidget(self.quizzesLayout)
        self.verticalLayout_2.addWidget(self.quizzesArea)
        self.bottomLayout = QtWidgets.QHBoxLayout()
        self.bottomLayout.setObjectName("bottomLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.bottomLayout.addItem(spacerItem1)
        self.pageSelectorPrevButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pageSelectorPrevButton.sizePolicy().hasHeightForWidth())
        self.pageSelectorPrevButton.setSizePolicy(sizePolicy)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/src/src/prev.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pageSelectorPrevButton.setIcon(icon3)
        self.pageSelectorPrevButton.setAutoRepeat(True)
        self.pageSelectorPrevButton.setAutoDefault(False)
        self.pageSelectorPrevButton.setObjectName("pageSelectorPrevButton")
        self.bottomLayout.addWidget(self.pageSelectorPrevButton)
        self.pageSelectorField = QtWidgets.QSpinBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pageSelectorField.sizePolicy().hasHeightForWidth())
        self.pageSelectorField.setSizePolicy(sizePolicy)
        self.pageSelectorField.setAlignment(QtCore.Qt.AlignCenter)
        self.pageSelectorField.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.pageSelectorField.setMinimum(1)
        self.pageSelectorField.setMaximum(1)
        self.pageSelectorField.setObjectName("pageSelectorField")
        self.bottomLayout.addWidget(self.pageSelectorField)
        self.pageSelectorNextButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pageSelectorNextButton.sizePolicy().hasHeightForWidth())
        self.pageSelectorNextButton.setSizePolicy(sizePolicy)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/src/src/next.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pageSelectorNextButton.setIcon(icon4)
        self.pageSelectorNextButton.setAutoRepeat(True)
        self.pageSelectorNextButton.setAutoDefault(False)
        self.pageSelectorNextButton.setObjectName("pageSelectorNextButton")
        self.bottomLayout.addWidget(self.pageSelectorNextButton)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.bottomLayout.addItem(spacerItem2)
        self.verticalLayout_2.addLayout(self.bottomLayout)
        self.createQuizButton = QtWidgets.QPushButton(self.centralwidget)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/src/src/plus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.createQuizButton.setIcon(icon5)
        self.createQuizButton.setAutoDefault(False)
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
        self.authButton.setText(_translate("MainMenu", "????????????????????????????"))
        self.searchField.setPlaceholderText(_translate("MainMenu", "?????? ????????????"))
        self.searchButton.setText(_translate("MainMenu", "??????????"))
        self.pageSelectorField.setSuffix(_translate("MainMenu", "/1"))
        self.createQuizButton.setText(_translate("MainMenu", "?????????????? ??????????"))
import src_rc
