# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './gui/widgets/editor/forms/checkbox.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Checkbox(object):
    def setupUi(self, Checkbox):
        Checkbox.setObjectName("Checkbox")
        Checkbox.resize(475, 38)
        Checkbox.setMinimumSize(QtCore.QSize(475, 0))
        self.verticalLayout = QtWidgets.QVBoxLayout(Checkbox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.defaultValue = QtWidgets.QCheckBox(Checkbox)
        self.defaultValue.setObjectName("defaultValue")
        self.verticalLayout.addWidget(self.defaultValue)

        self.retranslateUi(Checkbox)
        QtCore.QMetaObject.connectSlotsByName(Checkbox)

    def retranslateUi(self, Checkbox):
        _translate = QtCore.QCoreApplication.translate
        Checkbox.setWindowTitle(_translate("Checkbox", "Checkbox"))
        self.defaultValue.setText(_translate("Checkbox", "Значение по умолчанию"))
