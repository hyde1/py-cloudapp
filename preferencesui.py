# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'preferences.ui'
#
# Created: Wed Nov  3 20:49:18 2010
#      by: PyQt4 UI code generator 4.7.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Properties(object):
    def setupUi(self, Properties):
        Properties.setObjectName("Properties")
        Properties.resize(316, 193)
        self.verticalLayout = QtGui.QVBoxLayout(Properties)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtGui.QTabWidget(Properties)
        self.tabWidget.setObjectName("tabWidget")
        self.accountTab = QtGui.QWidget()
        self.accountTab.setObjectName("accountTab")
        self.formLayout = QtGui.QFormLayout(self.accountTab)
        self.formLayout.setObjectName("formLayout")
        self.label = QtGui.QLabel(self.accountTab)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.usernameLine = QtGui.QLineEdit(self.accountTab)
        self.usernameLine.setObjectName("usernameLine")
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.usernameLine)
        self.label_2 = QtGui.QLabel(self.accountTab)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.passwordLine = QtGui.QLineEdit(self.accountTab)
        self.passwordLine.setEchoMode(QtGui.QLineEdit.Password)
        self.passwordLine.setObjectName("passwordLine")
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.passwordLine)
        self.rememberCheckBox = QtGui.QCheckBox(self.accountTab)
        self.rememberCheckBox.setChecked(True)
        self.rememberCheckBox.setObjectName("rememberCheckBox")
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.rememberCheckBox)
        self.tabWidget.addTab(self.accountTab, "")
        self.tab = QtGui.QWidget()
        self.tab.setObjectName("tab")
        self.formLayout_2 = QtGui.QFormLayout(self.tab)
        self.formLayout_2.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_3 = QtGui.QLabel(self.tab)
        self.label_3.setObjectName("label_3")
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_3)
        self.fileListItems = QtGui.QSpinBox(self.tab)
        self.fileListItems.setMinimum(5)
        self.fileListItems.setMaximum(15)
        self.fileListItems.setObjectName("fileListItems")
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.fileListItems)
        self.label_4 = QtGui.QLabel(self.tab)
        self.label_4.setObjectName("label_4")
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_4)
        self.clipboardCheckBox = QtGui.QCheckBox(self.tab)
        self.clipboardCheckBox.setText("")
        self.clipboardCheckBox.setChecked(True)
        self.clipboardCheckBox.setObjectName("clipboardCheckBox")
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.FieldRole, self.clipboardCheckBox)
        self.tabWidget.addTab(self.tab, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.okButton = QtGui.QPushButton(Properties)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/dialog-ok.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.okButton.setIcon(icon)
        self.okButton.setObjectName("okButton")
        self.horizontalLayout.addWidget(self.okButton)
        self.cancelButton = QtGui.QPushButton(Properties)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/dialog-cancel.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.cancelButton.setIcon(icon1)
        self.cancelButton.setObjectName("cancelButton")
        self.horizontalLayout.addWidget(self.cancelButton)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Properties)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QObject.connect(self.cancelButton, QtCore.SIGNAL("clicked()"), Properties.close)
        QtCore.QObject.connect(self.okButton, QtCore.SIGNAL("clicked()"), Properties.close)
        QtCore.QMetaObject.connectSlotsByName(Properties)

    def retranslateUi(self, Properties):
        Properties.setWindowTitle(QtGui.QApplication.translate("Properties", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Properties", "UserName", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Properties", "Password", None, QtGui.QApplication.UnicodeUTF8))
        self.rememberCheckBox.setText(QtGui.QApplication.translate("Properties", "Remember Me", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.accountTab), QtGui.QApplication.translate("Properties", "Account", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Properties", "Number of items in filelist", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Properties", "Auto-copy short URL to clipboard", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("Properties", "General", None, QtGui.QApplication.UnicodeUTF8))
        self.okButton.setText(QtGui.QApplication.translate("Properties", "Ok", None, QtGui.QApplication.UnicodeUTF8))
        self.cancelButton.setText(QtGui.QApplication.translate("Properties", "Cancel", None, QtGui.QApplication.UnicodeUTF8))

import icons_rc