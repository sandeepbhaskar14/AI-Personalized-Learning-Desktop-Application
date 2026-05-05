from PyQt5.QtWidgets import (
    QWidget, QTextEdit, QVBoxLayout, QHBoxLayout,
    QLabel, QPushButton, QFrame, QSizePolicy
)
from PyQt5.QtCore import Qt, pyqtSignal, QEvent
from PyQt5.QtGui import QFont, QPixmap, QPainter, QPainterPath, QColor

import os


# ─────────────────────────────────────────────────────────────────────────────
# Helper: rounded-corner thumbnail
# ─────────────────────────────────────────────────────────────────────────────
def _rounded_pixmap(pixmap: QPixmap, radius: int = 8) -> QPixmap:
    result = QPixmap(pixmap.size())
    result.fill(Qt.transparent)
    painter = QPainter(result)
    painter.setRenderHint(QPainter.Antialiasing)
    path = QPainterPath()
    path.addRoundedRect(0, 0, pixmap.width(), pixmap.height(), radius, radius)
    painter.setClipPath(path)
    painter.drawPixmap(0, 0, pixmap)
    painter.end()
    return result


# ─────────────────────────────────────────────────────────────────────────────
# Attachment chip  (thumbnail / ext badge  +  filename  +  ✕)
# ─────────────────────────────────────────────────────────────────────────────
class _AttachChip(QFrame):
    remove_requested = pyqtSignal()

    def __init__(self, filename: str, pixmap: QPixmap | None = None, parent=None):
        super().__init__(parent)
        self.setStyleSheet("""
            QFrame {
                background-color: rgb(58, 63, 78);
                border-radius: 10px;
                border: none;
            }
        """)
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        row = QHBoxLayout(self)
        row.setContentsMargins(8, 6, 8, 6)
        row.setSpacing(8)

        # ── Thumbnail or extension badge ──────────────────────────────────────
        thumb = QLabel()
        thumb.setAlignment(Qt.AlignCenter)
        if pixmap and not pixmap.isNull():
            scaled = pixmap.scaled(72, 56, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            thumb.setPixmap(_rounded_pixmap(scaled, 6))
            thumb.setFixedSize(72, 56)
        else:
            ext = os.path.splitext(filename)[1].upper().lstrip('.') or "FILE"
            thumb.setText(ext)
            thumb.setFixedSize(52, 44)
            thumb.setStyleSheet("""
                background-color: rgb(80, 90, 115);
                border-radius: 8px;
                color: rgba(255,255,255,220);
                font-size: 10px;
                font-family: 'Roboto';
                font-weight: bold;
            """)
        row.addWidget(thumb)

        # ── Filename ──────────────────────────────────────────────────────────
        lbl = QLabel()
        lbl.setStyleSheet("""
            color: rgba(255,255,255,200);
            font-family: 'Roboto';
            font-size: 9pt;
            background: transparent;
            border: none;
        """)
        fm      = lbl.fontMetrics()
        elided  = fm.elidedText(filename, Qt.ElideMiddle, 150)
        lbl.setText(elided)
        lbl.setToolTip(filename)
        row.addWidget(lbl)

        # ── Remove button ─────────────────────────────────────────────────────
        btn = QPushButton("✕")
        btn.setFixedSize(20, 20)
        btn.setCursor(Qt.PointingHandCursor)
        btn.setStyleSheet("""
            QPushButton {
                background: rgba(255,255,255,25);
                color: rgba(255,255,255,150);
                border-radius: 10px;
                font-size: 9px;
                border: none;
            }
            QPushButton:hover {
                background: rgb(232, 0, 116);
                color: white;
            }
        """)
        btn.clicked.connect(self.remove_requested)
        row.addWidget(btn)

        self.adjustSize()


# ─────────────────────────────────────────────────────────────────────────────
# Bare inner QTextEdit — thin, no height logic
# ─────────────────────────────────────────────────────────────────────────────
class _InnerEdit(QTextEdit):
    def __init__(self, parent=None):
        super().__init__(parent)
        font = QFont("Roboto", 10)
        self.setFont(font)
        self._default_font = font
        self.setLineWrapMode(QTextEdit.WidgetWidth)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setFrameShape(QTextEdit.NoFrame)
        self.document().setDocumentMargin(2)
        self.setStyleSheet("""
            QTextEdit {
                background: transparent;
                color: rgba(255,255,255,210);
                border: none;
                padding: 0px;
            }
        """)

    def keyPressEvent(self, event):
        if event.key() in (Qt.Key_Return, Qt.Key_Enter):
            if event.modifiers() & Qt.ShiftModifier:
                super().keyPressEvent(event)
            else:
                event.ignore()
            return
        super().keyPressEvent(event)


# ─────────────────────────────────────────────────────────────────────────────
# PUBLIC  AutoGrowTextEdit
# ─────────────────────────────────────────────────────────────────────────────
class AutoGrowTextEdit(QWidget):
    """
    Composite input widget:
        ┌──────────────────────────────────────┐
        │  [thumb/ext]  filename.pdf    ✕      │  ← attachment strip (optional)
        │                                      │
        │  Ask Anything…                       │  ← _InnerEdit
        └──────────────────────────────────────┘

    Signals
    -------
    total_height_changed(int)
        Emitted every time the widget's own height changes.
        Connect this in main.py to resize the parent frame so the
        chat area shrinks (conversation page) or the box grows down
        (new-chat page).
    """

    total_height_changed = pyqtSignal(int)

    _TEXT_MIN  = 44      # minimum inner edit height (px)
    _TEXT_MAX  = 130     # max before scroll kicks in
    _STRIP_H   = 76      # height of the attachment strip row
    _V_PAD     = 20      # total vertical padding inside the frame

    # ── Stylesheet templates ──────────────────────────────────────────────────
    _SS_NORMAL = """
QFrame#inputFrame {{
    border: 2px solid rgb(41, 44, 53);
    border-radius: {r}px;
    background-color: rgb(41, 44, 53);
}}
QFrame#inputFrame:hover {{
    border: 2px solid rgb(220, 0, 220);
}}
"""
    _SS_FOCUS = """
QFrame#inputFrame {{
    border: 2px solid rgb(85, 170, 255);
    border-radius: {r}px;
    background-color: rgb(41, 44, 53);
}}
"""
    _RADIUS = 22

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        self._attachment = None
        self._chip: _AttachChip | None = None

        # ── Rounded frame ─────────────────────────────────────────────────────
        self._frame = QFrame(self)
        self._frame.setObjectName("inputFrame")
        self._frame.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self._frame.setStyleSheet(self._SS_NORMAL.format(r=self._RADIUS))

        # ── Frame inner layout: strip (hidden) + text ─────────────────────────
        self._flayout = QVBoxLayout(self._frame)
        self._flayout.setContentsMargins(14, 8, 14, 8)
        self._flayout.setSpacing(6)

        # Attachment strip row
        self._strip = QWidget()
        self._strip.setFixedHeight(self._STRIP_H)
        self._strip.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sl = QHBoxLayout(self._strip)
        sl.setContentsMargins(0, 0, 0, 0)
        sl.setSpacing(0)
        self._strip.hide()
        self._flayout.addWidget(self._strip)

        # Text edit
        self._edit = _InnerEdit(self._frame)
        self._edit.setFixedHeight(self._TEXT_MIN)
        self._edit.setPlaceholderText("Ask Anything")
        self._flayout.addWidget(self._edit)

        # Outer layout
        ol = QVBoxLayout(self)
        ol.setContentsMargins(0, 0, 0, 0)
        ol.addWidget(self._frame)

        self.setFixedHeight(self._TEXT_MIN + self._V_PAD)

        # ── Signals ───────────────────────────────────────────────────────────
        self._edit.document().documentLayout().documentSizeChanged.connect(
            self._on_doc_changed
        )
        self._edit.installEventFilter(self)   # for focus border

    # ── Focus border via event filter ─────────────────────────────────────────
    def eventFilter(self, obj, event):
        if obj is self._edit:
            if event.type() == QEvent.FocusIn:
                self._frame.setStyleSheet(self._SS_FOCUS.format(r=self._RADIUS))
            elif event.type() == QEvent.FocusOut:
                self._frame.setStyleSheet(self._SS_NORMAL.format(r=self._RADIUS))
        return super().eventFilter(obj, event)

    # ── QTextEdit-compatible public API ───────────────────────────────────────
    def toPlainText(self) -> str:
        return self._edit.toPlainText()

    def clear(self):
        self._edit.clear()
        self._edit.setFont(self._edit._default_font)
        self._set_edit_h(self._TEXT_MIN)

    def setPlaceholderText(self, text: str):
        self._edit.setPlaceholderText(text)

    def installEventFilter(self, obj):       # let StickyButton observe resizes
        super().installEventFilter(obj)

    def setFocus(self):
        self._edit.setFocus()

    def reset_height(self):
        """Snap back to minimum height — call after clear()."""
        self._set_edit_h(self._TEXT_MIN)

    # ── Attachment API ─────────────────────────────────────────────────────────
    def set_attachment(self, attachment: dict | None):
        """
        attachment dict keys used here:
            "filename" : str
            "pixmap"   : QPixmap | None   (only for images)
        Pass None to clear.
        """
        # Tear down old chip
        if self._chip:
            self._chip.setParent(None)
            self._chip = None

        self._attachment = attachment

        strip_layout = self._strip.layout()
        # Clear strip layout
        while strip_layout.count():
            item = strip_layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()

        if attachment:
            chip = _AttachChip(
                attachment["filename"],
                attachment.get("pixmap"),
                parent=self._strip,
            )
            chip.remove_requested.connect(self._on_remove)
            strip_layout.addWidget(chip)
            strip_layout.addStretch()
            self._chip = chip
            self._strip.show()
        else:
            self._strip.hide()

        self._recalc()

    def _on_remove(self):
        """✕ clicked — clear attachment and notify window."""
        self.set_attachment(None)
        win = self.window()
        if win and hasattr(win, "attached_document"):
            win.attached_document = None
            try:
                from services.handle_requests import _set_attach_button_inactive
                _set_attach_button_inactive(win)
            except ImportError:
                pass

    # ── Height logic ──────────────────────────────────────────────────────────
    def _on_doc_changed(self, _=None):
        doc_h = self._edit.document().size().height()
        cm    = self._edit.contentsMargins()
        raw   = int(doc_h + cm.top() + cm.bottom() + 6)
        self._set_edit_h(max(self._TEXT_MIN, min(raw, self._TEXT_MAX)))

    def _set_edit_h(self, h: int):
        if self._edit.height() != h:
            self._edit.setFixedHeight(h)
        self._recalc()

    def _recalc(self):
        strip_h = (self._STRIP_H + self._flayout.spacing()) if self._attachment else 0
        cm      = self._flayout.contentsMargins()
        total   = (strip_h + self._edit.height()
                   + cm.top() + cm.bottom())
        self.setFixedHeight(total)
        self.total_height_changed.emit(total)