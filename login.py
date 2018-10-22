# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from signup import *
import ibm_db
import ibmdbpy
from profile import *
from mssbox import *


class Ui_Login(object):
    def __init__(self):
        self.main_res = {}

    def profileview(self):
        print("called")
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.callme(self.main_res)
        self.ui.setupUi(self.window)
        self.window.show()

    def logincould():
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


    def clickLogin(self):

        Ui_Login.logincould()
        username = self.uname.text()
        password = self.pswd.text()
        print(username, password)
        query = "SELECT * from WKG83160.USERS1 where username='%s' and pasd = '%s'" % (username, password)
        result = ibm_db.exec_immediate(conn, query)
        self.main_res = ibm_db.fetch_both(result)
        if (self.main_res == False):
            print("Not Found")
            obj = App()
        else:
            print("found")
            self.profileview()

    def clickSignUp(self):
        self.window = QtWidgets.QMainWindow()
        self.uisignup = Ui_SignUp()
        self.uisignup.setupUiSignUp(self.window)
        self.window.show()

    def setupUiLogin(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(960, 640)
        MainWindow.setMinimumSize(QtCore.QSize(960, 640))
        MainWindow.setMaximumSize(QtCore.QSize(960, 640))
        MainWindow.setStyleSheet("background-image: url(:/newPrefix/watsonLogo.jpeg);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(320, 290, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setScaledContents(False)
        self.label.setWordWrap(False)
        self.label.setOpenExternalLinks(False)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(460, 180, 141, 71))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.uname = QtWidgets.QLineEdit(self.centralwidget)
        self.uname.setGeometry(QtCore.QRect(480, 300, 231, 25))
        self.uname.setStyleSheet("color: rgb(255, 255, 255);")
        self.uname.setObjectName("uname")
        self.pswd = QtWidgets.QLineEdit(self.centralwidget)
        self.pswd.setGeometry(QtCore.QRect(480, 360, 231, 25))
        self.pswd.setStyleSheet("color: rgb(255, 255, 255);")
        self.pswd.setText("")
        self.pswd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pswd.setObjectName("pswd")
        self.loginBtn = QtWidgets.QPushButton(self.centralwidget)
        self.loginBtn.setGeometry(QtCore.QRect(370, 470, 112, 34))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.loginBtn.setFont(font)
        self.loginBtn.setStyleSheet("color: rgb(255, 255, 255);")
        self.loginBtn.setObjectName("loginBtn")
        ####################login btn###################
        self.loginBtn.clicked.connect(self.clickLogin)
        ################################################
        self.signupBtn = QtWidgets.QPushButton(self.centralwidget)
        self.signupBtn.setGeometry(QtCore.QRect(560, 470, 112, 34))
        #########################signUp btn#######################
        self.signupBtn.clicked.connect(self.clickSignUp)
        ###################################################
        font = QtGui.QFont()
        font.setPointSize(15)
        self.signupBtn.setFont(font)
        self.signupBtn.setStyleSheet("color: rgb(255, 255, 255);")
        self.signupBtn.setAutoDefault(True)
        self.signupBtn.setDefault(False)
        self.signupBtn.setFlat(False)
        self.signupBtn.setObjectName("signupBtn")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(320, 340, 141, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(340, 130, 141, 131))
        self.label_4.setStyleSheet("background-image: url(:/newPrefix/Login-01-128.png);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Login"))
        self.label.setText(_translate("MainWindow", "USERNAME"))
        self.label_2.setText(_translate("MainWindow", "LOGIN"))
        self.uname.setPlaceholderText(_translate("MainWindow", "username"))
        self.pswd.setPlaceholderText(_translate("MainWindow", "password"))
        self.loginBtn.setText(_translate("MainWindow", "LOGIN"))
        self.signupBtn.setText(_translate("MainWindow", "SIGNUP"))
        self.label_3.setText(_translate("MainWindow", "PASSWORD"))


import picsIBM_rc

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Login()
    ui.setupUiLogin(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
