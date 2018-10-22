# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dashboard.ui.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import ibm_db
from userView import *


class Ui_fbLbl(object):
    print("dashboard callled!!!!!")
    conn = ''
    query_contact = ''
    query_username = ''
    query_email = ''
    query_username1 = ''
    query_conatact2 = ''
    query_email3 = ''

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

    def statusPage(self):
        print("1")
        self.window = QtWidgets.QMainWindow()
        self.statusview = Ui_MainWindowBoard()
        print("happends!")
        self.statusview.NameHolder(self.query_username1)
        self.statusview.setupUistatus(self.window)
        self.window.show()
        print("3")

    def callFun(self, name={'USERNAME': ''}):
        print("cloud call")
        Ui_fbLbl.cloudConnectiontwo()
        print("cloud connted ffinally")
        self.name = name
        # print(self.name)
        query1 = "SELECT USERNAME FROM WKG83160.USERS1 where USERNAME = '%s'" % self.name
        self.query_username = ibm_db.exec_immediate(conn, query1)

        var1 = ibm_db.fetch_both(self.query_username)
        self.query_username1 = var1['USERNAME']

        query2 = "SELECT CONTACT FROM WKG83160.USERS1 where USERNAME = '%s'" % self.name
        self.query_contact = ibm_db.exec_immediate(conn, query2)
        var2 = ibm_db.fetch_both(self.query_contact)
        self.query_conatact2 = var2['CONTACT']
        query3 = "SELECT EMAIL FROM WKG83160.USERS1 where USERNAME = '%s'" % self.name
        self.query_email = ibm_db.exec_immediate(conn, query3)
        var3 = ibm_db.fetch_both(self.query_email)
        self.query_email3 = var3['EMAIL']
        print("end here!")

        # query4 = "SELECT isntagram FROM links WHERE  "

    def booksRecommentdation(self):
        # dict to maintain mood with book generes
        books_mood = {'Joy': 'Mystery', 'Fear': 'Science Fiction & Fantasy', 'Confident': 'Literatue & Fiction',
                      'Sadness': 'Humor & Entertainment', 'Anger': 'Thriller & Suspense',
                      'Analytical': 'Science Fiction & Fantasy', 'Tentative': 'Comics & Graphics Novels'}
        print("in booksrecommed fun")
        # someobj = Ui_MainWindowBoard()
        # mainobj = someobj.temp
        # mood = books_mood[mainobj]
        # print(mood)

    def setupUidash(self, fbLbl):
        fbLbl.setObjectName("fbLbl")
        fbLbl.resize(960, 640)
        fbLbl.setMinimumSize(QtCore.QSize(960, 640))
        fbLbl.setMaximumSize(QtCore.QSize(960, 640))
        fbLbl.setStyleSheet("background-image: url(:/newPrefix/watsonLogo.jpeg);\n"
                            "color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(fbLbl)
        self.centralwidget.setObjectName("centralwidget")
        self.dahbboardLbl = QtWidgets.QLabel(self.centralwidget)
        self.dahbboardLbl.setGeometry(QtCore.QRect(450, 20, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.dahbboardLbl.setFont(font)
        self.dahbboardLbl.setStyleSheet("color: rgb(255, 255, 255);")
        self.dahbboardLbl.setObjectName("dahbboardLbl")
        self.unameLbl = QtWidgets.QLabel(self.centralwidget)
        self.unameLbl.setGeometry(QtCore.QRect(80, 80, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.unameLbl.setFont(font)
        self.unameLbl.setObjectName("unameLbl")
        self.contactLbl = QtWidgets.QLabel(self.centralwidget)
        self.contactLbl.setGeometry(QtCore.QRect(80, 120, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.contactLbl.setFont(font)
        self.contactLbl.setObjectName("contactLbl")
        self.emailLbl = QtWidgets.QLabel(self.centralwidget)
        self.emailLbl.setGeometry(QtCore.QRect(80, 160, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.emailLbl.setFont(font)
        self.emailLbl.setObjectName("emailLbl")
        self.fbLbl_2 = QtWidgets.QLabel(self.centralwidget)
        self.fbLbl_2.setGeometry(QtCore.QRect(550, 80, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.fbLbl_2.setFont(font)
        self.fbLbl_2.setObjectName("fbLbl_2")
        self.twitterLbl = QtWidgets.QLabel(self.centralwidget)
        self.twitterLbl.setGeometry(QtCore.QRect(550, 120, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.twitterLbl.setFont(font)
        self.twitterLbl.setObjectName("twitterLbl")
        self.instaLbl = QtWidgets.QLabel(self.centralwidget)
        self.instaLbl.setGeometry(QtCore.QRect(550, 160, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.instaLbl.setFont(font)
        self.instaLbl.setObjectName("instaLbl")
        self.editBtn = QtWidgets.QPushButton(self.centralwidget)
        self.editBtn.setGeometry(QtCore.QRect(860, 70, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.editBtn.setFont(font)
        self.editBtn.setObjectName("editBtn")
        ####################status btn clicked##########
        self.editBtn.clicked.connect(self.statusPage)
        ################################################
        font = QtGui.QFont()
        font.setPointSize(12)
        self.recommendListLbl = QtWidgets.QListWidget(self.centralwidget)
        self.recommendListLbl.setGeometry(QtCore.QRect(80, 300, 571, 311))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.recommendListLbl.setFont(font)
        self.recommendListLbl.setStyleSheet("background-image: url(:/newPrefix/blueBg.png);        ")
        self.recommendListLbl.setObjectName("recommendListLbl")
        item = QtWidgets.QListWidgetItem()
        # ------------books list name--------------
        self.recommendListLbl.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.recommendListLbl.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.recommendListLbl.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.recommendListLbl.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.recommendListLbl.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.recommendListLbl.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.recommendListLbl.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.recommendListLbl.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.recommendListLbl.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.recommendListLbl.addItem(item)
        self.myReccomendLbl = QtWidgets.QLabel(self.centralwidget)
        self.myReccomendLbl.setGeometry(QtCore.QRect(80, 270, 531, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.myReccomendLbl.setFont(font)
        self.myReccomendLbl.setObjectName("myReccomendLbl")
        self.instaIcon = QtWidgets.QLabel(self.centralwidget)
        self.instaIcon.setGeometry(QtCore.QRect(500, 160, 31, 31))
        self.instaIcon.setStyleSheet("background-image: url(:/newPrefix/instagram.png);")
        self.instaIcon.setText("")
        self.instaIcon.setObjectName("instaIcon")
        self.twitterIcon = QtWidgets.QLabel(self.centralwidget)
        self.twitterIcon.setGeometry(QtCore.QRect(500, 120, 31, 31))
        self.twitterIcon.setStyleSheet("background-image: url(:/newPrefix/twitter.png);    ")
        self.twitterIcon.setText("")
        self.twitterIcon.setObjectName("twitterIcon")
        self.fbIcon = QtWidgets.QLabel(self.centralwidget)
        self.fbIcon.setGeometry(QtCore.QRect(500, 80, 31, 31))
        self.fbIcon.setStyleSheet("background-image: url(:/newPrefix/facebook.png);\n"
                                  "")
        self.fbIcon.setText("")
        self.fbIcon.setObjectName("fbIcon")
        self.pswdLbl = QtWidgets.QLabel(self.centralwidget)
        self.pswdLbl.setGeometry(QtCore.QRect(80, 200, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pswdLbl.setFont(font)
        self.pswdLbl.setObjectName("pswdLbl")
        fbLbl.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(fbLbl)
        self.statusbar.setObjectName("statusbar")
        fbLbl.setStatusBar(self.statusbar)

        self.retranslateUi(fbLbl)
        QtCore.QMetaObject.connectSlotsByName(fbLbl)

    def retranslateUi(self, fbLbl):
        self.username_on_dash = "Username : " + self.query_username1
        self.contact_on_dash = "Contact : " + self.query_conatact2
        self.email_on_dash = "Email : " + self.query_email3

        # function call for recommendations of books based on mood!
        self.booksRecommentdation()

        _translate = QtCore.QCoreApplication.translate
        fbLbl.setWindowTitle(_translate("fbLbl", "Dash board"))
        self.dahbboardLbl.setText(_translate("fbLbl", "DASHBOARD"))
        self.unameLbl.setText(_translate("fbLbl", self.username_on_dash))
        self.contactLbl.setText(_translate("fbLbl", self.contact_on_dash))
        self.emailLbl.setText(_translate("fbLbl", self.email_on_dash))
        self.fbLbl_2.setText(_translate("fbLbl", "Facebbok Id"))
        self.twitterLbl.setText(_translate("fbLbl", "Twitter Id"))
        self.instaLbl.setText(_translate("fbLbl", "Instagram Id"))
        self.editBtn.setText(_translate("fbLbl", "STATUS"))
        __sortingEnabled = self.recommendListLbl.isSortingEnabled()
        self.recommendListLbl.setSortingEnabled(False)
        item = self.recommendListLbl.item(0)
        item.setText(_translate("fbLbl", "Dream come true by Mr. AB"))
        item = self.recommendListLbl.item(1)
        item.setText(_translate("fbLbl", "You can sell by SHIV KHERA"))
        item = self.recommendListLbl.item(2)
        item.setText(_translate("fbLbl", "You can win By SHIV KHERA"))
        item = self.recommendListLbl.item(3)
        item.setText(_translate("fbLbl", "From zero to one by ALEX MORTEN"))
        item = self.recommendListLbl.item(4)
        item.setText(_translate("fbLbl", "Think and grow rich by NAPOLEAN HILL"))
        item = self.recommendListLbl.item(5)
        item.setText(_translate("fbLbl", "The Leader with no title by ROBIN SHARMA"))
        item = self.recommendListLbl.item(6)
        item.setText(_translate("fbLbl", "Dream come true by Mr. AB"))
        item = self.recommendListLbl.item(7)
        item.setText(_translate("fbLbl", "The monk who sold his ferrari by ROBIN"))
        item = self.recommendListLbl.item(8)
        item.setText(_translate("fbLbl", "Fairy tails By Unknown"))
        item = self.recommendListLbl.item(9)
        item.setText(_translate("fbLbl", "Chhotu Motu BALHANS"))
        self.recommendListLbl.setSortingEnabled(__sortingEnabled)
        self.myReccomendLbl.setText(_translate("fbLbl", "Recommendations of Books on based of recent comments"))


import picsIBM_rc

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    fbLbl = QtWidgets.QMainWindow()
    ui = Ui_fbLbl()
    ui.setupUidash(fbLbl)
    fbLbl.show()
    sys.exit(app.exec_())
