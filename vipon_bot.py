from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
from time import sleep
import undetected_chromedriver as uc
from datetime import datetime
import sys
from  PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
import threading
from selenium import webdriver
from time import sleep
import csv
import pandas as pd

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.proxy import Proxy, ProxyType


import random
import undetected_chromedriver as uc
login_status=False
driver=None
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(780, 492)
        MainWindow.setMinimumSize(QtCore.QSize(250, 30))
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        MainWindow.setAutoFillBackground(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setAutoFillBackground(False)
        self.frame.setStyleSheet("background-color: rgb(158, 162, 125);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.frame_2.setFont(font)
        self.frame_2.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"background-color: rgb(158, 162, 125);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.frame_5 = QtWidgets.QFrame(self.frame_2)
        self.frame_5.setMinimumSize(QtCore.QSize(700, 100))
        self.frame_5.setMaximumSize(QtCore.QSize(700, 100))
        self.frame_5.setStyleSheet("")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.frame_5)
        self.label.setMinimumSize(QtCore.QSize(300, 75))
        self.label.setMaximumSize(QtCore.QSize(300, 75))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setItalic(True)
        font.setUnderline(True)
        font.setKerning(True)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(0, 0, 0);\n"
"")
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.verticalLayout_3.addWidget(self.frame_5)
        self.frame_4 = QtWidgets.QFrame(self.frame_2)
        self.frame_4.setMinimumSize(QtCore.QSize(700, 100))
        self.frame_4.setMaximumSize(QtCore.QSize(700, 100))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.frame_4)
        self.label_2.setMinimumSize(QtCore.QSize(100, 30))
        self.label_2.setMaximumSize(QtCore.QSize(120, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(3, 53, 100, 255), stop:1 rgba(61, 147, 212, 255));\n"
"border-radius: 3px;")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lineEdit = QtWidgets.QLineEdit(self.frame_4)
        self.lineEdit.setMinimumSize(QtCore.QSize(250, 30))
        self.lineEdit.setMaximumSize(QtCore.QSize(250, 30))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"border-radius: 3px;")
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_3.setMinimumSize(QtCore.QSize(60, 30))
        self.pushButton_3.setMaximumSize(QtCore.QSize(100, 30))
        self.pushButton_3.setStyleSheet("color: rgb(255, 255, 255);\n"
"border-radius: 3px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(74, 103, 7, 255), stop:1 rgba(130, 186, 27, 255));\n"
"\n"
"")
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_2.addWidget(self.pushButton_3)
        self.pushButton = QtWidgets.QPushButton(self.frame_4)
        self.pushButton.setMinimumSize(QtCore.QSize(60, 30))
        self.pushButton.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"border-radius: 3px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(74, 103, 7, 255), stop:1 rgba(130, 186, 27, 255))")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.verticalLayout_3.addWidget(self.frame_4)
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setMinimumSize(QtCore.QSize(700, 100))
        self.frame_3.setMaximumSize(QtCore.QSize(700, 100))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(self.frame_3)
        self.label_3.setMinimumSize(QtCore.QSize(100, 30))
        self.label_3.setMaximumSize(QtCore.QSize(120, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(3, 53, 100, 255), stop:1 rgba(61, 147, 212, 255));\n"
"border-radius: 3px;")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_2.setMinimumSize(QtCore.QSize(250, 30))
        self.lineEdit_2.setMaximumSize(QtCore.QSize(250, 30))
        self.lineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"border-radius: 3px;")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout.addWidget(self.lineEdit_2)
        self.pushButton_4 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_4.setMinimumSize(QtCore.QSize(60, 30))
        self.pushButton_4.setMaximumSize(QtCore.QSize(100, 30))
        self.pushButton_4.setStyleSheet("color: rgb(255, 255, 255);\n"
"border-radius: 3px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(74, 103, 7, 255), stop:1 rgba(130, 186, 27, 255))")
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout.addWidget(self.pushButton_4)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_2.setMinimumSize(QtCore.QSize(60, 30))
        self.pushButton_2.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(74, 103, 7, 255), stop:1 rgba(130, 186, 27, 255));\n"
"border-radius: 3px;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.verticalLayout_3.addWidget(self.frame_3)
        self.frame_7 = QtWidgets.QFrame(self.frame_2)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_5 = QtWidgets.QLabel(self.frame_7)
        self.label_5.setMinimumSize(QtCore.QSize(100, 30))
        self.label_5.setMaximumSize(QtCore.QSize(120, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(3, 53, 100, 255), stop:1 rgba(61, 147, 212, 255));\n"
"border-radius: 3px;")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame_7)
        self.lineEdit_3.setMinimumSize(QtCore.QSize(100, 30))
        self.lineEdit_3.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"border-radius: 3px;")
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout_4.addWidget(self.lineEdit_3)
        self.verticalLayout_3.addWidget(self.frame_7)
        self.frame_6 = QtWidgets.QFrame(self.frame_2)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 0, 4, 1, 1)
        self.checkBox = QtWidgets.QCheckBox(self.frame_6)
        self.checkBox.setMinimumSize(QtCore.QSize(75, 30))
        self.checkBox.setMaximumSize(QtCore.QSize(75, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox.setFont(font)
        self.checkBox.setStyleSheet("color: rgb(255, 255, 255);")
        self.checkBox.setObjectName("checkBox")
        self.gridLayout_2.addWidget(self.checkBox, 0, 2, 1, 1)
        self.checkBox_2 = QtWidgets.QCheckBox(self.frame_6)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_2.setFont(font)
        self.checkBox_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.checkBox_2.setObjectName("checkBox_2")
        self.gridLayout_2.addWidget(self.checkBox_2, 0, 3, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 0, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.frame_6)
        self.label_4.setMinimumSize(QtCore.QSize(75, 0))
        self.label_4.setMaximumSize(QtCore.QSize(75, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 0, 1, 1, 1)
        self.verticalLayout_3.addWidget(self.frame_6)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem3)
        self.verticalLayout.addWidget(self.frame_2, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_2.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 780, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Automation Bot"))
        self.label_2.setText(_translate("MainWindow", "Output Folder"))
        self.pushButton_3.setText(_translate("MainWindow", "Upload"))
        self.pushButton.setText(_translate("MainWindow", "Start"))
        self.label_3.setText(_translate("MainWindow", "Upload Xlsx "))
        self.pushButton_4.setText(_translate("MainWindow", "Browse"))
        self.pushButton_2.setText(_translate("MainWindow", "Start Posting"))
        self.label_5.setText(_translate("MainWindow", "No. of pages"))
        self.checkBox.setText(_translate("MainWindow", "Page"))
        self.checkBox_2.setText(_translate("MainWindow", "Group"))
        self.label_4.setText(_translate("MainWindow", "Publish On"))



class MainWindow(QMainWindow):
    global keywords
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.setWindowTitle('Form Filler')
       
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.start_scraping)
        self.ui.pushButton_3.clicked.connect(self.search_output_folder)
        self.ui.pushButton_4.clicked.connect(self.xlsx_file_found)
        self.ui.pushButton_2.clicked.connect(self.read_data_file)
        self.show()
        
    def xlsx_file_found(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Excel File (*.xlsx)", options=options)
        if fileName:
            print(fileName)
            self.ui.lineEdit_2.setText(fileName)
        if self.ui.checkBox.isChecked():
            abc = True
        else:
            abc = False
        print(abc)
    
    def search_output_folder(self):
        file = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        print(file)
        self.ui.lineEdit.setText(file)        

        
    #Tuesday Work 15/feb/2022#
    
    def POST(self, message, statuss):
        global login_status
        global driver
        # Set up Facebook login account name and password
        file=open('fb_creds.txt','r')
        ll=file.readlines()
        email=ll[0].replace("\n","")
        password=ll[1].replace("\n","")
        account = email
        password = password
        groups_links_list = []
        file=open("group.txt")
        grp_links=file.readlines()
        for i in range(0,len(grp_links)):
            grp_links[i]=grp_links[i].replace("\n",'')
            groups_links_list.append(grp_links[i])
        # Set up Facebook groups to post, you must be a member of the group
        
        

        # Set up Facebook pages to post, you must be a member of the pages
        page_links_list = []
        
     
        file=open("page.txt")
        pg_links=file.readlines()
        for i in range(0,len(pg_links)):
            pg_links[i]=pg_links[i].replace("\n",'')
            page_links_list.append(pg_links[i])
        # Set up text content to post
        #message = "hello world"

        # Set up paths of images to post

        if login_status==False:
            # Login Facebook
            print('Loging To Browser')
            chrome_options = webdriver.ChromeOptions()
            prefs = {"profile.default_content_setting_values.notifications" : 2}
            #chrome_options.add_experimental_option("prefs",prefs)
            chrome_options.add_argument("--disable-gpu")
            chrome_options.add_argument("--disable-crash-reporter")
            chrome_options.add_argument("--disable-extensions")
            chrome_options.add_argument("--disable-in-process-stack-traces")
            chrome_options.add_argument("--disable-logging")
            driver =uc.Chrome(chrome_options=chrome_options)
            driver.get('https://web.facebook.com/')
            emailelement = driver.find_element(By.XPATH,'//*[@id="email"]')
            emailelement.send_keys(account)
            passelement = driver.find_element(By.XPATH,'//*[@id="pass"]')
            passelement.send_keys(password)
            loginelement = driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]/button')
            loginelement.click()
            login_status=True

        # Post on each group
        for group in groups_links_list:
            driver.get(group)
            time.sleep(10)
            try:
                driver.find_element(By.XPATH,'/html/body/div[1]/div/div[4]/div/div[1]/div/div[3]/div/div[1]/div[2]/div').click()
                
                sleep(12)
                post_box=driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div[2]/div/div/div[5]/div[3]/form/div[3]/div[3]/textarea')
            except:
                driver.find_element(By.XPATH,'/html/body/div[1]/div/div[4]/div/div[1]/div/div[3]/div/div[1]/div[2]/div').click()
                sleep(6)
                post_box=driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div[1]/form/div/div[1]/div/div/div[1]/div/div[2]/div[1]/div[1]")
            post_box.send_keys(message)
            time.sleep(1)

            time.sleep(9)
            post_button = driver.find_element_by_xpath('//*[@id="composer-main-view-id"]/div[3]/div/div/button')
            clickable = False

            post_button.click()
            time.sleep(12)
        # Close driver
        print(statuss)
        if statuss == True:
            for page in page_links_list:
                driver.get(page)
                time.sleep(10)

                try:
                    driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div[1]/div/div[1]/div[2]/div[3]/div/div[1]/a').click()
                    sleep(10)
                    post_box=driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[5]/div[3]/form/div[2]/textarea')
                except:
                    #print('error')
                    post_box=driver.find_element_by_xpath("/html/body/div[2]/div[1]/div/div[5]/div[3]/form/div[2]/textarea")
                
                
                    
                post_box.send_keys(message)
                time.sleep(1)

                time.sleep(6)
                post_button = driver.find_element_by_xpath('//*[@id="composer-main-view-id"]/div[3]/div/div/button')
                clickable = False

                post_button.click()
                time.sleep(12)
            
        #driver.close()
    
    def start_posting(self, data):
#        print('start posting start')
#        print(len(data))
        data_s={"01":[],"02":[],"03":[],"04":[],"05":[],"06":[],"07":[],"08":[],
               "09":[],"10":[],"11":[],"12":[],"13":[],"!4":[],"15":[],
               "16":[],"17":[],"18":[],"19":[],"20":[],"21":[],"22":[],
               "23":[],"24":[]}
        for d in range(0,len(data)):
            name=data[d][0]
            
            discount=data[d][1]
            price=data[d][2]
            after_discount=data[d][3]
            full_fill=data[d][4]
            url=data[d][5]
            schedule=data[d][6]
            code=data[d][7]
            if int(schedule)<10:
                schedule="0"+str(schedule)
                pass
            else:
                schedule=str(schedule)
            data_s[schedule].append(data[d])
        already=[]
        already_hr=[]
        count=0
        i=0
        print(data_s)
        print('\n')
        while True:
            if len(already)==len(data):
                break
            if count==(len(data)-1):
                i=0
                count=0
            #print(i)
            #print(data[i])
            
            for ds in data_s:
                hour=datetime.today().strftime("%H")
                hour=str(hour)
                
                
                if hour not in already_hr:
                    already_hr.append(hour)
                    
                    
                if (hour==str(ds)) or (str(ds) in already_hr):
                    for k in data_s[ds]:
                        hour=datetime.today().strftime("%H")
                        hour=str(hour)
                        if hour not in already_hr:
                            already_hr.append(hour)
                        name=k[0]
                        discount=k[1]
                        price=k[2]
                        after_discount=k[3]
                        full_fill=k[4]
                        url=k[5]
                        schedule=k[6]
                        code=k[7]

                        if name not in already:
                            print("Posting Product No. : "+str(len(already)+1))
                            message='Product Name : '+str(name)+"\n"+'Discount : '+discount+"\n"+"Price : "+price+"\n"+"After Discount : "+after_discount+"\n"+"Full Fill By : "+full_fill+"\n"+url+"\nCode : "+code
                            status = self.ui.checkBox.isChecked()
                            self.POST(message, status)
                            already.append(name)
                            print("Posted !!\n\n")

            
        
            i+=1
            count+=1


            
    def read_data_file(self):
        file_path=self.ui.lineEdit_2.text()
        try:
            df = pd.read_csv(file_path,encoding='utf-8')
        except:
            try:
                df = pd.read_csv(file_path,encoding='latin_1')
            except:
                df = pd.read_csv(file_path,encoding='iso-8859-1')
        abc = df.iloc[:, 2]
        post=[]
        posts = []
        count = 0
        for i in abc:
            post.append(i)
            #print(post)
            count+=1
            #print(count)
            if count == 8:
                posts.append(post)
                #print(posts)
                post=[]
                count = 0
        print(len(posts))
        t1=threading.Thread(target=self.start_posting,args=(posts,))
        t1.start()
    
    def page_checkBox(self):
        if self.ui.checkBox.isChecked()==True:
            abc = True
            return abc
        else:
            abc = False
            return abc
    def start_scraping(self):
        t=threading.Thread(target=self.start_scrape)
        t.start()
    def start_scrape(self):
        vipon_result=[]
        url = "https://www.myvipon.com/shopper/request?ref=shopper_request"
        already=[]
        if True:
                driver= uc.Chrome()
                driver.maximize_window()
                driver.get('https://www.myvipon.com/login?sc=')
                login=driver.find_element_by_id('loginform-email')
                login.send_keys('berezhernandez95@gmail.com')
                password=driver.find_element_by_id('loginform-password')
                password.send_keys('berez1234567')
                btn=driver.find_element_by_id('login-button')
                btn.click()
                driver.get(url)     
                while_status=False
                ijj=self.ui.lineEdit_3.text()
                if ijj=="" or ijj==None:
                    ijj=1
                for ij in range(int(ijj)):
                    sleep(10)
                    if while_status==True:
                        break
                    listt=driver.find_element_by_class_name('product-list')
                    div=listt.find_elements_by_tag_name('div')
                    for d in div:
                        try:
                            t=d.find_element_by_class_name('product-title')
                            a=t.find_element_by_tag_name('a').get_attribute('href')
                            product_title=a
                            c=d.find_element_by_class_name('code')
                            code=c.text
                            #print(product_title)
                            print(code)
                            x=random.randrange(1,23)
                            x=int(x)
                            if x not in already:
                                already.append(x)
                            print(x)
                            if x<10:
                                x="0"+str(x)
                                print('yes')
                                print(x)
                            data={
                            'Product_Name': None,
                            'Discount':None,
                            'Price': None,
                            'After_Discond': None,
                            'Full_Filled_By': None,
                            'URL': product_title,
                            'schedule': str(x),
                            'code': code
                            }
                            vipon_result.append(data)

                        except Exception as e:
                            #print(e)
                            pass
                    #try:
                        #nextt=driver.find_element_by_xpath('//*[@id="reviewContainer"]/div[4]/ul[2]/li[4]/a')
                        #nextt.click()
                    #except:
                        #break
                    #try:
                        #nextt=driver.find_element_by_xpath('//*[@id="reviewContainer"]/div[4]/ul[2]/li[4]/a')
                        #c=nextt.get_attribute('class')
                        #nextt.click()
                        #c=nextt.get_attribute('class')
                        #if c=='noClick':
                            #break
                    #except Exception as e:
                        #print(e)
                        #try:
                            #ne=driver.find_element_by_xpath('//*[@id="reviewContainer"]/div[4]/ul[2]/li[3]/a')
                        #except:
                            #break
                    try:
                        nextt=driver.find_element_by_xpath('//*[@id="reviewContainer"]/div[4]/ul[2]')
                        a=nextt.find_elements_by_tag_name('a')
                        for aa in a:
                            if aa.text=='Next':
                                    aa.click()
                                    break
                    except:
                        pass

                
                    
                    
                for v in range(0,len(vipon_result)):
                    link=vipon_result[v]['URL']
                    driver.get(link)
                    sleep(5)
                    title=driver.find_element_by_class_name('product-title').text
                    price=(driver.find_element_by_class_name('product-price')).find_element_by_tag_name('s').text
                    p_discount=driver.find_element_by_class_name('product-price').find_element_by_tag_name('span').text
                    discount=driver.find_element_by_class_name('product-discount').text
                    full_fill=driver.find_element_by_xpath('//*[@id="product-page"]/div[1]/div[1]/div[3]/div/div[1]/p').text

                    l2=driver.find_element_by_xpath('//*[@id="product-page"]/div[1]/div[1]/div[2]/div/ul[2]/li/a').get_attribute('href')
                    driver.get(l2)
                    cur_url=driver.current_url
                    vipon_result[v]['URL']=str(cur_url)+"?tag=ukmegadeal09f-21"
                    vipon_result[v]['Product_Name']=title
                    vipon_result[v]['Price']=price
                    vipon_result[v]['Discount']=discount
                    vipon_result[v]['After_Discond']=p_discount
                    vipon_result[v]['Full_Filled_By']=full_fill


                df = pd.DataFrame(vipon_result)
                DataStack=df.stack()
                DataStack.head()
                DataStack.to_csv(self.ui.lineEdit.text()+'/NewScrapper.csv',index_label=['','','POST VALUE'],encoding = "utf-8")
                print(vipon_result)
                try:
                    ijj=self.ui.lineEdit_3.text()
                   
                    if ijj=="" or ijj==None:
                        ijj=1
                    for i in range(0,int(ijj)):
                        driver.get("https://www.myvipon.com/shopper/request?ref=shopper_request")
                        time.sleep(8)
                        select=driver.find_element_by_xpath('//*[@id="reviewContainer"]/div[4]/div[2]/a[1]')
                        select.click()
                        sleep(1)
                        delete=driver.find_element_by_xpath('//*[@id="reviewContainer"]/div[4]/div[2]/a[2]')
                        delete.click()
                        
                except:
                    pass
                #driver.close()
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    app.exec_()
    