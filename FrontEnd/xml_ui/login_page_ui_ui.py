# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login_page_ui.ui'
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
        Dialog.resize(480, 760)
        Dialog.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.drop_shadow_frame = QFrame(Dialog)
        self.drop_shadow_frame.setObjectName(u"drop_shadow_frame")
        self.drop_shadow_frame.setStyleSheet(u"QFrame{\n"
"	border-radius:10px;\n"
"}\n"
"")
        self.drop_shadow_frame.setFrameShape(QFrame.StyledPanel)
        self.drop_shadow_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.drop_shadow_frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.drop_shadow_frame)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 40))
        self.frame.setMaximumSize(QSize(16777215, 40))
        self.frame.setStyleSheet(u"background-color:rgb(29, 32, 38);\n"
"border-bottom-left-radius:0px;\n"
"border-bottom-right-radius:0px;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.frame_5)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 38))
        self.pushButton.setMaximumSize(QSize(16777215, 38))
        font = QFont()
        font.setFamily(u"Roboto")
        self.pushButton.setFont(font)
        self.pushButton.setFocusPolicy(Qt.NoFocus)
        self.pushButton.setStyleSheet(u"color: rgb(185, 185, 185);\n"
"text-align: left;\n"
"padding-left:15px;")
        icon = QIcon()
        icon.addFile(u"Reqs/app_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(25, 25))

        self.horizontalLayout_2.addWidget(self.pushButton)


        self.horizontalLayout.addWidget(self.frame_5)

        self.button_close = QPushButton(self.frame)
        self.button_close.setObjectName(u"button_close")
        self.button_close.setMinimumSize(QSize(0, 0))
        self.button_close.setMaximumSize(QSize(60, 40))
        self.button_close.setFocusPolicy(Qt.NoFocus)
        self.button_close.setStyleSheet(u"QPushButton{\n"
"	border:none;\n"
"	border-top-right-radius:10px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color:rgb(232, 0, 116)\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"Reqs/close-24 copy.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_close.setIcon(icon1)
        self.button_close.setIconSize(QSize(25, 25))

        self.horizontalLayout.addWidget(self.button_close)


        self.verticalLayout_2.addWidget(self.frame)

        self.frame_2 = QFrame(self.drop_shadow_frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"border-top-left-radius:0px;\n"
"border-top-right-radius:0px;")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.stackedWidget = QStackedWidget(self.frame_2)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(0, 0, 480, 720))
        self.stackedWidget.setStyleSheet(u"")
        self.signup_page = QWidget()
        self.signup_page.setObjectName(u"signup_page")
        self.frame_3 = QFrame(self.signup_page)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(0, 0, 480, 720))
        self.frame_3.setStyleSheet(u"background-color:rgb(27, 29, 35)")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 60, 461, 31))
        font1 = QFont()
        font1.setFamily(u"Roboto")
        font1.setPointSize(16)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"color:rgba(255, 255, 255, 180);")
        self.label.setAlignment(Qt.AlignCenter)
        self.email_lineEdit = QLineEdit(self.frame_3)
        self.email_lineEdit.setObjectName(u"email_lineEdit")
        self.email_lineEdit.setGeometry(QRect(120, 210, 241, 41))
        self.email_lineEdit.setFont(font)
        self.email_lineEdit.setStyleSheet(u"QLineEdit{\n"
"	border:2px solid rgb(37,39,48);\n"
"   	border-radius:20px;\n"
"    background-color:rgb(34,36,44);\n"
"    color:#FFF;\n"
"    padding-left:25px;\n"
"    padding-right:25px;\n"
"}\n"
"QLineEdit:hover{\n"
"    border:2px solid rgb(48,50,62);\n"
"}\n"
"QLineEdit:focus{\n"
"	border:2px solid rgb(85,170,255);\n"
"}")
        self.email_lineEdit.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.pass_lineEdit = QLineEdit(self.frame_3)
        self.pass_lineEdit.setObjectName(u"pass_lineEdit")
        self.pass_lineEdit.setGeometry(QRect(120, 270, 241, 41))
        self.pass_lineEdit.setFont(font)
        self.pass_lineEdit.setStyleSheet(u"QLineEdit{\n"
"	border:2px solid rgb(37,39,48);\n"
"   	border-radius:20px;\n"
"    background-color:rgb(34,36,44);\n"
"    color:#FFF;\n"
"    padding-left:25px;\n"
"    padding-right:25px;\n"
"}\n"
"QLineEdit:hover{\n"
"    border:2px solid rgb(48,50,62);\n"
"}\n"
"QLineEdit:focus{\n"
"	border:2px solid rgb(85,170,255);\n"
"}")
        self.pass_lineEdit.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.signup_button = QPushButton(self.frame_3)
        self.signup_button.setObjectName(u"signup_button")
        self.signup_button.setGeometry(QRect(180, 390, 121, 41))
        font2 = QFont()
        font2.setFamily(u"Roboto")
        font2.setPointSize(9)
        self.signup_button.setFont(font2)
        self.signup_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.signup_button.setStyleSheet(u"QPushButton{\n"
"      border-radius:16px;\n"
"      border:2px solid rgb(37,39,48);\n"
"      background-color:rgb(34,36,44);\n"
"      color:rgb(85,170,255);\n"
"      font-size:9pt;\n"
"}\n"
"QPushButton:hover{\n"
"      border:2px solid rgb(114, 254, 120);\n"
"}")
        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(120, 580, 181, 20))
        self.label_2.setFont(font2)
        self.label_2.setStyleSheet(u"color:rgba(255, 255, 255, 230);")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.login_page_button = QPushButton(self.frame_3)
        self.login_page_button.setObjectName(u"login_page_button")
        self.login_page_button.setGeometry(QRect(300, 580, 61, 20))
        self.login_page_button.setFont(font2)
        self.login_page_button.setFocusPolicy(Qt.NoFocus)
        self.login_page_button.setStyleSheet(u"QPushButton{\n"
"	color: rgb(0, 170, 255);\n"
"	border:none;\n"
"	background:none;\n"
"}")
        self.info_label = QLabel(self.frame_3)
        self.info_label.setObjectName(u"info_label")
        self.info_label.setGeometry(QRect(10, 320, 461, 41))
        font3 = QFont()
        font3.setFamily(u"Roboto Medium")
        font3.setPointSize(8)
        self.info_label.setFont(font3)
        self.info_label.setFocusPolicy(Qt.NoFocus)
        self.info_label.setStyleSheet(u"color:rgb(255, 0, 0);")
        self.info_label.setAlignment(Qt.AlignCenter)
        self.info_label.setWordWrap(True)
        self.uname_lineEdit = QLineEdit(self.frame_3)
        self.uname_lineEdit.setObjectName(u"uname_lineEdit")
        self.uname_lineEdit.setGeometry(QRect(120, 150, 241, 41))
        self.uname_lineEdit.setFont(font)
        self.uname_lineEdit.setStyleSheet(u"QLineEdit{\n"
"	border:2px solid rgb(37,39,48);\n"
"   	border-radius:20px;\n"
"    background-color:rgb(34,36,44);\n"
"    color:#FFF;\n"
"    padding-left:25px;\n"
"    padding-right:25px;\n"
"}\n"
"QLineEdit:hover{\n"
"    border:2px solid rgb(48,50,62);\n"
"}\n"
"QLineEdit:focus{\n"
"	border:2px solid rgb(85,170,255);\n"
"}")
        self.uname_lineEdit.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.stackedWidget.addWidget(self.signup_page)
        self.login_page = QWidget()
        self.login_page.setObjectName(u"login_page")
        self.frame_4 = QFrame(self.login_page)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(0, 0, 480, 720))
        self.frame_4.setStyleSheet(u"background-color:rgb(27, 29, 35)")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.label_3 = QLabel(self.frame_4)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 60, 461, 31))
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"color:rgba(255, 255, 255, 180);")
        self.label_3.setAlignment(Qt.AlignCenter)
        self.uid_lineEdit_2 = QLineEdit(self.frame_4)
        self.uid_lineEdit_2.setObjectName(u"uid_lineEdit_2")
        self.uid_lineEdit_2.setGeometry(QRect(120, 190, 241, 41))
        self.uid_lineEdit_2.setFont(font)
        self.uid_lineEdit_2.setStyleSheet(u"QLineEdit{\n"
"	border:2px solid rgb(37,39,48);\n"
"   	border-radius:20px;\n"
"    background-color:rgb(34,36,44);\n"
"    color:#FFF;\n"
"    padding-left:25px;\n"
"    padding-right:25px;\n"
"}\n"
"QLineEdit:hover{\n"
"    border:2px solid rgb(48,50,62);\n"
"}\n"
"QLineEdit:focus{\n"
"	border:2px solid rgb(85,170,255);\n"
"}")
        self.uid_lineEdit_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.pass_lineEdit_2 = QLineEdit(self.frame_4)
        self.pass_lineEdit_2.setObjectName(u"pass_lineEdit_2")
        self.pass_lineEdit_2.setGeometry(QRect(120, 250, 241, 41))
        self.pass_lineEdit_2.setFont(font)
        self.pass_lineEdit_2.setStyleSheet(u"QLineEdit{\n"
"	border:2px solid rgb(37,39,48);\n"
"   	border-radius:20px;\n"
"    background-color:rgb(34,36,44);\n"
"    color:#FFF;\n"
"    padding-left:25px;\n"
"    padding-right:25px;\n"
"}\n"
"QLineEdit:hover{\n"
"    border:2px solid rgb(48,50,62);\n"
"}\n"
"QLineEdit:focus{\n"
"	border:2px solid rgb(85,170,255);\n"
"}")
        self.pass_lineEdit_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.login_button = QPushButton(self.frame_4)
        self.login_button.setObjectName(u"login_button")
        self.login_button.setGeometry(QRect(180, 390, 121, 41))
        self.login_button.setFont(font2)
        self.login_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.login_button.setStyleSheet(u"QPushButton{\n"
"      border-radius:16px;\n"
"      border:2px solid rgb(37,39,48);\n"
"      background-color:rgb(34,36,44);\n"
"      color:rgb(85,170,255);\n"
"      font-size:9pt;\n"
"}\n"
"QPushButton:hover{\n"
"      /*border:2px solid rgb(114, 254, 120); */\n"
"	border: 2px solid rgb(231, 0, 116);\n"
"}")
        self.label_4 = QLabel(self.frame_4)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(120, 580, 171, 20))
        self.label_4.setFont(font2)
        self.label_4.setStyleSheet(u"color:rgba(255, 255, 255, 230);")
        self.label_4.setAlignment(Qt.AlignCenter)
        self.signup_page_button = QPushButton(self.frame_4)
        self.signup_page_button.setObjectName(u"signup_page_button")
        self.signup_page_button.setGeometry(QRect(290, 580, 61, 20))
        self.signup_page_button.setFont(font2)
        self.signup_page_button.setFocusPolicy(Qt.NoFocus)
        self.signup_page_button.setStyleSheet(u"QPushButton{\n"
"	color: rgb(0, 170, 255);\n"
"	border:none;\n"
"	background:none;\n"
"}")
        self.info_label2 = QLabel(self.frame_4)
        self.info_label2.setObjectName(u"info_label2")
        self.info_label2.setGeometry(QRect(10, 300, 461, 31))
        self.info_label2.setFont(font3)
        self.info_label2.setStyleSheet(u"color:rgb(255, 0, 0);")
        self.info_label2.setAlignment(Qt.AlignCenter)
        self.stackedWidget.addWidget(self.login_page)

        self.verticalLayout_2.addWidget(self.frame_2)


        self.verticalLayout.addWidget(self.drop_shadow_frame)


        self.retranslateUi(Dialog)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u" AI Personalized Learning App", None))
        self.button_close.setText("")
        self.label.setText(QCoreApplication.translate("Dialog", u"SIGN UP", None))
        self.email_lineEdit.setText("")
        self.email_lineEdit.setPlaceholderText(QCoreApplication.translate("Dialog", u"Email", None))
        self.pass_lineEdit.setText("")
        self.pass_lineEdit.setPlaceholderText(QCoreApplication.translate("Dialog", u"Password", None))
        self.signup_button.setText(QCoreApplication.translate("Dialog", u"Sign Up", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Already have an account ?", None))
        self.login_page_button.setText(QCoreApplication.translate("Dialog", u"Log in", None))
        self.info_label.setText("")
        self.uname_lineEdit.setText("")
        self.uname_lineEdit.setPlaceholderText(QCoreApplication.translate("Dialog", u"Username", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Log In", None))
        self.uid_lineEdit_2.setText("")
        self.uid_lineEdit_2.setPlaceholderText(QCoreApplication.translate("Dialog", u"Username", None))
        self.pass_lineEdit_2.setText("")
        self.pass_lineEdit_2.setPlaceholderText(QCoreApplication.translate("Dialog", u"Password", None))
        self.login_button.setText(QCoreApplication.translate("Dialog", u"Log In", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Don't have an account ?", None))
        self.signup_page_button.setText(QCoreApplication.translate("Dialog", u"Sign Up", None))
        self.info_label2.setText("")
    # retranslateUi

