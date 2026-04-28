from PyQt5.QtWidgets import QWidget, QLabel, QHBoxLayout, QVBoxLayout, QFrame, QSizePolicy, QTextBrowser
from PyQt5.QtCore import Qt
import markdown

class ChatBubble(QWidget):
    def __init__(self, text="", is_user=False):
        super().__init__()
    
        self.layout = QHBoxLayout()
        self.setLayout(self.layout)

        self.bubble = QFrame()
        self.bubble_layout = QVBoxLayout()
        self.bubble.setLayout(self.bubble_layout)

        self.label = QTextBrowser()
        self.label.setPlainText(text)
        self.label.setFrameShape(QTextBrowser.NoFrame)
        self.label.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.label.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        html = f"""
        <style>
        pre {{
            background-color: #1e1e1e;
            padding: 10px;
            border-radius: 6px;
            overflow-x: auto;
        }}
        code {{
            font-family: Consolas;
            font-size: 12px;
            color: #dcdcdc;
        }}
        </style>
        """
        # self.label.setAlignment(Qt.AlignLeft | Qt.AlignTop)

        self.bubble_layout.addWidget(self.label)
        
        self.adjust_height()

        if is_user:
            self.bubble.setStyleSheet("""
                background-color: #007AFF;
                color: white;
                border-radius: 10px;
                padding: 8px;
            """)
            self.bubble.setMaximumWidth(400)

            self.layout.addStretch()
            self.layout.addWidget(self.bubble, 0, Qt.AlignRight)

        else:
            self.bubble.setStyleSheet("""
                background-color: #2d2d2d;
                color: white;
                border-radius: 10px;
                padding: 8px;
            """)
            self.bubble.setMinimumWidth(700)
            self.bubble.setMaximumWidth(900)

            self.layout.addWidget(self.bubble, 0, Qt.AlignLeft)
            self.layout.addStretch()

    def append_text(self, text):
        current = self.label.text()
        self.label.setText(current + text)
    
    def adjust_height(self):
        doc_height = self.label.document().size().height()
        self.label.setFixedHeight(int(doc_height + 10))