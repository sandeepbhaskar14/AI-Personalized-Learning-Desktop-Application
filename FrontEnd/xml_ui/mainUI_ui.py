# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainUI.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from ui_controllers.auto_grow_text_edit import AutoGrowTextEdit
from ui_controllers.sticky_search_button import StickyButton


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1345, 759)
        MainWindow.setStyleSheet(u"QMainWindow{\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius:10px;\n"
"}\n"
"\n"
"/* Styles for the vertical scrollbar */\n"
"\n"
"QScrollBar:vertical {\n"
"	border-radius:4px;\n"
"    background-color: rgb(60, 60, 91);/* #F0F0F0; */\n"
"    width: 8px;\n"
"    margin: 0px 0px 20px 0px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    /*background-color: #4F9FFE;*/\n"
"	background-color:rgb(80, 80, 122);\n"
"	border-radius:4px;\n"
"    min-height: 20px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover {\n"
"    /*background-color: #4F9FFE;*/\n"
"	/*background-color: rgb(170, 0, 255);*/\n"
"	background-color:rgb(0, 128, 255);\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"    height: 0px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"    height: 0px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"    width: 0px;\n"
""
                        "    height: 0px;\n"
"    background: none;\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"    background: none;\n"
"}\n"
"\n"
"\n"
"/*stylesheet for horizontal scrollbar*/\n"
"\n"
"\n"
"QScrollBar:horizontal {\n"
"	border-radius:5px;\n"
"    background-color: rgb(60, 60, 91);/* #F0F0F0; */\n"
"    width: 12px;\n"
"    margin: 0px 0px 0px 0px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"    /*background-color: #4F9FFE;*/\n"
"	background-color:rgb(80, 80, 122);\n"
"	border-radius:5px;\n"
"    min-height: 20px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal:hover {\n"
"    /*background-color: #4F9FFE;*/\n"
"	background-color: rgb(170, 0, 255);;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"    height: 0px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"    height: 0px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::left-arrow:horizontal, QScr"
                        "ollBar::right-arrow:horizontal {\n"
"    width: 0px;\n"
"    height: 0px;\n"
"    background: none;\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {\n"
"    background: none;\n"
"}\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"border-radius:10px;")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.drop_shadow_frame = QFrame(self.centralwidget)
        self.drop_shadow_frame.setObjectName(u"drop_shadow_frame")
        self.drop_shadow_frame.setStyleSheet(u"QFrame{\n"
"	border-radius:10px;\n"
"}")
        self.drop_shadow_frame.setFrameShape(QFrame.StyledPanel)
        self.drop_shadow_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.drop_shadow_frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.Top_Bar = QFrame(self.drop_shadow_frame)
        self.Top_Bar.setObjectName(u"Top_Bar")
        self.Top_Bar.setMaximumSize(QSize(16777215, 40))
        self.Top_Bar.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(38, 42, 52);\n"
"}")
        self.Top_Bar.setFrameShape(QFrame.StyledPanel)
        self.Top_Bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.Top_Bar)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.toggle_frame = QFrame(self.Top_Bar)
        self.toggle_frame.setObjectName(u"toggle_frame")
        self.toggle_frame.setMaximumSize(QSize(85, 16777215))
        self.toggle_frame.setStyleSheet(u"QFrame{\n"
"	border-radius:0px;\n"
"	border-top-left-radius:10px;\n"
"}\n"
"QFrame:hover{\n"
"	background-color: rgba(79, 159, 254, 220);\n"
"}")
        self.toggle_frame.setFrameShape(QFrame.StyledPanel)
        self.toggle_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.toggle_frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.toggle_button = QPushButton(self.toggle_frame)
        self.toggle_button.setObjectName(u"toggle_button")
        self.toggle_button.setMinimumSize(QSize(0, 40))
        self.toggle_button.setMaximumSize(QSize(80, 16777215))
        self.toggle_button.setStyleSheet(u"QPushButton{\n"
"	border:none;\n"
"	background:none;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"../Reqs/menu-50 copy.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toggle_button.setIcon(icon1)
        self.toggle_button.setIconSize(QSize(25, 25))

        self.horizontalLayout_2.addWidget(self.toggle_button)


        self.horizontalLayout.addWidget(self.toggle_frame)

        self.top_bar_frame = QFrame(self.Top_Bar)
        self.top_bar_frame.setObjectName(u"top_bar_frame")
        self.top_bar_frame.setFrameShape(QFrame.StyledPanel)
        self.top_bar_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.top_bar_frame)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(10, 0, 0, 0)
        self.icon = QPushButton(self.top_bar_frame)
        self.icon.setObjectName(u"icon")
        self.icon.setMinimumSize(QSize(0, 35))
        self.icon.setMaximumSize(QSize(40, 16777215))
        self.icon.setStyleSheet(u"background-color: rgb(38, 42, 52);\n"
"border:none;")
        icon2 = QIcon()
        icon2.addFile(u"../Reqs/app_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.icon.setIcon(icon2)
        self.icon.setIconSize(QSize(27, 27))

        self.horizontalLayout_5.addWidget(self.icon)

        self.status_bar = QLabel(self.top_bar_frame)
        self.status_bar.setObjectName(u"status_bar")
        font = QFont()
        font.setFamily(u"Roboto")
        font.setPointSize(9)
        self.status_bar.setFont(font)
        self.status_bar.setStyleSheet(u"color: rgb(220, 220, 220);")

        self.horizontalLayout_5.addWidget(self.status_bar)


        self.horizontalLayout.addWidget(self.top_bar_frame)

        self.top_bar_button_frame = QFrame(self.Top_Bar)
        self.top_bar_button_frame.setObjectName(u"top_bar_button_frame")
        self.top_bar_button_frame.setMinimumSize(QSize(200, 0))
        self.top_bar_button_frame.setMaximumSize(QSize(200, 16777215))
        self.top_bar_button_frame.setStyleSheet(u"border-radius:0px;\n"
"border-top-right-radius:10px;\n"
"")
        self.top_bar_button_frame.setFrameShape(QFrame.StyledPanel)
        self.top_bar_button_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.top_bar_button_frame)
        self.horizontalLayout_3.setSpacing(2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.button_minimize = QPushButton(self.top_bar_button_frame)
        self.button_minimize.setObjectName(u"button_minimize")
        self.button_minimize.setMinimumSize(QSize(0, 40))
        self.button_minimize.setStyleSheet(u"QPushButton{\n"
"	border:none;\n"
"	background:none;\n"
"	border-radius:0px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(45, 50, 62);\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u"../Reqs/subtract-24 copy.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_minimize.setIcon(icon3)

        self.horizontalLayout_3.addWidget(self.button_minimize)

        self.button_restore = QPushButton(self.top_bar_button_frame)
        self.button_restore.setObjectName(u"button_restore")
        self.button_restore.setMinimumSize(QSize(0, 40))
        self.button_restore.setStyleSheet(u"QPushButton{\n"
"	border:none;\n"
"	background:none;\n"
"	border-radius:0px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color:  rgb(45, 50, 62);\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u"../Reqs/maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_restore.setIcon(icon4)

        self.horizontalLayout_3.addWidget(self.button_restore)

        self.button_close = QPushButton(self.top_bar_button_frame)
        self.button_close.setObjectName(u"button_close")
        self.button_close.setMinimumSize(QSize(0, 40))
        self.button_close.setStyleSheet(u"QPushButton{\n"
"	border:none;\n"
"	background:none;\n"
"	border-radius:0px;\n"
"	border-top-right-radius:10px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color:rgb(212, 58, 212)\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u"../Reqs/close-24 copy.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_close.setIcon(icon5)

        self.horizontalLayout_3.addWidget(self.button_close)


        self.horizontalLayout.addWidget(self.top_bar_button_frame)


        self.verticalLayout_2.addWidget(self.Top_Bar)

        self.Content = QFrame(self.drop_shadow_frame)
        self.Content.setObjectName(u"Content")
        self.Content.setStyleSheet(u"border-bottom-left-radius:10px;\n"
"border-bottom-right-radius:10px;")
        self.Content.setFrameShape(QFrame.StyledPanel)
        self.Content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.Content)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.toggle_frame_left = QFrame(self.Content)
        self.toggle_frame_left.setObjectName(u"toggle_frame_left")
        self.toggle_frame_left.setMinimumSize(QSize(85, 0))
        self.toggle_frame_left.setMaximumSize(QSize(85, 16777215))
        self.toggle_frame_left.setStyleSheet(u"background-color: #272C36;\n"
"border-radius:0px;\n"
"border-bottom-left-radius:10px;\n"
"")
        self.toggle_frame_left.setFrameShape(QFrame.StyledPanel)
        self.toggle_frame_left.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.toggle_frame_left)
        self.verticalLayout_3.setSpacing(5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_status = QFrame(self.toggle_frame_left)
        self.frame_status.setObjectName(u"frame_status")
        self.frame_status.setMinimumSize(QSize(0, 50))
        self.frame_status.setMaximumSize(QSize(16777215, 50))
        self.frame_status.setCursor(QCursor(Qt.PointingHandCursor))
        self.frame_status.setStyleSheet(u"QFrame{\n"
"	border-radius: 0px;\n"
"	border-bottom: 1px solid rgba(255, 255, 255, 30);\n"
"}\n"
"QFrame:hover{\n"
"	background-color: rgb(55, 62, 76);\n"
"	border:2px solid rgba(0, 159, 238, 140);\n"
"	border-radius:5px;\n"
"}")
        self.frame_status.setFrameShape(QFrame.StyledPanel)
        self.frame_status.setFrameShadow(QFrame.Raised)
        self.button_new_chat = QPushButton(self.frame_status)
        self.button_new_chat.setObjectName(u"button_new_chat")
        self.button_new_chat.setGeometry(QRect(5, 0, 231, 50))
        self.button_new_chat.setMinimumSize(QSize(70, 50))
        self.button_new_chat.setMaximumSize(QSize(16777215, 50))
        font1 = QFont()
        font1.setFamily(u"Noto Sans")
        font1.setPointSize(10)
        self.button_new_chat.setFont(font1)
        self.button_new_chat.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_new_chat.setLayoutDirection(Qt.LeftToRight)
        self.button_new_chat.setStyleSheet(u"background:none;\n"
"border:none;\n"
"color: rgba(255, 255, 255, 180);")
        icon6 = QIcon()
        icon6.addFile(u"../Reqs/new_chat.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_new_chat.setIcon(icon6)
        self.button_new_chat.setIconSize(QSize(35, 35))

        self.verticalLayout_3.addWidget(self.frame_status)

        self.label_7 = QLabel(self.toggle_frame_left)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(0, 40))
        self.label_7.setStyleSheet(u"background:none;\n"
"border:none;\n"
"padding-left:10px;\n"
"color: rgba(255, 255, 255, 140);")

        self.verticalLayout_3.addWidget(self.label_7)

        self.frame_driver_protection_2 = QFrame(self.toggle_frame_left)
        self.frame_driver_protection_2.setObjectName(u"frame_driver_protection_2")
        self.frame_driver_protection_2.setFrameShape(QFrame.StyledPanel)
        self.frame_driver_protection_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_driver_protection_2)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.chat_history = QListWidget(self.frame_driver_protection_2)
        self.chat_history.setObjectName(u"chat_history")

        self.verticalLayout_10.addWidget(self.chat_history)


        self.verticalLayout_3.addWidget(self.frame_driver_protection_2)

        self.frame_settings = QFrame(self.toggle_frame_left)
        self.frame_settings.setObjectName(u"frame_settings")
        self.frame_settings.setMinimumSize(QSize(0, 60))
        self.frame_settings.setMaximumSize(QSize(16777215, 60))
        self.frame_settings.setCursor(QCursor(Qt.PointingHandCursor))
        self.frame_settings.setStyleSheet(u"QFrame{\n"
"	border-radius: 0px;\n"
"	border-top: 1px solid rgba(255, 255, 255, 30);\n"
"}\n"
"QFrame:hover{\n"
"	background-color: rgb(55, 62, 76);\n"
"	border:2px solid rgba(0, 159, 238, 140);\n"
"	border-radius:0px;\n"
"	border-bottom-left-radius:10px;\n"
"}")
        self.frame_settings.setFrameShape(QFrame.StyledPanel)
        self.frame_settings.setFrameShadow(QFrame.Raised)
        self.button_settings = QPushButton(self.frame_settings)
        self.button_settings.setObjectName(u"button_settings")
        self.button_settings.setGeometry(QRect(-2, 0, 221, 60))
        self.button_settings.setMinimumSize(QSize(0, 60))
        self.button_settings.setMaximumSize(QSize(250, 250))
        self.button_settings.setFont(font1)
        self.button_settings.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_settings.setStyleSheet(u"background:none;\n"
"border:none;\n"
"color: rgba(255, 255, 255, 180);")
        icon7 = QIcon()
        icon7.addFile(u"../Reqs/settings-50 copy.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_settings.setIcon(icon7)
        self.button_settings.setIconSize(QSize(35, 35))

        self.verticalLayout_3.addWidget(self.frame_settings)


        self.horizontalLayout_4.addWidget(self.toggle_frame_left)

        self.content_page_frame = QFrame(self.Content)
        self.content_page_frame.setObjectName(u"content_page_frame")
        self.content_page_frame.setStyleSheet(u"background-color:#2C313C;\n"
"border-radius:0px;\n"
"border-bottom-right-radius:10px;\n"
"")
        self.content_page_frame.setFrameShape(QFrame.StyledPanel)
        self.content_page_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.content_page_frame)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.content_page_frame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"")
        self.new_chat_page = QWidget()
        self.new_chat_page.setObjectName(u"new_chat_page")
        self.verticalLayout_5 = QVBoxLayout(self.new_chat_page)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_8 = QFrame(self.new_chat_page)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_11 = QFrame(self.frame_8)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_7.addWidget(self.frame_11)

        self.frame_9 = QFrame(self.frame_8)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMinimumSize(QSize(700, 0))
        self.frame_9.setMaximumSize(QSize(600, 16777215))
        font2 = QFont()
        font2.setFamily(u"MingLiU_HKSCS-ExtB")
        self.frame_9.setFont(font2)
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_9)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_12 = QFrame(self.frame_9)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label = QLabel(self.frame_12)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"background:none;\n"
"border:none;")
        self.label.setPixmap(QPixmap(u"C:/Users/san76/.designer/backup/Reqs/protected.png"))
        self.label.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.horizontalLayout_8.addWidget(self.label)


        self.verticalLayout_6.addWidget(self.frame_12)

        self.frame_13 = QFrame(self.frame_9)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setMinimumSize(QSize(0, 400))
        self.frame_13.setLayoutDirection(Qt.LeftToRight)
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.labelProtection = QLabel(self.frame_13)
        self.labelProtection.setObjectName(u"labelProtection")
        self.labelProtection.setGeometry(QRect(170, 60, 382, 54))
        self.labelProtection.setMaximumSize(QSize(16777215, 80))
        font3 = QFont()
        font3.setFamily(u"Roboto")
        font3.setPointSize(30)
        self.labelProtection.setFont(font3)
        self.labelProtection.setStyleSheet(u"background:none;\n"
"border:none;\n"
"color:rgba(255, 255, 255, 180);")
        self.labelProtection.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.searchButton = StickyButton(self.frame_13)
        self.searchButton.setObjectName(u"searchButton")
        self.searchButton.setGeometry(QRect(642, 141, 45, 45))
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.searchButton.sizePolicy().hasHeightForWidth())
        self.searchButton.setSizePolicy(sizePolicy)
        self.searchButton.setMinimumSize(QSize(45, 45))
        self.searchButton.setMaximumSize(QSize(45, 45))
        font4 = QFont()
        font4.setFamily(u"Noto Sans Medium")
        font4.setPointSize(10)
        self.searchButton.setFont(font4)
        self.searchButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.searchButton.setStyleSheet(u"QPushButton{\n"
"	background:none;\n"
"	border:none;\n"
"	color:rgba(255, 255, 255, 180);\n"
"	background-color: rgb(41, 44, 53);\n"
"	border-radius: 21px ;\n"
"	margin-top:3px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(45, 48, 58);\n"
"}")
        icon8 = QIcon()
        icon8.addFile(u"../Reqs/search.png", QSize(), QIcon.Normal, QIcon.Off)
        self.searchButton.setIcon(icon8)
        self.searchButton.setIconSize(QSize(27, 27))
        self.addButton = StickyButton(self.frame_13)
        self.addButton.setObjectName(u"addButton")
        self.addButton.setGeometry(QRect(12, 140, 51, 45))
        self.addButton.setMinimumSize(QSize(0, 45))
        self.addButton.setMaximumSize(QSize(160, 16777215))
        self.addButton.setFont(font4)
        self.addButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.addButton.setStyleSheet(u"QPushButton{\n"
"	background:none;\n"
"	border:none;\n"
"	color:rgba(255, 255, 255, 180);\n"
"	border-radius: 21px ;\n"
"	margin-top:3px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(45, 48, 58);\n"
"}")
        icon9 = QIcon()
        icon9.addFile(u"../Reqs/add_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.addButton.setIcon(icon9)
        self.addButton.setIconSize(QSize(22, 22))
        self.text_prompt = AutoGrowTextEdit(self.frame_13)
        self.text_prompt.setObjectName(u"text_prompt")
        self.text_prompt.setEnabled(True)
        self.text_prompt.setGeometry(QRect(10, 140, 681, 50))
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.text_prompt.sizePolicy().hasHeightForWidth())
        self.text_prompt.setSizePolicy(sizePolicy1)
        self.text_prompt.setMinimumSize(QSize(0, 50))
        self.text_prompt.setMaximumSize(QSize(16777215, 50))
        self.text_prompt.setSizeIncrement(QSize(0, 0))
        self.text_prompt.setBaseSize(QSize(0, 0))
        font5 = QFont()
        font5.setFamily(u"Roboto")
        font5.setPointSize(10)
        self.text_prompt.setFont(font5)
        self.text_prompt.setStyleSheet(u"QTextEdit{\n"
" 	border:2px solid rgb(41, 44, 53);\n"
"    border-radius:22px;\n"
"	background-color: rgb(41, 44, 53);\n"
"    color:rgba(255, 	255, 255, 210);\n"
"    padding-left:20px;\n"
"	padding-top:10px;\n"
"	padding-right:15px;\n"
"	padding-bottom:45px;\n"
"}\n"
"\n"
"QTextEdit:hover{\n"
"	border:2px solid rgb(220, 0, 220);\n"
"}\n"
"\n"
"QTextEdit:focus{\n"
"	border:2px solid rgb(85,170,255);\n"
"}")
        self.text_prompt.setFrameShape(QFrame.StyledPanel)
        self.text_prompt.setFrameShadow(QFrame.Plain)
        self.text_prompt.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.text_prompt.raise_()
        self.labelProtection.raise_()
        self.searchButton.raise_()
        self.addButton.raise_()

        self.verticalLayout_6.addWidget(self.frame_13)

        self.frame_14 = QFrame(self.frame_9)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)

        self.verticalLayout_6.addWidget(self.frame_14)


        self.horizontalLayout_7.addWidget(self.frame_9)

        self.frame_10 = QFrame(self.frame_8)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_10)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame_21 = QFrame(self.frame_10)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setMaximumSize(QSize(16777215, 100))
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_21)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.frame_23 = QFrame(self.frame_21)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_16.addWidget(self.frame_23)

        self.frame_24 = QFrame(self.frame_21)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setMinimumSize(QSize(0, 40))
        self.frame_24.setMaximumSize(QSize(120, 16777215))
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_24)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.login_button = QPushButton(self.frame_24)
        self.login_button.setObjectName(u"login_button")
        self.login_button.setMaximumSize(QSize(16777215, 30))
        font6 = QFont()
        font6.setFamily(u"Roboto")
        self.login_button.setFont(font6)
        self.login_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.login_button.setStyleSheet(u"QPushButton{\n"
"	color: rgba(255, 255, 255, 200);\n"
"	background-color: rgb(48, 53, 65);\n"
"	\n"
"	border-radius:10px;\n"
"}\n"
"QPushButton:hover{\n"
"	color:rgb(85, 170, 255);\n"
"	background-color:rgb(52, 57, 70)\n"
"}")

        self.horizontalLayout_17.addWidget(self.login_button)


        self.horizontalLayout_16.addWidget(self.frame_24)


        self.verticalLayout_11.addWidget(self.frame_21)

        self.frame_22 = QFrame(self.frame_10)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)

        self.verticalLayout_11.addWidget(self.frame_22)


        self.horizontalLayout_7.addWidget(self.frame_10)


        self.verticalLayout_5.addWidget(self.frame_8)

        self.stackedWidget.addWidget(self.new_chat_page)
        self.settings_page = QWidget()
        self.settings_page.setObjectName(u"settings_page")
        self.verticalLayout_4 = QVBoxLayout(self.settings_page)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_48 = QFrame(self.settings_page)
        self.frame_48.setObjectName(u"frame_48")
        self.frame_48.setFrameShape(QFrame.StyledPanel)
        self.frame_48.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_48)
        self.horizontalLayout_22.setSpacing(0)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.frame_49 = QFrame(self.frame_48)
        self.frame_49.setObjectName(u"frame_49")
        self.frame_49.setMinimumSize(QSize(250, 0))
        self.frame_49.setMaximumSize(QSize(250, 16777215))
        self.frame_49.setStyleSheet(u"background-color: rgb(43, 47, 58)")
        self.frame_49.setFrameShape(QFrame.StyledPanel)
        self.frame_49.setFrameShadow(QFrame.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.frame_49)
        self.verticalLayout_27.setSpacing(10)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.frame_51 = QFrame(self.frame_49)
        self.frame_51.setObjectName(u"frame_51")
        self.frame_51.setMaximumSize(QSize(16777215, 60))
        self.frame_51.setFrameShape(QFrame.StyledPanel)
        self.frame_51.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_51)
        self.horizontalLayout_23.setSpacing(0)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.label_32 = QLabel(self.frame_51)
        self.label_32.setObjectName(u"label_32")
        font7 = QFont()
        font7.setFamily(u"Roboto")
        font7.setPointSize(12)
        self.label_32.setFont(font7)
        self.label_32.setStyleSheet(u"color:rgba(255, 255, 255, 180);")
        self.label_32.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_23.addWidget(self.label_32)


        self.verticalLayout_27.addWidget(self.frame_51)

        self.frame_25 = QFrame(self.frame_49)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setMaximumSize(QSize(16777215, 50))
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_25)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.acc_button = QPushButton(self.frame_25)
        self.acc_button.setObjectName(u"acc_button")
        self.acc_button.setMinimumSize(QSize(0, 40))
        font8 = QFont()
        font8.setFamily(u"Roboto")
        font8.setPointSize(11)
        self.acc_button.setFont(font8)
        self.acc_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.acc_button.setStyleSheet(u"QPushButton{\n"
"	border-radius:5px;\n"
"	color:rgb(180, 180, 180);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color:rgb(59, 66, 81);\n"
"	border:2px solid rgb(212, 58, 212);\n"
"	border-radius:5px;\n"
"}")

        self.horizontalLayout_18.addWidget(self.acc_button)


        self.verticalLayout_27.addWidget(self.frame_25)

        self.frame_56 = QFrame(self.frame_49)
        self.frame_56.setObjectName(u"frame_56")
        self.frame_56.setMaximumSize(QSize(16777215, 50))
        self.frame_56.setFrameShape(QFrame.StyledPanel)
        self.frame_56.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.frame_56)
        self.horizontalLayout_24.setSpacing(0)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.buttonUI = QPushButton(self.frame_56)
        self.buttonUI.setObjectName(u"buttonUI")
        self.buttonUI.setMinimumSize(QSize(0, 40))
        self.buttonUI.setFont(font8)
        self.buttonUI.setCursor(QCursor(Qt.PointingHandCursor))
        self.buttonUI.setStyleSheet(u"QPushButton{\n"
"	border-radius:5px;\n"
"	color:rgb(180, 180, 180);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color:rgb(59, 66, 81);\n"
"	border:2px solid rgb(212, 58, 212);\n"
"	border-radius:5px;\n"
"}")

        self.horizontalLayout_24.addWidget(self.buttonUI)


        self.verticalLayout_27.addWidget(self.frame_56)

        self.frame_52 = QFrame(self.frame_49)
        self.frame_52.setObjectName(u"frame_52")
        self.frame_52.setMaximumSize(QSize(16777215, 50))
        self.frame_52.setFrameShape(QFrame.StyledPanel)
        self.frame_52.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.frame_52)
        self.horizontalLayout_25.setSpacing(0)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.buttonNotification = QPushButton(self.frame_52)
        self.buttonNotification.setObjectName(u"buttonNotification")
        self.buttonNotification.setMinimumSize(QSize(0, 40))
        self.buttonNotification.setFont(font8)
        self.buttonNotification.setCursor(QCursor(Qt.PointingHandCursor))
        self.buttonNotification.setStyleSheet(u"QPushButton{\n"
"	border-radius:5px;\n"
"	color:rgb(180, 180, 180);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color:rgb(59, 66, 81);\n"
"	border:2px solid rgb(212, 58, 212);\n"
"	border-radius:5px;\n"
"}")

        self.horizontalLayout_25.addWidget(self.buttonNotification)


        self.verticalLayout_27.addWidget(self.frame_52)

        self.frame_53 = QFrame(self.frame_49)
        self.frame_53.setObjectName(u"frame_53")
        self.frame_53.setMaximumSize(QSize(16777215, 50))
        self.frame_53.setFrameShape(QFrame.StyledPanel)
        self.frame_53.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.frame_53)
        self.horizontalLayout_26.setSpacing(0)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.buttonUpdate = QPushButton(self.frame_53)
        self.buttonUpdate.setObjectName(u"buttonUpdate")
        self.buttonUpdate.setMinimumSize(QSize(0, 40))
        self.buttonUpdate.setFont(font8)
        self.buttonUpdate.setCursor(QCursor(Qt.PointingHandCursor))
        self.buttonUpdate.setStyleSheet(u"QPushButton{\n"
"	border-radius:5px;\n"
"	color:rgb(180, 180, 180);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color:rgb(59, 66, 81);\n"
"	border:2px solid rgb(212, 58, 212);\n"
"	border-radius:5px;\n"
"}")

        self.horizontalLayout_26.addWidget(self.buttonUpdate)


        self.verticalLayout_27.addWidget(self.frame_53)

        self.button_preferences = QPushButton(self.frame_49)
        self.button_preferences.setObjectName(u"button_preferences")
        self.button_preferences.setMinimumSize(QSize(0, 40))
        self.button_preferences.setFont(font8)
        self.button_preferences.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_preferences.setStyleSheet(u"QPushButton{\n"
"	border-radius:5px;\n"
"	color:rgb(180, 180, 180);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color:rgb(59, 66, 81);\n"
"	border:2px solid rgb(212, 58, 212);\n"
"	border-radius:5px;\n"
"}")

        self.verticalLayout_27.addWidget(self.button_preferences)

        self.frame_54 = QFrame(self.frame_49)
        self.frame_54.setObjectName(u"frame_54")
        self.frame_54.setMaximumSize(QSize(16777215, 50))
        self.frame_54.setFrameShape(QFrame.StyledPanel)
        self.frame_54.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_27 = QHBoxLayout(self.frame_54)
        self.horizontalLayout_27.setSpacing(0)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.buttonAbout = QPushButton(self.frame_54)
        self.buttonAbout.setObjectName(u"buttonAbout")
        self.buttonAbout.setMinimumSize(QSize(0, 40))
        self.buttonAbout.setFont(font8)
        self.buttonAbout.setCursor(QCursor(Qt.PointingHandCursor))
        self.buttonAbout.setStyleSheet(u"QPushButton{\n"
"	border-radius:5px;\n"
"	color:rgb(180, 180, 180);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color:rgb(59, 66, 81);\n"
"	border:2px solid rgb(212, 58, 212);\n"
"	border-radius:5px;\n"
"}")

        self.horizontalLayout_27.addWidget(self.buttonAbout)


        self.verticalLayout_27.addWidget(self.frame_54)

        self.frame_57 = QFrame(self.frame_49)
        self.frame_57.setObjectName(u"frame_57")
        self.frame_57.setMaximumSize(QSize(16777215, 50))
        self.frame_57.setFrameShape(QFrame.StyledPanel)
        self.frame_57.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_28 = QHBoxLayout(self.frame_57)
        self.horizontalLayout_28.setSpacing(0)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_27.addWidget(self.frame_57)

        self.frame_55 = QFrame(self.frame_49)
        self.frame_55.setObjectName(u"frame_55")
        self.frame_55.setFrameShape(QFrame.StyledPanel)
        self.frame_55.setFrameShadow(QFrame.Raised)

        self.verticalLayout_27.addWidget(self.frame_55)


        self.horizontalLayout_22.addWidget(self.frame_49)

        self.frame_50 = QFrame(self.frame_48)
        self.frame_50.setObjectName(u"frame_50")
        self.frame_50.setFrameShape(QFrame.StyledPanel)
        self.frame_50.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_50)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.setting_pages = QStackedWidget(self.frame_50)
        self.setting_pages.setObjectName(u"setting_pages")
        self.preference_page = QWidget()
        self.preference_page.setObjectName(u"preference_page")
        self.horizontalLayout_9 = QHBoxLayout(self.preference_page)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.preference_page)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMaximumSize(QSize(350, 16777215))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_9.addWidget(self.frame_5)

        self.frame_3 = QFrame(self.preference_page)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(700, 0))
        self.frame_3.setStyleSheet(u"")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_3)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 20, 0, 0)
        self.frame_6 = QFrame(self.frame_3)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMaximumSize(QSize(16777215, 70))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.frame_6)
        self.label_2.setObjectName(u"label_2")
        font9 = QFont()
        font9.setFamily(u"Roboto")
        font9.setPointSize(13)
        self.label_2.setFont(font9)
        self.label_2.setStyleSheet(u"color:rgb(180, 180, 180);\n"
"background:transparent;")

        self.horizontalLayout_10.addWidget(self.label_2)


        self.verticalLayout_9.addWidget(self.frame_6)

        self.frame_15 = QFrame(self.frame_3)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setMaximumSize(QSize(16777215, 80))
        self.frame_15.setStyleSheet(u"#frame_15{\n"
"	background-color: rgb(52, 58, 71);\n"
"	border-radius:0px;\n"
"	border-top-left-radius:10px;\n"
"	border-top-right-radius:10px;\n"
"}")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(20, 0, 20, 0)
        self.label_3 = QLabel(self.frame_15)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font8)
        self.label_3.setStyleSheet(u"color:rgb(180, 180, 180);\n"
"background:transparent;\n"
"padding-top:15px;")
        self.label_3.setWordWrap(True)

        self.horizontalLayout_11.addWidget(self.label_3)

        self.learning_type = QComboBox(self.frame_15)
        self.learning_type.addItem("")
        self.learning_type.addItem("")
        self.learning_type.addItem("")
        self.learning_type.setObjectName(u"learning_type")
        self.learning_type.setMinimumSize(QSize(0, 30))
        self.learning_type.setMaximumSize(QSize(130, 16777215))
        self.learning_type.setStyleSheet(u"QComboBox {\n"
"    background:transparent ;\n"
"    border: 1px solid rgb(130, 130, 130);\n"
"    border-radius: 6px;\n"
"    padding: 6px 10px;\n"
"    padding-right: 30px; /* space for arrow */\n"
"    font-size: 14px;\n"
"    color:rgb(190, 190, 190);\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"    border: 1px solid #90caf9;\n"
"}\n"
"\n"
"QComboBox:focus {\n"
"    border: 1px solid #3a7bd5;\n"
"}\n"
"\n"
"/* Dropdown list */\n"
"QComboBox QAbstractItemView {\n"
"    background-color: rgb(52, 58, 71);\n"
"	color:rgb(190, 190, 190);\n"
"    border: 1px solid #c4c4c4;\n"
"	border-radius: 5px;\n"
"    selection-background-color:rgb(56, 63, 77);\n"
"    selection-color: rgb(200, 200, 200);\n"
"    padding: 5px;\n"
"    outline: 0;\n"
"	min-height: 80px;\n"
"}\n"
"\n"
"/* Selected item */\n"
"QComboBox QAbstractItemView::item {\n"
"	padding: 0px;\n"
"	font-size: 14px;\n"
"	min-height:40px;\n"
"    \n"
"}\n"
"\n"
"/* Hover item */\n"
"QComboBox QAbstractItemView::item:hover {\n"
"    background-color: #fff;\n"
"}\n"
"\n"
""
                        "\n"
"")

        self.horizontalLayout_11.addWidget(self.learning_type)


        self.verticalLayout_9.addWidget(self.frame_15)

        self.frame_7 = QFrame(self.frame_3)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMaximumSize(QSize(16777215, 80))
        self.frame_7.setStyleSheet(u"#frame_7{\n"
"	background-color: rgb(52, 58, 71);\n"
"	border-radius:0px;\n"
"}")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(20, 0, 20, 0)
        self.label_4 = QLabel(self.frame_7)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font8)
        self.label_4.setStyleSheet(u"color:rgb(180, 180, 180);\n"
"background:transparent;\n"
"padding-top:15px;")

        self.horizontalLayout_12.addWidget(self.label_4)

        self.difficulty_type = QComboBox(self.frame_7)
        self.difficulty_type.addItem("")
        self.difficulty_type.addItem("")
        self.difficulty_type.addItem("")
        self.difficulty_type.setObjectName(u"difficulty_type")
        self.difficulty_type.setMinimumSize(QSize(0, 30))
        self.difficulty_type.setMaximumSize(QSize(130, 16777215))
        self.difficulty_type.setStyleSheet(u"QComboBox {\n"
"    background:transparent ;\n"
"    border: 1px solid rgb(130, 130, 130);\n"
"    border-radius: 6px;\n"
"    padding: 6px 10px;\n"
"    padding-right: 30px; /* space for arrow */\n"
"    font-size: 14px;\n"
"    color:rgb(190, 190, 190);\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"    border: 1px solid #90caf9;\n"
"}\n"
"\n"
"QComboBox:focus {\n"
"    border: 1px solid #3a7bd5;\n"
"}\n"
"\n"
"/* Dropdown list */\n"
"QComboBox QAbstractItemView {\n"
"    background-color: rgb(52, 58, 71);\n"
"	color:rgb(190, 190, 190);\n"
"    border: 1px solid #c4c4c4;\n"
"	border-radius: 5px;\n"
"    selection-background-color:rgb(56, 63, 77);\n"
"    selection-color: rgb(200, 200, 200);\n"
"    padding: 5px;\n"
"    outline: 0;\n"
"	min-height: 80px;\n"
"}\n"
"\n"
"/* Selected item */\n"
"QComboBox QAbstractItemView::item {\n"
"	padding: 0px;\n"
"	font-size: 14px;\n"
"	min-height:40px;\n"
"    \n"
"}\n"
"\n"
"/* Hover item */\n"
"QComboBox QAbstractItemView::item:hover {\n"
"    background-color: #fff;\n"
"}\n"
"\n"
""
                        "\n"
"")

        self.horizontalLayout_12.addWidget(self.difficulty_type)


        self.verticalLayout_9.addWidget(self.frame_7)

        self.frame_16 = QFrame(self.frame_3)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setMaximumSize(QSize(16777215, 80))
        self.frame_16.setStyleSheet(u"#frame_16{\n"
"	background-color: rgb(52, 58, 71);\n"
"	border-radius:0px;\n"
"}")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_15.setSpacing(10)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(20, 0, 20, 0)
        self.label_5 = QLabel(self.frame_16)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font8)
        self.label_5.setStyleSheet(u"color:rgb(180, 180, 180);\n"
"background:transparent;\n"
"padding-top:15px;")

        self.horizontalLayout_15.addWidget(self.label_5)

        self.spinHour = QSpinBox(self.frame_16)
        self.spinHour.setObjectName(u"spinHour")
        self.spinHour.setEnabled(True)
        self.spinHour.setMaximumSize(QSize(61, 31))
        self.spinHour.setStyleSheet(u"QSpinBox {\n"
"    background-color: transparent;\n"
"    border: 1px solid rgb(139, 139, 139);\n"
"    border-radius: 6px;\n"
"    padding: 4px 15px 4px 8px;  /* space for arrows */\n"
"    font-size: 14px;\n"
"    color: rgb(200, 200, 200);\n"
"}\n"
"\n"
"QSpinBox:hover {\n"
"    border: 1px solid #90caf9;\n"
"}\n"
"\n"
"QSpinBox:focus {\n"
"    border: 1px solid #42a5f5;\n"
"}\n"
"\n"
"/* Up & Down buttons */\n"
"QSpinBox::up-button,\n"
"QSpinBox::down-button {\n"
"    width: 18px;\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}\n"
"\n"
"QSpinBox::up-button:hover,\n"
"QSpinBox::down-button:hover {\n"
"    background-color: rgb(56, 63, 77);\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"/* Arrows */\n"
"QSpinBox::up-arrow {\n"
"    image: none;\n"
"    width: 0;\n"
"    height: 0;\n"
"    border-left: 3px solid transparent;\n"
"    border-right: 3px solid transparent;\n"
"    border-bottom: 6px solid #546e7a;\n"
"}\n"
"\n"
"QSpinBox::down-arrow {\n"
"    image: none;\n"
"    width: 0;\n"
"    "
                        "height: 0;\n"
"    border-left: 3px solid transparent;\n"
"    border-right: 3px solid transparent;\n"
"    border-top: 6px solid #546e7a;\n"
"}\n"
"\n"
"/* Disabled state */\n"
"QSpinBox:disabled {\n"
"    background-color: #f5f5f5;\n"
"    color: #9e9e9e;\n"
"    border: 1px solid #e0e0e0;\n"
"}\n"
"")

        self.horizontalLayout_15.addWidget(self.spinHour)

        self.spinMinute = QSpinBox(self.frame_16)
        self.spinMinute.setObjectName(u"spinMinute")
        self.spinMinute.setMaximumSize(QSize(61, 31))
        self.spinMinute.setStyleSheet(u"QSpinBox {\n"
"    background-color: transparent;\n"
"    border: 1px solid rgb(139, 139, 139);\n"
"    border-radius: 6px;\n"
"    padding: 4px 15px 4px 8px;  /* space for arrows */\n"
"    font-size: 14px;\n"
"    color: rgb(200, 200, 200);\n"
"}\n"
"\n"
"QSpinBox:hover {\n"
"    border: 1px solid #90caf9;\n"
"}\n"
"\n"
"QSpinBox:focus {\n"
"    border: 1px solid #42a5f5;\n"
"}\n"
"\n"
"/* Up & Down buttons */\n"
"QSpinBox::up-button,\n"
"QSpinBox::down-button {\n"
"    width: 18px;\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}\n"
"\n"
"QSpinBox::up-button:hover,\n"
"QSpinBox::down-button:hover {\n"
"    background-color: rgb(56, 63, 77);\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"/* Arrows */\n"
"QSpinBox::up-arrow {\n"
"    image: none;\n"
"    width: 0;\n"
"    height: 0;\n"
"    border-left: 3px solid transparent;\n"
"    border-right: 3px solid transparent;\n"
"    border-bottom: 6px solid #546e7a;\n"
"}\n"
"\n"
"QSpinBox::down-arrow {\n"
"    image: none;\n"
"    width: 0;\n"
"    "
                        "height: 0;\n"
"    border-left: 3px solid transparent;\n"
"    border-right: 3px solid transparent;\n"
"    border-top: 6px solid #546e7a;\n"
"}\n"
"\n"
"/* Disabled state */\n"
"QSpinBox:disabled {\n"
"    background-color: #f5f5f5;\n"
"    color: #9e9e9e;\n"
"    border: 1px solid #e0e0e0;\n"
"}\n"
"")

        self.horizontalLayout_15.addWidget(self.spinMinute)


        self.verticalLayout_9.addWidget(self.frame_16)

        self.frame_17 = QFrame(self.frame_3)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setMaximumSize(QSize(16777215, 80))
        self.frame_17.setStyleSheet(u"#frame_17{\n"
"	background-color: rgb(52, 58, 71);\n"
"	border-radius:0px;\n"
"	border-bottom-left-radius:10px;\n"
"	border-bottom-right-radius:10px;\n"
"}")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(20, 0, 20, 0)
        self.label_6 = QLabel(self.frame_17)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font8)
        self.label_6.setStyleSheet(u"color:rgb(180, 180, 180);\n"
"background:transparent;\n"
"padding-top:15px;")

        self.horizontalLayout_14.addWidget(self.label_6)

        self.preferred_output = QComboBox(self.frame_17)
        self.preferred_output.addItem("")
        self.preferred_output.addItem("")
        self.preferred_output.addItem("")
        self.preferred_output.addItem("")
        self.preferred_output.setObjectName(u"preferred_output")
        self.preferred_output.setMinimumSize(QSize(0, 30))
        self.preferred_output.setMaximumSize(QSize(130, 16777215))
        self.preferred_output.setStyleSheet(u"QComboBox {\n"
"    background:transparent ;\n"
"    border: 1px solid rgb(130, 130, 130);\n"
"    border-radius: 6px;\n"
"    padding: 6px 10px;\n"
"    padding-right: 30px; /* space for arrow */\n"
"    font-size: 14px;\n"
"    color:rgb(190, 190, 190);\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"    border: 1px solid #5a9bd5;\n"
"}\n"
"\n"
"QComboBox:focus {\n"
"    border: 1px solid #3a7bd5;\n"
"}\n"
"\n"
"/* Dropdown list */\n"
"QComboBox QAbstractItemView {\n"
"    background-color: rgb(52, 58, 71);\n"
"	color:rgb(190, 190, 190);\n"
"    border: 1px solid #c4c4c4;\n"
"	border-radius: 5px;\n"
"    selection-background-color:rgb(56, 63, 77);\n"
"    selection-color: rgb(200, 200, 200);\n"
"    padding: 5px;\n"
"    outline: 0;\n"
"	min-height: 80px;\n"
"}\n"
"\n"
"/* Selected item */\n"
"QComboBox QAbstractItemView::item {\n"
"	padding: 0px;\n"
"	font-size: 14px;\n"
"	min-height:40px;\n"
"    \n"
"}\n"
"\n"
"/* Hover item */\n"
"QComboBox QAbstractItemView::item:hover {\n"
"    background-color: #fff;\n"
"}\n"
"\n"
""
                        "\n"
"")

        self.horizontalLayout_14.addWidget(self.preferred_output)


        self.verticalLayout_9.addWidget(self.frame_17)

        self.frame_19 = QFrame(self.frame_3)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setMaximumSize(QSize(16777215, 80))
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(-1, 20, -1, 0)
        self.frame_20 = QFrame(self.frame_19)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setMaximumSize(QSize(16777215, 50))
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_13.addWidget(self.frame_20)

        self.button_save = QPushButton(self.frame_19)
        self.button_save.setObjectName(u"button_save")
        self.button_save.setMinimumSize(QSize(100, 32))
        self.button_save.setMaximumSize(QSize(120, 16777215))
        font10 = QFont()
        font10.setFamily(u"Roboto Medium")
        font10.setPointSize(9)
        self.button_save.setFont(font10)
        self.button_save.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_save.setFocusPolicy(Qt.NoFocus)
        self.button_save.setStyleSheet(u"QPushButton{\n"
"	color:  rgb(180, 180, 180);\n"
"	border: 2px solid #5a9bd5;\n"
"	border-radius : 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(56, 63, 77);\n"
"	border: 2px solid rgb(170, 0, 255);\n"
"}")

        self.horizontalLayout_13.addWidget(self.button_save)


        self.verticalLayout_9.addWidget(self.frame_19)

        self.frame_18 = QFrame(self.frame_3)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)

        self.verticalLayout_9.addWidget(self.frame_18)


        self.horizontalLayout_9.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.preference_page)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(350, 16777215))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_9.addWidget(self.frame_4)

        self.setting_pages.addWidget(self.preference_page)
        self.account_page = QWidget()
        self.account_page.setObjectName(u"account_page")
        self.horizontalLayout_19 = QHBoxLayout(self.account_page)
        self.horizontalLayout_19.setSpacing(0)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.frame_27 = QFrame(self.account_page)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setMaximumSize(QSize(350, 16777215))
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_19.addWidget(self.frame_27)

        self.frame_28 = QFrame(self.account_page)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setMinimumSize(QSize(700, 0))
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_28)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 20, 0, 0)
        self.frame_29 = QFrame(self.frame_28)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setMaximumSize(QSize(16777215, 70))
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_29)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(-1, -1, 20, -1)
        self.account_label = QLabel(self.frame_29)
        self.account_label.setObjectName(u"account_label")
        self.account_label.setFont(font9)
        self.account_label.setStyleSheet(u"color:rgb(180, 180, 180);\n"
"background:transparent;")

        self.horizontalLayout_20.addWidget(self.account_label)

        self.logged_in_label = QLabel(self.frame_29)
        self.logged_in_label.setObjectName(u"logged_in_label")
        self.logged_in_label.setFont(font5)
        self.logged_in_label.setStyleSheet(u"color: rgba(255, 0, 0, 200);")
        self.logged_in_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_20.addWidget(self.logged_in_label)


        self.verticalLayout_12.addWidget(self.frame_29)

        self.frame_30 = QFrame(self.frame_28)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_30)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.frame_32 = QFrame(self.frame_30)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setMaximumSize(QSize(16777215, 100))
        self.frame_32.setStyleSheet(u"#frame_32{\n"
"	background-color: rgb(52, 58, 71);\n"
"	border-radius:0px;\n"
"	border-top-left-radius:10px;\n"
"	border-top-right-radius:10px;\n"
"	border-bottom-left-radius:10px;\n"
"	border-bottom-right-radius:10px;\n"
"}")
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_32)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.username_label = QLabel(self.frame_32)
        self.username_label.setObjectName(u"username_label")
        self.username_label.setFont(font5)
        self.username_label.setStyleSheet(u"color:rgb(180, 180, 180);\n"
"background:transparent;")

        self.verticalLayout_14.addWidget(self.username_label)

        self.email_label = QLabel(self.frame_32)
        self.email_label.setObjectName(u"email_label")
        self.email_label.setFont(font5)
        self.email_label.setStyleSheet(u"color:rgb(180, 180, 180);\n"
"background:transparent;")

        self.verticalLayout_14.addWidget(self.email_label)


        self.verticalLayout_13.addWidget(self.frame_32)

        self.frame_33 = QFrame(self.frame_30)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setMaximumSize(QSize(16777215, 50))
        self.frame_33.setFrameShape(QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_33)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(-1, -1, 30, -1)
        self.frame_34 = QFrame(self.frame_33)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_21.addWidget(self.frame_34)

        self.button_logout = QPushButton(self.frame_33)
        self.button_logout.setObjectName(u"button_logout")
        self.button_logout.setMinimumSize(QSize(100, 32))
        self.button_logout.setMaximumSize(QSize(120, 16777215))
        self.button_logout.setFont(font10)
        self.button_logout.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_logout.setFocusPolicy(Qt.NoFocus)
        self.button_logout.setStyleSheet(u"QPushButton{\n"
"	color:  rgb(180, 180, 180);\n"
"	border: 1px solid #5a9bd5;\n"
"	border-radius : 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(56, 63, 77);\n"
"	border: 2px solid rgb(170, 0, 255);\n"
"}")

        self.horizontalLayout_21.addWidget(self.button_logout)


        self.verticalLayout_13.addWidget(self.frame_33)

        self.frame_31 = QFrame(self.frame_30)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)

        self.verticalLayout_13.addWidget(self.frame_31)


        self.verticalLayout_12.addWidget(self.frame_30)


        self.horizontalLayout_19.addWidget(self.frame_28)

        self.frame_26 = QFrame(self.account_page)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setMaximumSize(QSize(350, 16777215))
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_19.addWidget(self.frame_26)

        self.setting_pages.addWidget(self.account_page)
        self.about_page = QWidget()
        self.about_page.setObjectName(u"about_page")
        self.horizontalLayout_29 = QHBoxLayout(self.about_page)
        self.horizontalLayout_29.setSpacing(0)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.frame_35 = QFrame(self.about_page)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setFrameShape(QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_32 = QHBoxLayout(self.frame_35)
        self.horizontalLayout_32.setSpacing(0)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.horizontalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.frame_36 = QFrame(self.frame_35)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setFrameShape(QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_32.addWidget(self.frame_36)

        self.frame_38 = QFrame(self.frame_35)
        self.frame_38.setObjectName(u"frame_38")
        self.frame_38.setMinimumSize(QSize(700, 0))
        self.frame_38.setFrameShape(QFrame.StyledPanel)
        self.frame_38.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_38)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 20, 0, 0)
        self.frame_39 = QFrame(self.frame_38)
        self.frame_39.setObjectName(u"frame_39")
        self.frame_39.setMaximumSize(QSize(16777215, 70))
        self.frame_39.setFrameShape(QFrame.StyledPanel)
        self.frame_39.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_30 = QHBoxLayout(self.frame_39)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalLayout_30.setContentsMargins(-1, -1, 20, -1)
        self.account_label_2 = QLabel(self.frame_39)
        self.account_label_2.setObjectName(u"account_label_2")
        self.account_label_2.setFont(font9)
        self.account_label_2.setStyleSheet(u"color:rgb(180, 180, 180);\n"
"background:transparent;")

        self.horizontalLayout_30.addWidget(self.account_label_2)


        self.verticalLayout_15.addWidget(self.frame_39)

        self.frame_40 = QFrame(self.frame_38)
        self.frame_40.setObjectName(u"frame_40")
        self.frame_40.setFrameShape(QFrame.StyledPanel)
        self.frame_40.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_40)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.frame_41 = QFrame(self.frame_40)
        self.frame_41.setObjectName(u"frame_41")
        self.frame_41.setMaximumSize(QSize(16777215, 100))
        self.frame_41.setStyleSheet(u"#frame_41{\n"
"	background-color: rgb(52, 58, 71);\n"
"	border-radius:0px;\n"
"	border-top-left-radius:10px;\n"
"	border-top-right-radius:10px;\n"
"	border-bottom-left-radius:10px;\n"
"	border-bottom-right-radius:10px;\n"
"}")
        self.frame_41.setFrameShape(QFrame.StyledPanel)
        self.frame_41.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_41)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.label_11 = QLabel(self.frame_41)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font5)
        self.label_11.setStyleSheet(u"color:rgb(180, 180, 180);\n"
"background:transparent;")

        self.verticalLayout_17.addWidget(self.label_11)

        self.label_12 = QLabel(self.frame_41)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font5)
        self.label_12.setStyleSheet(u"color:rgb(180, 180, 180);\n"
"background:transparent;")

        self.verticalLayout_17.addWidget(self.label_12)


        self.verticalLayout_16.addWidget(self.frame_41)

        self.frame_42 = QFrame(self.frame_40)
        self.frame_42.setObjectName(u"frame_42")
        self.frame_42.setMaximumSize(QSize(16777215, 50))
        self.frame_42.setFrameShape(QFrame.StyledPanel)
        self.frame_42.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_31 = QHBoxLayout(self.frame_42)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.horizontalLayout_31.setContentsMargins(-1, -1, 40, -1)
        self.frame_43 = QFrame(self.frame_42)
        self.frame_43.setObjectName(u"frame_43")
        self.frame_43.setFrameShape(QFrame.StyledPanel)
        self.frame_43.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_31.addWidget(self.frame_43)

        self.button_check_update = QPushButton(self.frame_42)
        self.button_check_update.setObjectName(u"button_check_update")
        self.button_check_update.setMinimumSize(QSize(100, 32))
        self.button_check_update.setMaximumSize(QSize(150, 16777215))
        self.button_check_update.setFont(font10)
        self.button_check_update.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_check_update.setFocusPolicy(Qt.NoFocus)
        self.button_check_update.setStyleSheet(u"QPushButton{\n"
"	color:  rgb(180, 180, 180);\n"
"	border: 1px solid #5a9bd5;\n"
"	border-radius : 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(56, 63, 77);\n"
"	border: 2px solid rgb(170, 0, 255);\n"
"}")

        self.horizontalLayout_31.addWidget(self.button_check_update)


        self.verticalLayout_16.addWidget(self.frame_42)

        self.frame_44 = QFrame(self.frame_40)
        self.frame_44.setObjectName(u"frame_44")
        self.frame_44.setFrameShape(QFrame.StyledPanel)
        self.frame_44.setFrameShadow(QFrame.Raised)

        self.verticalLayout_16.addWidget(self.frame_44)


        self.verticalLayout_15.addWidget(self.frame_40)


        self.horizontalLayout_32.addWidget(self.frame_38)

        self.frame_37 = QFrame(self.frame_35)
        self.frame_37.setObjectName(u"frame_37")
        self.frame_37.setFrameShape(QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_32.addWidget(self.frame_37)


        self.horizontalLayout_29.addWidget(self.frame_35)

        self.setting_pages.addWidget(self.about_page)

        self.verticalLayout_8.addWidget(self.setting_pages)


        self.horizontalLayout_22.addWidget(self.frame_50)


        self.verticalLayout_4.addWidget(self.frame_48)

        self.stackedWidget.addWidget(self.settings_page)
        self.conversation_page = QWidget()
        self.conversation_page.setObjectName(u"conversation_page")
        self.verticalLayout_7 = QVBoxLayout(self.conversation_page)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.conversation_page)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_33 = QHBoxLayout(self.frame)
        self.horizontalLayout_33.setSpacing(0)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.horizontalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.frame_46 = QFrame(self.frame)
        self.frame_46.setObjectName(u"frame_46")
        self.frame_46.setMinimumSize(QSize(280, 0))
        self.frame_46.setMaximumSize(QSize(400, 16777215))
        self.frame_46.setFrameShape(QFrame.StyledPanel)
        self.frame_46.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_33.addWidget(self.frame_46)

        self.frame_45 = QFrame(self.frame)
        self.frame_45.setObjectName(u"frame_45")
        self.frame_45.setMinimumSize(QSize(700, 0))
        self.frame_45.setMaximumSize(QSize(1100, 16777215))
        self.frame_45.setFrameShape(QFrame.StyledPanel)
        self.frame_45.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_45)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.frame_58 = QFrame(self.frame_45)
        self.frame_58.setObjectName(u"frame_58")
        self.frame_58.setMaximumSize(QSize(16777215, 16777215))
        self.frame_58.setStyleSheet(u"background-color: rgb(50, 56, 68);")
        self.frame_58.setFrameShape(QFrame.StyledPanel)
        self.frame_58.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.frame_58)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.chat_layout = QVBoxLayout()
        self.chat_layout.setObjectName(u"chat_layout")

        self.verticalLayout_20.addLayout(self.chat_layout)


        self.verticalLayout_18.addWidget(self.frame_58)

        self.frame_2 = QFrame(self.frame_45)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 150))
        self.frame_2.setMaximumSize(QSize(16777215, 150))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_34 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_34.setSpacing(0)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.horizontalLayout_34.setContentsMargins(0, 0, 0, 0)
        self.frame_59 = QFrame(self.frame_2)
        self.frame_59.setObjectName(u"frame_59")
        self.frame_59.setFrameShape(QFrame.StyledPanel)
        self.frame_59.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_34.addWidget(self.frame_59)

        self.frame_60 = QFrame(self.frame_2)
        self.frame_60.setObjectName(u"frame_60")
        self.frame_60.setMinimumSize(QSize(700, 0))
        self.frame_60.setFrameShape(QFrame.StyledPanel)
        self.frame_60.setFrameShadow(QFrame.Raised)
        self.addButton_2 = StickyButton(self.frame_60)
        self.addButton_2.setObjectName(u"addButton_2")
        self.addButton_2.setGeometry(QRect(10, 50, 51, 45))
        self.addButton_2.setMinimumSize(QSize(0, 45))
        self.addButton_2.setMaximumSize(QSize(160, 16777215))
        self.addButton_2.setFont(font4)
        self.addButton_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.addButton_2.setStyleSheet(u"QPushButton{\n"
"	background:none;\n"
"	border:none;\n"
"	color:rgba(255, 255, 255, 180);\n"
"	border-radius: 21px ;\n"
"	margin-top:3px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(45, 48, 58);\n"
"}")
        self.addButton_2.setIcon(icon9)
        self.addButton_2.setIconSize(QSize(22, 22))
        self.text_prompt_2 = AutoGrowTextEdit(self.frame_60)
        self.text_prompt_2.setObjectName(u"text_prompt_2")
        self.text_prompt_2.setEnabled(True)
        self.text_prompt_2.setGeometry(QRect(10, 50, 681, 50))
        sizePolicy1.setHeightForWidth(self.text_prompt_2.sizePolicy().hasHeightForWidth())
        self.text_prompt_2.setSizePolicy(sizePolicy1)
        self.text_prompt_2.setMinimumSize(QSize(0, 50))
        self.text_prompt_2.setMaximumSize(QSize(16777215, 50))
        self.text_prompt_2.setSizeIncrement(QSize(0, 0))
        self.text_prompt_2.setBaseSize(QSize(0, 0))
        self.text_prompt_2.setFont(font5)
        self.text_prompt_2.setStyleSheet(u"QTextEdit{\n"
" 	border:2px solid rgb(41, 44, 53);\n"
"    border-radius:22px;\n"
"	background-color: rgb(41, 44, 53);\n"
"    color:rgba(255, 	255, 255, 210);\n"
"    padding-left:20px;\n"
"	padding-top:10px;\n"
"	padding-right:15px;\n"
"	padding-bottom:45px;\n"
"}\n"
"\n"
"QTextEdit:hover{\n"
"	border:2px solid rgb(220, 0, 220);\n"
"}\n"
"\n"
"QTextEdit:focus{\n"
"	border:2px solid rgb(85,170,255);\n"
"}")
        self.text_prompt_2.setFrameShape(QFrame.StyledPanel)
        self.text_prompt_2.setFrameShadow(QFrame.Plain)
        self.text_prompt_2.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.searchButton_2 = StickyButton(self.frame_60)
        self.searchButton_2.setObjectName(u"searchButton_2")
        self.searchButton_2.setGeometry(QRect(640, 50, 45, 45))
        sizePolicy.setHeightForWidth(self.searchButton_2.sizePolicy().hasHeightForWidth())
        self.searchButton_2.setSizePolicy(sizePolicy)
        self.searchButton_2.setMinimumSize(QSize(45, 45))
        self.searchButton_2.setMaximumSize(QSize(45, 45))
        self.searchButton_2.setFont(font4)
        self.searchButton_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.searchButton_2.setStyleSheet(u"QPushButton{\n"
"	background:none;\n"
"	border:none;\n"
"	color:rgba(255, 255, 255, 180);\n"
"	background-color: rgb(41, 44, 53);\n"
"	border-radius: 21px ;\n"
"	margin-top:3px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(45, 48, 58);\n"
"}")
        self.searchButton_2.setIcon(icon8)
        self.searchButton_2.setIconSize(QSize(27, 27))
        self.text_prompt_2.raise_()
        self.addButton_2.raise_()
        self.searchButton_2.raise_()

        self.horizontalLayout_34.addWidget(self.frame_60)

        self.frame_61 = QFrame(self.frame_2)
        self.frame_61.setObjectName(u"frame_61")
        self.frame_61.setFrameShape(QFrame.StyledPanel)
        self.frame_61.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_34.addWidget(self.frame_61)


        self.verticalLayout_18.addWidget(self.frame_2)


        self.horizontalLayout_33.addWidget(self.frame_45)

        self.frame_47 = QFrame(self.frame)
        self.frame_47.setObjectName(u"frame_47")
        self.frame_47.setMinimumSize(QSize(280, 0))
        self.frame_47.setMaximumSize(QSize(400, 16777215))
        self.frame_47.setFrameShape(QFrame.StyledPanel)
        self.frame_47.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_33.addWidget(self.frame_47)


        self.verticalLayout_7.addWidget(self.frame)

        self.stackedWidget.addWidget(self.conversation_page)

        self.horizontalLayout_6.addWidget(self.stackedWidget)


        self.horizontalLayout_4.addWidget(self.content_page_frame)


        self.verticalLayout_2.addWidget(self.Content)


        self.verticalLayout.addWidget(self.drop_shadow_frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.toggle_button.setText("")
        self.icon.setText("")
        self.status_bar.setText(QCoreApplication.translate("MainWindow", u"  AI Personalized Learning App", None))
        self.button_minimize.setText("")
        self.button_restore.setText("")
        self.button_close.setText("")
        self.button_new_chat.setText(QCoreApplication.translate("MainWindow", u"     New Chat           ", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Recent chats", None))
        self.button_settings.setText(QCoreApplication.translate("MainWindow", u"      Settings        ", None))
        self.label.setText("")
        self.labelProtection.setText(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Roboto'; font-size:30pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'ui-sans-serif','-apple-system','system-ui','Segoe UI','Helvetica','Apple Color Emoji','Arial','sans-serif','Segoe UI Emoji','Segoe UI Symbol'; font-size:24pt;\">What can I help with?</span></p></body></html>", None))
        self.searchButton.setText("")
        self.addButton.setText("")
        self.text_prompt.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Roboto'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'MS Shell Dlg 2'; font-size:7.8pt;\"><br /></p></body></html>", None))
        self.text_prompt.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ask Anything", None))
#if QT_CONFIG(tooltip)
        self.login_button.setToolTip(QCoreApplication.translate("MainWindow", u"Not logged in!", None))
#endif // QT_CONFIG(tooltip)
        self.login_button.setText(QCoreApplication.translate("MainWindow", u"Log In", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.acc_button.setText(QCoreApplication.translate("MainWindow", u"Account", None))
        self.buttonUI.setText(QCoreApplication.translate("MainWindow", u"User Interface", None))
        self.buttonNotification.setText(QCoreApplication.translate("MainWindow", u"Notifications", None))
        self.buttonUpdate.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.button_preferences.setText(QCoreApplication.translate("MainWindow", u"Preferences", None))
        self.buttonAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Preferences", None))
#if QT_CONFIG(whatsthis)
        self.label_3.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<span style=\"font-size:18px;\">Learning style</span><br>\n"
"<span style=\"font-size:16px;color:rgb(150, 150, 150)\">Choose your learning style as visual/text/quiz</span><br>\n"
"", None))
        self.learning_type.setItemText(0, QCoreApplication.translate("MainWindow", u"Text", None))
        self.learning_type.setItemText(1, QCoreApplication.translate("MainWindow", u"Visual", None))
        self.learning_type.setItemText(2, QCoreApplication.translate("MainWindow", u"Quiz", None))

        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<span style=\"font-size:18px;\">Diffiulty</span><br>\n"
"<span style=\"font-size:16px;color:rgb(150, 150, 150)\">Select your difficulty level as easy/medium/high</span><br>\n"
"", None))
        self.difficulty_type.setItemText(0, QCoreApplication.translate("MainWindow", u"Easy", None))
        self.difficulty_type.setItemText(1, QCoreApplication.translate("MainWindow", u"Medium", None))
        self.difficulty_type.setItemText(2, QCoreApplication.translate("MainWindow", u"Hard", None))

        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<span style=\"font-size:18px;\">Daily goal H:M</span><br>\n"
"<span style=\"font-size:16px;color:rgb(150, 150, 150)\">Set your daily goal example 1 hour, 30 min etc</span><br>\n"
"", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<span style=\"font-size:18px;\">Preferred output</span><br>\n"
"<span style=\"font-size:16px;color:rgb(150, 150, 150)\">Set your preffered output as summary, MCQs or flashcards</span><br>\n"
"", None))
        self.preferred_output.setItemText(0, QCoreApplication.translate("MainWindow", u"Search", None))
        self.preferred_output.setItemText(1, QCoreApplication.translate("MainWindow", u"Summary", None))
        self.preferred_output.setItemText(2, QCoreApplication.translate("MainWindow", u"MCQs", None))
        self.preferred_output.setItemText(3, QCoreApplication.translate("MainWindow", u"Flashcard", None))

        self.button_save.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.account_label.setText(QCoreApplication.translate("MainWindow", u"Account", None))
        self.logged_in_label.setText(QCoreApplication.translate("MainWindow", u" Not Logged In", None))
#if QT_CONFIG(whatsthis)
        self.username_label.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.username_label.setText(QCoreApplication.translate("MainWindow", u"Username: ", None))
        self.email_label.setText(QCoreApplication.translate("MainWindow", u"Email: ", None))
        self.button_logout.setText(QCoreApplication.translate("MainWindow", u"Log In", None))
        self.account_label_2.setText(QCoreApplication.translate("MainWindow", u"About", None))
#if QT_CONFIG(whatsthis)
        self.label_11.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"AI Personalized Learning App", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"version: 1.0", None))
        self.button_check_update.setText(QCoreApplication.translate("MainWindow", u"Check for Update", None))
        self.addButton_2.setText("")
        self.text_prompt_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Roboto'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'MS Shell Dlg 2'; font-size:7.8pt;\"><br /></p></body></html>", None))
        self.text_prompt_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ask Anything", None))
        self.searchButton_2.setText("")
    # retranslateUi

