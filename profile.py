from PyQt5 import QtCore, QtGui, QtWidgets
import picsIBM_rc
from dashboard import *
import ibm_db


class Ui_MainWindow(object):
    conn = ""
    tweeter_username = ''
    def callme(self, main_res={"USERNAME": ""}):
        self.main_res = main_res

    def usernamefun(self):
        t_user = ''
        print("in function buddy!")
        t_user = tweeter_username
        print(t_user)
        return t_user

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
        #ibm_db.close(conn)



    def gotodashboard(self):
        self.window = QtWidgets.QMainWindow()
        print("somthing")
        self.uiobj = Ui_fbLbl()
        print("caliing dashboad fun")
        self.uiobj.callFun(self.main_res['USERNAME'])
        self.uiobj.setupUidash(self.window)
        self.window.show()


    def insertDatainLinks(self):
        print("start")
        Ui_MainWindow.cloudConnectiontwo()
        print("cloud clonnecte 2")
        insta_link = self.instaInp.text()
        fb_link = self.fbInp.text()
        twitter_link = self.twitterInp.text()
        print(insta_link, fb_link, twitter_link)
        query_for_id_fetch = "Select id from WKG83160.USERS1 where USERNAME='%s'" % (self.main_res["USERNAME"])
        print(query_for_id_fetch)
        stmt1 = ibm_db.exec_immediate(conn, query_for_id_fetch)
        print(stmt1)
        ress = ibm_db.fetch_both(stmt1)
        print(ress['ID'])
        id_fetched = str(ress['ID'])
        self.query = "INSERT INTO WKG83160.LINKS(instagram, facebook, twitter, CUID) VALUES ('%s', '%s', '%s', '%s')"%(insta_link,fb_link,twitter_link, id_fetched)
        stmt = ibm_db.exec_immediate(conn, self.query)
        print(stmt)
        username_fetch = twitter_link.split('/')
        global tweeter_username
        tweeter_username = username_fetch[-1]
        print("-----user name from profile page", tweeter_username)
        self.gotodashboard()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(960, 640)
        MainWindow.setMinimumSize(QtCore.QSize(960, 640))
        MainWindow.setMaximumSize(QtCore.QSize(960, 640))
        MainWindow.setStyleSheet("background-image: url(:/newPrefix/watsonLogo.jpeg);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.welcomeLbl = QtWidgets.QLabel(self.centralwidget)
        self.welcomeLbl.setGeometry(QtCore.QRect(320, 30, 440, 61))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.welcomeLbl.setFont(font)
        self.welcomeLbl.setStyleSheet("color:rgb(255, 255, 255);")
        self.welcomeLbl.setObjectName("welcomeLbl")
        self.twitterLbl = QtWidgets.QLabel(self.centralwidget)
        self.twitterLbl.setGeometry(QtCore.QRect(280, 350, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.twitterLbl.setFont(font)
        self.twitterLbl.setStyleSheet("color: rgb(255, 255, 255);")
        self.twitterLbl.setScaledContents(False)
        self.twitterLbl.setWordWrap(False)
        self.twitterLbl.setOpenExternalLinks(False)
        self.twitterLbl.setObjectName("twitterLbl")
        self.userIcon = QtWidgets.QLabel(self.centralwidget)
        self.userIcon.setGeometry(QtCore.QRect(200, 0, 121, 111))
        self.userIcon.setStyleSheet("background-image:url(:/newPrefix/User-Login-128.png);")
        self.userIcon.setText("")
        self.userIcon.setObjectName("userIcon")
        self.submitBtn = QtWidgets.QPushButton(self.centralwidget)
        self.submitBtn.setGeometry(QtCore.QRect(310, 470, 112, 34))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.submitBtn.setFont(font)
        self.submitBtn.setStyleSheet("color: rgb(255, 255, 255);")
        self.submitBtn.setAutoDefault(True)
        self.submitBtn.setDefault(False)
        self.submitBtn.setFlat(False)
        self.submitBtn.setObjectName("submitBtn")
        #########################submit btn clikced##########
        self.submitBtn.clicked.connect(self.insertDatainLinks)
        #####################################################

        self.fbLbl = QtWidgets.QLabel(self.centralwidget)
        self.fbLbl.setGeometry(QtCore.QRect(280, 280, 141, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.fbLbl.setFont(font)
        self.fbLbl.setStyleSheet("color: rgb(255, 255, 255);")
        self.fbLbl.setObjectName("fbLbl")
        self.instaInp = QtWidgets.QLineEdit(self.centralwidget)
        self.instaInp.setGeometry(QtCore.QRect(440, 240, 231, 25))
        self.instaInp.setStyleSheet("color: rgb(255, 255, 255);")
        self.instaInp.setText("")
        self.instaInp.setObjectName("instaInp")
        self.resetBtn = QtWidgets.QPushButton(self.centralwidget)
        self.resetBtn.setGeometry(QtCore.QRect(490, 470, 112, 34))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.resetBtn.setFont(font)
        self.resetBtn.setStyleSheet("color: rgb(255, 255, 255);")
        self.resetBtn.setAutoDefault(True)
        self.resetBtn.setDefault(False)
        self.resetBtn.setFlat(False)
        self.resetBtn.setObjectName("resetBtn")
        self.instaLbl = QtWidgets.QLabel(self.centralwidget)
        self.instaLbl.setGeometry(QtCore.QRect(280, 230, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.instaLbl.setFont(font)
        self.instaLbl.setStyleSheet("color: rgb(255, 255, 255);")
        self.instaLbl.setScaledContents(False)
        self.instaLbl.setWordWrap(False)
        self.instaLbl.setOpenExternalLinks(False)
        self.instaLbl.setObjectName("instaLbl")
        self.twitterInp = QtWidgets.QLineEdit(self.centralwidget)
        self.twitterInp.setGeometry(QtCore.QRect(440, 360, 231, 25))
        self.twitterInp.setStyleSheet("color: rgb(255, 255, 255);")
        self.twitterInp.setObjectName("twitterInp")
        self.fbInp = QtWidgets.QLineEdit(self.centralwidget)
        self.fbInp.setGeometry(QtCore.QRect(440, 300, 231, 25))
        self.fbInp.setStyleSheet("color: rgb(255, 255, 255);")
        self.fbInp.setText("")
        self.fbInp.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.fbInp.setObjectName("fbInp")
        self.updateDetailsLbl = QtWidgets.QLabel(self.centralwidget)
        self.updateDetailsLbl.setGeometry(QtCore.QRect(140, 150, 291, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.updateDetailsLbl.setFont(font)
        self.updateDetailsLbl.setStyleSheet("color: rgb(255, 255, 255);")
        self.updateDetailsLbl.setObjectName("updateDetailsLbl")
        self.instaIcon = QtWidgets.QLabel(self.centralwidget)
        self.instaIcon.setGeometry(QtCore.QRect(230, 240, 31, 31))
        self.instaIcon.setStyleSheet("background-image: url(:/newPrefix/instagram.png);")
        self.instaIcon.setText("")
        self.instaIcon.setObjectName("instaIcon")
        self.fbIcon = QtWidgets.QLabel(self.centralwidget)
        self.fbIcon.setGeometry(QtCore.QRect(230, 295, 31, 31))
        self.fbIcon.setStyleSheet("background-image: url(:/newPrefix/facebook.png);\n"
                                  "")
        self.fbIcon.setText("")
        self.fbIcon.setObjectName("fbIcon")
        self.twitterIcon = QtWidgets.QLabel(self.centralwidget)
        self.twitterIcon.setGeometry(QtCore.QRect(230, 360, 31, 31))
        self.twitterIcon.setStyleSheet("background-image: url(:/newPrefix/twitter.png);    ")
        self.twitterIcon.setText("")
        self.twitterIcon.setObjectName("twitterIcon")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        user = ""
        user = self.main_res["USERNAME"]
        var = "welcome " + user
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Profile"))
        self.welcomeLbl.setText(_translate("MainWindow", var))
        self.twitterLbl.setText(_translate("MainWindow", "TWITTER"))
        self.submitBtn.setText(_translate("MainWindow", "SUBMIT"))
        self.fbLbl.setText(_translate("MainWindow", "FACEBOOK"))
        self.instaInp.setPlaceholderText(_translate("MainWindow", "instagram"))
        self.resetBtn.setText(_translate("MainWindow", "RESET"))
        self.instaLbl.setText(_translate("MainWindow", "INSTAGRAM"))
        self.twitterInp.setPlaceholderText(_translate("MainWindow", "twitter"))
        self.fbInp.setPlaceholderText(_translate("MainWindow", "facebook"))
        self.updateDetailsLbl.setText(_translate("MainWindow", "Update your details"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.callme()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
