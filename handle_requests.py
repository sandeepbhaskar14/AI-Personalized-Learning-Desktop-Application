from main import *

# importing login window
# from login_window import LoginWindow
from functools import partial
import re
import requests
from termcolor import colored

# importing message window
# from show_message import messageWindow


LOGGED_IN = False

# worker thread to acheive parallelism and avoid GUI frezzing
class WorkerThread(QThread): 
    # esatablishes a connection between secondary thread and main thread
    data_fetched = pyqtSignal(dict)      # for JSON or general metadata
    products_data_fetched = pyqtSignal(str)      # for JSON or general metadata
    # image_fetched = pyqtSignal(bytes)    # specifically for image data 
    
    def __init__(self, data, method, route, headers=None):
        super().__init__()
        self.data = data
        self.method = method
        self.route = route
        self.headers = headers

    def run(self):         
        if self.method == 'POST' and self.route == 'register':
            try:
                response = requests.post('http://localhost:5000/signup', json=self.data)
                self.data_fetched.emit(response.json())
                print("Server responded with:", response.json())
            except requests.exceptions.ConnectionError:
                print(colored('Failed to establish a new connection: [WinError 10061]', 'red'))
         
        elif self.method == 'POST' and self.route == 'login':
            try:
                response = requests.post('http://localhost:5000/login', json=self.data)
                self.data_fetched.emit(response.json())
                print("Server responded with:", response.json())
            except requests.exceptions.ConnectionError:
                print(colored('Failed to establish a new connection: [WinError 10061]', 'red'))
         
         
        elif self.method == 'POST' and self.route == 'preferences':
            try:
                response = requests.post('http://localhost:5000/user/preferences', json=self.data, headers=self.headers)
                self.data_fetched.emit(response.json())
                print("Server responded with:", response.json())
            except requests.exceptions.RequestException as e:
                print(colored('Connection Error: Server not reachable', 'red'))
                # QMessageBox.critical(
                #     self,
                #     "Connection Error",
                #     f"Server not reachable:\n{str(e)}"
                # )
        elif self.method == 'GET' and self.route == 'preferences':
            try:
                response = requests.get('http://localhost:5000/user/preferences', headers=self.headers)
                self.data_fetched.emit(response.json())
                print("Server responded with:", response.json())
            except requests.exceptions.RequestException as e:
                print(colored('Connection Error: Server not reachable', 'red'))
          
              
        # elif self.method == 'GET' and self.route == 'verify_token':
        #     try:
        #         response = requests.get('http://localhost:5000/verify_token', headers=self.headers)
        #         self.data_fetched.emit(response.json())
        #         print("Server responded with:", response.json())
        #     except requests.exceptions.RequestException as e:
        #         print(colored('Connection Error: Server not reachable', 'red'))
                
        elif self.method == 'POST' and self.route == 'prompt':
            try:
                response = requests.post('http://localhost:5000/prompt', json=self.data, headers=self.headers)
                self.data_fetched.emit(response.json())
                # print("Server responded with:", response.json())
            except requests.exceptions.RequestException as e:
                print(colored('Connection Error: Server not reachable', 'red'))
                
                
'''          
def get_token_verification(self, response):  
    if response['status_code'] == 200:
        self.status = response['status_code']

def verify_token(self):
    subprocess.run(["icacls", "auth_token.x", "/remove:d", "Everyone"], check=True)
    file = open('auth_token.x', 'r', encoding='utf-8')
    self.jwt_token = file.read()
    file.close()
    subprocess.run(["icacls", "auth_token.x", "/deny", "Everyone:(R)"], check=True)
    
    # Prepare headers with JWT
    headers = {
        "Authorization": f"Bearer {self.jwt_token}",
        "Content-Type": "application/json"
    }
    
    self.thread = WorkerThread(None, 'GET', 'verify_token', headers=headers)
    self.thread.data_fetched.connect(lambda response: get_token_verification(self, response))
    self.thread.start()
'''
                
def signup_update_ui(self):
    self.ui.signup_button.setEnabled(True)
    self.ui.label.setText('SIGN UP')
    self.ui.label.setStyleSheet('color:rgba(255, 255, 255, 180);')
    
@pyqtSlot(dict)
def handle_signup_response(self, response):
    if response['status_code'] == 201:   # user registered
        self.ui.uname_lineEdit.setText('')
        self.ui.email_lineEdit.setText('')
        self.ui.pass_lineEdit.setText('')
        
        self.ui.info_label.setStyleSheet('color: rgb(0, 255, 127);')
        self.ui.info_label.setText('User registered, go to the login page!')
        
    elif response['status_code'] == 400:  # Entry error
        self.ui.uname_lineEdit.setText('')
        self.ui.email_lineEdit.setText('')
        self.ui.pass_lineEdit.setText('')
        
        self.ui.info_label.setStyleSheet('color: rgb(255, 0, 0);')
        self.ui.info_label.setText("Invalid username, email or password")
        
    elif response['status_code'] == 409:  # username already exists
        self.ui.uname_lineEdit.setText('')
        self.ui.email_lineEdit.setText('')
        self.ui.pass_lineEdit.setText('')
        
        self.ui.info_label.setStyleSheet('color: rgb(255, 0, 0);')
        self.ui.info_label.setText("User or email already exists")
        
    elif response['status_code'] == 500:  # username already exists
        self.ui.uname_lineEdit.setText('')
        self.ui.email_lineEdit.setText('')
        self.ui.pass_lineEdit.setText('')
        
        self.ui.info_label.setStyleSheet('color: rgb(255, 0, 0);')
        self.ui.info_label.setText("Internal server error")
        
        
# signup function
def signup(self):
    username = self.ui.uname_lineEdit.text()
    email = self.ui.email_lineEdit.text()
    password = self.ui.pass_lineEdit.text()
    
    password_pattern = r'(?=.*[a-z])(?=.*[A-Z])(?=.*\W)'
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    self.ui.info_label.setStyleSheet('color:rgb(255, 0, 0);')
    if username == '' or email == '' or password == '':
        self.ui.info_label.setText("username, email or password can't be empty")
        
    elif len(password) < 8:
        self.ui.info_label.setText("password must contain at least 8 characters")
        
    elif bool(re.search(password_pattern, password)) == False:
        self.ui.info_label.setText("password must contain at least 1 upper case, lower case and a special symbol")
        
    elif bool(re.search(email_pattern, email)) == False:
        self.ui.info_label.setText("Invalid Email address")
        
    else:
        payload = {
            "username":username,
            "email":email,
            "password":password
        }
        
        self.ui.signup_button.setEnabled(False)
        self.ui.label.setText('Signing up...')
        self.ui.label.setStyleSheet('color: rgb(0, 255, 127);')
        
        self.thread = WorkerThread(payload, 'POST', 'register')
        self.thread.data_fetched.connect(lambda response: handle_signup_response(self, response))
        self.thread.finished.connect(lambda: signup_update_ui(self))
        self.thread.start()
        
def login_update_ui(self):
    self.ui.login_button.setEnabled(True)
    self.ui.label_3.setText('LOG IN')
    self.ui.label_3.setStyleSheet('color:rgba(255, 255, 255, 180);')    

@pyqtSlot(dict)
def handle_login_response(self, response, main_win):
    global LOGGED_IN
    if 'token' in response:   # user logged in
        uname = self.ui.uid_lineEdit_2.text()
        self.ui.uid_lineEdit_2.setText('')
        self.ui.pass_lineEdit_2.setText('')
        self.close()
        
        subprocess.run(["icacls", "auth_token.x", "/remove:d", "Everyone"], check=True)
        file = open('auth_token.x', 'w', encoding='utf-8')
        file.write(response['token'])
        file.close()
        subprocess.run(["icacls", "auth_token.x", "/deny", "Everyone:(R)"], check=True)
        
        get_user_preferences(main_win)
        
        LOGGED_IN = True
        
        # update main ui
        
        
        
    else:  # username doesn't exists
        # uid = self.ui.uid_lineEdit.text()
        self.ui.pass_lineEdit_2.setText('')
        self.ui.uid_lineEdit_2.setText('')
        
        self.ui.info_label2.setStyleSheet('color: rgb(255, 0, 0);')
        self.ui.info_label2.setText("Invalid credentials")
    
def login(self, main_win):
    self.ui.info_label.setText('')
    
    username = self.ui.uid_lineEdit_2.text()
    password = self.ui.pass_lineEdit_2.text()
    
    if username == '' or password == '':
        self.ui.info_label2.setStyleSheet('color:rgb(255, 0, 0);')
        self.ui.info_label2.setText("username or password can't be empty")
    else:
        payload = {
            "username":username,
            "password":password
        }

        self.ui.login_button.setEnabled(False)
        self.ui.label_3.setText('Signing in...')
        self.ui.label_3.setStyleSheet('color: rgb(0, 255, 127);')
        
        self.thread = WorkerThread(payload, 'POST', 'login')
        self.thread.data_fetched.connect(lambda response: handle_login_response(self, response, main_win))
        self.thread.finished.connect(lambda: login_update_ui(self))
        self.thread.start()
        
def update_preference_button(self):
    # change save button state
    self.ui.button_save.setText('Save')
    self.ui.button_save.setEnabled(True)

@pyqtSlot(dict)
def handle_preference_response(self, response):
    if 'saved' in response['message']:
        from show_message import messageWindow
        msg_win = messageWindow(self)
        msg_win.exec_()

def save_user_preferences(self):
    # update save button state
    self.ui.button_save.setText('Saving...')
    self.ui.button_save.setEnabled(False)
    
    # Extract values from UI
    learning_style = self.ui.learning_type.currentText()
    difficulty_level = self.ui.difficulty_type.currentText()
    preferred_task = self.ui.preferred_output.currentText()
    
    h = int(self.ui.spinHour.value())
    m = int(self.ui.spinMinute.value())
    daily_goal_minutes = (h * 60) + m
    
    subprocess.run(["icacls", "auth_token.x", "/remove:d", "Everyone"], check=True)
    file = open('auth_token.x', 'r', encoding='utf-8')
    self.jwt_token = file.read()
    file.close()
    subprocess.run(["icacls", "auth_token.x", "/deny", "Everyone:(R)"], check=True)

    # Prepare payload
    payload = {
        "learning_style": learning_style,
        "difficulty_level": difficulty_level,
        "preferred_task": preferred_task,
        "daily_goal_minutes": daily_goal_minutes
    }
    
    # Prepare headers with JWT
    headers = {
        "Authorization": f"Bearer {self.jwt_token}",
        "Content-Type": "application/json"
    }
    
    self.thread = WorkerThread(payload, 'POST', 'preferences', headers=headers)
    self.thread.data_fetched.connect(lambda response: handle_preference_response(self, response))
    self.thread.finished.connect(lambda: update_preference_button(self))
    self.thread.start()


def handle_token_expired(main_window):
    from main import run_login
    run_login(main_window, 'forced')
    

@pyqtSlot(dict)
def get_preference_response(self, response):
    if response['status_code'] == 200:
        learning_style = response["learning_style"]
        difficulty_level = response["difficulty_level"]
        daily_goal_minutes = response["daily_goal_minutes"]
        preferred_task = response["preferred_task"]
        
        print(colored(("SELF TYPE:", type(self), type(self.ui)), 'green'))
        # Extract values from UI
        self.ui.learning_type.setCurrentText(learning_style)
        self.ui.difficulty_type.setCurrentText(difficulty_level)
        self.ui.preferred_output.setCurrentText(preferred_task)
        
        hour = daily_goal_minutes // 60
        minute = daily_goal_minutes % 60
        
        self.ui.spinHour.setValue(hour)
        self.ui.spinMinute.setValue(minute)
         
    elif response['status_code'] == 404: # prefernces not set 
        pass
    else: # invalid or missing token
        handle_token_expired(self)
     
def get_user_preferences(self):
    subprocess.run(["icacls", "auth_token.x", "/remove:d", "Everyone"], check=True)
    file = open('auth_token.x', 'r', encoding='utf-8')
    self.jwt_token = file.read()
    file.close()
    subprocess.run(["icacls", "auth_token.x", "/deny", "Everyone:(R)"], check=True)
    
    # Prepare headers with JWT
    headers = {
        "Authorization": f"Bearer {self.jwt_token}",
        "Content-Type": "application/json"
    }
    
    self.thread = WorkerThread(None, 'GET', 'preferences', headers=headers)
    self.thread.data_fetched.connect(lambda response: get_preference_response(self, response))
    self.thread.start()
    

def get_prompt_response(self, response):
    if response['status_code'] == 200:
        print(colored(response, 'green'))

def send_prompt(self):
    payload = {
    "prompt_text": self.ui.text_prompt.toPlainText(),
    "prompt_type": self.ui.preferred_output.currentText().lower() #task type
    }

    subprocess.run(["icacls", "auth_token.x", "/remove:d", "Everyone"], check=True)
    file = open('auth_token.x', 'r', encoding='utf-8')
    self.jwt_token = file.read()
    file.close()
    subprocess.run(["icacls", "auth_token.x", "/deny", "Everyone:(R)"], check=True)
    
    headers = {
        "Authorization": f"Bearer {self.jwt_token}"
    }
    
    self.thread = WorkerThread(payload, 'POST', 'prompt', headers=headers)
    self.thread.data_fetched.connect(lambda response: get_prompt_response(self, response))
    self.thread.start()


