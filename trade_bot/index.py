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

from telegram_bot.telebot import TeleBot

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyStock")
        self.setGeometry(300, 300, 300, 150)

        a = Kiwoom.instance()
        dataFeeder = DataFeeder(a)
        a.commConnect()
        a.getConditionLoad()
    
        # a.sendCondition(condition[0][0], condition[0][1], 0)
   

    def event_connect(self, err_code):
        if err_code == 0:
            self.text_edit.append("로그인 성공")

if __name__ == "__main__":


    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()

