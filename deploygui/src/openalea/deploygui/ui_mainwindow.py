# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resources/mainwindow.ui'
#
# Created: Wed Jun 11 09:40:46 2008
#      by: PyQt4 UI code generator 4.4.2
#
# WARNING! All changes made in this file will be lost!

from Qt import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(703,681)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/openalea_icon.png"),QtGui.QIcon.Normal,QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setGeometry(QtCore.QRect(0,21,703,660))
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.tabWidget = QtWidgets.QTabWidget(self.splitter)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setGeometry(QtCore.QRect(0,0,679,373))
        self.tab.setObjectName("tab")
        self.vboxlayout = QtWidgets.QVBoxLayout(self.tab)
        self.vboxlayout.setObjectName("vboxlayout")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setOpenExternalLinks(True)
        self.label_4.setObjectName("label_4")
        self.vboxlayout.addWidget(self.label_4)
        self.hboxlayout = QtWidgets.QHBoxLayout()
        self.hboxlayout.setObjectName("hboxlayout")
        self.radioRecommended = QtWidgets.QRadioButton(self.tab)
        self.radioRecommended.setChecked(True)
        self.radioRecommended.setObjectName("radioRecommended")
        self.hboxlayout.addWidget(self.radioRecommended)
        self.radioAll = QtWidgets.QRadioButton(self.tab)
        self.radioAll.setObjectName("radioAll")
        self.hboxlayout.addWidget(self.radioAll)
        self.radioUpdate = QtWidgets.QRadioButton(self.tab)
        self.radioUpdate.setObjectName("radioUpdate")
        self.hboxlayout.addWidget(self.radioUpdate)
        self.radioInstalled = QtWidgets.QRadioButton(self.tab)
        self.radioInstalled.setObjectName("radioInstalled")
        self.hboxlayout.addWidget(self.radioInstalled)
        self.vboxlayout.addLayout(self.hboxlayout)
        self.packageList = QtWidgets.QListWidget(self.tab)
        self.packageList.setAlternatingRowColors(True)
        self.packageList.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.packageList.setSortingEnabled(True)
        self.packageList.setObjectName("packageList")
        self.vboxlayout.addWidget(self.packageList)
        self.hboxlayout1 = QtWidgets.QHBoxLayout()
        self.hboxlayout1.setObjectName("hboxlayout1")
        self.checkAll = QtWidgets.QPushButton(self.tab)
        self.checkAll.setFlat(True)
        self.checkAll.setObjectName("checkAll")
        self.hboxlayout1.addWidget(self.checkAll)
        self.ClearAll = QtWidgets.QPushButton(self.tab)
        self.ClearAll.setFlat(True)
        self.ClearAll.setObjectName("ClearAll")
        self.hboxlayout1.addWidget(self.ClearAll)
        spacerItem = QtWidgets.QSpacerItem(521,20,QtWidgets.QSizePolicy.Expanding,QtWidgets.QSizePolicy.Minimum)
        self.hboxlayout1.addItem(spacerItem)
        self.vboxlayout.addLayout(self.hboxlayout1)
        self.hboxlayout2 = QtWidgets.QHBoxLayout()
        self.hboxlayout2.setSpacing(6)
        self.hboxlayout2.setContentsMargins(0, 0, 0, 0)
        self.hboxlayout2.setObjectName("hboxlayout2")
        self.proceedButton = QtWidgets.QPushButton(self.tab)
        self.proceedButton.setObjectName("proceedButton")
        self.hboxlayout2.addWidget(self.proceedButton)
        self.refreshButton = QtWidgets.QPushButton(self.tab)
        self.refreshButton.setObjectName("refreshButton")
        self.hboxlayout2.addWidget(self.refreshButton)
        self.vboxlayout.addLayout(self.hboxlayout2)
        self.tabWidget.addTab(self.tab,"")
        self.OtherEggs = QtWidgets.QWidget()
        self.OtherEggs.setGeometry(QtCore.QRect(0,0,679,373))
        self.OtherEggs.setObjectName("OtherEggs")
        self.vboxlayout1 = QtWidgets.QVBoxLayout(self.OtherEggs)
        self.vboxlayout1.setObjectName("vboxlayout1")
        self.label = QtWidgets.QLabel(self.OtherEggs)
        self.label.setOpenExternalLinks(True)
        self.label.setObjectName("label")
        self.vboxlayout1.addWidget(self.label)
        self.hboxlayout3 = QtWidgets.QHBoxLayout()
        self.hboxlayout3.setObjectName("hboxlayout3")
        self.requestEdit = QtWidgets.QLineEdit(self.OtherEggs)
        self.requestEdit.setObjectName("requestEdit")
        self.hboxlayout3.addWidget(self.requestEdit)
        self.fileButton = QtWidgets.QPushButton(self.OtherEggs)
        self.fileButton.setObjectName("fileButton")
        self.hboxlayout3.addWidget(self.fileButton)
        self.vboxlayout1.addLayout(self.hboxlayout3)
        spacerItem1 = QtWidgets.QSpacerItem(20,40,QtWidgets.QSizePolicy.Minimum,QtWidgets.QSizePolicy.Expanding)
        self.vboxlayout1.addItem(spacerItem1)
        self.hboxlayout4 = QtWidgets.QHBoxLayout()
        self.hboxlayout4.setObjectName("hboxlayout4")
        self.customInstallButton = QtWidgets.QPushButton(self.OtherEggs)
        self.customInstallButton.setObjectName("customInstallButton")
        self.hboxlayout4.addWidget(self.customInstallButton)
        self.vboxlayout1.addLayout(self.hboxlayout4)
        self.tabWidget.addTab(self.OtherEggs,"")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setGeometry(QtCore.QRect(0,0,679,373))
        self.tab_2.setObjectName("tab_2")
        self.vboxlayout2 = QtWidgets.QVBoxLayout(self.tab_2)
        self.vboxlayout2.setObjectName("vboxlayout2")
        self.label_2 = QtWidgets.QLabel(self.tab_2)
        self.label_2.setObjectName("label_2")
        self.vboxlayout2.addWidget(self.label_2)
        self.locationList = QtWidgets.QListWidget(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding,QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.locationList.sizePolicy().hasHeightForWidth())
        self.locationList.setSizePolicy(sizePolicy)
        self.locationList.setObjectName("locationList")
        self.vboxlayout2.addWidget(self.locationList)
        self.hboxlayout5 = QtWidgets.QHBoxLayout()
        self.hboxlayout5.setSpacing(6)
        self.hboxlayout5.setContentsMargins(0, 0, 0, 0)
        self.hboxlayout5.setObjectName("hboxlayout5")
        self.addLocButton = QtWidgets.QPushButton(self.tab_2)
        self.addLocButton.setObjectName("addLocButton")
        self.hboxlayout5.addWidget(self.addLocButton)
        self.removeLocButton = QtWidgets.QPushButton(self.tab_2)
        self.removeLocButton.setObjectName("removeLocButton")
        self.hboxlayout5.addWidget(self.removeLocButton)
        self.vboxlayout2.addLayout(self.hboxlayout5)
        self.tabWidget.addTab(self.tab_2,"")
        self.customPackagePage = QtWidgets.QWidget()
        self.customPackagePage.setGeometry(QtCore.QRect(0,0,679,373))
        self.customPackagePage.setObjectName("customPackagePage")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.customPackagePage)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_5 = QtWidgets.QLabel(self.customPackagePage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5,0,0,1,5)
        self.label_6 = QtWidgets.QLabel(self.customPackagePage)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6,1,0,1,1)
        self.customPackageNameEdit = QtWidgets.QLineEdit(self.customPackagePage)
        self.customPackageNameEdit.setObjectName("customPackageNameEdit")
        self.gridLayout_2.addWidget(self.customPackageNameEdit,1,1,1,4)
        self.label_7 = QtWidgets.QLabel(self.customPackagePage)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7,2,0,1,1)
        self.customPackageVersionEdit = QtWidgets.QLineEdit(self.customPackagePage)
        self.customPackageVersionEdit.setObjectName("customPackageVersionEdit")
        self.gridLayout_2.addWidget(self.customPackageVersionEdit,2,1,1,1)
        spacerItem2 = QtWidgets.QSpacerItem(291,20,QtWidgets.QSizePolicy.Expanding,QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2,2,2,1,2)
        self.label_8 = QtWidgets.QLabel(self.customPackagePage)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8,3,0,1,1)
        self.customPackageDirEdit = QtWidgets.QLineEdit(self.customPackagePage)
        self.customPackageDirEdit.setObjectName("customPackageDirEdit")
        self.gridLayout_2.addWidget(self.customPackageDirEdit,3,1,1,3)
        self.customPackageDirButton = QtWidgets.QPushButton(self.customPackagePage)
        self.customPackageDirButton.setObjectName("customPackageDirButton")
        self.gridLayout_2.addWidget(self.customPackageDirButton,3,4,1,1)
        self.customCppPackageFrame = QtWidgets.QGroupBox(self.customPackagePage)
        self.customCppPackageFrame.setEnabled(True)
        self.customCppPackageFrame.setCheckable(True)
        self.customCppPackageFrame.setChecked(False)
        self.customCppPackageFrame.setObjectName("customCppPackageFrame")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.customCppPackageFrame)
        self.gridLayout_3.setSpacing(1)
        self.gridLayout_3.setContentsMargins(4,1,4,1)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_9 = QtWidgets.QLabel(self.customCppPackageFrame)
        self.label_9.setObjectName("label_9")
        self.gridLayout_3.addWidget(self.label_9,0,0,1,1)
        self.customPackageIncludeEdit = QtWidgets.QLineEdit(self.customCppPackageFrame)
        self.customPackageIncludeEdit.setObjectName("customPackageIncludeEdit")
        self.gridLayout_3.addWidget(self.customPackageIncludeEdit,0,1,1,1)
        self.customPackageIncludeButton = QtWidgets.QPushButton(self.customCppPackageFrame)
        self.customPackageIncludeButton.setObjectName("customPackageIncludeButton")
        self.gridLayout_3.addWidget(self.customPackageIncludeButton,0,2,1,1)
        self.label_11 = QtWidgets.QLabel(self.customCppPackageFrame)
        self.label_11.setObjectName("label_11")
        self.gridLayout_3.addWidget(self.label_11,1,0,1,1)
        self.customPackageLibEdit = QtWidgets.QLineEdit(self.customCppPackageFrame)
        self.customPackageLibEdit.setObjectName("customPackageLibEdit")
        self.gridLayout_3.addWidget(self.customPackageLibEdit,1,1,1,1)
        self.customPackageLibButton = QtWidgets.QPushButton(self.customCppPackageFrame)
        self.customPackageLibButton.setObjectName("customPackageLibButton")
        self.gridLayout_3.addWidget(self.customPackageLibButton,1,2,1,1)
        self.label_13 = QtWidgets.QLabel(self.customCppPackageFrame)
        self.label_13.setObjectName("label_13")
        self.gridLayout_3.addWidget(self.label_13,2,0,1,1)
        self.customPackageBinEdit = QtWidgets.QLineEdit(self.customCppPackageFrame)
        self.customPackageBinEdit.setObjectName("customPackageBinEdit")
        self.gridLayout_3.addWidget(self.customPackageBinEdit,2,1,1,1)
        self.customPackageBinButton = QtWidgets.QPushButton(self.customCppPackageFrame)
        self.customPackageBinButton.setObjectName("customPackageBinButton")
        self.gridLayout_3.addWidget(self.customPackageBinButton,2,2,1,1)
        self.gridLayout_2.addWidget(self.customCppPackageFrame,4,0,1,5)
        self.customPythonPackageFrame = QtWidgets.QGroupBox(self.customPackagePage)
        self.customPythonPackageFrame.setEnabled(True)
        self.customPythonPackageFrame.setCheckable(True)
        self.customPythonPackageFrame.setChecked(False)
        self.customPythonPackageFrame.setObjectName("customPythonPackageFrame")
        self.gridLayout = QtWidgets.QGridLayout(self.customPythonPackageFrame)
        self.gridLayout.setSpacing(2)
        self.gridLayout.setContentsMargins(4,0,2,4)
        self.gridLayout.setObjectName("gridLayout")
        self.label_12 = QtWidgets.QLabel(self.customPythonPackageFrame)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12,0,0,1,1)
        self.customPythonPackageEdit = QtWidgets.QLineEdit(self.customPythonPackageFrame)
        self.customPythonPackageEdit.setObjectName("customPythonPackageEdit")
        self.gridLayout.addWidget(self.customPythonPackageEdit,0,1,1,1)
        self.customPythonPackageButton = QtWidgets.QPushButton(self.customPythonPackageFrame)
        self.customPythonPackageButton.setObjectName("customPythonPackageButton")
        self.gridLayout.addWidget(self.customPythonPackageButton,0,2,1,1)
        self.pythonNamespaceFrame = QtWidgets.QGroupBox(self.customPythonPackageFrame)
        self.pythonNamespaceFrame.setCheckable(True)
        self.pythonNamespaceFrame.setChecked(False)
        self.pythonNamespaceFrame.setObjectName("pythonNamespaceFrame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.pythonNamespaceFrame)
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setContentsMargins(4,1,4,4)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_10 = QtWidgets.QLabel(self.pythonNamespaceFrame)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout.addWidget(self.label_10)
        self.namespaceEdit = QtWidgets.QLineEdit(self.pythonNamespaceFrame)
        self.namespaceEdit.setObjectName("namespaceEdit")
        self.horizontalLayout.addWidget(self.namespaceEdit)
        self.gridLayout.addWidget(self.pythonNamespaceFrame,1,1,1,1)
        self.gridLayout_2.addWidget(self.customPythonPackageFrame,5,0,1,5)
        spacerItem3 = QtWidgets.QSpacerItem(40,20,QtWidgets.QSizePolicy.Expanding,QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem3,6,1,1,2)
        self.customResetButton = QtWidgets.QPushButton(self.customPackagePage)
        self.customResetButton.setObjectName("customResetButton")
        self.gridLayout_2.addWidget(self.customResetButton,6,3,1,1)
        self.customApplyButton = QtWidgets.QPushButton(self.customPackagePage)
        self.customApplyButton.setObjectName("customApplyButton")
        self.gridLayout_2.addWidget(self.customApplyButton,6,4,1,1)
        self.tabWidget.addTab(self.customPackagePage,"")
        self.layoutWidget = QtWidgets.QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.vboxlayout3 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.vboxlayout3.setObjectName("vboxlayout3")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.vboxlayout3.addWidget(self.label_3)
        self.logText = QtWidgets.QTextEdit(self.layoutWidget)
        self.logText.setReadOnly(True)
        self.logText.setObjectName("logText")
        self.vboxlayout3.addWidget(self.logText)
        self.gridLayout_4.addWidget(self.splitter,0,0,1,1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0,0,703,21))
        self.menubar.setObjectName("menubar")
        self.menuAuthentification = QtWidgets.QMenu(self.menubar)
        self.menuAuthentification.setObjectName("menuAuthentification")
        self.menu_File = QtWidgets.QMenu(self.menubar)
        self.menu_File.setObjectName("menu_File")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.actionCookie_Session = QtWidgets.QAction(MainWindow)
        self.actionCookie_Session.setObjectName("actionCookie_Session")
        self.action_Quit = QtWidgets.QAction(MainWindow)
        self.action_Quit.setObjectName("action_Quit")
        self.action_About = QtWidgets.QAction(MainWindow)
        self.action_About.setObjectName("action_About")
        self.action_Web = QtWidgets.QAction(MainWindow)
        self.action_Web.setObjectName("action_Web")
        self.menuAuthentification.addAction(self.actionCookie_Session)
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
        MainWindow.setTabOrder(self.radioRecommended,self.radioAll)
        MainWindow.setTabOrder(self.radioAll,self.radioUpdate)
        MainWindow.setTabOrder(self.radioUpdate,self.radioInstalled)
        MainWindow.setTabOrder(self.radioInstalled,self.packageList)
        MainWindow.setTabOrder(self.packageList,self.checkAll)
        MainWindow.setTabOrder(self.checkAll,self.ClearAll)
        MainWindow.setTabOrder(self.ClearAll,self.proceedButton)
        MainWindow.setTabOrder(self.proceedButton,self.refreshButton)
        MainWindow.setTabOrder(self.refreshButton,self.logText)
        MainWindow.setTabOrder(self.logText,self.requestEdit)
        MainWindow.setTabOrder(self.requestEdit,self.fileButton)
        MainWindow.setTabOrder(self.fileButton,self.customInstallButton)
        MainWindow.setTabOrder(self.customInstallButton,self.locationList)
        MainWindow.setTabOrder(self.locationList,self.addLocButton)
        MainWindow.setTabOrder(self.addLocButton,self.removeLocButton)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "OpenAlea Installer", None, QtWidgets.QApplication.UnicodeUTF8))
        self.label_4.setText(QtWidgets.QApplication.translate("MainWindow", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Packages</span> : Select the packages you want to install/update/remove and click on <span style=\" font-weight:600;\">Install/Remove</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600;\">Package descriptions are available in the <a href=\"http://openalea.gforge.inria.fr/packages.php\"><span style=\" text-decoration: underline; color:#0000ff;\">Package index</span></a></p></body></html>", None, QtWidgets.QApplication.UnicodeUTF8))
        self.radioRecommended.setText(QtWidgets.QApplication.translate("MainWindow", "Install Recommended packages", None, QtWidgets.QApplication.UnicodeUTF8))
        self.radioAll.setText(QtWidgets.QApplication.translate("MainWindow", "Install All packages", None, QtWidgets.QApplication.UnicodeUTF8))
        self.radioUpdate.setText(QtWidgets.QApplication.translate("MainWindow", " Update packages", None, QtWidgets.QApplication.UnicodeUTF8))
        self.radioInstalled.setText(QtWidgets.QApplication.translate("MainWindow", "List/Remove packages", None, QtWidgets.QApplication.UnicodeUTF8))
        self.checkAll.setText(QtWidgets.QApplication.translate("MainWindow", "CheckAll", None, QtWidgets.QApplication.UnicodeUTF8))
        self.ClearAll.setText(QtWidgets.QApplication.translate("MainWindow", "ClearAll", None, QtWidgets.QApplication.UnicodeUTF8))
        self.proceedButton.setText(QtWidgets.QApplication.translate("MainWindow", "Install/Remove", None, QtWidgets.QApplication.UnicodeUTF8))
        self.refreshButton.setText(QtWidgets.QApplication.translate("MainWindow", "Refresh List", None, QtWidgets.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtWidgets.QApplication.translate("MainWindow", "Install/Remove OpenAlea Packages", None, QtWidgets.QApplication.UnicodeUTF8))
        self.label.setText(QtWidgets.QApplication.translate("MainWindow", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Install a custom python package</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">See </span><a href=\"http://openalea.gforge.inria.fr/packages.php\"><span style=\" font-weight:600; text-decoration: underline; color:#0000ff;\">Openalea Package index</span></a><span style=\" font-weight:600;\"> and </span><a href=\"http://pypi.python.org/pypi\"><span style=\" font-weight:600; text-decoration: underline; color:#0000ff;\">PyPi index</span></a></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600;\">Enter  : </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  + a Python<span style=\" font-style:italic;\"> package name (ex : ipython, numpy...)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  + or the <span style=\" font-style:italic;\">URL of an Egg</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  + or the <span style=\" font-style:italic;\">local path of an Egg</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-style:italic;\"><span style=\" font-style:normal;\">and click </span><span style=\" font-weight:600; font-style:normal;\">Install</span></p></body></html>", None, QtWidgets.QApplication.UnicodeUTF8))
        self.fileButton.setText(QtWidgets.QApplication.translate("MainWindow", "...", None, QtWidgets.QApplication.UnicodeUTF8))
        self.customInstallButton.setText(QtWidgets.QApplication.translate("MainWindow", "Install", None, QtWidgets.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.OtherEggs), QtWidgets.QApplication.translate("MainWindow", "Install Other Eggs", None, QtWidgets.QApplication.UnicodeUTF8))
        self.label_2.setText(QtWidgets.QApplication.translate("MainWindow", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Locations </span>: repository URLs</p></body></html>", None, QtWidgets.QApplication.UnicodeUTF8))
        self.addLocButton.setText(QtWidgets.QApplication.translate("MainWindow", "Add", None, QtWidgets.QApplication.UnicodeUTF8))
        self.removeLocButton.setText(QtWidgets.QApplication.translate("MainWindow", "Remove", None, QtWidgets.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QtWidgets.QApplication.translate("MainWindow", "Repository", None, QtWidgets.QApplication.UnicodeUTF8))
        self.label_5.setText(QtWidgets.QApplication.translate("MainWindow", "<b>Custom Package:</b> To declare in the package database a local version of a package", None, QtWidgets.QApplication.UnicodeUTF8))
        self.label_6.setText(QtWidgets.QApplication.translate("MainWindow", "Package name :", None, QtWidgets.QApplication.UnicodeUTF8))
        self.label_7.setText(QtWidgets.QApplication.translate("MainWindow", "Version : ", None, QtWidgets.QApplication.UnicodeUTF8))
        self.label_8.setText(QtWidgets.QApplication.translate("MainWindow", "Directory :", None, QtWidgets.QApplication.UnicodeUTF8))
        self.customPackageDirButton.setText(QtWidgets.QApplication.translate("MainWindow", "...", None, QtWidgets.QApplication.UnicodeUTF8))
        self.customCppPackageFrame.setTitle(QtWidgets.QApplication.translate("MainWindow", "C++ Directories", None, QtWidgets.QApplication.UnicodeUTF8))
        self.label_9.setText(QtWidgets.QApplication.translate("MainWindow", "Include :", None, QtWidgets.QApplication.UnicodeUTF8))
        self.customPackageIncludeButton.setText(QtWidgets.QApplication.translate("MainWindow", "...", None, QtWidgets.QApplication.UnicodeUTF8))
        self.label_11.setText(QtWidgets.QApplication.translate("MainWindow", "Lib:", None, QtWidgets.QApplication.UnicodeUTF8))
        self.customPackageLibButton.setText(QtWidgets.QApplication.translate("MainWindow", "...", None, QtWidgets.QApplication.UnicodeUTF8))
        self.label_13.setText(QtWidgets.QApplication.translate("MainWindow", "Bin:", None, QtWidgets.QApplication.UnicodeUTF8))
        self.customPackageBinButton.setText(QtWidgets.QApplication.translate("MainWindow", "...", None, QtWidgets.QApplication.UnicodeUTF8))
        self.customPythonPackageFrame.setTitle(QtWidgets.QApplication.translate("MainWindow", "Python", None, QtWidgets.QApplication.UnicodeUTF8))
        self.label_12.setText(QtWidgets.QApplication.translate("MainWindow", "Path:", None, QtWidgets.QApplication.UnicodeUTF8))
        self.customPythonPackageButton.setText(QtWidgets.QApplication.translate("MainWindow", "...", None, QtWidgets.QApplication.UnicodeUTF8))
        self.pythonNamespaceFrame.setTitle(QtWidgets.QApplication.translate("MainWindow", "Include in Namespace", None, QtWidgets.QApplication.UnicodeUTF8))
        self.label_10.setText(QtWidgets.QApplication.translate("MainWindow", "Name:", None, QtWidgets.QApplication.UnicodeUTF8))
        self.namespaceEdit.setText(QtWidgets.QApplication.translate("MainWindow", "openalea", None, QtWidgets.QApplication.UnicodeUTF8))
        self.customResetButton.setText(QtWidgets.QApplication.translate("MainWindow", "Reset", None, QtWidgets.QApplication.UnicodeUTF8))
        self.customApplyButton.setText(QtWidgets.QApplication.translate("MainWindow", "Apply", None, QtWidgets.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.customPackagePage), QtWidgets.QApplication.translate("MainWindow", "Custom Local Package", None, QtWidgets.QApplication.UnicodeUTF8))
        self.label_3.setText(QtWidgets.QApplication.translate("MainWindow", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Log</span> : System Output</p></body></html>", None, QtWidgets.QApplication.UnicodeUTF8))
        self.menuAuthentification.setTitle(QtWidgets.QApplication.translate("MainWindow", "&Authentification", None, QtWidgets.QApplication.UnicodeUTF8))
        self.menu_File.setTitle(QtWidgets.QApplication.translate("MainWindow", "&File", None, QtWidgets.QApplication.UnicodeUTF8))
        self.menuHelp.setTitle(QtWidgets.QApplication.translate("MainWindow", "Help", None, QtWidgets.QApplication.UnicodeUTF8))
        self.actionCookie_Session.setText(QtWidgets.QApplication.translate("MainWindow", "INRIA GForge Session", None, QtWidgets.QApplication.UnicodeUTF8))
        self.action_Quit.setText(QtWidgets.QApplication.translate("MainWindow", "&Quit", None, QtWidgets.QApplication.UnicodeUTF8))
        self.action_Quit.setShortcut(QtWidgets.QApplication.translate("MainWindow", "Ctrl+Q", None, QtWidgets.QApplication.UnicodeUTF8))
        self.action_About.setText(QtWidgets.QApplication.translate("MainWindow", "&About", None, QtWidgets.QApplication.UnicodeUTF8))
        self.action_Web.setText(QtWidgets.QApplication.translate("MainWindow", "&Web", None, QtWidgets.QApplication.UnicodeUTF8))

import images_rc
