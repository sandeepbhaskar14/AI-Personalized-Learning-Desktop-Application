from PyQt5.QtCore import QThread, pyqtSignal, pyqtSlot, QTimer, QSize, Qt
from PyQt5.QtWidgets import QDialog
from PyQt5.QtGui import QIcon
from PyQt5 import QtGui, QtWidgets


from termcolor import colored
import subprocess, re
import requests

import uuid



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
         
        elif self.method == 'GET' and self.route == 'verify_token':
            try:
                response = requests.get('http://localhost:5000/verify_token', headers=self.headers)

                print("Status Code:", response.status_code)
                print("Raw Response:", response.text)  # IMPORTANT

                data = response.json()  # this is failing
                self.data_fetched.emit(data)

            except requests.exceptions.ConnectionError:
                print("Connection failed")

            except ValueError:  # catches JSON decode error
                print("Invalid JSON received")
         
         
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
                
        elif self.method == 'POST' and self.route == '/prompt/stream':
            try:
                response = requests.post(
                    'http://localhost:5000/prompt/stream',
                    json=self.data,
                    headers=self.headers,
                    stream=True   # IMPORTANT
                )

                for chunk in response.iter_lines(chunk_size=1, decode_unicode=True):
                    if chunk:
                        self.products_data_fetched.emit(chunk)  # stream token

            except requests.exceptions.RequestException as e:
                print(colored('Connection Error: Server not reachable', 'red'))
        
        elif self.method == 'GET' and self.route == 'chats':
            try:
                response = requests.get(
                    'http://localhost:5000/chat',
                    headers=self.headers
                )
                self.data_fetched.emit(response.json())
            except requests.exceptions.RequestException as e:
                print(colored(f'Connection Error: {e}', 'red'))

        elif self.method == 'GET' and self.route.startswith('chat/'):
            try:
                chat_id = self.route.split('/', 1)[1]
                response = requests.get(
                    f'http://localhost:5000/chat/{chat_id}',
                    headers=self.headers
                )
                self.data_fetched.emit(response.json())
            except requests.exceptions.RequestException as e:
                print(colored(f'Connection Error: {e}', 'red'))
                        
                        
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
    
    
    
    
def run_login(self):
    from auth.login_window import LoginWindow
    login = LoginWindow(self)
    # login.exec_()
    result = login.exec_()  # modal dialog

    if result == QDialog.Accepted:
        self.ui.login_button.setText("Logged In")
        self.ui.login_button.setEnabled(False)
        
def after_verify_token(self, response):
    if response.get("status_code") == 200:
        username = response.get("user")
        email = response.get("email")
        print(colored(f"Logged in user: {username}", 'green'))
        
        stylesheet = """
                        font-family: 'Roboto';       /* font family */
                        font-size: 10pt;            /* font size */
                        font-style: italic;         /* italic text */
                        color: green;                /* text color */
                """
        self.ui.login_button.setText("Logged In")
        self.ui.login_button.setStyleSheet(stylesheet)
        self.ui.login_button.setEnabled(False)
        self.ui.login_button.setToolTip(username)
        self.ui.logged_in_label.setText('Logged In')
        self.ui.logged_in_label.setStyleSheet(stylesheet)
        
        self.ui.username_label.setText(f"Username: {username}")
        self.ui.email_label.setText(f"Email: {email}")
        self.ui.button_logout.setText('Log Out')
        self.ui.button_save.setEnabled(True)
        
        self.update_user_preferences()
        load_chat_history(self)
    else:
        print(colored(response.get("message"), 'red'))
        run_login(self)
        
def verify_token_(self, token, callback):
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    self.thread = WorkerThread(None, 'GET', 'verify_token', headers=headers)

    def handle_response(response):
        callback(self, response)

    self.thread.data_fetched.connect(handle_response)
    self.thread.start()
    
def verify_token(self):
    subprocess.run(
        ["icacls", "auth_token.x", "/remove:d", "Everyone"],
        check=True
    )
    with open("auth_token.x", "r") as token_file:
        token = token_file.read()
        token_file.close()
        
    if token:
        # call async function with callback
        verify_token_(self, token, after_verify_token)
    else:
        run_login(self)

    subprocess.run(
        ["icacls", "auth_token.x", "/deny", "Everyone:(R)"],
        check=True
    )
    
    
@pyqtSlot(dict)
def handle_login_response(self, response, main_win):
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
 
        print(colored('Verifying token!', 'magenta'))
        # MainWindow.verify_token(main_win)
        verify_token(main_win)
        
        
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
        from ui_controllers.show_message import messageWindow
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
    run_login(main_window)
    

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
    print(colored(type(self), 'cyan'))
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
    

def get_prompt_stream(self, chunk):    
    if not hasattr(self, "full_text"):
        self.full_text = ""

    self.full_text += chunk.replace("<<NEWLINE>>", "\n")

    # Update bubble text (throttled internally by QTimer)
    self.ai_bubble.append_stream(self.full_text)

    # Throttle scroll: only scroll if not already scheduled
    if not getattr(self, '_scroll_pending', False):
        self._scroll_pending = True
        QTimer.singleShot(100, lambda: _do_scroll(self))


def _do_scroll(self):
    self._scroll_pending = False
    self.chat_area.scroll_to_bottom()


def finalize_stream(self):
    self._is_streaming = False
    if hasattr(self, 'full_text') and self.full_text:
        self.ai_bubble.finish_stream(self.full_text)
    self._scroll_pending = False
    self.chat_area.scroll_to_bottom()
    
    stop_icon = QtGui.QIcon()
    stop_icon.addPixmap(QtGui.QPixmap("Reqs/search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    self.ui.searchButton_2.setIcon(stop_icon)
    self.ui.searchButton_2.setIconSize(QSize(27, 27))
    
    load_chat_history(self)


def stop_prompt(self):
    """Send stop signal to server."""
    chat_id = getattr(self, 'current_chat_id', None)
    if not chat_id:
        return

    headers = {}
    token = getattr(self, 'jwt_token', '')
    if token:
        headers["Authorization"] = f"Bearer {token}"

    try:
        requests.post(
            'http://localhost:5000/prompt/stop',
            json={"chat_id": chat_id},
            headers=headers,
            timeout=3
        )
    except requests.exceptions.RequestException:
        pass

    # Reset UI immediately
    _on_stream_stopped(self)


def _on_stream_stopped(self):
    # self.ui.searchButton.setIcon(...)   # restore search icon
    self.ui.searchButton_2.setIcon(QIcon('/Reqs/search.png')) # restore search icon


def send_prompt(self):
    from ui.widgets.chat_bubble import ChatBubble
    import uuid

    if hasattr(self, 'full_text'):
        del self.full_text
    self._scroll_pending = False

    self.ui.stackedWidget.setCurrentWidget(self.ui.conversation_page)

    text = self.ui.text_prompt.toPlainText().strip()
    if not text:
        text = self.ui.text_prompt_2.toPlainText().strip()
    if not text:
        return

    self.ui.text_prompt.clear()
    self.ui.text_prompt_2.clear()

    self._is_streaming = True

    stop_icon = QtGui.QIcon()
    stop_icon.addPixmap(QtGui.QPixmap("Reqs/stop.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    self.ui.searchButton_2.setIcon(stop_icon)
    self.ui.searchButton_2.setIconSize(QSize(32, 32))

    # ── KEY FIX: reuse the same chat_id for the whole session ──
    # Only generate a new UUID if there is no active chat session yet.
    # handle_new_chat() resets self.current_chat_id to None, so a new
    # UUID is created only for the very first message of each session.
    if not getattr(self, 'current_chat_id', None):
        self.current_chat_id = str(uuid.uuid4())

    chat_width = self.chat_area.width()
    user_bubble = ChatBubble(text, is_user=True, available_width=chat_width)
    self.chat_area.add_bubble(user_bubble)

    self.ai_bubble = ChatBubble("", is_user=False, available_width=chat_width)
    self.ai_bubble.start_stream()
    self.chat_area.add_bubble(self.ai_bubble)

    payload = {
        "prompt_text": text,
        "prompt_type": self.ui.preferred_output.currentText().lower(),
        "chat_id": self.current_chat_id,
    }

    subprocess.run(["icacls", "auth_token.x", "/remove:d", "Everyone"], check=True)
    with open('auth_token.x', 'r', encoding='utf-8') as f:
        self.jwt_token = f.read().strip()
    subprocess.run(["icacls", "auth_token.x", "/deny", "Everyone:(R)"], check=True)

    headers = ({"Authorization": f"Bearer {self.jwt_token}"}
               if self.jwt_token else None)

    self.thread = WorkerThread(payload, 'POST', '/prompt/stream', headers=headers)
    self.thread.products_data_fetched.connect(
        lambda chunk: get_prompt_stream(self, chunk))
    self.thread.finished.connect(lambda: finalize_stream(self))
    self.thread.start()
    
    
    
# ── Chat History ──────────────────────────────────────────────────────────────

def load_chat_history(self):
    """Fetch all chats for the logged-in user and populate the sidebar."""
    token = getattr(self, 'jwt_token', '')
    if not token:
        return

    headers = {"Authorization": f"Bearer {token}"}
    self.chat_history_thread = WorkerThread(None, 'GET', 'chats', headers=headers)
    self.chat_history_thread.data_fetched.connect(
        lambda response: _populate_chat_history(self, response)
    )
    self.chat_history_thread.start()


def _populate_chat_history(self, response):
    if response.get('status_code') != 200:
        return

    chats = response.get('chats', [])
    list_widget = self.ui.chat_history
    list_widget.clear()

    for chat in chats:
        item = QtWidgets.QListWidgetItem(chat['title'])
        item.setData(Qt.UserRole, chat['chat_id'])          # store chat_id on item
        item.setToolTip(chat['title'])
        list_widget.addItem(item)


def on_chat_history_item_clicked(self, item):
    """Load a previous chat when the user clicks it in the sidebar."""
    chat_id = item.data(Qt.UserRole)
    if not chat_id:
        return

    token = getattr(self, 'jwt_token', '')
    headers = {"Authorization": f"Bearer {token}"}

    self.load_chat_thread = WorkerThread(None, 'GET', f'chat/{chat_id}', headers=headers)
    self.load_chat_thread.data_fetched.connect(
        lambda response: _render_loaded_chat(self, response)
    )
    self.load_chat_thread.start()


def _render_loaded_chat(self, response):
    if response.get('status_code') != 200:
        return

    from ui.widgets.chat_bubble import ChatBubble

    # Switch to conversation page and clear existing bubbles
    self.ui.stackedWidget.setCurrentWidget(self.ui.conversation_page)
    self.clear_chat()

    chat_id   = response['chat_id']
    messages  = response.get('messages', [])
    chat_width = self.chat_area.width()

    for msg in messages:
        is_user = msg['role'] == 'user'
        bubble  = ChatBubble(msg['text'], is_user=is_user, available_width=chat_width)
        self.chat_area.add_bubble(bubble)

    # Resume this chat so new messages continue the same session
    self.current_chat_id = chat_id
    self.chat_area.scroll_to_bottom()