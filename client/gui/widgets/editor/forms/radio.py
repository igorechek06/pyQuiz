# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './gui/widgets/editor/forms/radio.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Radio(object):
    def setupUi(self, Radio):
        Radio.setObjectName("Radio")
        Radio.resize(475, 38)
        Radio.setMinimumSize(QtCore.QSize(475, 0))
        self.verticalLayout = QtWidgets.QVBoxLayout(Radio)
        self.verticalLayout.setObjectName("verticalLayout")
        self.defaultValue = QtWidgets.QRadioButton(Radio)
        self.defaultValue.setObjectName("defaultValue")
        self.verticalLayout.addWidget(self.defaultValue)

        self.retranslateUi(Radio)
        QtCore.QMetaObject.connectSlotsByName(Radio)

    def retranslateUi(self, Radio):
        _translate = QtCore.QCoreApplication.translate
        Radio.setWindowTitle(_translate("Radio", "Radio"))
        self.defaultValue.setText(_translate("Radio", "Значение по умолчанию"))
