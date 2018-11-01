# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'welcomeAdmin.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import ibm_db
from PyQt5.QtCore import QModelIndex
from graph import *
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mp


class Ui_MainWindowWelcome(object):
    conn = ""
    l = []
    row_ans = ''
    username = ''

    def nameReturner(self):
        self.namereturn = self.username
        return self.namereturn
    
    def cloudConnectiontwo(self):
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
        Ui_MainWindowWelcome.conn = conn
        print("cloud connected")

    def fetchUserdetails(self):
        self.cloudConnectiontwo()
        print("yeh")
        query_for_table = "SELECT ID,USERNAME,EMAIL from WKG83160.USERS1 ORDER BY ID DESC LIMIT 10"
        result_data = ibm_db.exec_immediate(Ui_MainWindowWelcome.conn, query_for_table)
        # ans = ibm_db.fetch_assoc(result_data)
        data = ibm_db.fetch_both(result_data)
        self.ids = []
        self.names = []
        self.emails = []
        while data != False:
            self.ids.append(data['ID'])
            self.names.append(data['USERNAME'])
            self.emails.append(data['EMAIL'])
            data = ibm_db.fetch_both(result_data)

        return self.ids, self.names, self.emails

    # function for plotting graph
    def plotGraph(self):
        print("inside")
        query = "select * from  WKG83160.MOOD where id='%s'" % (self.row_ans)
        stmt = ibm_db.exec_immediate(conn, query)
        print("no 1")
        data = ibm_db.fetch_assoc(stmt)
        l = []
        while data != False:
            l.append(data)
            data = ibm_db.fetch_assoc(stmt)

        df = pd.DataFrame(l)
        print(df)
        co = list(df['MOOD'].value_counts())
        print(co)
        y = list(pd.unique(df['MOOD']))
        y = [y[i].strip(' ') for i in range(len(y))]
        print(y)
        colo = {'Joy': 'blue', 'Fear': 'black', 'Anger': 'red', 'Sadness': 'grey', 'Analytical': 'Green',
                'Confident': 'pink', 'Tentative': 'brown'}
        print("one  step ")
        index = np.arange(len(y))
        # plt.figure(figsize=(0.430,0.287), dpi=200)
        plt.bar(index, co, color=['red', 'green', 'blue', 'yellow', 'brown', 'black', 'grey'])
        plt.xticks(index, y)

        plt.savefig('E:\\New folder (2)\\Sentimetal_analysis_desktopApp-master\\images\\barplot1.png')
        print("finalllyyy!")

    # function for opening the panel using show button:
    def funtionPanelOpener(self):

        print("function called!")
        if self.b1.isChecked():
            row = 0
            r = self.tableWidget.currentRow()
            row_ans = self.tableWidget.item(row, 0).text()
            username_ans = self.tableWidget.item(row, 1).text()

            self.row_ans = row_ans
            self.username = username_ans


        elif self.b2.isChecked():
            row = 1
            r = self.tableWidget.currentRow()
            row_ans = self.tableWidget.item(row, 0).text()
            username_ans = self.tableWidget.item(row, 1).text()
            self.row_ans = row_ans
            self.username = username_ans

        elif self.b3.isChecked():
            row = 2
            r = self.tableWidget.currentRow()
            row_ans = self.tableWidget.item(row, 0).text()
            username_ans = self.tableWidget.item(row, 1).text()
            self.row_ans = row_ans
            self.username = username_ans
        elif self.b4.isChecked():
            row = 3
            r = self.tableWidget.currentRow()
            row_ans = self.tableWidget.item(row, 0).text()
            username_ans = self.tableWidget.item(row, 1).text()
            self.row_ans = row_ans
            self.username = username_ans
        elif self.b5.isChecked():
            row = 4
            r = self.tableWidget.currentRow()
            row_ans = self.tableWidget.item(row, 0).text()
            username_ans = self.tableWidget.item(row, 1).text()
            self.row_ans = row_ans
            self.username = username_ans
        elif self.b6.isChecked():
            row = 5
            r = self.tableWidget.currentRow()
            row_ans = self.tableWidget.item(row, 0).text()
            username_ans = self.tableWidget.item(row, 1).text()
            self.row_ans = row_ans
            self.username = username_ans
        elif self.b7.isChecked():
            row = 6
            r = self.tableWidget.currentRow()
            row_ans = self.tableWidget.item(row, 0).text()
            username_ans = self.tableWidget.item(row, 1).text()
            self.row_ans = row_ans
            self.username = username_ans
        elif self.b8.isChecked():
            row = 7
            r = self.tableWidget.currentRow()
            row_ans = self.tableWidget.item(row, 0).text()
            username_ans = self.tableWidget.item(row, 1).text()
            self.row_ans = row_ans
            self.username = username_ans
        elif self.b9.isChecked():
            row = 8
            r = self.tableWidget.currentRow()
            row_ans = self.tableWidget.item(row, 0).text()
            username_ans = self.tableWidget.item(row, 1).text()
            self.row_ans = row_ans
            self.username = username_ans
        elif self.b10.isChecked():
            row = 9
            r = self.tableWidget.currentRow()
            row_ans = self.tableWidget.item(row, 0).text()
            username_ans = self.tableWidget.item(row, 1).text()
            self.row_ans = row_ans
            self.username = username_ans
        print(row)
        print(self.row_ans)
        print(self.username)
        self.plotGraph()

        self.window = QtWidgets.QMainWindow()
        self.graphobj = Ui_MainWindowGraphView()
        self.graphobj.setupUiGraph(self.window)
        self.window.show()

    def setupUiWelcome(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(960, 640)
        MainWindow.setMinimumSize(QtCore.QSize(960, 640))
        MainWindow.setMaximumSize(QtCore.QSize(960, 640))
        MainWindow.setStyleSheet("background-image: url(:/newPrefix/watsonLogo.jpeg);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.loginLbl = QtWidgets.QLabel(self.centralwidget)
        self.loginLbl.setGeometry(QtCore.QRect(340, 10, 451, 71))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.loginLbl.setFont(font)
        self.loginLbl.setStyleSheet("color: rgb(255, 255, 255);")
        self.loginLbl.setObjectName("loginLbl")
        self.loginIcon = QtWidgets.QLabel(self.centralwidget)
        self.loginIcon.setGeometry(QtCore.QRect(220, -20, 141, 131))
        self.loginIcon.setStyleSheet("background-image: url(:/newPrefix/Login-01-128 (1).png);\n"
                                     "image: url(:/newPrefix/User-Login-128.png);")
        self.loginIcon.setText("")
        self.loginIcon.setObjectName("loginIcon")
        self.a_signupbtn = QtWidgets.QPushButton(self.centralwidget)
        self.a_signupbtn.setGeometry(QtCore.QRect(450, 570, 112, 34))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.a_signupbtn.setFont(font)
        self.a_signupbtn.setStyleSheet("color: rgb(255, 255, 255);")
        self.a_signupbtn.setAutoDefault(True)
        self.a_signupbtn.setDefault(False)
        self.a_signupbtn.setFlat(False)
        self.a_signupbtn.setObjectName("a_signupbtn")
        self.unameLbl_2 = QtWidgets.QLabel(self.centralwidget)
        self.unameLbl_2.setGeometry(QtCore.QRect(380, 100, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.unameLbl_2.setFont(font)
        self.unameLbl_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.unameLbl_2.setScaledContents(False)
        self.unameLbl_2.setWordWrap(False)
        self.unameLbl_2.setOpenExternalLinks(False)
        self.unameLbl_2.setObjectName("unameLbl_2")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(80, 150, 800, 400))
        self.tableWidget.setMinimumSize(QtCore.QSize(800, 400))
        self.tableWidget.setMaximumSize(QtCore.QSize(800, 400))
        self.tableWidget.setStyleSheet("background-image: url(:/newPrefix/blueBg.png);\n"
                                       "background-color: rgb(85, 0, 255);\n"
                                       "selection-color: rgb(255, 170, 255);\n"
                                       "color: rgb(255, 255, 255);\n"
                                       "")
        self.tableWidget.setRowCount(10)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        item = QtWidgets.QTableWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tableWidget.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tableWidget.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tableWidget.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tableWidget.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        ######################################################3

        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tableWidget.setHorizontalHeaderItem(3, item)

        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(3, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(3, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(4, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(4, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(4, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(5, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(5, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(5, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(6, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(6, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(6, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(7, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(7, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(7, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(8, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(8, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(8, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(9, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(9, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(9, 2, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(50)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(True)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setSortIndicatorShown(False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)

        self.b1 = QtWidgets.QPushButton(self.centralwidget)
        self.b1.setGeometry(QtCore.QRect(700, 180, 181, 23))
        self.b1.setStyleSheet("color: rgb(255, 255, 255);")
        self.b1.setObjectName("b1")
        #####################################################
        self.b1.setCheckable(True)
        self.b1.clicked.connect(self.funtionPanelOpener)
        #######################################################
        self.b2 = QtWidgets.QPushButton(self.centralwidget)
        self.b2.setGeometry(QtCore.QRect(700, 209, 181, 23))
        self.b2.setStyleSheet("color: rgb(255, 255, 255);")
        self.b2.setObjectName("b2")
        #####################################################
        self.b2.setCheckable(True)
        self.b2.clicked.connect(self.funtionPanelOpener)
        #######################################################
        self.b3 = QtWidgets.QPushButton(self.centralwidget)
        self.b3.setGeometry(QtCore.QRect(700, 239, 181, 23))
        self.b3.setStyleSheet("color: rgb(255, 255, 255);")
        self.b3.setObjectName("b3")
        #####################################################
        self.b3.setCheckable(True)
        self.b3.clicked.connect(self.funtionPanelOpener)
        #######################################################
        self.b4 = QtWidgets.QPushButton(self.centralwidget)
        self.b4.setGeometry(QtCore.QRect(700, 268, 181, 23))
        self.b4.setStyleSheet("color: rgb(255, 255, 255);")
        self.b4.setObjectName("b4")
        #####################################################
        self.b4.setCheckable(True)
        self.b4.clicked.connect(self.funtionPanelOpener)
        #######################################################
        self.b5 = QtWidgets.QPushButton(self.centralwidget)
        self.b5.setGeometry(QtCore.QRect(700, 295, 181, 23))
        self.b5.setStyleSheet("color: rgb(255, 255, 255);")
        self.b5.setObjectName("b5")
        #####################################################
        self.b5.setCheckable(True)
        self.b5.clicked.connect(self.funtionPanelOpener)
        #######################################################
        self.b6 = QtWidgets.QPushButton(self.centralwidget)
        self.b6.setGeometry(QtCore.QRect(700, 325, 181, 23))
        self.b6.setStyleSheet("color: rgb(255, 255, 255);")
        self.b6.setObjectName("b6")
        #####################################################
        self.b6.setCheckable(True)
        self.b6.clicked.connect(self.funtionPanelOpener)
        #######################################################
        self.b7 = QtWidgets.QPushButton(self.centralwidget)
        self.b7.setGeometry(QtCore.QRect(700, 354, 181, 23))
        self.b7.setStyleSheet("color: rgb(255, 255, 255);")
        self.b7.setObjectName("b7")
        #####################################################
        self.b7.setCheckable(True)
        self.b7.clicked.connect(self.funtionPanelOpener)
        #######################################################
        self.b8 = QtWidgets.QPushButton(self.centralwidget)
        self.b8.setGeometry(QtCore.QRect(700, 385, 181, 23))
        self.b8.setStyleSheet("color: rgb(255, 255, 255);")
        self.b8.setObjectName("b8")
        #####################################################
        self.b8.setCheckable(True)
        self.b8.clicked.connect(self.funtionPanelOpener)
        #######################################################
        self.b9 = QtWidgets.QPushButton(self.centralwidget)
        self.b9.setGeometry(QtCore.QRect(700, 415, 181, 23))
        self.b9.setStyleSheet("color: rgb(255, 255, 255);")
        self.b9.setObjectName("b9")
        #####################################################
        self.b9.setCheckable(True)
        self.b9.clicked.connect(self.funtionPanelOpener)
        #######################################################
        self.b10 = QtWidgets.QPushButton(self.centralwidget)
        self.b10.setGeometry(QtCore.QRect(700, 447, 181, 23))
        self.b10.setStyleSheet("color: rgb(255, 255, 255);")
        self.b10.setObjectName("b10")
        #####################################################
        self.b10.setCheckable(True)
        self.b10.clicked.connect(self.funtionPanelOpener)
        #######################################################
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        detailed_ids, detailed_names, detailed_emails = self.fetchUserdetails()
        detailed_ids = [str(detailed_ids[i]) for i in range(len(detailed_ids))]
        detailed_names = [detailed_names[j].rstrip(' ') for j in range(len(detailed_names))]
        detailed_emails = [detailed_emails[j].rstrip(' ') for j in range(len(detailed_emails))]
        print(detailed_ids)
        print(detailed_names)
        print(detailed_emails)
        print("----------------------")
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.loginLbl.setText(_translate("MainWindow", "WELCOME ADMIN"))
        self.a_signupbtn.setText(_translate("MainWindow", "SEARCH"))
        self.unameLbl_2.setText(_translate("MainWindow", "List of Users"))
        self.tableWidget.setSortingEnabled(True)
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "2"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "3"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "4"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "5"))
        item = self.tableWidget.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "6"))
        item = self.tableWidget.verticalHeaderItem(6)
        item.setText(_translate("MainWindow", "7"))
        item = self.tableWidget.verticalHeaderItem(7)
        item.setText(_translate("MainWindow", "8"))
        item = self.tableWidget.verticalHeaderItem(8)
        item.setText(_translate("MainWindow", "9"))
        item = self.tableWidget.verticalHeaderItem(9)
        item.setText(_translate("MainWindow", "10"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "User ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Username"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Email ID"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Status"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("MainWindow", detailed_ids[0]))
        item = self.tableWidget.item(0, 1)
        item.setText(_translate("MainWindow", detailed_names[0]))
        item = self.tableWidget.item(0, 2)
        item.setText(_translate("MainWindow", detailed_emails[0]))
        item = self.tableWidget.item(1, 0)
        item.setText(_translate("MainWindow", detailed_ids[1]))
        item = self.tableWidget.item(1, 1)
        item.setText(_translate("MainWindow", detailed_names[1]))
        item = self.tableWidget.item(1, 2)
        item.setText(_translate("MainWindow", detailed_emails[1]))
        item = self.tableWidget.item(2, 0)
        item.setText(_translate("MainWindow", detailed_ids[2]))
        item = self.tableWidget.item(2, 1)
        item.setText(_translate("MainWindow", detailed_names[2]))
        item = self.tableWidget.item(2, 2)
        item.setText(_translate("MainWindow", detailed_emails[2]))
        item = self.tableWidget.item(3, 0)
        item.setText(_translate("MainWindow", detailed_ids[3]))
        item = self.tableWidget.item(3, 1)
        item.setText(_translate("MainWindow", detailed_names[3]))
        item = self.tableWidget.item(3, 2)
        item.setText(_translate("MainWindow", detailed_emails[3]))
        item = self.tableWidget.item(4, 0)
        item.setText(_translate("MainWindow", detailed_ids[4]))
        item = self.tableWidget.item(4, 1)
        item.setText(_translate("MainWindow", detailed_names[4]))
        item = self.tableWidget.item(4, 2)
        item.setText(_translate("MainWindow", detailed_emails[4]))
        item = self.tableWidget.item(5, 0)
        item.setText(_translate("MainWindow", detailed_ids[5]))
        item = self.tableWidget.item(5, 1)
        item.setText(_translate("MainWindow", detailed_names[5]))
        item = self.tableWidget.item(5, 2)
        item.setText(_translate("MainWindow", detailed_emails[5]))
        item = self.tableWidget.item(6, 0)
        item.setText(_translate("MainWindow", detailed_ids[6]))
        item = self.tableWidget.item(6, 1)
        item.setText(_translate("MainWindow", detailed_names[6]))
        item = self.tableWidget.item(6, 2)
        item.setText(_translate("MainWindow", detailed_emails[6]))
        item = self.tableWidget.item(7, 0)
        item.setText(_translate("MainWindow", "11"))
        item = self.tableWidget.item(7, 1)
        item.setText(_translate("MainWindow", "nono"))
        item = self.tableWidget.item(7, 2)
        item.setText(_translate("MainWindow", "nono@gmail.com"))
        item = self.tableWidget.item(8, 0)
        item.setText(_translate("MainWindow", "109"))
        item = self.tableWidget.item(8, 1)
        item.setText(_translate("MainWindow", "nitin"))
        item = self.tableWidget.item(8, 2)
        item.setText(_translate("MainWindow", "nitin@email.com"))
        item = self.tableWidget.item(9, 0)
        item.setText(_translate("MainWindow", "110"))
        item = self.tableWidget.item(9, 1)
        item.setText(_translate("MainWindow", "om"))
        item = self.tableWidget.item(9, 2)
        item.setText(_translate("MainWindow", "om@email.com"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.b1.setText(_translate("MainWindow", "SHOW "))
        self.b2.setText(_translate("MainWindow", "SHOW "))
        self.b3.setText(_translate("MainWindow", "SHOW "))
        self.b4.setText(_translate("MainWindow", "SHOW "))
        self.b5.setText(_translate("MainWindow", "SHOW "))
        self.b6.setText(_translate("MainWindow", "SHOW "))
        self.b7.setText(_translate("MainWindow", "SHOW "))
        self.b8.setText(_translate("MainWindow", "SHOW "))
        self.b9.setText(_translate("MainWindow", "SHOW "))
        self.b10.setText(_translate("MainWindow", "SHOW "))


import picsIBM_rc

if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindowWelcome()
    ui.setupUiWelcome(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
