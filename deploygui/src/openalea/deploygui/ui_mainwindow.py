# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Thu Sep 27 18:40:22 2007
#      by: PyQt4 UI code generator 4.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(QtCore.QSize(QtCore.QRect(0,0,779,662).size()).expandedTo(MainWindow.minimumSizeHint()))
        MainWindow.setWindowIcon(QtGui.QIcon(":/icons/openalea_icon.png"))

        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.vboxlayout = QtGui.QVBoxLayout(self.centralwidget)
        self.vboxlayout.setObjectName("vboxlayout")

        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")

        self.tab = QtGui.QWidget()
        self.tab.setObjectName("tab")

        self.vboxlayout1 = QtGui.QVBoxLayout(self.tab)
        self.vboxlayout1.setObjectName("vboxlayout1")

        self.label_4 = QtGui.QLabel(self.tab)
        self.label_4.setObjectName("label_4")
        self.vboxlayout1.addWidget(self.label_4)

        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setObjectName("hboxlayout")

        self.radioRecommended = QtGui.QRadioButton(self.tab)
        self.radioRecommended.setChecked(True)
        self.radioRecommended.setObjectName("radioRecommended")
        self.hboxlayout.addWidget(self.radioRecommended)

        self.radioAll = QtGui.QRadioButton(self.tab)
        self.radioAll.setObjectName("radioAll")
        self.hboxlayout.addWidget(self.radioAll)

        self.radioUpdate = QtGui.QRadioButton(self.tab)
        self.radioUpdate.setObjectName("radioUpdate")
        self.hboxlayout.addWidget(self.radioUpdate)

        self.radioInstalled = QtGui.QRadioButton(self.tab)
        self.radioInstalled.setObjectName("radioInstalled")
        self.hboxlayout.addWidget(self.radioInstalled)
        self.vboxlayout1.addLayout(self.hboxlayout)

        self.packageList = QtGui.QListWidget(self.tab)
        self.packageList.setAlternatingRowColors(True)
        self.packageList.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
        self.packageList.setSortingEnabled(True)
        self.packageList.setObjectName("packageList")
        self.vboxlayout1.addWidget(self.packageList)

        self.hboxlayout1 = QtGui.QHBoxLayout()
        self.hboxlayout1.setSpacing(6)
        self.hboxlayout1.setMargin(0)
        self.hboxlayout1.setObjectName("hboxlayout1")

        self.proceedButton = QtGui.QPushButton(self.tab)
        self.proceedButton.setObjectName("proceedButton")
        self.hboxlayout1.addWidget(self.proceedButton)

        self.refreshButton = QtGui.QPushButton(self.tab)
        self.refreshButton.setObjectName("refreshButton")
        self.hboxlayout1.addWidget(self.refreshButton)
        self.vboxlayout1.addLayout(self.hboxlayout1)

        self.label_3 = QtGui.QLabel(self.tab)
        self.label_3.setObjectName("label_3")
        self.vboxlayout1.addWidget(self.label_3)

        self.logText = QtGui.QTextEdit(self.tab)
        self.logText.setReadOnly(True)
        self.logText.setObjectName("logText")
        self.vboxlayout1.addWidget(self.logText)
        self.tabWidget.addTab(self.tab,"")

        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName("tab_2")

        self.vboxlayout2 = QtGui.QVBoxLayout(self.tab_2)
        self.vboxlayout2.setObjectName("vboxlayout2")

        self.label_2 = QtGui.QLabel(self.tab_2)
        self.label_2.setObjectName("label_2")
        self.vboxlayout2.addWidget(self.label_2)

        self.locationList = QtGui.QListWidget(self.tab_2)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.locationList.sizePolicy().hasHeightForWidth())
        self.locationList.setSizePolicy(sizePolicy)
        self.locationList.setObjectName("locationList")
        self.vboxlayout2.addWidget(self.locationList)

        self.hboxlayout2 = QtGui.QHBoxLayout()
        self.hboxlayout2.setSpacing(6)
        self.hboxlayout2.setMargin(0)
        self.hboxlayout2.setObjectName("hboxlayout2")

        self.addLocButton = QtGui.QPushButton(self.tab_2)
        self.addLocButton.setObjectName("addLocButton")
        self.hboxlayout2.addWidget(self.addLocButton)

        self.removeLocButton = QtGui.QPushButton(self.tab_2)
        self.removeLocButton.setObjectName("removeLocButton")
        self.hboxlayout2.addWidget(self.removeLocButton)
        self.vboxlayout2.addLayout(self.hboxlayout2)
        self.tabWidget.addTab(self.tab_2,"")
        self.vboxlayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0,0,779,25))
        self.menubar.setObjectName("menubar")

        self.menuAuthentification = QtGui.QMenu(self.menubar)
        self.menuAuthentification.setObjectName("menuAuthentification")

        self.menu_File = QtGui.QMenu(self.menubar)
        self.menu_File.setObjectName("menu_File")

        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.actionCookie_Session = QtGui.QAction(MainWindow)
        self.actionCookie_Session.setObjectName("actionCookie_Session")

        self.action_Quit = QtGui.QAction(MainWindow)
        self.action_Quit.setObjectName("action_Quit")

        self.action_About = QtGui.QAction(MainWindow)
        self.action_About.setObjectName("action_About")

        self.action_Web = QtGui.QAction(MainWindow)
        self.action_Web.setObjectName("action_Web")

        self.actionInstall_Egg = QtGui.QAction(MainWindow)
        self.actionInstall_Egg.setObjectName("actionInstall_Egg")
        self.menuAuthentification.addAction(self.actionCookie_Session)
        self.menu_File.addAction(self.actionInstall_Egg)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.action_Quit)
        self.menuHelp.addAction(self.action_About)
        self.menuHelp.addAction(self.action_Web)
        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menuAuthentification.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.tabWidget,self.radioRecommended)
        MainWindow.setTabOrder(self.radioRecommended,self.radioUpdate)
        MainWindow.setTabOrder(self.radioUpdate,self.radioAll)
        MainWindow.setTabOrder(self.radioAll,self.radioInstalled)
        MainWindow.setTabOrder(self.radioInstalled,self.packageList)
        MainWindow.setTabOrder(self.packageList,self.proceedButton)
        MainWindow.setTabOrder(self.proceedButton,self.refreshButton)
        MainWindow.setTabOrder(self.refreshButton,self.logText)
        MainWindow.setTabOrder(self.logText,self.locationList)
        MainWindow.setTabOrder(self.locationList,self.addLocButton)
        MainWindow.setTabOrder(self.addLocButton,self.removeLocButton)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "OpenAlea Installer", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Packages</span> : Select the packages you want to install/update/remove and click on <span style=\" font-weight:600;\">Install/Remove</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.radioRecommended.setText(QtGui.QApplication.translate("MainWindow", "Install Recommended packages", None, QtGui.QApplication.UnicodeUTF8))
        self.radioAll.setText(QtGui.QApplication.translate("MainWindow", "Install All packages", None, QtGui.QApplication.UnicodeUTF8))
        self.radioUpdate.setText(QtGui.QApplication.translate("MainWindow", " Update packages", None, QtGui.QApplication.UnicodeUTF8))
        self.radioInstalled.setText(QtGui.QApplication.translate("MainWindow", "Remove packages", None, QtGui.QApplication.UnicodeUTF8))
        self.proceedButton.setText(QtGui.QApplication.translate("MainWindow", "Install/Remove", None, QtGui.QApplication.UnicodeUTF8))
        self.refreshButton.setText(QtGui.QApplication.translate("MainWindow", "Refresh List", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Log</span> : System Output</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("MainWindow", "Install/Remove Packages", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Locations </span>: repository URLs</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.addLocButton.setText(QtGui.QApplication.translate("MainWindow", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.removeLocButton.setText(QtGui.QApplication.translate("MainWindow", "Remove", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QtGui.QApplication.translate("MainWindow", "Repository", None, QtGui.QApplication.UnicodeUTF8))
        self.menuAuthentification.setTitle(QtGui.QApplication.translate("MainWindow", "&Authentification", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_File.setTitle(QtGui.QApplication.translate("MainWindow", "&File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setTitle(QtGui.QApplication.translate("MainWindow", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCookie_Session.setText(QtGui.QApplication.translate("MainWindow", "INRIA GForge Session", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Quit.setText(QtGui.QApplication.translate("MainWindow", "&Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Quit.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Q", None, QtGui.QApplication.UnicodeUTF8))
        self.action_About.setText(QtGui.QApplication.translate("MainWindow", "&About", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Web.setText(QtGui.QApplication.translate("MainWindow", "&Web", None, QtGui.QApplication.UnicodeUTF8))
        self.actionInstall_Egg.setText(QtGui.QApplication.translate("MainWindow", "Install Egg File", None, QtGui.QApplication.UnicodeUTF8))

import images_rc
