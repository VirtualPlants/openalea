# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'oalab/example/control_sizes.ui'
#
# Created: Fri Apr  3 12:26:18 2015
#      by: PyQt4 UI code generator 4.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(747, 667)
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setMargin(5)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_6 = QtGui.QLabel(Form)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 7, 2, 1, 1)
        self.line_5 = QtGui.QFrame(Form)
        self.line_5.setFrameShadow(QtGui.QFrame.Plain)
        self.line_5.setFrameShape(QtGui.QFrame.HLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName(_fromUtf8("line_5"))
        self.gridLayout.addWidget(self.line_5, 3, 0, 1, 3)
        self.widget = QtGui.QWidget(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.widget)
        self.gridLayout_2.setSpacing(5)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.large = QtGui.QWidget(self.widget)
        self.large.setMinimumSize(QtCore.QSize(200, 200))
        self.large.setObjectName(_fromUtf8("large"))
        self.l_large_box = QtGui.QGridLayout(self.large)
        self.l_large_box.setMargin(0)
        self.l_large_box.setObjectName(_fromUtf8("l_large_box"))
        self.label_7 = QtGui.QLabel(self.large)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.l_large_box.addWidget(self.label_7, 0, 0, 1, 1)
        self.large_2 = QtGui.QFrame(self.large)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.large_2.sizePolicy().hasHeightForWidth())
        self.large_2.setSizePolicy(sizePolicy)
        self.large_2.setMinimumSize(QtCore.QSize(300, 300))
        self.large_2.setFrameShape(QtGui.QFrame.Box)
        self.large_2.setObjectName(_fromUtf8("large_2"))
        self.l_large = QtGui.QVBoxLayout(self.large_2)
        self.l_large.setObjectName(_fromUtf8("l_large"))
        self.l_large_box.addWidget(self.large_2, 1, 0, 1, 1)
        self.gridLayout_2.addWidget(self.large, 5, 0, 1, 1)
        self.gridLayout.addWidget(self.widget, 7, 0, 4, 2)
        self.small = QtGui.QWidget(Form)
        self.small.setMinimumSize(QtCore.QSize(50, 50))
        self.small.setMaximumSize(QtCore.QSize(50, 50))
        self.small.setStyleSheet(_fromUtf8("background-color: rgb(170, 160, 255);"))
        self.small.setObjectName(_fromUtf8("small"))
        self.l_small = QtGui.QHBoxLayout(self.small)
        self.l_small.setMargin(0)
        self.l_small.setObjectName(_fromUtf8("l_small"))
        self.gridLayout.addWidget(self.small, 8, 2, 1, 1)
        self.responsive = QtGui.QWidget(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.responsive.sizePolicy().hasHeightForWidth())
        self.responsive.setSizePolicy(sizePolicy)
        self.responsive.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.responsive.setObjectName(_fromUtf8("responsive"))
        self.l_responsive = QtGui.QHBoxLayout(self.responsive)
        self.l_responsive.setMargin(0)
        self.l_responsive.setObjectName(_fromUtf8("l_responsive"))
        self.gridLayout.addWidget(self.responsive, 12, 4, 1, 1)
        self.label_4 = QtGui.QLabel(Form)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)
        self.l_title = QtGui.QLabel(Form)
        self.l_title.setObjectName(_fromUtf8("l_title"))
        self.gridLayout.addWidget(self.l_title, 2, 0, 1, 1)
        self.line_6 = QtGui.QFrame(Form)
        self.line_6.setFrameShadow(QtGui.QFrame.Plain)
        self.line_6.setFrameShape(QtGui.QFrame.HLine)
        self.line_6.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_6.setObjectName(_fromUtf8("line_6"))
        self.gridLayout.addWidget(self.line_6, 6, 0, 1, 3)
        self.hline = QtGui.QWidget(Form)
        self.hline.setMinimumSize(QtCore.QSize(200, 30))
        self.hline.setMaximumSize(QtCore.QSize(16777215, 30))
        self.hline.setStyleSheet(_fromUtf8("background-color: rgb(170, 255, 184);"))
        self.hline.setObjectName(_fromUtf8("hline"))
        self.l_hline = QtGui.QHBoxLayout(self.hline)
        self.l_hline.setMargin(0)
        self.l_hline.setObjectName(_fromUtf8("l_hline"))
        self.gridLayout.addWidget(self.hline, 5, 0, 1, 3)
        self.label = QtGui.QLabel(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 1, 0, 1, 2)
        self.vline = QtGui.QWidget(Form)
        self.vline.setMinimumSize(QtCore.QSize(30, 200))
        self.vline.setMaximumSize(QtCore.QSize(30, 16777215))
        self.vline.setStyleSheet(_fromUtf8("background-color: rgb(255, 226, 212);"))
        self.vline.setObjectName(_fromUtf8("vline"))
        self.l_vline = QtGui.QHBoxLayout(self.vline)
        self.l_vline.setMargin(0)
        self.l_vline.setObjectName(_fromUtf8("l_vline"))
        self.gridLayout.addWidget(self.vline, 9, 2, 3, 1)
        self.groupBox_2 = QtGui.QGroupBox(Form)
        self.groupBox_2.setTitle(_fromUtf8(""))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.widget_3 = QtGui.QWidget(self.groupBox_2)
        self.widget_3.setObjectName(_fromUtf8("widget_3"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.widget_3)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label_8 = QtGui.QLabel(self.widget_3)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.verticalLayout_2.addWidget(self.label_8)
        self.label_2 = QtGui.QLabel(self.widget_3)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_2.addWidget(self.label_2)
        self.cb_read = QtGui.QCheckBox(self.widget_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cb_read.sizePolicy().hasHeightForWidth())
        self.cb_read.setSizePolicy(sizePolicy)
        self.cb_read.setChecked(True)
        self.cb_read.setObjectName(_fromUtf8("cb_read"))
        self.verticalLayout_2.addWidget(self.cb_read)
        self.cb_apply = QtGui.QCheckBox(self.widget_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cb_apply.sizePolicy().hasHeightForWidth())
        self.cb_apply.setSizePolicy(sizePolicy)
        self.cb_apply.setChecked(True)
        self.cb_apply.setObjectName(_fromUtf8("cb_apply"))
        self.verticalLayout_2.addWidget(self.cb_apply)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout.addWidget(self.widget_3)
        self.frame = QtGui.QFrame(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(150, 150))
        self.frame.setFrameShape(QtGui.QFrame.Box)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.layout_sample = QtGui.QVBoxLayout(self.frame)
        self.layout_sample.setMargin(5)
        self.layout_sample.setObjectName(_fromUtf8("layout_sample"))
        self.label_3 = QtGui.QLabel(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.layout_sample.addWidget(self.label_3)
        self.horizontalLayout.addWidget(self.frame)
        self.gridLayout.addWidget(self.groupBox_2, 11, 0, 1, 2)
        self.label_5 = QtGui.QLabel(Form)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 12, 0, 1, 3)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label_6.setText(_translate("Form", "shape=small, vline", None))
        self.label_7.setText(_translate("Form", "shape=large (300x300)", None))
        self.label_4.setText(_translate("Form", "shape=hline", None))
        self.l_title.setText(_translate("Form", "TextLabel", None))
        self.label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Check shapes and read/apply modes ...</span></p></body></html>", None))
        self.label_8.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Test read/apply modes</span></p></body></html>", None))
        self.label_2.setText(_translate("Form", "Check \"auto-read\" and \"auto-apply\"", None))
        self.cb_read.setToolTip(_translate("Form", "<html><head/><body><p>If checked, all modification done in test control is seen in all widgets</p></body></html>", None))
        self.cb_read.setText(_translate("Form", "auto-read  <<", None))
        self.cb_apply.setToolTip(_translate("Form", "<html><head/><body><p>If checked, all changes done in all widget is seen in test control</p></body></html>", None))
        self.cb_apply.setText(_translate("Form", "auto-apply  >>", None))
        self.label_3.setToolTip(_translate("Form", "Widget in this frame has mode auto-read ON, auto-apply ON", None))
        self.label_3.setText(_translate("Form", "Test Control", None))
        self.label_5.setText(_translate("Form", "shape=responsive ->", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

