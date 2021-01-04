# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'vowels.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(523, 575)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.BtnOpen = QtWidgets.QPushButton(self.centralwidget)
        self.BtnOpen.setObjectName("BtnOpen")
        self.gridLayout.addWidget(self.BtnOpen, 0, 0, 1, 1)
        self.TxtVowel = QtWidgets.QTextBrowser(self.centralwidget)
        self.TxtVowel.setObjectName("TxtVowel")
        self.gridLayout.addWidget(self.TxtVowel, 2, 0, 1, 1)
        self.TxtConsonant = QtWidgets.QTextBrowser(self.centralwidget)
        self.TxtConsonant.setObjectName("TxtConsonant")
        self.gridLayout.addWidget(self.TxtConsonant, 2, 1, 1, 1)
        self.BtnSave = QtWidgets.QPushButton(self.centralwidget)
        self.BtnSave.setObjectName("BtnSave")
        self.gridLayout.addWidget(self.BtnSave, 0, 1, 1, 1)
        self.LblVowel = QtWidgets.QLabel(self.centralwidget)
        self.LblVowel.setObjectName("LblVowel")
        self.gridLayout.addWidget(self.LblVowel, 1, 0, 1, 1)
        self.LblConsonant = QtWidgets.QLabel(self.centralwidget)
        self.LblConsonant.setObjectName("LblConsonant")
        self.gridLayout.addWidget(self.LblConsonant, 1, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 523, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Гласные и согласные"))
        self.BtnOpen.setText(_translate("MainWindow", "Выбрать файл"))
        self.BtnSave.setText(_translate("MainWindow", "Сохранить"))
        self.LblVowel.setText(_translate("MainWindow", "Гласные"))
        self.LblConsonant.setText(_translate("MainWindow", "Согласные"))

