# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'message_ui.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(600, 180)
        self.drop_shadow_frame = QFrame(Dialog)
        self.drop_shadow_frame.setObjectName(u"drop_shadow_frame")
        self.drop_shadow_frame.setGeometry(QRect(10, 10, 578, 158))
        self.drop_shadow_frame.setStyleSheet(u"background-color: rgb(27, 29, 35);\n"
"border-radius:5px;")
        self.drop_shadow_frame.setFrameShape(QFrame.StyledPanel)
        self.drop_shadow_frame.setFrameShadow(QFrame.Raised)
        self.msg = QLabel(self.drop_shadow_frame)
        self.msg.setObjectName(u"msg")
        self.msg.setGeometry(QRect(0, 0, 578, 31))
        font = QFont()
        font.setFamily(u"Roboto")
        font.setPointSize(9)
        self.msg.setFont(font)
        self.msg.setStyleSheet(u"#msg{\n"
"	padding-left:20px;\n"
"	background-color: rgb(37, 40, 48);\n"
"	color:rgba(255, 255, 255, 180);\n"
"	border-top-left-radius: 5px;\n"
"	border-top-right-radius:5px;\n"
"}")
        self.btn_ok = QPushButton(self.drop_shadow_frame)
        self.btn_ok.setObjectName(u"btn_ok")
        self.btn_ok.setGeometry(QRect(430, 100, 91, 31))
        self.btn_ok.setFont(font)
        self.btn_ok.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_ok.setStyleSheet(u"QPushButton{\n"
"      border-radius:12px;\n"
"      /*border:2px solid rgb(41, 44, 53);*/\n"
"	  border:2px solid rgb(58, 175, 175);\n"
"      background-color:rgb(34,36,44);\n"
"      color:rgba(255, 255, 255, 180);\n"
"      font-size:9pt;\n"
"}\n"
"QPushButton:hover{\n"
"      /*border:2px solid rgb(114, 254, 120); */\n"
"	border: 2px solid rgb(231, 0, 116);\n"
"}")
        self.info = QLabel(self.drop_shadow_frame)
        self.info.setObjectName(u"info")
        self.info.setGeometry(QRect(10, 60, 551, 31))
        font1 = QFont()
        font1.setFamily(u"Roboto Medium")
        font1.setPointSize(10)
        self.info.setFont(font1)
        self.info.setStyleSheet(u"color:rgba(255, 255, 255, 180);")
        self.info.setAlignment(Qt.AlignCenter)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.msg.setText(QCoreApplication.translate("Dialog", u"Message from Server", None))
        self.btn_ok.setText(QCoreApplication.translate("Dialog", u"Ok", None))
        self.info.setText(QCoreApplication.translate("Dialog", u"User Preferences updated successfully", None))
    # retranslateUi

