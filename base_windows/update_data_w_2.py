# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'update_data_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(483, 191)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.UpdateDataBox = QtWidgets.QComboBox(self.centralwidget)
        self.UpdateDataBox.setMinimumSize(QtCore.QSize(200, 0))
        self.UpdateDataBox.setMaximumSize(QtCore.QSize(200, 16777215))
        self.UpdateDataBox.setObjectName("UpdateDataBox")
        self.gridLayout.addWidget(self.UpdateDataBox, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setIndent(15)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 1, 1, 1)
        self.UpdateDataEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.UpdateDataEdit.setMinimumSize(QtCore.QSize(200, 0))
        self.UpdateDataEdit.setMaximumSize(QtCore.QSize(200, 16777215))
        self.UpdateDataEdit.setObjectName("UpdateDataEdit")
        self.gridLayout.addWidget(self.UpdateDataEdit, 0, 2, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout, 1, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_3, 0, 0, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(256, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem, 1, 0, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.OkButton = QtWidgets.QPushButton(self.centralwidget)
        self.OkButton.setObjectName("OkButton")
        self.gridLayout_2.addWidget(self.OkButton, 1, 0, 1, 1)
        self.ExitButton = QtWidgets.QPushButton(self.centralwidget)
        self.ExitButton.setObjectName("ExitButton")
        self.gridLayout_2.addWidget(self.ExitButton, 1, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem1, 0, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_2, 1, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Изменить"))
        self.label.setText(_translate("MainWindow", "TextLabel"))
        self.label_3.setText(_translate("MainWindow", "~"))
        self.OkButton.setText(_translate("MainWindow", "Ок"))
        self.ExitButton.setText(_translate("MainWindow", "Отмена"))
