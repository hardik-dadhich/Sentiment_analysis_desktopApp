# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'userView.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from tonanalyser import *
import ibm_db
import random
from datetime import datetime
from mailsend import *


class Ui_MainWindowBoard(object):
    conn = ''
    temp = ''
    pic_name = ''
    movie = ''
    recom_of_movies = []
    l = []
    name_of_user = ''
    query_id = ''

    def NameHolder(self, name=''):
        self.name = name

    def Moodholder(self):
        self.mood = Ui_MainWindowBoard.temp
        return self.mood

    def Namereturner(self):
        print(self.name)
        return self.name

    def status(self):
        obj = TonAna()
        val = obj.statusfun()
        #function calling for insert mood status in db
        self.insertmoodstatus(val)
        Ui_MainWindowBoard.temp = val
        if val == 'Joy':
            self.pic_name = 'joy.png'
            return self.pic_name
        elif val == 'Fear':
            self.pic_name = 'fear.png'
            return self.pic_name
        elif val == 'Sadness':
            self.pic_name = 'sadness.png'
            return self.pic_name
        elif val == 'Anger':
            self.pic_name = 'anger.png'
            return self.pic_name
        elif val == 'Analytical':
            self.pic_name = 'analytical.png'
            return self.pic_name
        elif val == 'Confident':
            self.pic_name = 'confident.png'
            return self.pic_name
        elif val == 'Tentative':
            self.pic_name = 'tentative.png'
            return self.pic_name


    def emailgenerate(self):
        se=SendMail()
        print("email generate function")
        query = "select * from  WKG83160.MOOD where id='%s'" % (self.query_id)
        stmt = ibm_db.exec_immediate(conn, query)
        print("no 1")
        data = ibm_db.fetch_assoc(stmt)
        l = []
        while data != False:
            l.append(data)
            data = ibm_db.fetch_assoc(stmt)

        df = pd.DataFrame(l)
        print(df)
        empty = []
        empty = [i.strip(' ') for i in df['MOOD']]
        print(empty)
        df['MOOD'] = pd.Series(empty)
        print("new df called!")
        print(df)
        s = (df['MOOD'].groupby((df['MOOD']!=df['MOOD'].shift()).cumsum()).transform('count').lt(1) | (df['MOOD'].eq('Joy')) | (df['MOOD'].eq('Anger')) | (df['MOOD'].eq('Analytical')) | (df['MOOD'].eq('Confident')) | (df['MOOD'].eq('Tentative') ))
        print('finally email grnerator')
        print(type(s))
        print(s)

        for u in range(s.shape[0]):
            if(s.iloc[u]==False):
                print('funtion cll')
                se.main()
                print(u)
                query = "delete from WKG83160.MOOD where id='%s'" % (u)
                stmt = ibm_db.exec_immediate(conn, query)
                break;

    def recommendation(self):
        movie_moods = {'Joy': 'Adventure' or 'Comedy', 'Fear': 'Romance', 'Confident': 'Action', 'Sadness': 'Comedy',
                       'Anger': 'Comedy', 'Analytical': 'Sci-Fi', 'Tentative': 'Drama'}

        self.cloudConnect()
        gen = movie_moods[Ui_MainWindowBoard.temp]
        self.query = "SELECT * FROM WKG83160.MOVIES WHERE GENRES = '%s'" % gen
        self.stmt = ibm_db.exec_immediate(conn, self.query)
        data = ibm_db.fetch_both(self.stmt)
        self.l = []
        while data != False:
            self.l.append(data['TITLE'])
            data = ibm_db.fetch_both(self.stmt)

        # self.movie = data['TITLE']
        self.recom_of_movies = random.sample(range(len(self.l)), 10)

    def cloudConnect(self):
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
        Ui_MainWindowBoard.conn = conn
        print("cloud connected")

    def insertmoodstatus(self, val):
        today = str(datetime.now())
        today_date, today_time = today.split(' ')
        print(today_date, today_time)
        print(self.name)
        tm = today_time
        hr = tm.split(":")
        ##  fetching person id by using his name
        query_id = "SELECT ID FROM WKG83160.USERS1 WHERE USERNAME ='%s'" % (self.name).strip(' ')
        print(query_id)
        self.cloudConnect()
        data_res = ibm_db.exec_immediate(conn, query_id)
        main_data = ibm_db.fetch_both(data_res)
        user_main_id = str(main_data['ID'])
        Ui_MainWindowBoard.query_id = user_main_id
        ## inserting person mood according to his id!
        query_for_data = "INSERT INTO WKG83160.MOOD VALUES('%s', '%s', '%s', '%s')" % (user_main_id, today_date, hr[0], val)
        #query_for_data = "INSERT INTO WKG83160.MOOD VALUES('%s', '%s', '%s', '%s')" % ('1', '18/2/13', '13', 'Joy')
        print(query_for_data)
        print(Ui_MainWindowBoard.conn)
        data_inserted = ibm_db.exec_immediate(Ui_MainWindowBoard.conn, query_for_data)
        print("successs full insetion of mood")
        #self.emailgenerate()

    def setupUistatus(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(960, 640)
        MainWindow.setMinimumSize(QtCore.QSize(960, 640))
        MainWindow.setMaximumSize(QtCore.QSize(960, 640))
        MainWindow.setStyleSheet("background-image: url(:/newPrefix/watsonLogo.jpeg);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.unameLbl = QtWidgets.QLabel(self.centralwidget)
        self.unameLbl.setGeometry(QtCore.QRect(30, 10, 241, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.unameLbl.setFont(font)
        self.unameLbl.setStyleSheet("color: rgb(255, 255, 255);")
        self.unameLbl.setObjectName("unameLbl")
        self.statusLbl = QtWidgets.QLabel(self.centralwidget)
        self.statusLbl.setGeometry(QtCore.QRect(540, 10, 71, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.statusLbl.setFont(font)
        self.statusLbl.setStyleSheet("color: rgb(255, 255, 255);")
        self.statusLbl.setObjectName("statusLbl")
        self.recommendLbl = QtWidgets.QLabel(self.centralwidget)
        self.recommendLbl.setGeometry(QtCore.QRect(120, 310, 550, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.recommendLbl.setFont(font)
        self.recommendLbl.setStyleSheet("color: rgb(255, 255, 255);")
        self.recommendLbl.setObjectName("recommendLbl")
        self.suggestBtn = QtWidgets.QPushButton(self.centralwidget)
        self.suggestBtn.setGeometry(QtCore.QRect(740, 330, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.suggestBtn.setFont(font)
        self.suggestBtn.setStyleSheet("color: rgb(255, 255, 255);")
        self.suggestBtn.setObjectName("suggestBtn")
        self.listOfReccomendations = QtWidgets.QListWidget(self.centralwidget)
        self.listOfReccomendations.setGeometry(QtCore.QRect(120, 370, 721, 251))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.listOfReccomendations.setFont(font)
        self.listOfReccomendations.setStyleSheet("color: rgb(255, 255, 255);\n"
                                                 "background-image: url(:/newPrefix/blueBg.png);")
        self.listOfReccomendations.setObjectName("listOfReccomendations")
        item = QtWidgets.QListWidgetItem()
        self.listOfReccomendations.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listOfReccomendations.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listOfReccomendations.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listOfReccomendations.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listOfReccomendations.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listOfReccomendations.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listOfReccomendations.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listOfReccomendations.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listOfReccomendations.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listOfReccomendations.addItem(item)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.statusNameLbl = QtWidgets.QLabel(self.centralwidget)
        self.statusNameLbl.setGeometry(QtCore.QRect(620, 10, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.statusNameLbl.setFont(font)
        self.statusNameLbl.setStyleSheet("color: rgb(255, 255, 255);")
        self.statusNameLbl.setObjectName("statusNameLbl")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(350, 80, 221, 221))
        self.label.setStyleSheet("background-image: url(:/newPrefix/" + self.status() + ");")
        self.label.setText("")
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        self.recommendation()
        self.status_dash = ''

        self.status_dash = Ui_MainWindowBoard.temp
        # self.recom_dash = str(self.movie)
        self.name_of_user = "USERNAME : " + str(self.name)
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Status Board"))
        self.unameLbl.setText(_translate("MainWindow", self.name_of_user))
        self.statusLbl.setText(_translate("MainWindow", "Status : "))
        self.recommendLbl.setText(_translate("MainWindow", "RECOMMENDED MOVIES BASED ON PAST 24 HOURS COMMENTS"))
        self.suggestBtn.setText(_translate("MainWindow", "SUGGEST"))
        __sortingEnabled = self.listOfReccomendations.isSortingEnabled()
        self.listOfReccomendations.setSortingEnabled(False)
        item = self.listOfReccomendations.item(0)
        item.setText(_translate("MainWindow", self.l[self.recom_of_movies[0]]))
        item = self.listOfReccomendations.item(1)
        item.setText(_translate("MainWindow", self.l[self.recom_of_movies[2]]))
        item = self.listOfReccomendations.item(2)
        item.setText(_translate("MainWindow", self.l[self.recom_of_movies[3]]))
        item = self.listOfReccomendations.item(3)
        item.setText(_translate("MainWindow", self.l[self.recom_of_movies[4]]))
        item = self.listOfReccomendations.item(4)
        item.setText(_translate("MainWindow", self.l[self.recom_of_movies[5]]))
        item = self.listOfReccomendations.item(5)
        item.setText(_translate("MainWindow", self.l[self.recom_of_movies[5]]))
        item = self.listOfReccomendations.item(6)
        item.setText(_translate("MainWindow", self.l[self.recom_of_movies[6]]))
        item = self.listOfReccomendations.item(7)
        item.setText(_translate("MainWindow", self.l[self.recom_of_movies[7]]))
        item = self.listOfReccomendations.item(8)
        item.setText(_translate("MainWindow", self.l[self.recom_of_movies[8]]))
        item = self.listOfReccomendations.item(9)
        item.setText(_translate("MainWindow", self.l[self.recom_of_movies[9]]))
        # item = self.listOfReccomendations.item(10)
        # item.setText(_translate("MainWindow", self.recom_of_movies[10]))
        self.listOfReccomendations.setSortingEnabled(__sortingEnabled)
        # self.backBtn.setText(_translate("MainWindow", "Show More"))
        ########################################################################
        # self.backBtn.clicked.connect(self.showMore)
        #######################################################################
        self.statusNameLbl.setText(_translate("MainWindow", self.status_dash))


import picsIBM_rc

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindowBoard()
    ui.setupUistatus(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
