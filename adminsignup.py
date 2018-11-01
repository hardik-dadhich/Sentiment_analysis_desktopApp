# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'adminSignup.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import ibm_db
from adminlogin import *

class Ui_MainWindowAdminSignUp(object):
    conn = ""

    def cloudConnectiontwo():
        print("called")
        dsn_driver = "IBM DB2 ODBC DRIVER"
        dsn_databases = "BLUDB"
        dsn_hostname = 'dashdb-txn-sbox-yp-lon02-01.services.eu-gb.bluemix.net'
        dsn_port = "50000"
        dsn_protocal = "TCPIP"
        dsn_uid = 'wkg83160'
        dsn_pwd = "8g2kgt18+2tljbrb"
        dsn = ("DRIVER={{IBM DB2 ODBC DRIVER}};"
               "DATABASE={0};"
               "HOSTNAME = {1};"
               "PORT = {2};"
               "PROTOCOL = TCPIP;"
               "UID={3};"
               "pwd ={4};").format(dsn_databases, dsn_hostname, dsn_port, dsn_uid, dsn_pwd)
        global conn
        conn = ibm_db.connect(dsn, "", "")
        print("cloud connected")

    def clickLoginAdmin(self):
        self.window = QtWidgets.QMainWindow()
        self.uiadminLog = Ui_MainWindowAdmin()
        self.uiadminLog.setupUiforadmin(self.window)
        self.window.show()

    def signup(self):
        Ui_MainWindowAdminSignUp.cloudConnectiontwo()
        username = self.unameInp.text()
        password = self.pswdInp.text()
        email = self.emailInp.text()
        conatct = int(self.contactInp.text())
        query = "insert into WKG83160.Admin(USERNAME, PASD, EMAIL, CONTACT) values ('%s','%s','%s','%s')" % (username, password, email, conatct)
        stmt = ibm_db.exec_immediate(conn, query)
        self.clickLoginAdmin()

    def setupUiSignUp(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(960, 640)
        MainWindow.setMinimumSize(QtCore.QSize(960, 640))
        MainWindow.setMaximumSize(QtCore.QSize(960, 640))
        MainWindow.setStyleSheet("background-image: url(:/newPrefix/watsonLogo.jpeg);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(220, -10, 121, 101))
        self.label.setStyleSheet("background-image:url(:/newPrefix/User-Login-128.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.signupLbl = QtWidgets.QLabel(self.centralwidget)
        self.signupLbl.setGeometry(QtCore.QRect(350, 20, 321, 61))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.signupLbl.setFont(font)
        self.signupLbl.setStyleSheet("color:rgb(255, 255, 255);")
        self.signupLbl.setObjectName("signupLbl")
        self.pswdLbl = QtWidgets.QLabel(self.centralwidget)
        self.pswdLbl.setGeometry(QtCore.QRect(280, 200, 141, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.pswdLbl.setFont(font)
        self.pswdLbl.setStyleSheet("color: rgb(255, 255, 255);")
        self.pswdLbl.setObjectName("pswdLbl")
        self.unameLbl = QtWidgets.QLabel(self.centralwidget)
        self.unameLbl.setGeometry(QtCore.QRect(280, 150, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.unameLbl.setFont(font)
        self.unameLbl.setStyleSheet("color: rgb(255, 255, 255);")
        self.unameLbl.setScaledContents(False)
        self.unameLbl.setWordWrap(False)
        self.unameLbl.setOpenExternalLinks(False)
        self.unameLbl.setObjectName("unameLbl")
        self.unameInp = QtWidgets.QLineEdit(self.centralwidget)
        self.unameInp.setGeometry(QtCore.QRect(440, 160, 231, 25))
        self.unameInp.setStyleSheet("color: rgb(255, 255, 255);")
        self.unameInp.setText("")
        self.unameInp.setObjectName("unameInp")
        self.contactInp = QtWidgets.QLineEdit(self.centralwidget)
        self.contactInp.setGeometry(QtCore.QRect(440, 340, 231, 25))
        self.contactInp.setStyleSheet("color: rgb(255, 255, 255);")
        self.contactInp.setText("")
        self.contactInp.setObjectName("contactInp")
        self.pswdInp = QtWidgets.QLineEdit(self.centralwidget)
        self.pswdInp.setGeometry(QtCore.QRect(440, 220, 231, 25))
        self.pswdInp.setStyleSheet("color: rgb(255, 255, 255);")
        self.pswdInp.setText("")
        self.pswdInp.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pswdInp.setObjectName("pswdInp")
        self.emailInp = QtWidgets.QLineEdit(self.centralwidget)
        self.emailInp.setGeometry(QtCore.QRect(440, 280, 231, 25))
        self.emailInp.setStyleSheet("color: rgb(255, 255, 255);")
        self.emailInp.setObjectName("emailInp")
        self.contactLbl = QtWidgets.QLabel(self.centralwidget)
        self.contactLbl.setGeometry(QtCore.QRect(280, 320, 141, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.contactLbl.setFont(font)
        self.contactLbl.setStyleSheet("color: rgb(255, 255, 255);")
        self.contactLbl.setObjectName("contactLbl")
        self.emailLbl = QtWidgets.QLabel(self.centralwidget)
        self.emailLbl.setGeometry(QtCore.QRect(280, 270, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.emailLbl.setFont(font)
        self.emailLbl.setStyleSheet("color: rgb(255, 255, 255);")
        self.emailLbl.setScaledContents(False)
        self.emailLbl.setWordWrap(False)
        self.emailLbl.setOpenExternalLinks(False)
        self.emailLbl.setObjectName("emailLbl")
        self.submitBtn = QtWidgets.QPushButton(self.centralwidget)
        self.submitBtn.setGeometry(QtCore.QRect(520, 460, 112, 34))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.submitBtn.setFont(font)
        self.submitBtn.setStyleSheet("color: rgb(255, 255, 255);")
        self.submitBtn.setAutoDefault(True)
        self.submitBtn.setDefault(False)
        self.submitBtn.setFlat(False)
        self.submitBtn.setObjectName("submitBtn")
        #################3submit button clicked #################
        self.submitBtn.clicked.connect(self.signup)
        ##########################################################
        self.loginBtn = QtWidgets.QPushButton(self.centralwidget)
        self.loginBtn.setGeometry(QtCore.QRect(330, 460, 112, 34))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.loginBtn.setFont(font)
        self.loginBtn.setStyleSheet("color: rgb(255, 255, 255);")
        self.loginBtn.setObjectName("loginBtn")
        #####################login button clicked!##############
        self.loginBtn.clicked.connect(self.clickLoginAdmin)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.signupLbl.setText(_translate("MainWindow", "ADMIN SIGNUP"))
        self.pswdLbl.setText(_translate("MainWindow", "PASSWORD"))
        self.unameLbl.setText(_translate("MainWindow", "USERNAME"))
        self.unameInp.setPlaceholderText(_translate("MainWindow", "username"))
        self.contactInp.setPlaceholderText(_translate("MainWindow", "contact"))
        self.pswdInp.setPlaceholderText(_translate("MainWindow", "password"))
        self.emailInp.setPlaceholderText(_translate("MainWindow", "email"))
        self.contactLbl.setText(_translate("MainWindow", "CONTACT"))
        self.emailLbl.setText(_translate("MainWindow", "EMAIL ID"))
        self.submitBtn.setText(_translate("MainWindow", "SUBMIT"))
        self.loginBtn.setText(_translate("MainWindow", "LOGIN"))

import picsIBM_rc

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindowAdminSignUp()
    ui.setupUiSignUp(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
