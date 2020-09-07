

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


import os
from os import path
import sys
import webbrowser
import urllib.request
from pro import Ui_SocialMedia



class MainApp(QMainWindow,Ui_SocialMedia):
    def __init__(self,parent=None):
        super(MainApp,self).__init__(parent)
        
        self.setupUi(self)
        self.Handel_ui()
        self.pushButton.clicked.connect(self.open_facebook)
        self.pushButton_2.clicked.connect(self.open_youtube)
        self.pushButton_4.clicked.connect(self.open_Instagrame)
        self.pushButton_3.clicked.connect(self.open_Twitter)

    def Handel_ui(self):
            self.setWindowTitle('open social media')
            self.setFixedSize(564, 263)







    def open_facebook(self):
        url = 'https://www.facebook.com'
        webbrowser.open(url, new=1)

    def open_youtube(self):
        url = 'www.youtube.com'
        webbrowser.open(url,new=1)
    def open_Instagrame(self):
        url = 'www.instagrame.com'
        webbrowser.open(url,new=1)
    def open_Twitter(self):
        url = 'www.twitter.com'
        webbrowser.open(url,new=1)












def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()
if __name__ == '__main__':
    main()
