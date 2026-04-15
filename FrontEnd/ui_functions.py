## IMPORTING UI MAIN FILE
from main import *

## ==>> GLOBALS
GLOBAL_STATE = 0


class UIFunctions(MainWindow) :
    # ==>> Maximize Restore Function
    def maximize_restore(self) :
        global GLOBAL_STATE
        status = GLOBAL_STATE

        # IF NOT MAXIMIZED
        if status == 0 :
            #self.showNormal()
            self.ui.verticalLayout.setContentsMargins(0, 0, 0, 0)
            self.ui.verticalLayout.setSpacing(0)
            self.showMaximized()
            
            # self.ui.frame_43.setMinimumSize(QtCore.QSize(540, 0))

            # SET GLOBAL TO 1
            GLOBAL_STATE = 1

            # SET ICON TO RESTORE
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("Reqs/restore-down.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.ui.button_restore.setIcon(icon)
            self.ui.button_restore.setToolTip("Restore")

        else :
            GLOBAL_STATE = 0
            self.ui.verticalLayout.setContentsMargins(11, 11, 11, 11)
            self.showNormal()
            self.resize(self.width() +1, self.height()+1 )

            # SET ICON TO RESTORE
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("Reqs/maximize.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.ui.button_restore.setIcon(icon)
            self.ui.button_restore.setToolTip("Maximize")
    
    
    def returnStatus(self) :
        return GLOBAL_STATE


    # ==>>TOGGLE BUTTON
    def toggle(self, maxWidth, enable) :
        if enable :

            # GET WIDTH
            width = self.ui.toggle_frame_left.width()
            maxExtend = maxWidth
            standard = 85

            # SET MAX WIDTH
            if width == 85:
                widthExtended = maxExtend
            else :
                widthExtended = standard

            # ANIMATION
            self.animation = QPropertyAnimation(self.ui.toggle_frame_left, b"minimumWidth")
            self.animation.setDuration(160)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtended)
            #self.animation.setStartValue(QRect(-200, 0, 200, 600))
            #self.animation.setEndValue(QRect(0, 0, 200, 600))
            self.animation.start()
            
    
    # UI FUNCTIONS
    def uiDefinitions(self) :

        # ==>> REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        
        self.ui.verticalLayout.setContentsMargins(11, 11, 11, 11)

        ## drop shaodow effect
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(40)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QtGui.QColor(0, 0, 0, 255))
        self.ui.drop_shadow_frame.setGraphicsEffect(self.shadow)

        # MINIMIZE 
        self.ui.button_minimize.clicked.connect(lambda: self.showMinimized())

        # MAXIMIZE/RESTORE
        self.ui.button_restore.clicked.connect(lambda: UIFunctions.maximize_restore(self))

        # CLOSE
        self.ui.button_close.clicked.connect(lambda: UIFunctions.close_win(self))
        
        
    def setDefaultPage(self):
        self.ui.stackedWidget_2.setCurrentWidget(self.ui.defaultPage)

        
    def setNewChatPage(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.new_chat_page)
        
    def setSettingsPage(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.settings_page)
        self.ui.setting_pages.setCurrentWidget(self.ui.account_page)
 
    def setAboutPage(self):
        self.ui.setting_pages.setCurrentWidget(self.ui.about_page)
        
    def setAccountPage(self):
        self.ui.setting_pages.setCurrentWidget(self.ui.account_page)
        
    def setPreferencesPage(self):
        self.ui.setting_pages.setCurrentWidget(self.ui.preference_page)
    
    def close_win(self) :
        print(colored('Exiting ...', 'red'))
        self.close()
  

   

   
   