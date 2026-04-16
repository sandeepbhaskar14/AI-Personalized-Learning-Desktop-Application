from PyQt5.QtWidgets import QTextEdit
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QTextCursor, QFont


class AutoGrowTextEdit(QTextEdit):
    def __init__(self, parent=None):
        super().__init__(parent)

        # ---- Configuration ----
        self.min_height = 50
        self.max_height = 200
        self.first_expand_px = 10
        self.bottom_padding_px = 30

        self._is_expanded = False
        
        font = QFont("Roboto", 10)
        font.setPointSize(10)
        self.setFont(font)
        self._default_font = font

        self.setLineWrapMode(QTextEdit.WidgetWidth)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)

        # Default height on window open
        self.setFixedHeight(self.min_height)

        # Default style (single line)
        self._normal_style = """
        QTextEdit{
            border:2px solid rgb(41, 44, 53);
            border-radius:22px;
            background-color: rgb(41, 44, 53);
            color:rgba(255, 255, 255, 210);
            padding: 8px 15px 6px 50px;
        }
        QTextEdit:hover{
            border:2px solid rgb(220, 0, 220);
        }
        QTextEdit:focus{
            border:2px solid rgb(85,170,255);
        }
        """

        # Expanded style (2+ lines)
        self._expanded_style = f"""
QTextEdit{{
    border:2px solid rgb(41, 44, 53);
    border-radius:22px;
    background-color: rgb(41, 44, 53);
    color:rgba(255, 255, 255, 210);
    padding: 8px 15px {self.bottom_padding_px}px 50px;
}}
QTextEdit:hover{{
    border:2px solid rgb(220, 0, 220);
}}
QTextEdit:focus{{
    border:2px solid rgb(85,170,255);
}}
"""
        

        self.setStyleSheet(self._normal_style)

        self.document().documentLayout().documentSizeChanged.connect(
            self.adjust_height
        )

    def keyPressEvent(self, event):
        if event.key() in (Qt.Key_Return, Qt.Key_Enter):
            # Shift + Enter → allow new line
            if event.modifiers() & Qt.ShiftModifier:
                super().keyPressEvent(event)
                return
            # Enter alone → ignore
            event.ignore()
            return

        super().keyPressEvent(event)
        
    def _reset_cursor_format(self):
        cursor = self.textCursor()
        cursor.select(QTextCursor.Document)
        cursor.setCharFormat(QTextCursor().charFormat())
        cursor.clearSelection()
        cursor.setCharFormat(self._default_font)
        self.setTextCursor(cursor)

    def adjust_height(self):
        if not self.toPlainText():
            self.setCurrentCharFormat(QTextCursor().charFormat())
            self.setFont(self._default_font)
        
        block_count = self.document().blockCount()

        # ---- Padding logic (ONLY when 2 lines exist) ----
        if block_count >= 2 and not self._is_expanded:
            self.setStyleSheet(self._expanded_style)
            self._is_expanded = True

        elif block_count == 1 and self._is_expanded:
            self.setStyleSheet(self._normal_style)
            self._is_expanded = False
            self.setFixedHeight(self.min_height)
            return

        # ---- Height calculation ----
        doc_height = self.document().size().height()
        margins = self.contentsMargins()
        extra = margins.top() + margins.bottom()

        new_height = int(doc_height + extra + self.first_expand_px)
        new_height = max(self.min_height, min(new_height, self.max_height))

        self.setFixedHeight(new_height)
