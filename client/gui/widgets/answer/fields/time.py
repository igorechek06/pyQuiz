# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './gui/widgets/answer/fields/time.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Time(object):
    def setupUi(self, Time):
        Time.setObjectName("Time")
        Time.resize(400, 48)
        Time.setMinimumSize(QtCore.QSize(400, 0))
        Time.setMaximumSize(QtCore.QSize(475, 16777215))
        self.horizontalLayout = QtWidgets.QHBoxLayout(Time)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Time)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.field = QtWidgets.QTimeEdit(Time)
        self.field.setObjectName("field")
        self.horizontalLayout.addWidget(self.field)

        self.retranslateUi(Time)
        QtCore.QMetaObject.connectSlotsByName(Time)

    def retranslateUi(self, Time):
        _translate = QtCore.QCoreApplication.translate
        Time.setWindowTitle(_translate("Time", "Time"))
        self.label.setText(_translate("Time", "Form label"))
        self.field.setDisplayFormat(_translate("Time", "HH:mm:ss"))