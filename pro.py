# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pro.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SocialMedia(object):
    def setupUi(self, SocialMedia):
        SocialMedia.setObjectName("SocialMedia")
        SocialMedia.resize(564, 263)
        SocialMedia.setStyleSheet("QWidget\n"
"{\n"
"    background-color: #1a1a1a;\n"
"    color: #000000;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QLabel-----*/\n"
"QLabel\n"
"{\n"
"    background-color: transparent;\n"
"    color: #c2c7d5;\n"
"    font-size: 13px;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QPushButton-----*/\n"
"QPushButton\n"
"{\n"
"    background-color: #ff3333;\n"
"    color: #fff;\n"
"    font-size: 11px;\n"
"    font-weight: bold;\n"
"    border: none;\n"
"    border-radius: 25px;\n"
"    padding: 5px;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton::disabled\n"
"{\n"
"    background-color: #5c5c5c;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"    background-color: #ff4747;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QCheckBox-----*/\n"
"QCheckBox\n"
"{\n"
"    background-color: transparent;\n"
"    color: #fff;\n"
"    font-size: 10px;\n"
"    font-weight: bold;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QCheckBox-----*/\n"
"QCheckBox::indicator\n"
"{\n"
"    color: #b1b1b1;\n"
"    background-color: #323232;\n"
"    border: 1px solid darkgray;\n"
"    width: 12px;\n"
"    height: 12px;\n"
"\n"
"}\n"
"\n"
"\n"
"QCheckBox::indicator:checked\n"
"{\n"
"    image:url(\"./ressources/check.png\");\n"
"    background-color: #ff3333;\n"
"    border: 1px solid #ff3333;\n"
"\n"
"}\n"
"\n"
"\n"
"QCheckBox::indicator:unchecked:hover\n"
"{\n"
"    border: 1px solid #ff3333;\n"
"\n"
"}\n"
"\n"
"\n"
"QCheckBox::disabled\n"
"{\n"
"    color: #656565;\n"
"\n"
"}\n"
"\n"
"\n"
"QCheckBox::indicator:disabled\n"
"{\n"
"    background-color: #656565;\n"
"    color: #656565;\n"
"    border: 1px solid #656565;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QLineEdit-----*/\n"
"QLineEdit\n"
"{\n"
"    background-color: #c2c7d5;\n"
"    color: #000;\n"
"    font-weight: bold;\n"
"    border: none;\n"
"    border-radius: 2px;\n"
"    padding: 3px;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QListView-----*/\n"
"QListView\n"
"{\n"
"    background-color: #333333;\n"
"    color: #fff;\n"
"    font-size: 12px;\n"
"    font-weight: bold;\n"
"    border: 1px solid #191919;\n"
"    show-decoration-selected: 0;\n"
"    padding-left: -13px;\n"
"    padding-right: -13px;\n"
"\n"
"}\n"
"\n"
"\n"
"QListView::item\n"
"{\n"
"    color: #31cecb;\n"
"    background-color: #454e5e;\n"
"    border: none;\n"
"    padding: 5px;\n"
"    border-radius: 0px;\n"
"    padding-left : 10px;\n"
"    height: 42px;\n"
"\n"
"}\n"
"\n"
"QListView::item:selected\n"
"{\n"
"    color: #000;\n"
"    background-color: #ff3333;\n"
"\n"
"}\n"
"\n"
"\n"
"QListView::item:!selected\n"
"{\n"
"    color:white;\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    padding-left : 10px;\n"
"\n"
"}\n"
"\n"
"\n"
"QListView::item:!selected:hover\n"
"{\n"
"    color: #000;\n"
"    background-color: #bcbdbb;\n"
"    border: none;\n"
"    padding-left : 10px;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QTreeView-----*/\n"
"QTreeView \n"
"{\n"
"    background-color: #252525;\n"
"    show-decoration-selected: 0;\n"
"    color: #c2c8d7;\n"
"\n"
"}\n"
"\n"
"\n"
"QTreeView::item \n"
"{\n"
"    border-top-color: transparent;\n"
"    border-bottom-color: transparent;\n"
"\n"
"}\n"
"\n"
"\n"
"QTreeView::item:hover \n"
"{\n"
"    background-color: #bcbdbb;\n"
"    color: #000;\n"
"\n"
"}\n"
"\n"
"\n"
"QTreeView::item:selected \n"
"{\n"
"    background-color: #ff3333;\n"
"    color: #000;\n"
"\n"
"}\n"
"\n"
"\n"
"QTreeView::item:selected:active\n"
"{\n"
"    background-color: #ff3333;\n"
"    color: #000;\n"
"\n"
"}\n"
"\n"
"\n"
"QTreeView::branch:has-children:!has-siblings:closed,\n"
"QTreeView::branch:closed:has-children:has-siblings \n"
"{\n"
"    image: url(://tree-closed.png);\n"
"\n"
"}\n"
"\n"
"QTreeView::branch:open:has-children:!has-siblings,\n"
"QTreeView::branch:open:has-children:has-siblings  \n"
"{\n"
"    image: url(://tree-open.png);\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QTableView & QTableWidget-----*/\n"
"QTableView\n"
"{\n"
"    background-color: #252525;\n"
"    border: 1px solid gray;\n"
"    color: #f0f0f0;\n"
"    gridline-color: gray;\n"
"    outline : 0;\n"
"\n"
"}\n"
"\n"
"\n"
"QTableView::disabled\n"
"{\n"
"    background-color: #242526;\n"
"    border: 1px solid #32414B;\n"
"    color: #656565;\n"
"    gridline-color: #656565;\n"
"    outline : 0;\n"
"\n"
"}\n"
"\n"
"\n"
"QTableView::item:hover \n"
"{\n"
"    background-color: #bcbdbb;\n"
"    color: #000;\n"
"\n"
"}\n"
"\n"
"\n"
"QTableView::item:selected \n"
"{\n"
"    background-color: #ff3333;\n"
"    color: #000;\n"
"\n"
"}\n"
"\n"
"\n"
"QTableView::item:selected:disabled\n"
"{\n"
"    background-color: #1a1b1c;\n"
"    border: 2px solid #525251;\n"
"    color: #656565;\n"
"\n"
"}\n"
"\n"
"\n"
"QTableCornerButton::section\n"
"{\n"
"    background-color: #343a49;\n"
"    color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView::section\n"
"{\n"
"    color: #fff;\n"
"    border-top: 0px;\n"
"    border-bottom: 1px solid gray;\n"
"    border-right: 1px solid gray;\n"
"    background-color: #343a49;\n"
"    margin-top:1px;\n"
"    margin-bottom:1px;\n"
"    padding: 5px;\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView::section:disabled\n"
"{\n"
"    background-color: #525251;\n"
"    color: #656565;\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView::section:checked\n"
"{\n"
"    color: #000;\n"
"    background-color: #ff3333;\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView::section:checked:disabled\n"
"{\n"
"    color: #656565;\n"
"    background-color: #525251;\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView::section::vertical::first,\n"
"QHeaderView::section::vertical::only-one\n"
"{\n"
"    border-top: 1px solid #353635;\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView::section::vertical\n"
"{\n"
"    border-top: 1px solid #353635;\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView::section::horizontal::first,\n"
"QHeaderView::section::horizontal::only-one\n"
"{\n"
"    border-left: 1px solid #353635;\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView::section::horizontal\n"
"{\n"
"    border-left: 1px solid #353635;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QScrollBar-----*/\n"
"QScrollBar:horizontal \n"
"{\n"
"    background-color: transparent;\n"
"    height: 8px;\n"
"    margin: 0px;\n"
"    padding: 0px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::handle:horizontal \n"
"{\n"
"    border: none;\n"
"    min-width: 100px;\n"
"    background-color: #9b9b9b;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:horizontal, \n"
"QScrollBar::sub-line:horizontal,\n"
"QScrollBar::add-page:horizontal, \n"
"QScrollBar::sub-page:horizontal \n"
"{\n"
"    width: 0px;\n"
"    background-color: transparent;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar:vertical \n"
"{\n"
"    background-color: transparent;\n"
"    width: 8px;\n"
"    margin: 0;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::handle:vertical \n"
"{\n"
"    border: none;\n"
"    min-height: 100px;\n"
"    background-color: #9b9b9b;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:vertical, \n"
"QScrollBar::sub-line:vertical,\n"
"QScrollBar::add-page:vertical, \n"
"QScrollBar::sub-page:vertical \n"
"{\n"
"    height: 0px;\n"
"    background-color: transparent;\n"
"\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(SocialMedia)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(60, 172, 75, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(170, 172, 75, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(280, 172, 75, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(410, 172, 75, 31))
        self.pushButton_4.setObjectName("pushButton_4")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-70, 50, 641, 71))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(28)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("font: 28pt \"Segoe UI\";")
        self.label.setObjectName("label")
        SocialMedia.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(SocialMedia)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 564, 20))
        self.menubar.setObjectName("menubar")
        SocialMedia.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(SocialMedia)
        self.statusbar.setObjectName("statusbar")
        SocialMedia.setStatusBar(self.statusbar)

        self.retranslateUi(SocialMedia)
        QtCore.QMetaObject.connectSlotsByName(SocialMedia)

    def retranslateUi(self, SocialMedia):
        _translate = QtCore.QCoreApplication.translate
        SocialMedia.setWindowTitle(_translate("SocialMedia", "MainWindow"))
        self.pushButton.setText(_translate("SocialMedia", "facebook"))
        self.pushButton_2.setText(_translate("SocialMedia", "youtube"))
        self.pushButton_3.setText(_translate("SocialMedia", "twiter"))
        self.pushButton_4.setText(_translate("SocialMedia", "instagram"))
        self.label.setText(_translate("SocialMedia", "         Just one click open social media"))
