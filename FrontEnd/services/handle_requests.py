from PyQt5.QtCore import QThread, pyqtSignal, pyqtSlot, QTimer, QSize, Qt
from PyQt5.QtWidgets import QDialog, QFileDialog, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5 import QtGui, QtWidgets


from termcolor import colored
import subprocess, re, os
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
                
        elif self.method == 'DELETE' and self.route.startswith('chat/'):
            try:
                chat_id = self.route.split('/', 1)[1]
                response = requests.delete(
                    f'http://localhost:5000/chat/{chat_id}',
                    headers=self.headers
                )
                self.data_fetched.emit(response.json())
            except requests.exceptions.RequestException as e:
                print(colored(f'Connection Error: {e}', 'red'))

        elif self.method == 'PATCH' and self.route.startswith('chat/'):
            try:
                chat_id = self.route.split('/', 1)[1]
                response = requests.patch(
                    f'http://localhost:5000/chat/{chat_id}',
                    json=self.data,
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

# ── Document extraction helpers ───────────────────────────────────────────────
 
def _extract_text_from_pdf(path: str) -> str:
    """Extract text from a PDF file using PyMuPDF (fitz) or pdfplumber as fallback."""
    text = ""
    try:
        import fitz  # PyMuPDF
        doc = fitz.open(path)
        for page in doc:
            text += page.get_text()
        doc.close()
        return text.strip()
    except ImportError:
        pass
 
    try:
        import fitz  # PyMuPDF

        text = ""
        with fitz.open(path) as pdf:
            for page in pdf:
                page_text = page.get_text()
                if page_text:
                    text += page_text + "\n"

        return text.strip()

    except ImportError:
        pass
 
    raise ImportError(
        "PDF reading requires either PyMuPDF or pdfplumber.\n"
        "Install one with:\n  pip install pymupdf\nor\n  pip install pdfplumber"
    )
 
 
def _extract_text_from_docx(path: str) -> str:
    """Extract text from a .docx file using python-docx."""
    try:
        from docx import Document
        doc = Document(path)
        return "\n".join(p.text for p in doc.paragraphs if p.text.strip())
    except ImportError:
        raise ImportError(
            "DOCX reading requires python-docx.\n"
            "Install it with:  pip install python-docx"
        )
 
 
def _extract_text_from_file(path: str) -> str:
    """Dispatch to the correct extractor based on file extension."""
    ext = os.path.splitext(path)[1].lower()
    if ext == ".pdf":
        return _extract_text_from_pdf(path)
    elif ext in (".docx", ".doc"):
        return _extract_text_from_docx(path)
    elif ext in (".txt", ".md", ".csv", ".py", ".js", ".ts", ".html",
                  ".css", ".json", ".xml", ".yaml", ".yml", ".rst"):
        with open(path, "r", encoding="utf-8", errors="ignore") as f:
            return f.read()
    else:
        raise ValueError(f"Unsupported file type: {ext}")
 
 
# ── Document open / clear ─────────────────────────────────────────────────────
 
# Supported file types for the file dialog
_SUPPORTED_FILTERS = (
    "Documents (*.pdf *.docx *.doc *.txt *.md *.csv "
    "*.py *.js *.ts *.html *.css *.json *.xml *.yaml *.yml *.rst);;"
    "PDF Files (*.pdf);;"
    "Word Documents (*.docx *.doc);;"
    "Text Files (*.txt *.md *.csv);;"
    "Code Files (*.py *.js *.ts *.html *.css *.json *.xml *.yaml *.yml *.rst);;"
    "All Files (*)"
)
 
_ADD_ICON_PATH    = "Reqs/add_icon.png"
_ATTACH_ICON_PATH = "Reqs/add_icon.png"   # swap to a paperclip icon if you have one
 
 
def open_document(self):
    """
    Open a file dialog, extract text from the chosen document,
    and store it on the window for the next prompt submission.
    If a document is already attached, clicking the button removes it.
    """
    # --- Toggle: if already attached, clear it ---
    if getattr(self, 'attached_document', None):
        clear_document(self)
        return
 
    path, _ = QFileDialog.getOpenFileName(
        self,
        "Attach a Document",
        "",
        _SUPPORTED_FILTERS
    )
 
    if not path:
        return  # user cancelled
 
    try:
        text = _extract_text_from_file(path)
    except (ImportError, ValueError, Exception) as e:
        QMessageBox.critical(
            self,
            "Document Error",
            f"Could not read the file:\n\n{e}"
        )
        return
 
    if not text.strip():
        QMessageBox.warning(
            self,
            "Empty Document",
            "The selected file appears to be empty or contains no readable text."
        )
        return
 
    # Truncate very large documents to avoid token overflow (≈ 12 000 chars ≈ 3 000 tokens)
    MAX_CHARS = 12_000
    truncated = False
    if len(text) > MAX_CHARS:
        text = text[:MAX_CHARS]
        truncated = True
 
    filename = os.path.basename(path)
 
    # Store on the window
    self.attached_document = {
        "filename": filename,
        "text": text,
        "truncated": truncated,
    }
 
    print(colored(f"Document attached: {filename} ({len(text)} chars)", "cyan"))
 
    # Update both add-buttons to show the attachment
    _set_attach_button_active(self, filename)
 
    if truncated:
        QMessageBox.information(
            self,
            "Document Truncated",
            f"'{filename}' is large and has been truncated to the first "
            f"{MAX_CHARS:,} characters to fit within the AI context window."
        )
 
 
def clear_document(self):
    """Remove the currently attached document and reset button icons."""
    self.attached_document = None
    _set_attach_button_inactive(self)
    print(colored("Document detached", "yellow"))
 
 
def _set_attach_button_active(self, filename: str):
    """Tint / re-label both add-buttons to indicate an attachment is loaded."""
    tooltip = f"📎 {filename}\n(click to remove)"
    active_style = """
        QPushButton {
            background: none;
            border: 2px solid rgb(85, 170, 255);
            color: rgb(85, 170, 255);
            border-radius: 21px;
            margin-top: 3px;
        }
        QPushButton:hover {
            background-color: rgba(85, 170, 255, 30);
            border-color: rgb(231, 0, 116);
        }
    """
    for btn in (self.ui.addButton, self.ui.addButton_2):
        btn.setStyleSheet(active_style)
        btn.setToolTip(tooltip)
 
 
def _set_attach_button_inactive(self):
    """Restore both add-buttons to their default style."""
    default_style = """
        QPushButton {
            background: none;
            border: none;
            color: rgba(255, 255, 255, 180);
            border-radius: 21px;
            margin-top: 3px;
        }
        QPushButton:hover {
            background-color: rgb(45, 48, 58);
        }
    """
    for btn in (self.ui.addButton, self.ui.addButton_2):
        btn.setStyleSheet(default_style)
        btn.setToolTip("Attach a document")
 
                
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
    # If stop_prompt already handled the finalization, just clean up and return.
    if getattr(self, '_stream_stopped', False):
        self._stream_stopped = False
        load_chat_history(self)
        return

    self._is_streaming = False
    if hasattr(self, 'full_text') and self.full_text:
        self.ai_bubble.finish_stream(self.full_text)
    self._scroll_pending = False
    self.chat_area.scroll_to_bottom()

    search_icon = QtGui.QIcon()
    search_icon.addPixmap(QtGui.QPixmap("Reqs/search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    self.ui.searchButton_2.setIcon(search_icon)
    self.ui.searchButton_2.setIconSize(QSize(27, 27))
    
    # Clear attached document after a successful send
    clear_document(self)


    load_chat_history(self)


def stop_prompt(self):
    """Send stop signal to server."""
    chat_id = getattr(self, 'current_chat_id', None)
    if not chat_id:
        return
    
    # Mark as stopped so finalize_stream (fired by thread.finished) is a no-op
    self._stream_stopped = True


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
    """Finalize bubble with partial text and restore the search icon."""
    self._is_streaming = False
    self._scroll_pending = False

    # Render whatever we received so far as proper markdown
    if hasattr(self, 'full_text') and self.full_text:
        self.ai_bubble.finish_stream(self.full_text)

    self.chat_area.scroll_to_bottom()

    # Restore search icon
    search_icon = QtGui.QIcon()
    search_icon.addPixmap(QtGui.QPixmap("Reqs/search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    self.ui.searchButton_2.setIcon(search_icon)
    self.ui.searchButton_2.setIconSize(QSize(27, 27))
    
    # Clear attached document on stop too
    clear_document(self)


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
    
    # ── Build display text for the user bubble ──────────────────────────
    doc = getattr(self, 'attached_document', None)
    if doc:
        display_text = f"📎 {doc['filename']}\n\n{text}"
    else:
        display_text = text
        
    user_bubble = ChatBubble(text, is_user=True, available_width=chat_width)
    self.chat_area.add_bubble(user_bubble)

    self.ai_bubble = ChatBubble("", is_user=False, available_width=chat_width)
    self.ai_bubble.start_stream()
    self.chat_area.add_bubble(self.ai_bubble)
    
    # ── Build payload — include document_text if present ────────────────

    payload = {
        "prompt_text": text,
        "prompt_type": self.ui.preferred_output.currentText().lower(),
        "chat_id": self.current_chat_id,
    }
    
    if doc:
        payload["document_text"] = doc["text"]
        payload["document_name"] = doc["filename"]

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
    
    
# ── Rename / Delete via right-click context menu ──────────────────────────────

def _show_chat_context_menu(self, position):
    """Right-click context menu on a chat history item."""
    from PyQt5.QtWidgets import QMenu, QAction, QInputDialog, QMessageBox

    item = self.ui.chat_history.itemAt(position)
    if not item:
        return

    chat_id = item.data(Qt.UserRole)
    current_title = item.text()

    menu = QMenu(self.ui.chat_history)
    menu.setStyleSheet("""
        QMenu {
            background-color: rgb(43, 47, 58);
            color: rgba(255, 255, 255, 200);
            border: 1px solid rgba(255, 255, 255, 30);
            border-radius: 6px;
            padding: 4px;
            font-family: 'Roboto';
            font-size: 10pt;
        }
        QMenu::item {
            padding: 8px 20px;
            border-radius: 4px;
        }
        QMenu::item:selected {
            background-color: rgb(55, 62, 76);
            color: white;
        }
        QMenu::separator {
            height: 1px;
            background: rgba(255, 255, 255, 20);
            margin: 3px 8px;
        }
    """)

    from PyQt5.QtWidgets import QAction
    rename_action = QAction("✏  Rename", self.ui.chat_history)
    delete_action = QAction("🗑  Delete", self.ui.chat_history)

    menu.addAction(rename_action)
    menu.addSeparator()
    menu.addAction(delete_action)

    action = menu.exec_(self.ui.chat_history.mapToGlobal(position))

    if action == rename_action:
        _rename_chat_dialog(self, item, chat_id, current_title)
    elif action == delete_action:
        _delete_chat_confirm(self, item, chat_id)


def _rename_chat_dialog(self, item, chat_id, current_title):
    """Show inline input dialog to rename a chat."""
    from PyQt5.QtWidgets import QInputDialog, QLineEdit

    dialog = QInputDialog(self.ui.chat_history)
    dialog.setWindowTitle("Rename Chat")
    dialog.setLabelText("New name:")
    dialog.setTextValue(current_title)
    dialog.setStyleSheet("""
        QInputDialog, QDialog {
            background-color: rgb(35, 38, 47);
        }
        QLabel {
            color: rgba(255, 255, 255, 180);
            font-family: 'Roboto';
            font-size: 10pt;
        }
        QLineEdit {
            background-color: rgb(41, 44, 53);
            color: white;
            border: 2px solid rgb(85, 170, 255);
            border-radius: 6px;
            padding: 6px 12px;
            font-family: 'Roboto';
            font-size: 10pt;
        }
        QPushButton {
            background-color: rgb(48, 53, 65);
            color: rgba(255, 255, 255, 200);
            border: 1px solid rgba(255, 255, 255, 40);
            border-radius: 6px;
            padding: 6px 16px;
            font-family: 'Roboto';
            font-size: 9pt;
            min-width: 70px;
        }
        QPushButton:hover {
            background-color: rgb(55, 62, 76);
            border: 1px solid rgb(85, 170, 255);
            color: white;
        }
        QPushButton:default {
            border: 1px solid rgb(85, 170, 255);
        }
    """)

    ok = dialog.exec_()
    new_title = dialog.textValue().strip()

    if not ok or not new_title or new_title == current_title:
        return

    token = getattr(self, 'jwt_token', '')
    headers = {"Authorization": f"Bearer {token}"}

    self.rename_thread = WorkerThread(
        {"title": new_title}, 'PATCH', f'chat/{chat_id}', headers=headers
    )

    def on_renamed(response):
        if response.get('status_code') == 200:
            item.setText(new_title)
            item.setToolTip(new_title)

    self.rename_thread.data_fetched.connect(on_renamed)
    self.rename_thread.start()


def _delete_chat_confirm(self, item, chat_id):
    """Show confirmation dialog then delete the chat."""
    from ui_controllers.show_confirm_dialog import ConfirmDialog
    
    dialog = ConfirmDialog()

    if dialog.exec_() == QDialog.Accepted:
        dialog.close()


    token = getattr(self, 'jwt_token', '')
    headers = {"Authorization": f"Bearer {token}"}

    self.delete_thread = WorkerThread(
        None, 'DELETE', f'chat/{chat_id}', headers=headers
    )

    def on_deleted(response):
        if response.get('status_code') == 200:
            row = self.ui.chat_history.row(item)
            self.ui.chat_history.takeItem(row)

            # If this was the active chat, reset to new chat state
            if getattr(self, 'current_chat_id', None) == chat_id:
                self.handle_new_chat()

    self.delete_thread.data_fetched.connect(on_deleted)
    self.delete_thread.start()