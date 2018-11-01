# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'adminLogin.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import ibm_db
from mssbox import *
from adminsignup import *
from welcomeAdmin import *


class Ui_MainWindowAdmin(object):
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

    def clickLoginadmin(self):

        Ui_MainWindowAdmin.cloudConnectiontwo()
        username = self.a_uname.text()
        password = self.a_pswd.text()
        print(username, password)
        query = "SELECT * from WKG83160.Admin where username='%s' and pasd = '%s'" % (username, password)
        result = ibm_db.exec_immediate(conn, query)
        self.main_res = ibm_db.fetch_both(result)
        if (self.main_res == False):
            print("Not Found")
            obj = App()
        else:
            print("found")
            self.welcomewindowfun()

    def clickSignUpAdmin(self):
        self.windows = QtWidgets.QMainWindow()
        self.uiadminLog = Ui_MainWindowAdminSignUp()
        self.uiadminLog.setupUiSignUp(self.windows)
        self.windows.show()

    def welcomewindowfun(self):
        print("enter")
        self.window = QtWidgets.QMainWindow()
        self.windowobj = QtWidgets.QMainWindow()
        self.windowobj = Ui_MainWindowWelcome()
        self.windowobj.setupUiWelcome(self.window)
        self.window.show()
        print("exit")

    def setupUiforadmin(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(960, 640)
        MainWindow.setMinimumSize(QtCore.QSize(960, 640))
        MainWindow.setMaximumSize(QtCore.QSize(960, 640))
        MainWindow.setStyleSheet("background-image: url(:/newPrefix/watsonLogo.jpeg);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.a_uname = QtWidgets.QLineEdit(self.centralwidget)
        self.a_uname.setGeometry(QtCore.QRect(410, 260, 231, 25))
        self.a_uname.setStyleSheet("color: rgb(255, 255, 255);")
        self.a_uname.setObjectName("a_uname")
        self.pswdLbl = QtWidgets.QLabel(self.centralwidget)
        self.pswdLbl.setGeometry(QtCore.QRect(250, 300, 141, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.pswdLbl.setFont(font)
        self.pswdLbl.setStyleSheet("color: rgb(255, 255, 255);")
        self.pswdLbl.setObjectName("pswdLbl")
        self.loginLbl = QtWidgets.QLabel(self.centralwidget)
        self.loginLbl.setGeometry(QtCore.QRect(340, 120, 311, 71))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.loginLbl.setFont(font)
        self.loginLbl.setStyleSheet("color: rgb(255, 255, 255);")
        self.loginLbl.setObjectName("loginLbl")
        self.loginIcon = QtWidgets.QLabel(self.centralwidget)
        self.loginIcon.setGeometry(QtCore.QRect(220, 90, 141, 131))
        self.loginIcon.setStyleSheet("background-image: url(:/newPrefix/Login-01-128 (1).png);\n"
                                     "image: url(:/newPrefix/Login-01-128.png);")
        self.loginIcon.setText("")
        self.loginIcon.setObjectName("loginIcon")
        self.a_loginbtn = QtWidgets.QPushButton(self.centralwidget)
        self.a_loginbtn.setGeometry(QtCore.QRect(300, 430, 112, 34))
        ##############################signup #########################
        self.a_loginbtn.clicked.connect(self.clickSignUpAdmin)
        #############################################################
        font = QtGui.QFont()
        font.setPointSize(15)
        self.a_loginbtn.setFont(font)
        self.a_loginbtn.setStyleSheet("color: rgb(255, 255, 255);")
        self.a_loginbtn.setObjectName("a_loginbtn")
        self.a_pswd = QtWidgets.QLineEdit(self.centralwidget)
        self.a_pswd.setGeometry(QtCore.QRect(410, 320, 231, 25))
        self.a_pswd.setStyleSheet("color: rgb(255, 255, 255);")
        self.a_pswd.setObjectName("a_pswd")
        self.unameLbl = QtWidgets.QLabel(self.centralwidget)
        self.unameLbl.setGeometry(QtCore.QRect(250, 250, 141, 51))
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
        self.a_signupbtn = QtWidgets.QPushButton(self.centralwidget)
        self.a_signupbtn.setGeometry(QtCore.QRect(490, 430, 112, 34))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.a_signupbtn.setFont(font)
        self.a_signupbtn.setStyleSheet("color: rgb(255, 255, 255);")
        self.a_signupbtn.setAutoDefault(True)
        self.a_signupbtn.setDefault(False)
        self.a_signupbtn.setFlat(False)
        self.a_signupbtn.setObjectName("a_signupbtn")
        #######################3signup button clicked!###########
        self.a_signupbtn.clicked.connect(self.clickLoginadmin)
        #########################################################
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.a_uname.setPlaceholderText(_translate("MainWindow", "username"))
        self.pswdLbl.setText(_translate("MainWindow", "PASSWORD"))
        self.loginLbl.setText(_translate("MainWindow", "ADMIN LOGIN"))
        self.a_loginbtn.setText(_translate("MainWindow", "SIGN UP"))
        self.a_pswd.setPlaceholderText(_translate("MainWindow", "password"))
        self.unameLbl.setText(_translate("MainWindow", "USERNAME"))
        self.a_signupbtn.setText(_translate("MainWindow", "SUBMIT"))


import picsIBM_rc

if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindowAdmin()
    ui.setupUiforadmin(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
