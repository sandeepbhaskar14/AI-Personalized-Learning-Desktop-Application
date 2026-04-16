from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QGraphicsDropShadowEffect
from PyQt5.QtCore import QPropertyAnimation
from termcolor import colored

## ==>> GLOBALS
GLOBAL_STATE = 0


class UIFunctions:
    def __init__(self, window):
        self.window = window
        
    # ==>> Maximize Restore Function
    def maximize_restore(self) :
        global GLOBAL_STATE
        status = GLOBAL_STATE

        # IF NOT MAXIMIZED
        if status == 0 :
            #self.window.showNormal()
            self.window.ui.verticalLayout.setContentsMargins(0, 0, 0, 0)
            self.window.ui.verticalLayout.setSpacing(0)
            self.window.showMaximized()
            
            # self.window.ui.frame_43.setMinimumSize(QtCore.QSize(540, 0))

            # SET GLOBAL TO 1
            GLOBAL_STATE = 1

            # SET ICON TO RESTORE
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("Reqs/restore-down.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.window.ui.button_restore.setIcon(icon)
            self.window.ui.button_restore.setToolTip("Restore")

        else :
            GLOBAL_STATE = 0
            self.window.ui.verticalLayout.setContentsMargins(11, 11, 11, 11)
            self.window.showNormal()
            self.window.resize(self.window.width() +1, self.window.height()+1 )

            # SET ICON TO RESTORE
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("Reqs/maximize.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.window.ui.button_restore.setIcon(icon)
            self.window.ui.button_restore.setToolTip("Maximize")
    
    
    def returnStatus(self) :
        return GLOBAL_STATE


    # ==>>TOGGLE BUTTON
    def toggle(self, maxWidth, enable) :
        if enable :

            # GET WIDTH
            width = self.window.ui.toggle_frame_left.width()
            maxExtend = maxWidth
            standard = 85

            # SET MAX WIDTH
            if width == 85:
                widthExtended = maxExtend
            else :
                widthExtended = standard

            # ANIMATION
            self.window.animation = QPropertyAnimation(self.window.ui.toggle_frame_left, b"minimumWidth")
            self.window.animation.setDuration(160)
            self.window.animation.setStartValue(width)
            self.window.animation.setEndValue(widthExtended)
            #self.window.animation.setStartValue(QRect(-200, 0, 200, 600))
            #self.window.animation.setEndValue(QRect(0, 0, 200, 600))
            self.window.animation.start()
            
    
    # UI FUNCTIONS
    def uiDefinitions(self) :

        # ==>> REMOVE TITLE BAR
        self.window.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.window.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        
        self.window.ui.verticalLayout.setContentsMargins(11, 11, 11, 11)

        ## drop shaodow effect
        self.window.shadow = QGraphicsDropShadowEffect(self.window)
        self.window.shadow.setBlurRadius(40)
        self.window.shadow.setXOffset(0)
        self.window.shadow.setYOffset(0)
        self.window.shadow.setColor(QtGui.QColor(0, 0, 0, 255))
        self.window.ui.drop_shadow_frame.setGraphicsEffect(self.window.shadow)

        # MINIMIZE 
        self.window.ui.button_minimize.clicked.connect(lambda: self.window.showMinimized())

        # MAXIMIZE/RESTORE
        self.window.ui.button_restore.clicked.connect(lambda: self.maximize_restore())

        # CLOSE
        self.window.ui.button_close.clicked.connect(lambda: self.close_win())
        
        
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
    
    def close_win(self) :
        print(colored('Exiting ...', 'red'))
        self.window.close()
  

   

   
   