from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QGraphicsDropShadowEffect
from PyQt5.QtCore import QPropertyAnimation
from termcolor import colored

GLOBAL_STATE = 0
SIDEBAR_EXPANDED = True   # track sidebar state


class UIFunctions:
    def __init__(self, window):
        self.window = window
        self.prev_button = None

    def maximize_restore(self):
        global GLOBAL_STATE
        status = GLOBAL_STATE
        if status == 0:
            self.window.ui.verticalLayout.setContentsMargins(0, 0, 0, 0)
            self.window.ui.verticalLayout.setSpacing(0)
            self.window.showMaximized()
            GLOBAL_STATE = 1
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("Reqs/restore-down.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.window.ui.button_restore.setIcon(icon)
            self.window.ui.button_restore.setToolTip("Restore")
        else:
            GLOBAL_STATE = 0
            self.window.ui.verticalLayout.setContentsMargins(11, 11, 11, 11)
            self.window.showNormal()
            self.window.resize(self.window.width() + 1, self.window.height() + 1)
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("Reqs/maximize.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.window.ui.button_restore.setIcon(icon)
            self.window.ui.button_restore.setToolTip("Maximize")

    def returnStatus(self):
        return GLOBAL_STATE

    def toggle(self, maxWidth, enable):
        global SIDEBAR_EXPANDED
        if not enable:
            return

        width = self.window.ui.toggle_frame_left.width()
        standard = 85

        if width == standard:
            # ── Expanding ──
            widthExtended = maxWidth
            SIDEBAR_EXPANDED = True
        else:
            # ── Collapsing ──
            widthExtended = standard
            SIDEBAR_EXPANDED = False
            # Hide text widgets immediately when collapsing
            self._set_sidebar_text_visible(False)

        self.window.animation = QPropertyAnimation(
            self.window.ui.toggle_frame_left, b"minimumWidth"
        )
        self.window.animation.setDuration(160)
        self.window.animation.setStartValue(width)
        self.window.animation.setEndValue(widthExtended)
        self.window.animation.start()

        # Show text widgets only after animation finishes (expanding)
        if SIDEBAR_EXPANDED:
            self.window.animation.finished.connect(
                lambda: self._set_sidebar_text_visible(True)
            )

    def _set_sidebar_text_visible(self, visible):
        """Show or hide the text-heavy sidebar widgets."""
        ui = self.window.ui

        # "Recent chats" label
        ui.label_7.setVisible(visible)

        # The chat history list
        ui.chat_history.setVisible(visible)

        # Button text (keep icon, just toggle the label part)
        if visible:
            ui.button_new_chat.setText("     New Chat           ")
            ui.button_settings.setText("      Settings        ")
        else:
            ui.button_new_chat.setText("                              ")
            ui.button_settings.setText("                          ")

    def uiDefinitions(self):
        self.window.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.window.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.window.ui.verticalLayout.setContentsMargins(11, 11, 11, 11)

        self.window.shadow = QGraphicsDropShadowEffect(self.window)
        self.window.shadow.setBlurRadius(40)
        self.window.shadow.setXOffset(0)
        self.window.shadow.setYOffset(0)
        self.window.shadow.setColor(QtGui.QColor(0, 0, 0, 255))
        self.window.ui.drop_shadow_frame.setGraphicsEffect(self.window.shadow)

        self.window.ui.button_minimize.clicked.connect(
            lambda: self.window.showMinimized())
        self.window.ui.button_restore.clicked.connect(
            lambda: self.maximize_restore())
        self.window.ui.button_close.clicked.connect(
            lambda: self.close_win())
        
    def update_button_ui(self, button):
        if self.prev_button:
            self.prev_button.setStyleSheet("""
                            QPushButton{
                                border-radius:5px;
                                color:rgb(180, 180, 180);
                                text-align:left;
                                padding-left:40px;
                            }
                            QPushButton:hover{
                                background-color:rgb(59, 66, 81);
                                border:2px solid rgb(212, 58, 212);
                                border-radius:5px;
                            }
                                """)
        
        self.prev_button = button
        button.setStyleSheet("""
                    QPushButton{
                        border-radius:5px;
                        color:rgb(200, 200, 200);
                        background-color: rgba(0, 151, 227, 240);
                        text-align:left;
                        padding-left:40px;
                        border-radius:5px;
                    }
                    QPushButton:hover{
                        background-color: rgba(0, 151, 227, 190);
                    }
                             """)

    def setDefaultPage(self):
        self.window.ui.stackedWidget_2.setCurrentWidget(self.window.ui.defaultPage)

    def setNewChatPage(self):
        from services.handle_requests import clear_document
        clear_document(self.window)
        self.window.ui.stackedWidget.setCurrentWidget(self.window.ui.new_chat_page)

    def setSettingsPage(self):
        self.update_button_ui(self.window.ui.acc_button)
        self.window.ui.stackedWidget.setCurrentWidget(self.window.ui.settings_page)
        self.window.ui.setting_pages.setCurrentWidget(self.window.ui.account_page)

    def setAboutPage(self):
        self.update_button_ui(self.window.ui.buttonAbout)
        self.window.ui.setting_pages.setCurrentWidget(self.window.ui.about_page)

    def setAccountPage(self):
        self.update_button_ui(self.window.ui.acc_button)
        self.window.ui.setting_pages.setCurrentWidget(self.window.ui.account_page)
        
    def setUserInterfacePage(self):
        self.update_button_ui(self.window.ui.buttonUI)
        self.window.ui.setting_pages.setCurrentWidget(self.window.ui.user_interface_page)
        
    def setNotificationPage(self):
        self.update_button_ui(self.window.ui.buttonNotification)
        self.window.ui.setting_pages.setCurrentWidget(self.window.ui.notification_page)

    def setPreferencesPage(self):
        self.update_button_ui(self.window.ui.button_preferences)
        self.window.ui.setting_pages.setCurrentWidget(self.window.ui.preference_page)

    def setUpdatePage(self):
        self.update_button_ui(self.window.ui.buttonUpdate)
        self.window.ui.setting_pages.setCurrentWidget(self.window.ui.update_page)

    def close_win(self):
        print(colored('Exiting ...', 'red'))
        self.window.close()
        
    def load_icons(self):        
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./Reqs/menu-50 copy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.window.ui.toggle_button.setIcon(icon)
        self.window.ui.toggle_button.setIconSize(QtCore.QSize(25, 25))
        
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("./Reqs/new_chat.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.window.ui.button_new_chat.setIcon(icon5)
        self.window.ui.button_new_chat.setIconSize(QtCore.QSize(35, 35))
        
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("./Reqs/settings-50 copy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.window.ui.button_settings.setIcon(icon6)
        self.window.ui.button_settings.setIconSize(QtCore.QSize(35, 35))
        
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("./Reqs/user.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.window.ui.login_button.setIcon(icon9)
        self.window.ui.login_button.setIconSize(QtCore.QSize(20, 20))
        
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("./Reqs/add_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.window.ui.addButton.setIcon(icon8)
        self.window.ui.addButton_2.setIcon(icon8)
        self.window.ui.addButton.setIconSize(QtCore.QSize(22, 22))
        
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("./Reqs/search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.window.ui.searchButton.setIcon(icon7)
        self.window.ui.searchButton_2.setIcon(icon7)
        self.window.ui.searchButton.setIconSize(QtCore.QSize(27, 27))
        
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("./Reqs/user2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.window.ui.acc_button.setIcon(icon10)
        self.window.ui.acc_button.setIconSize(QtCore.QSize(25, 25))
        
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("./Reqs/ui_.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.window.ui.buttonUI.setIcon(icon11)
        self.window.ui.buttonUI.setIconSize(QtCore.QSize(25, 25))
        
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap("./Reqs/notification_.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.window.ui.buttonNotification.setIcon(icon12)
        self.window.ui.buttonNotification.setIconSize(QtCore.QSize(30, 30))
        
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap("./Reqs/update_.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.window.ui.buttonUpdate.setIcon(icon13)
        self.window.ui.buttonUpdate.setIconSize(QtCore.QSize(25, 25))
        
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap("./Reqs/preferences.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.window.ui.button_preferences.setIcon(icon14)
        self.window.ui.button_preferences.setIconSize(QtCore.QSize(25, 25))
        
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap("./Reqs/about_.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.window.ui.buttonAbout.setIcon(icon15)
        self.window.ui.buttonAbout.setIconSize(QtCore.QSize(25, 25))
        
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap("./Reqs/arrow-right.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.window.ui.btn_change_pass.setIcon(icon16)
        self.window.ui.buttonAbout.setIconSize(QtCore.QSize(25, 25))
        
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap("./Reqs/arrow-right-off.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.window.ui.btn_2FA.setIcon(icon17)
        self.window.ui.buttonAbout.setIconSize(QtCore.QSize(25, 25))
        
        icon18 = QtGui.QIcon()
        icon18.addPixmap(QtGui.QPixmap("./Reqs/system-default.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.window.ui.btn_system_theme.setIcon(icon18)
        self.window.ui.btn_system_theme.setIconSize(QtCore.QSize(50, 50))
        
        icon19 = QtGui.QIcon()
        icon19.addPixmap(QtGui.QPixmap("./Reqs/light-theme.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.window.ui.btn_light_theme.setIcon(icon19)
        self.window.ui.btn_light_theme.setIconSize(QtCore.QSize(50, 50))
        
        icon26 = QtGui.QIcon()
        icon26.addPixmap(QtGui.QPixmap("./Reqs/dark-theme.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.window.ui.btn_dark_theme.setIcon(icon26)
        self.window.ui.btn_dark_theme.setIconSize(QtCore.QSize(50, 50))
        
        icon20 = QtGui.QIcon()
        icon20.addPixmap(QtGui.QPixmap("./Reqs/solid-blue.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.window.ui.accent_color_1.setIcon(icon20)
        self.window.ui.accent_color_1.setIconSize(QtCore.QSize(60, 60))
        
        icon21 = QtGui.QIcon()
        icon21.addPixmap(QtGui.QPixmap("./Reqs/solid-green.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.window.ui.accent_color_2.setIcon(icon21)
        self.window.ui.accent_color_2.setIconSize(QtCore.QSize(60, 60))
        
        icon22 = QtGui.QIcon()
        icon22.addPixmap(QtGui.QPixmap("./Reqs/solid-purple.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.window.ui.accent_color_3.setIcon(icon22)
        self.window.ui.accent_color_3.setIconSize(QtCore.QSize(60, 60))
        
        icon23 = QtGui.QIcon()
        icon23.addPixmap(QtGui.QPixmap("./Reqs/solid-orange.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.window.ui.accent_color_4.setIcon(icon23)
        self.window.ui.accent_color_4.setIconSize(QtCore.QSize(60, 60))
        
        icon24 = QtGui.QIcon()
        icon24.addPixmap(QtGui.QPixmap("./Reqs/solid-magenta.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.window.ui.accent_color_5.setIcon(icon24)
        self.window.ui.accent_color_5.setIconSize(QtCore.QSize(60, 60))
        
        icon25 = QtGui.QIcon()
        icon25.addPixmap(QtGui.QPixmap("./Reqs/solid-dark-blue.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.window.ui.accent_color_6.setIcon(icon25)
        self.window.ui.accent_color_6.setIconSize(QtCore.QSize(60, 60))
        
        icon26 = QtGui.QIcon()
        icon26.addPixmap(QtGui.QPixmap("./Reqs/App_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.window.ui.app_icon.setIcon(icon26)
        self.window.ui.app_icon.setIconSize(QtCore.QSize(120, 120))
        
        icon27 = QtGui.QIcon()
        icon27.addPixmap(QtGui.QPixmap("./Reqs/link.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.window.ui.link_website.setIcon(icon27)
        self.window.ui.link_website.setIconSize(QtCore.QSize(30, 30))
        
        icon28 = QtGui.QIcon()
        icon28.addPixmap(QtGui.QPixmap("./Reqs/link.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.window.ui.link_support.setIcon(icon28)
        self.window.ui.link_support.setIconSize(QtCore.QSize(30, 30))
        
        icon29 = QtGui.QIcon()
        icon29.addPixmap(QtGui.QPixmap("./Reqs/link.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.window.ui.link_privacy_policy.setIcon(icon29)
        self.window.ui.link_privacy_policy.setIconSize(QtCore.QSize(30, 30))
        
        icon30 = QtGui.QIcon()
        icon30.addPixmap(QtGui.QPixmap("./Reqs/link.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.window.ui.link_terms_services.setIcon(icon30)
        self.window.ui.link_terms_services.setIconSize(QtCore.QSize(30, 30))
        
        icon31 = QtGui.QIcon()
        icon31.addPixmap(QtGui.QPixmap("./Reqs/link.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.window.ui.link_open_source.setIcon(icon31)
        self.window.ui.link_open_source.setIconSize(QtCore.QSize(30, 30))
        
        icon32 = QtGui.QIcon()
        icon32.addPixmap(QtGui.QPixmap("./Reqs/GitHub.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.window.ui.btn_gitHub.setIcon(icon32)
        self.window.ui.btn_gitHub.setIconSize(QtCore.QSize(30, 30))
        
        icon33 = QtGui.QIcon()
        icon33.addPixmap(QtGui.QPixmap("./Reqs/LinkedIn.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.window.ui.btn_linkedIn.setIcon(icon33)
        self.window.ui.btn_linkedIn.setIconSize(QtCore.QSize(30, 30))
        
        
        
        
        
        
        
        
        