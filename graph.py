# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'graph.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from mailsend import *

class Ui_MainWindowGraphView(object):

    def emailClicked(self):
        self.sent_m = SendMail()
        self.sent_m.main()

    def setupUiGraph(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(960, 640)
        MainWindow.setMinimumSize(QtCore.QSize(960, 640))
        MainWindow.setMaximumSize(QtCore.QSize(960, 640))
        MainWindow.setStyleSheet("background-image: url(:/newPrefix/watsonLogo.jpeg);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.reportLbl = QtWidgets.QLabel(self.centralwidget)
        self.reportLbl.setGeometry(QtCore.QRect(310, 20, 411, 71))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.reportLbl.setFont(font)
        self.reportLbl.setStyleSheet("color: rgb(255, 255, 255);")
        self.reportLbl.setObjectName("reportLbl")
        self.sendMail_btn = QtWidgets.QPushButton(self.centralwidget)
        self.sendMail_btn.setGeometry(QtCore.QRect(700, 490, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.sendMail_btn.setFont(font)
        self.sendMail_btn.setStyleSheet("color: rgb(255, 255, 255);")
        self.sendMail_btn.setObjectName("sendMail_btn")
        ##################################################button email clicked######
        self.sendMail_btn.clicked.connect(self.emailClicked)
        ############################################################################
        self.graph1 = QtWidgets.QLabel(self.centralwidget)
        self.graph1.setGeometry(QtCore.QRect(60, 70, 610, 350))
        self.graph1.setMinimumSize(QtCore.QSize(610, 480))
        self.graph1.setMaximumSize(QtCore.QSize(610, 480))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.graph1.setFont(font)
        self.graph1.setStyleSheet("color: rgb(255, 255, 255);\n"
                                  "image: url(:/newPrefix/barplot1.png);")

        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.reportLbl.setText(_translate("MainWindow", "REPORT ANALYTICS"))
        self.sendMail_btn.setText(_translate("MainWindow", "SEND MAIL"))



import picsIBM_rc

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindowGraphView()
    ui.setupUiGraph(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
