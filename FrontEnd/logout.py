from main import *

def update_ui(self):     
    username = self.ui.username_label.text()
    self.ui.login_button.setText("Log In")
    self.ui.login_button.setStyleSheet('''QPushButton{
                                            color: rgba(255, 255, 255, 200);
                                            font-family: 'Roboto';       /* font family */
                                            font-size: 10pt;            /* font size */
                                            background-color: rgb(48, 53, 65);
                                            border-radius:10px;
                                          }
                                          QPushButton:hover{
                                            color:rgb(85, 170, 255);
                                            background-color:rgb(52, 57, 70)
                                          }''')
    self.ui.login_button.setEnabled(True)
    self.ui.login_button.setToolTip("")
    
    self.ui.logged_in_label.setText('Not Logged In')
    self.ui.logged_in_label.setStyleSheet('''color: rgba(255, 0, 0, 200);
                                             font-family: 'Roboto';       /* font family */
                                             font-size: 10pt;            /* font size */
                                            ''')
    
    self.ui.username_label.setText("Username: ")
    self.ui.email_label.setText("Email: ")
    self.ui.button_logout.setText('Log In')

    print(colored(f"LOGGED OUT User: {username.split()[1]}", 'green'))
    
def reset_preferences(self):
    self.ui.learning_type.setCurrentText('Text')
    self.ui.difficulty_type.setCurrentText('Easy')
    self.ui.preferred_output.setCurrentText('Search')
    
    self.ui.spinHour.setValue(0)
    self.ui.spinMinute.setValue(0)
    
    print(colored('All Preferences got RESET', 'green'))
    
def LogOut(self):
    subprocess.run(
        ["icacls", "auth_token.x", "/remove:d", "Everyone"],
        check=True
    )
    with open("auth_token.x", "w"):
        pass

    subprocess.run(
        ["icacls", "auth_token.x", "/deny", "Everyone:(R)"],
        check=True
    )
    update_ui(self)
    reset_preferences(self)