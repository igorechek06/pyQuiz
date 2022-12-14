# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './gui/widgets/editor/forms/integer.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Integer(object):
    def setupUi(self, Integer):
        Integer.setObjectName("Integer")
        Integer.resize(475, 214)
        Integer.setMinimumSize(QtCore.QSize(475, 0))
        self.verticalLayout = QtWidgets.QVBoxLayout(Integer)
        self.verticalLayout.setObjectName("verticalLayout")
        self.defaultLayout = QtWidgets.QHBoxLayout()
        self.defaultLayout.setObjectName("defaultLayout")
        self.defaultLabel = QtWidgets.QLabel(Integer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.defaultLabel.sizePolicy().hasHeightForWidth())
        self.defaultLabel.setSizePolicy(sizePolicy)
        self.defaultLabel.setObjectName("defaultLabel")
        self.defaultLayout.addWidget(self.defaultLabel)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.defaultLayout.addItem(spacerItem)
        self.defaultField = QtWidgets.QSpinBox(Integer)
        self.defaultField.setMinimumSize(QtCore.QSize(200, 0))
        self.defaultField.setMinimum(-2147483647)
        self.defaultField.setMaximum(2147483647)
        self.defaultField.setObjectName("defaultField")
        self.defaultLayout.addWidget(self.defaultField)
        self.verticalLayout.addLayout(self.defaultLayout)
        self.minValueLayout = QtWidgets.QHBoxLayout()
        self.minValueLayout.setObjectName("minValueLayout")
        self.minValueLabel = QtWidgets.QLabel(Integer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.minValueLabel.sizePolicy().hasHeightForWidth())
        self.minValueLabel.setSizePolicy(sizePolicy)
        self.minValueLabel.setObjectName("minValueLabel")
        self.minValueLayout.addWidget(self.minValueLabel)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.minValueLayout.addItem(spacerItem1)
        self.minValueField = QtWidgets.QSpinBox(Integer)
        self.minValueField.setMinimumSize(QtCore.QSize(200, 0))
        self.minValueField.setMinimum(-2147483647)
        self.minValueField.setMaximum(2147483647)
        self.minValueField.setObjectName("minValueField")
        self.minValueLayout.addWidget(self.minValueField)
        self.verticalLayout.addLayout(self.minValueLayout)
        self.maxValueLayout = QtWidgets.QHBoxLayout()
        self.maxValueLayout.setObjectName("maxValueLayout")
        self.maxValueLabel = QtWidgets.QLabel(Integer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.maxValueLabel.sizePolicy().hasHeightForWidth())
        self.maxValueLabel.setSizePolicy(sizePolicy)
        self.maxValueLabel.setObjectName("maxValueLabel")
        self.maxValueLayout.addWidget(self.maxValueLabel)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.maxValueLayout.addItem(spacerItem2)
        self.maxValueField = QtWidgets.QSpinBox(Integer)
        self.maxValueField.setMinimumSize(QtCore.QSize(200, 0))
        self.maxValueField.setMinimum(-2147483647)
        self.maxValueField.setMaximum(2147483647)
        self.maxValueField.setObjectName("maxValueField")
        self.maxValueLayout.addWidget(self.maxValueField)
        self.verticalLayout.addLayout(self.maxValueLayout)
        self.stepLayout = QtWidgets.QHBoxLayout()
        self.stepLayout.setObjectName("stepLayout")
        self.stepLabel = QtWidgets.QLabel(Integer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stepLabel.sizePolicy().hasHeightForWidth())
        self.stepLabel.setSizePolicy(sizePolicy)
        self.stepLabel.setObjectName("stepLabel")
        self.stepLayout.addWidget(self.stepLabel)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.stepLayout.addItem(spacerItem3)
        self.stepField = QtWidgets.QSpinBox(Integer)
        self.stepField.setMinimumSize(QtCore.QSize(200, 0))
        self.stepField.setMinimum(1)
        self.stepField.setMaximum(2147483647)
        self.stepField.setObjectName("stepField")
        self.stepLayout.addWidget(self.stepField)
        self.verticalLayout.addLayout(self.stepLayout)
        self.increaseButtonsCheckbox = QtWidgets.QCheckBox(Integer)
        self.increaseButtonsCheckbox.setChecked(True)
        self.increaseButtonsCheckbox.setObjectName("increaseButtonsCheckbox")
        self.verticalLayout.addWidget(self.increaseButtonsCheckbox)

        self.retranslateUi(Integer)
        QtCore.QMetaObject.connectSlotsByName(Integer)

    def retranslateUi(self, Integer):
        _translate = QtCore.QCoreApplication.translate
        Integer.setWindowTitle(_translate("Integer", "Integer"))
        self.defaultLabel.setText(_translate("Integer", "???????????????? ???? ??????????????????"))
        self.minValueLabel.setText(_translate("Integer", "?????????????????????? ????????????????"))
        self.maxValueLabel.setText(_translate("Integer", "???????????????????????? ????????????????"))
        self.stepLabel.setText(_translate("Integer", "?????? ????????????????????"))
        self.increaseButtonsCheckbox.setText(_translate("Integer", "???????????? ???????????????????? ??????????"))
