# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './gui/widgets/answer/fields/float.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Float(object):
    def setupUi(self, Float):
        Float.setObjectName("Float")
        Float.resize(400, 48)
        Float.setMinimumSize(QtCore.QSize(400, 0))
        Float.setMaximumSize(QtCore.QSize(475, 16777215))
        self.horizontalLayout = QtWidgets.QHBoxLayout(Float)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Float)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.field = QtWidgets.QDoubleSpinBox(Float)
        self.field.setObjectName("field")
        self.horizontalLayout.addWidget(self.field)

        self.retranslateUi(Float)
        QtCore.QMetaObject.connectSlotsByName(Float)

    def retranslateUi(self, Float):
        _translate = QtCore.QCoreApplication.translate
        Float.setWindowTitle(_translate("Float", "Float"))
        self.label.setText(_translate("Float", "Form label"))
