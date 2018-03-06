# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Proxybrowser.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Proxy_browser(object):
    def setupUi(self, Proxy_browser):
        Proxy_browser.setObjectName("Proxy_browser")
        Proxy_browser.setEnabled(True)
        Proxy_browser.resize(310, 480)
        Proxy_browser.setMinimumSize(QtCore.QSize(310, 480))
        Proxy_browser.setMaximumSize(QtCore.QSize(310, 480))
        Proxy_browser.setWindowTitle("Proxy_browser")
        self.centralwidget = QtWidgets.QWidget(Proxy_browser)
        self.centralwidget.setObjectName("centralwidget")
        Proxy_browser.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Proxy_browser)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 310, 23))
        self.menubar.setObjectName("menubar")
        Proxy_browser.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Proxy_browser)
        self.statusbar.setObjectName("statusbar")
        Proxy_browser.setStatusBar(self.statusbar)

        self.retranslateUi(Proxy_browser)
        QtCore.QMetaObject.connectSlotsByName(Proxy_browser)

    def retranslateUi(self, Proxy_browser):
        pass

