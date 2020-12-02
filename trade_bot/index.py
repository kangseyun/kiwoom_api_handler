from datetime import datetime as dt
from functools import wraps
import os
import sys
import time


sys.path.append(r"C:\Users\seyun\Documents\project\kiwoom_api_handler")
import unittest

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QAxContainer import *

from kiwoom_api.api import Kiwoom, DataFeeder
from pymongo import MongoClient

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyStock")
        self.setGeometry(300, 300, 300, 150)

        a = Kiwoom.instance()
        dataFeeder = DataFeeder(a)
        a.commConnect()
        getServerGubun = a.getServerGubun()
        login_info = a.getLoginInfo("USER_NAME")
        a.getConditionLoad()    
        self.my_client = MongoClient("mongodb://localhost:27017/")
        self.mydb = self.my_client['trade_bot']
        self.mycol = self.mydb['trade_bot']
        x = self.mycol.insert_one({"name":"SOMJANG", "address":"Dongjakgu, Seoul"})
        print(self.my_client.list_database_names())



    def event_connect(self, err_code):
        if err_code == 0:
            self.text_edit.append("로그인 성공")

if __name__ == "__main__":
    app = QApplication(sys.argv)

    myWindow = MyWindow()
    myWindow.show()
    app.exec_()

