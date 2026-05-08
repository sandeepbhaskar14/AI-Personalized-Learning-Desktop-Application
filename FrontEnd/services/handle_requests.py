from PyQt5.QtCore import QThread, pyqtSignal, pyqtSlot, QTimer, QSize, Qt
from PyQt5.QtWidgets import QDialog, QFileDialog, QMessageBox
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5 import QtGui, QtWidgets

from termcolor import colored
import subprocess, re, os, base64
import requests
import uuid


# ── Image extensions — handled as pixmaps + vision payload ────────────────────
_IMAGE_EXTS = {".png", ".jpg", ".jpeg", ".gif", ".bmp", ".webp"}

# MIME type lookup for base64 image payloads
_MIME_TYPES = {
    ".png":  "image/png",
    ".jpg":  "image/jpeg",
    ".jpeg": "image/jpeg",
    ".gif":  "image/gif",
    ".bmp":  "image/bmp",
    ".webp": "image/webp",
}


# ── Worker thread ──────────────────────────────────────────────────────────────
class WorkerThread(QThread):
    data_fetched = pyqtSignal(dict)
    products_data_fetched = pyqtSignal(str)

    def __init__(self, data, method, route, headers=None):
        super().__init__()
        self.data    = data
        self.method  = method
        self.route   = route
        self.headers = headers

    def run(self):
        if self.method == 'POST' and self.route == 'register':
            try:
                response = requests.post('http://localhost:5000/signup', json=self.data)
                self.data_fetched.emit(response.json())
            except requests.exceptions.ConnectionError:
                print(colored('Failed to establish a new connection: [WinError 10061]', 'red'))

        elif self.method == 'POST' and self.route == 'login':
            try:
                response = requests.post('http://localhost:5000/login', json=self.data)
                self.data_fetched.emit(response.json())
            except requests.exceptions.ConnectionError:
                print(colored('Failed to establish a new connection: [WinError 10061]', 'red'))

        elif self.method == 'GET' and self.route == 'verify_token':
            try:
                response = requests.get('http://localhost:5000/verify_token', headers=self.headers)
                self.data_fetched.emit(response.json())
            except requests.exceptions.ConnectionError:
                print("Connection failed")
            except ValueError:
                print("Invalid JSON received")

        elif self.method == 'POST' and self.route == 'preferences':
            try:
                response = requests.post(
                    'http://localhost:5000/user/preferences',
                    json=self.data, headers=self.headers)
                self.data_fetched.emit(response.json())
            except requests.exceptions.RequestException:
                print(colored('Connection Error: Server not reachable', 'red'))

        elif self.method == 'GET' and self.route == 'preferences':
            try:
                response = requests.get(
                    'http://localhost:5000/user/preferences', headers=self.headers)
                self.data_fetched.emit(response.json())
            except requests.exceptions.RequestException:
                print(colored('Connection Error: Server not reachable', 'red'))

        elif self.method == 'POST' and self.route == '/prompt/stream':
            try:
                response = requests.post(
                    'http://localhost:5000/prompt/stream',
                    json=self.data, headers=self.headers, stream=True)
                for chunk in response.iter_lines(chunk_size=1, decode_unicode=True):
                    if chunk:
                        self.products_data_fetched.emit(chunk)
            except requests.exceptions.RequestException:
                print(colored('Connection Error: Server not reachable', 'red'))

        elif self.method == 'GET' and self.route == 'chats':
            try:
                response = requests.get('http://localhost:5000/chat', headers=self.headers)
                self.data_fetched.emit(response.json())
            except requests.exceptions.RequestException as e:
                print(colored(f'Connection Error: {e}', 'red'))

        elif self.method == 'GET' and self.route.startswith('chat/'):
            try:
                chat_id  = self.route.split('/', 1)[1]
                response = requests.get(
                    f'http://localhost:5000/chat/{chat_id}', headers=self.headers)
                self.data_fetched.emit(response.json())
            except requests.exceptions.RequestException as e:
                print(colored(f'Connection Error: {e}', 'red'))

        elif self.method == 'DELETE' and self.route.startswith('chat/'):
            try:
                chat_id  = self.route.split('/', 1)[1]
                response = requests.delete(
                    f'http://localhost:5000/chat/{chat_id}', headers=self.headers)
                self.data_fetched.emit(response.json())
            except requests.exceptions.RequestException as e:
                print(colored(f'Connection Error: {e}', 'red'))

        elif self.method == 'PATCH' and self.route.startswith('chat/'):
            try:
                chat_id  = self.route.split('/', 1)[1]
                response = requests.patch(
                    f'http://localhost:5000/chat/{chat_id}',
                    json=self.data, headers=self.headers)
                self.data_fetched.emit(response.json())
            except requests.exceptions.RequestException as e:
                print(colored(f'Connection Error: {e}', 'red'))


# ── Text-extraction helpers ────────────────────────────────────────────────────

def _extract_text_from_pdf(path: str) -> str:
    try:
        import fitz
        doc  = fitz.open(path)
        text = "".join(page.get_text() for page in doc)
        doc.close()
        return text.strip()
    except ImportError:
        pass
    try:
        import pdfplumber
        text = ""
        with pdfplumber.open(path) as pdf:
            for page in pdf.pages:
                t = page.extract_text()
                if t:
                    text += t + "\n"
        return text.strip()
    except ImportError:
        pass
    raise ImportError(
        "PDF reading requires PyMuPDF or pdfplumber.\n"
        "Install with:  pip install pymupdf  or  pip install pdfplumber"
    )


def _extract_text_from_docx(path: str) -> str:
    try:
        from docx import Document
        doc = Document(path)
        return "\n".join(p.text for p in doc.paragraphs if p.text.strip())
    except ImportError:
        raise ImportError(
            "DOCX reading requires python-docx.\n"
            "Install with:  pip install python-docx"
        )


def _extract_text_from_file(path: str) -> str:
    ext = os.path.splitext(path)[1].lower()
    if ext in _IMAGE_EXTS:
        raise ValueError("Images are handled as vision input, not text extraction.")
    if ext == ".pdf":
        return _extract_text_from_pdf(path)
    if ext in (".docx", ".doc"):
        return _extract_text_from_docx(path)
    if ext in (".txt", ".md", ".csv", ".py", ".js", ".ts", ".html",
               ".css", ".json", ".xml", ".yaml", ".yml", ".rst"):
        with open(path, "r", encoding="utf-8", errors="ignore") as f:
            return f.read()
    raise ValueError(
        f"Unsupported file type: '{ext}'\n\n"
        "Supported documents: PDF, DOCX, TXT, MD, CSV, and common code files.\n"
        "Supported images: PNG, JPG, JPEG, GIF, BMP, WEBP."
    )


# ── File-dialog filter ─────────────────────────────────────────────────────────
_SUPPORTED_FILTERS = (
    "All Supported Files ("
    "*.pdf *.docx *.doc *.txt *.md *.csv "
    "*.py *.js *.ts *.html *.css *.json *.xml *.yaml *.yml *.rst "
    "*.png *.jpg *.jpeg *.gif *.bmp *.webp"
    ");;"
    "Documents (*.pdf *.docx *.doc *.txt *.md *.csv);;"
    "Images (*.png *.jpg *.jpeg *.gif *.bmp *.webp);;"
    "Code Files (*.py *.js *.ts *.html *.css *.json *.xml *.yaml *.yml *.rst);;"
    "All Files (*)"
)


# ── Document open / clear ──────────────────────────────────────────────────────

def open_document(self):
    """
    Open a file-picker and attach the chosen file to the next prompt.

    • Images  (png/jpg/jpeg/gif/bmp/webp)
          → loaded as QPixmap for the thumbnail chip.
            The original file PATH is stored so send_prompt() can read the raw
            bytes and base64-encode them for the vision API call.
    • PDFs, DOCX, text/code files
          → text is extracted (≤ 12 000 chars) and sent as document context.

    Clicking the button when a file is already attached clears it (toggle).
    """
    if getattr(self, 'attached_document', None):
        clear_document(self)
        return

    path, _ = QFileDialog.getOpenFileName(
        self, "Attach a File", "", _SUPPORTED_FILTERS
    )
    if not path:
        return

    filename = os.path.basename(path)
    ext      = os.path.splitext(path)[1].lower()

    # ── Branch A: IMAGE ───────────────────────────────────────────────────────
    if ext in _IMAGE_EXTS:
        pixmap = QPixmap(path)
        if pixmap.isNull():
            QMessageBox.critical(
                self, "Image Error",
                f"Could not load the image:\n{filename}\n\n"
                "The file may be corrupt or in an unsupported format."
            )
            return

        # Cap image file size at 20 MB to avoid accidentally huge payloads
        file_size = os.path.getsize(path)
        if file_size > 20 * 1024 * 1024:
            QMessageBox.warning(
                self, "Image Too Large",
                f"'{filename}' is {file_size // (1024*1024)} MB.\n"
                "Please use an image smaller than 20 MB."
            )
            return

        self.attached_document = {
            "filename":  filename,
            "path":      path,          # ← needed for base64 encoding in send_prompt
            "text":      "",
            "truncated": False,
            "is_image":  True,
            "pixmap":    pixmap,
        }

        print(colored(
            f"Image attached: {filename} ({pixmap.width()}×{pixmap.height()}, "
            f"{file_size // 1024} KB)",
            "cyan"
        ))

        for te in (self.ui.text_prompt, self.ui.text_prompt_2):
            te.set_attachment(self.attached_document)

        _set_attach_button_active(self, filename)
        return

    # ── Branch B: DOCUMENT / TEXT / CODE ─────────────────────────────────────
    for te in (self.ui.text_prompt, self.ui.text_prompt_2):
        te.show_loading(filename)

    from PyQt5.QtWidgets import QApplication
    QApplication.processEvents()

    try:
        text = _extract_text_from_file(path)
    except Exception as e:
        for te in (self.ui.text_prompt, self.ui.text_prompt_2):
            te.hide_loading()
        QMessageBox.critical(self, "File Read Error",
                             f"Could not read '{filename}':\n\n{e}")
        return

    for te in (self.ui.text_prompt, self.ui.text_prompt_2):
        te.hide_loading()

    if not text.strip():
        QMessageBox.warning(self, "Empty File",
                            f"'{filename}' appears to be empty or contains no readable text.")
        return

    MAX_CHARS = 80_000 # ~20k tokens
    truncated = len(text) > MAX_CHARS
    if truncated:
        text = text[:MAX_CHARS]

    self.attached_document = {
        "filename":  filename,
        "path":      path,
        "text":      text,
        "truncated": truncated,
        "is_image":  False,
        "pixmap":    None,
    }

    print(colored(f"Document attached: {filename} ({len(text)} chars)", "cyan"))

    for te in (self.ui.text_prompt, self.ui.text_prompt_2):
        te.set_attachment(self.attached_document)

    _set_attach_button_active(self, filename)

    if truncated:
        QMessageBox.information(
            self, "Document Truncated",
            f"'{filename}' was truncated to the first {MAX_CHARS:,} characters\n"
            "to fit within the AI context window."
        )


def clear_document(self):
    if self.attached_document:
        for te in (self.ui.text_prompt, self.ui.text_prompt_2):
            te.set_attachment(None)
        _set_attach_button_inactive(self)
        print(colored("Document detached", "yellow"))
    self.attached_document = None


def _set_attach_button_active(self, filename: str):
    tooltip = f"📎 {filename}\n(click to remove)"
    style   = """
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
        btn.setStyleSheet(style)
        btn.setToolTip(tooltip)


def _set_attach_button_inactive(self):
    style = """
        QPushButton {
            background: none;
            border: none;
            color: rgba(255, 255, 255, 180);
            border-radius: 21px;
            margin-top: 3px;
        }
        QPushButton:hover { background-color: rgb(45, 48, 58); }
    """
    for btn in (self.ui.addButton, self.ui.addButton_2):
        btn.setStyleSheet(style)
        btn.setToolTip("Attach a document or image")


# ── Auth helpers (unchanged) ──────────────────────────────────────────────────

def signup_update_ui(self):
    self.ui.signup_button.setEnabled(True)
    self.ui.label.setText('SIGN UP')
    self.ui.label.setStyleSheet('color:rgba(255, 255, 255, 180);')


@pyqtSlot(dict)
def handle_signup_response(self, response):
    code = response['status_code']
    self.ui.uname_lineEdit.setText('')
    self.ui.email_lineEdit.setText('')
    self.ui.pass_lineEdit.setText('')
    if code == 201:
        self.ui.info_label.setStyleSheet('color: rgb(0, 255, 127);')
        self.ui.info_label.setText('User registered, go to the login page!')
    elif code == 400:
        self.ui.info_label.setStyleSheet('color: rgb(255, 0, 0);')
        self.ui.info_label.setText("Invalid username, email or password")
    elif code == 409:
        self.ui.info_label.setStyleSheet('color: rgb(255, 0, 0);')
        self.ui.info_label.setText("User or email already exists")
    else:
        self.ui.info_label.setStyleSheet('color: rgb(255, 0, 0);')
        self.ui.info_label.setText("Internal server error")


def signup(self):
    username = self.ui.uname_lineEdit.text()
    email    = self.ui.email_lineEdit.text()
    password = self.ui.pass_lineEdit.text()
    pw_pat    = r'(?=.*[a-z])(?=.*[A-Z])(?=.*\W)'
    email_pat = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    self.ui.info_label.setStyleSheet('color:rgb(255, 0, 0);')
    if not username or not email or not password:
        self.ui.info_label.setText("username, email or password can't be empty")
    elif len(password) < 8:
        self.ui.info_label.setText("password must contain at least 8 characters")
    elif not re.search(pw_pat, password):
        self.ui.info_label.setText(
            "password must contain at least 1 upper case, lower case and a special symbol")
    elif not re.search(email_pat, email):
        self.ui.info_label.setText("Invalid Email address")
    else:
        payload = {"username": username, "email": email, "password": password}
        self.ui.signup_button.setEnabled(False)
        self.ui.label.setText('Signing up...')
        self.ui.label.setStyleSheet('color: rgb(0, 255, 127);')
        self.thread = WorkerThread(payload, 'POST', 'register')
        self.thread.data_fetched.connect(lambda r: handle_signup_response(self, r))
        self.thread.finished.connect(lambda: signup_update_ui(self))
        self.thread.start()


def login_update_ui(self):
    self.ui.login_button.setEnabled(True)
    self.ui.label_3.setText('LOG IN')
    self.ui.label_3.setStyleSheet('color:rgba(255, 255, 255, 180);')


def run_login(self):
    from auth.login_window import LoginWindow
    login  = LoginWindow(self)
    result = login.exec_()
    if result == QDialog.Accepted:
        self.ui.login_button.setText("")
        self.ui.login_button.setEnabled(False)


def after_verify_token(self, response):
    if response.get("status_code") == 200:
        username = response.get("user")
        email    = response.get("email")
        print(colored(f"Logged in user: {username}", 'green'))
        ss = "font-family:'Roboto'; font-size:10pt; color:green;"
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Reqs/user.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ui.login_button.setIcon(icon)
        self.ui.login_button.setText('   ' + username)
        self.ui.login_button.setToolTip('')
        self.ui.login_button.setStyleSheet(ss)
        self.ui.login_button.setEnabled(False)
        self.ui.logged_in_label.setText('Logged In')
        self.ui.logged_in_label.setStyleSheet(ss)
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
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    self.thread = WorkerThread(None, 'GET', 'verify_token', headers=headers)
    self.thread.data_fetched.connect(lambda r: callback(self, r))
    self.thread.start()


def verify_token(self):
    subprocess.run(["icacls", "auth_token.x", "/remove:d", "Everyone"], check=True)
    with open("auth_token.x", "r") as f:
        token = f.read()
    if token:
        verify_token_(self, token, after_verify_token)
    else:
        run_login(self)
    subprocess.run(["icacls", "auth_token.x", "/deny", "Everyone:(R)"], check=True)


@pyqtSlot(dict)
def handle_login_response(self, response, main_win):
    if 'token' in response:
        self.ui.uid_lineEdit_2.setText('')
        self.ui.pass_lineEdit_2.setText('')
        self.close()
        subprocess.run(["icacls", "auth_token.x", "/remove:d", "Everyone"], check=True)
        with open('auth_token.x', 'w', encoding='utf-8') as f:
            f.write(response['token'])
        subprocess.run(["icacls", "auth_token.x", "/deny", "Everyone:(R)"], check=True)
        print(colored('Verifying token!', 'magenta'))
        verify_token(main_win)
    else:
        self.ui.pass_lineEdit_2.setText('')
        self.ui.uid_lineEdit_2.setText('')
        self.ui.info_label2.setStyleSheet('color: rgb(255, 0, 0);')
        self.ui.info_label2.setText("Invalid credentials")


def login(self, main_win):
    self.ui.info_label.setText('')
    username = self.ui.uid_lineEdit_2.text()
    password = self.ui.pass_lineEdit_2.text()
    if not username or not password:
        self.ui.info_label2.setStyleSheet('color:rgb(255, 0, 0);')
        self.ui.info_label2.setText("username or password can't be empty")
    else:
        payload = {"username": username, "password": password}
        self.ui.login_button.setEnabled(False)
        self.ui.label_3.setText('Signing in...')
        self.ui.label_3.setStyleSheet('color: rgb(0, 255, 127);')
        self.thread = WorkerThread(payload, 'POST', 'login')
        self.thread.data_fetched.connect(lambda r: handle_login_response(self, r, main_win))
        self.thread.finished.connect(lambda: login_update_ui(self))
        self.thread.start()


def update_preference_button(self):
    self.ui.button_save.setText('Save')
    self.ui.button_save.setEnabled(True)


@pyqtSlot(dict)
def handle_preference_response(self, response):
    if 'saved' in response['message']:
        from ui_controllers.show_message import messageWindow
        messageWindow(self).exec_()


def save_user_preferences(self):
    self.ui.button_save.setText('Saving...')
    self.ui.button_save.setEnabled(False)
    subprocess.run(["icacls", "auth_token.x", "/remove:d", "Everyone"], check=True)
    with open('auth_token.x', 'r', encoding='utf-8') as f:
        self.jwt_token = f.read()
    subprocess.run(["icacls", "auth_token.x", "/deny", "Everyone:(R)"], check=True)
    payload = {
        "learning_style":     self.ui.learning_type.currentText(),
        "difficulty_level":   self.ui.difficulty_type.currentText(),
        "preferred_task":     self.ui.preferred_output.currentText(),
        "daily_goal_minutes": (self.ui.spinHour.value() * 60) + self.ui.spinMinute.value(),
    }
    headers = {"Authorization": f"Bearer {self.jwt_token}", "Content-Type": "application/json"}
    self.thread = WorkerThread(payload, 'POST', 'preferences', headers=headers)
    self.thread.data_fetched.connect(lambda r: handle_preference_response(self, r))
    self.thread.finished.connect(lambda: update_preference_button(self))
    self.thread.start()


def handle_token_expired(main_window):
    run_login(main_window)


@pyqtSlot(dict)
def get_preference_response(self, response):
    if response['status_code'] == 200:
        self.ui.learning_type.setCurrentText(response["learning_style"])
        self.ui.difficulty_type.setCurrentText(response["difficulty_level"])
        self.ui.preferred_output.setCurrentText(response["preferred_task"])
        self.ui.spinHour.setValue(response["daily_goal_minutes"] // 60)
        self.ui.spinMinute.setValue(response["daily_goal_minutes"] % 60)
    elif response['status_code'] == 404:
        pass
    else:
        handle_token_expired(self)


def get_user_preferences(self):
    subprocess.run(["icacls", "auth_token.x", "/remove:d", "Everyone"], check=True)
    with open('auth_token.x', 'r', encoding='utf-8') as f:
        self.jwt_token = f.read()
    subprocess.run(["icacls", "auth_token.x", "/deny", "Everyone:(R)"], check=True)
    headers = {"Authorization": f"Bearer {self.jwt_token}", "Content-Type": "application/json"}
    self.thread = WorkerThread(None, 'GET', 'preferences', headers=headers)
    self.thread.data_fetched.connect(lambda r: get_preference_response(self, r))
    self.thread.start()


# ── Streaming ──────────────────────────────────────────────────────────────────

def get_prompt_stream(self, chunk):
    if not hasattr(self, "full_text"):
        self.full_text = ""
    self.full_text += chunk.replace("<<NEWLINE>>", "\n")
    self.ai_bubble.append_stream(self.full_text)
    if not getattr(self, '_scroll_pending', False):
        self._scroll_pending = True
        QTimer.singleShot(100, lambda: _do_scroll(self))


def _do_scroll(self):
    self._scroll_pending = False
    self.chat_area.scroll_to_bottom()


def finalize_stream(self):
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
    search_icon.addPixmap(QtGui.QPixmap("Reqs/search.png"),
                          QtGui.QIcon.Normal, QtGui.QIcon.Off)
    self.ui.text_prompt_2.search_btn.setIcon(search_icon)
    self.ui.text_prompt_2.search_btn.setIconSize(QSize(24, 24))
    self.ui.text_prompt.search_btn.setIcon(search_icon)
    self.ui.text_prompt.search_btn.setIconSize(QSize(24, 24))
    clear_document(self)
    load_chat_history(self)


def stop_prompt(self):
    chat_id = getattr(self, 'current_chat_id', None)
    if not chat_id:
        return
    self._stream_stopped = True
    headers = {}
    token = getattr(self, 'jwt_token', '')
    if token:
        headers["Authorization"] = f"Bearer {token}"
    try:
        requests.post('http://localhost:5000/prompt/stop',
                      json={"chat_id": chat_id}, headers=headers, timeout=3)
    except requests.exceptions.RequestException:
        pass
    _on_stream_stopped(self)


def _on_stream_stopped(self):
    self._is_streaming   = False
    self._scroll_pending = False
    if hasattr(self, 'full_text') and self.full_text:
        self.ai_bubble.finish_stream(self.full_text)
    self.chat_area.scroll_to_bottom()
    search_icon = QtGui.QIcon()
    search_icon.addPixmap(QtGui.QPixmap("Reqs/search.png"),
                          QtGui.QIcon.Normal, QtGui.QIcon.Off)
    self.ui.text_prompt_2.search_btn.setIcon(search_icon)
    self.ui.text_prompt_2.search_btn.setIconSize(QSize(24, 24))
    self.ui.text_prompt.search_btn.setIcon(search_icon)
    self.ui.text_prompt.search_btn.setIconSize(QSize(24, 24))
    clear_document(self)


def send_prompt(self):
    from ui.widgets.chat_bubble import ChatBubble

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
    self.ui.text_prompt.reset_height()
    self.ui.text_prompt_2.clear()
    self.ui.text_prompt_2.reset_height()

    self._is_streaming = True

    stop_icon = QtGui.QIcon()
    stop_icon.addPixmap(QtGui.QPixmap("Reqs/stop.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
    self.ui.text_prompt_2.search_btn.setIcon(stop_icon)
    self.ui.text_prompt_2.search_btn.setIconSize(QSize(32, 32))
    self.ui.text_prompt.search_btn.setIcon(stop_icon)
    self.ui.text_prompt.search_btn.setIconSize(QSize(32, 32))

    if not getattr(self, 'current_chat_id', None):
        self.current_chat_id = str(uuid.uuid4())

    chat_width = self.chat_area.width()

    doc = getattr(self, 'attached_document', None)
    user_bubble = ChatBubble(text, is_user=True,
                             available_width=chat_width, attachment=doc)
    self.chat_area.add_bubble(user_bubble)

    for te in (self.ui.text_prompt, self.ui.text_prompt_2):
        te.set_attachment(None)

    self.ai_bubble = ChatBubble("", is_user=False, available_width=chat_width)
    self.ai_bubble.start_stream()
    self.chat_area.add_bubble(self.ai_bubble)

    # ── Build payload ───────────────────────────────────────────────────────
    payload = {
        "prompt_text": text,
        "prompt_type": self.ui.preferred_output.currentText().lower(),
        "chat_id":     self.current_chat_id,
    }

    if doc:
        payload["document_name"] = doc["filename"]

        if doc.get("is_image"):
            # ── Vision: read the file, base64-encode, send to backend ──────
            img_path = doc.get("path", "")
            ext      = os.path.splitext(img_path)[1].lower()
            mime     = _MIME_TYPES.get(ext, "image/png")

            try:
                with open(img_path, "rb") as img_file:
                    b64_data = base64.b64encode(img_file.read()).decode("utf-8")
                payload["document_image_b64"]  = b64_data
                payload["document_image_mime"] = mime
                print(colored(
                    f"Image encoded: {doc['filename']} "
                    f"({len(b64_data) // 1024} KB base64)", "cyan"))
            except Exception as e:
                print(colored(f"Failed to encode image: {e}", "red"))
                # Fall back to a text note so the request still works
                payload["document_text"] = (
                    f"[User attached an image '{doc['filename']}' "
                    "but it could not be read from disk.]"
                )
        else:
            # ── Document: send extracted text ──────────────────────────────
            payload["document_text"] = doc["text"]

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


# ── Chat history ───────────────────────────────────────────────────────────────

def load_chat_history(self):
    token = getattr(self, 'jwt_token', '')
    if not token:
        return
    headers = {"Authorization": f"Bearer {token}"}
    self.chat_history_thread = WorkerThread(None, 'GET', 'chats', headers=headers)
    self.chat_history_thread.data_fetched.connect(
        lambda r: _populate_chat_history(self, r))
    self.chat_history_thread.start()


def _populate_chat_history(self, response):
    if response.get('status_code') != 200:
        return
    chats = response.get('chats', [])
    lw    = self.ui.chat_history
    lw.clear()
    for chat in chats:
        item = QtWidgets.QListWidgetItem(chat['title'])
        item.setData(Qt.UserRole, chat['chat_id'])
        item.setToolTip(chat['title'])
        lw.addItem(item)


def on_chat_history_item_clicked(self, item):
    chat_id = item.data(Qt.UserRole)
    if not chat_id:
        return
    token   = getattr(self, 'jwt_token', '')
    headers = {"Authorization": f"Bearer {token}"}
    self.load_chat_thread = WorkerThread(None, 'GET', f'chat/{chat_id}', headers=headers)
    self.load_chat_thread.data_fetched.connect(lambda r: _render_loaded_chat(self, r))
    self.load_chat_thread.start()


def _render_loaded_chat(self, response):
    clear_document(self)
    if response.get('status_code') != 200:
        return
    from ui.widgets.chat_bubble import ChatBubble
    self.ui.stackedWidget.setCurrentWidget(self.ui.conversation_page)
    self.clear_chat()
    chat_id    = response['chat_id']
    messages   = response.get('messages', [])
    chat_width = self.chat_area.width()
    for msg in messages:
        is_user    = msg['role'] == 'user'
        attachment = None
        if is_user:
            doc_name = msg.get('document_name')
            if doc_name:
                ext        = os.path.splitext(doc_name)[1].lower()
                attachment = {
                    "filename":  doc_name,
                    "path":      "",
                    "pixmap":    None,
                    "is_image":  ext in _IMAGE_EXTS,
                    "text":      "",
                    "truncated": False,
                }
        bubble = ChatBubble(msg['text'], is_user=is_user,
                            available_width=chat_width, attachment=attachment)
        self.chat_area.add_bubble(bubble)
    self.current_chat_id = chat_id
    self.chat_area.scroll_to_bottom()


# ── Context menu ───────────────────────────────────────────────────────────────

def _show_chat_context_menu(self, position):
    from PyQt5.QtWidgets import QMenu, QAction
    item = self.ui.chat_history.itemAt(position)
    if not item:
        return
    chat_id       = item.data(Qt.UserRole)
    current_title = item.text()
    menu = QMenu(self.ui.chat_history)
    menu.setStyleSheet("""
        QMenu {
            background-color: rgb(43,47,58); color:rgba(255,255,255,200);
            border:1px solid rgba(255,255,255,30); border-radius:6px;
            padding:4px; font-family:'Roboto'; font-size:10pt;
        }
        QMenu::item{padding:8px 20px;border-radius:4px;}
        QMenu::item:selected{background-color:rgb(55,62,76);color:white;}
        QMenu::separator{height:1px;background:rgba(255,255,255,20);margin:3px 8px;}
    """)
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
    from PyQt5.QtWidgets import QInputDialog
    dialog = QInputDialog(self.ui.chat_history)
    dialog.setWindowTitle("Rename Chat")
    dialog.setLabelText("New name:")
    dialog.setTextValue(current_title)
    dialog.setStyleSheet("""
        QInputDialog,QDialog{background-color:rgb(35,38,47);}
        QLabel{color:rgba(255,255,255,180);font-family:'Roboto';font-size:10pt;}
        QLineEdit{background-color:rgb(41,44,53);color:white;
            border:2px solid rgb(85,170,255);border-radius:6px;
            padding:6px 12px;font-family:'Roboto';font-size:10pt;}
        QPushButton{background-color:rgb(48,53,65);color:rgba(255,255,255,200);
            border:1px solid rgba(255,255,255,40);border-radius:6px;
            padding:6px 16px;font-family:'Roboto';font-size:9pt;min-width:70px;}
        QPushButton:hover{background-color:rgb(55,62,76);
            border:1px solid rgb(85,170,255);}
    """)
    ok        = dialog.exec_()
    new_title = dialog.textValue().strip()
    if not ok or not new_title or new_title == current_title:
        return
    token   = getattr(self, 'jwt_token', '')
    headers = {"Authorization": f"Bearer {token}"}
    self.rename_thread = WorkerThread(
        {"title": new_title}, 'PATCH', f'chat/{chat_id}', headers=headers)
    def on_renamed(r):
        if r.get('status_code') == 200:
            item.setText(new_title)
            item.setToolTip(new_title)
    self.rename_thread.data_fetched.connect(on_renamed)
    self.rename_thread.start()


def _delete_chat_confirm(self, item, chat_id):
    from ui_controllers.show_confirm_dialog import ConfirmDialog
    dialog = ConfirmDialog()
    if dialog.exec_() != QDialog.Accepted:
        return
    token   = getattr(self, 'jwt_token', '')
    headers = {"Authorization": f"Bearer {token}"}
    self.delete_thread = WorkerThread(
        None, 'DELETE', f'chat/{chat_id}', headers=headers)
    def on_deleted(r):
        if r.get('status_code') == 200:
            row = self.ui.chat_history.row(item)
            self.ui.chat_history.takeItem(row)
            if getattr(self, 'current_chat_id', None) == chat_id:
                self.handle_new_chat()
    self.delete_thread.data_fetched.connect(on_deleted)
    self.delete_thread.start()