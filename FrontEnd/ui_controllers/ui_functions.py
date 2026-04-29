from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QGraphicsDropShadowEffect
from PyQt5.QtCore import QPropertyAnimation
from termcolor import colored

GLOBAL_STATE = 0
SIDEBAR_EXPANDED = True   # track sidebar state


class UIFunctions:
    def __init__(self, window):
        self.window = window

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
            ui.button_new_chat.setText("")
            ui.button_settings.setText("")

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

    def setDefaultPage(self):
        self.window.ui.stackedWidget_2.setCurrentWidget(self.window.ui.defaultPage)

    def setNewChatPage(self):
        self.window.ui.stackedWidget.setCurrentWidget(self.window.ui.new_chat_page)

    def setSettingsPage(self):
        self.window.ui.stackedWidget.setCurrentWidget(self.window.ui.settings_page)
        self.window.ui.setting_pages.setCurrentWidget(self.window.ui.account_page)

    def setAboutPage(self):
        self.window.ui.setting_pages.setCurrentWidget(self.window.ui.about_page)

    def setAccountPage(self):
        self.window.ui.setting_pages.setCurrentWidget(self.window.ui.account_page)

    def setPreferencesPage(self):
        self.window.ui.setting_pages.setCurrentWidget(self.window.ui.preference_page)

    def close_win(self):
        print(colored('Exiting ...', 'red'))
        self.window.close()
        
        
        
        
        
        
        