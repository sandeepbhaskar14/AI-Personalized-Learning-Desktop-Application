from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QVBoxLayout,
                              QFrame, QSizePolicy, QTextBrowser,
                              QScrollArea)
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QFont, QFontMetrics
import markdown
from markdown.extensions.codehilite import CodeHiliteExtension
from markdown.extensions.fenced_code import FencedCodeExtension


PYGMENTS_CSS = """
<style>
* { box-sizing: border-box; }
body {
    color: rgba(255,255,255,220);
    font-family: 'Roboto', sans-serif;
    font-size: 10pt;
    margin: 0; padding: 0;
    background: transparent;
}
p { margin: 0 0 6px 0; line-height: 1.45; }
p:last-child { margin-bottom: 0; }
h1,h2,h3,h4 { color: rgba(255,255,255,230); margin: 8px 0 3px 0; line-height: 1.3; }
ul,ol { margin: 2px 0 6px 0; padding-left: 20px; }
li { margin: 1px 0; line-height: 1.45; }
strong { color: white; }
em { color: rgba(255,255,255,180); }
p code, li code {
    font-family: 'Consolas', monospace; font-size: 9.5pt;
    background-color: #1e1e2e; color: #e8e8e8;
    padding: 1px 5px; border-radius: 3px;
}
.codehilite {
    display: block; background-color: #0d1117 !important;
    border-left: 3px solid #4a9eff; border-radius: 8px;
    padding: 0; margin: 6px 0;
}
.codehilite pre {
    display: block; background-color: #0d1117 !important;
    color: #d4d4d4; font-family: 'Consolas', 'Courier New', monospace;
    font-size: 9.5pt; margin: 0; padding: 12px 14px;
    white-space: pre-wrap; word-wrap: break-word; border-radius: 8px;
}
.codehilite .c,.codehilite .c1,.codehilite .cm,
.codehilite .cp,.codehilite .cs { color: #6a9955; }
.codehilite .k,.codehilite .kc,.codehilite .kd,
.codehilite .kn,.codehilite .kp,.codehilite .kr { color: #569cd6; }
.codehilite .kt  { color: #4ec9b0; }
.codehilite .m,.codehilite .mb,.codehilite .mf,
.codehilite .mh,.codehilite .mi,.codehilite .mo { color: #b5cea8; }
.codehilite .s,.codehilite .s1,.codehilite .s2,
.codehilite .sa,.codehilite .sb,.codehilite .sc,
.codehilite .dl,.codehilite .sh,.codehilite .si,
.codehilite .sx { color: #ce9178; }
.codehilite .sd { color: #6a9955; }
.codehilite .se { color: #d7ba7d; }
.codehilite .sr { color: #d16969; }
.codehilite .na { color: #9cdcfe; }
.codehilite .nb { color: #4ec9b0; }
.codehilite .nc { color: #4ec9b0; }
.codehilite .nd { color: #dcdcaa; }
.codehilite .ne { color: #f44747; }
.codehilite .nf { color: #dcdcaa; }
.codehilite .n,.codehilite .ni,.codehilite .nl,
.codehilite .nv { color: #9cdcfe; }
.codehilite .nn { color: #4ec9b0; }
.codehilite .nt { color: #569cd6; }
.codehilite .o,.codehilite .ow { color: #569cd6; }
.codehilite .p,.codehilite .w { color: #d4d4d4; }
</style>
"""


def build_html(text):
    body = markdown.markdown(
        text,
        extensions=[
            FencedCodeExtension(),
            CodeHiliteExtension(
                guess_lang=True,
                noclasses=False,
                linenums=False,
                pygments_style='default'
            ),
            'tables',
        ]
    )
    return PYGMENTS_CSS + body


def _get_scroll_area_viewport_width(widget):
    """
    Walk up the parent chain to find the QScrollArea and return
    its viewport width — the true usable width for chat bubbles.
    Returns None if not found.
    """
    p = widget.parent()
    while p is not None:
        if isinstance(p, QScrollArea):
            vw = p.viewport().width()
            # Subtract scrollbar width (typically 8px from stylesheet)
            return max(vw - 10, 100)
        p = p.parent()
    return None


class ChatBubble(QWidget):
    _FONT = QFont("Roboto", 10)

    def __init__(self, text="", is_user=False, available_width=800):
        super().__init__()
        self.is_user = is_user
        self._available_width = available_width  # fallback only
        self._user_text = text if is_user else ""
        self._shown_once = False
        self._streaming = False

        self._height_timer = QTimer(self)
        self._height_timer.setSingleShot(True)
        self._height_timer.setInterval(150)
        self._height_timer.timeout.connect(self._do_adjust_height)

        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)

        outer = QHBoxLayout(self)
        outer.setContentsMargins(10, 4, 10, 4)
        outer.setSpacing(0)

        self.bubble = QFrame()
        self.bubble.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        bubble_layout = QVBoxLayout(self.bubble)
        bubble_layout.setContentsMargins(12, 10, 12, 10)
        bubble_layout.setSpacing(0)

        self.label = QTextBrowser()
        self.label.setOpenExternalLinks(True)
        self.label.setFrameShape(QTextBrowser.NoFrame)
        self.label.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.label.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.label.setMinimumHeight(36)
        self.label.document().setDocumentMargin(2)
        bubble_layout.addWidget(self.label)

        if is_user:
            self.bubble.setStyleSheet(
                "QFrame { background-color: #1a56a0; border-radius: 12px; }")
            self.label.setStyleSheet(
                "QTextBrowser { color: white; background: transparent; "
                "font-family: Roboto; font-size: 10pt; border: none; }")

            spacer = QWidget()
            spacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
            outer.addWidget(spacer, 1)
            outer.addWidget(self.bubble, 0)
            self.bubble.setMaximumWidth(550)
            # self.bubble.setMaximumHeight(50)

            if text:
                self.label.setPlainText(text)
                # Set a safe initial height — will be corrected in showEvent
                self._set_user_height_with_width(text, available_width)

        else:
            self.bubble.setStyleSheet(
                "QFrame { background-color: #2d3240; border-radius: 12px; }")
            self.label.setStyleSheet(
                "QTextBrowser { color: rgba(255,255,255,220); "
                "background: transparent; font-family: Roboto; "
                "font-size: 10pt; border: none; }")
            outer.addWidget(self.bubble, 1)

            if text:
                self.label.setHtml(build_html(text))
                QTimer.singleShot(0, self._do_adjust_height)

    def _set_user_height_with_width(self, text, container_width):
        """
        Calculate user bubble height given a known container width.
        MAX_BUBBLE=550, subtract all padding layers to get inner text width.

        container_width: the QScrollArea viewport width (most accurate)
                         or chat_area.width() (fallback)
        """
        MAX_BUBBLE = 550
        # Layers subtracted from container_width to reach inner text area:
        #   outer QHBoxLayout margins: left=10, right=10  → 20
        #   bubble QVBoxLayout padding: left=12, right=12  → 24
        #   QTextBrowser doc margin: 2+2                   → 4
        #   safety buffer                                   → 4
        # Total: 52
        TOTAL_PADDING = 52

        bubble_w = min(container_width, MAX_BUBBLE)
        inner_w  = max(bubble_w - TOTAL_PADDING, 60)

        fm   = QFontMetrics(self._FONT)
        rect = fm.boundingRect(
            0, 0, inner_w, 100_000,
            Qt.TextWordWrap | Qt.AlignLeft,
            text
        )
        new_h = max(36, rect.height() + fm.lineSpacing())
        self.label.setFixedHeight(new_h)
        self.updateGeometry()

    # ── showEvent: widget is now painted, real geometry available ──────
    def showEvent(self, event):
        super().showEvent(event)
        if self.is_user and self._user_text and not self._shown_once:
            self._shown_once = True

            # Try to get the true viewport width from the QScrollArea
            vp_width = _get_scroll_area_viewport_width(self)
            if vp_width and vp_width > 50:
                self._set_user_height_with_width(self._user_text, vp_width)
            else:
                # Fallback: use the bubble's own painted width
                bw = self.bubble.width()
                if bw > 20:
                    self._set_user_height_with_width(self._user_text, bw + 52)

    # ── Streaming ──────────────────────────────────────────────────────
    def start_stream(self):
        self._streaming = True
        self.label.setFixedHeight(36)

    def append_stream(self, full_text):
        self.label.setPlainText(full_text)
        if not self._height_timer.isActive():
            self._height_timer.start()

    def finish_stream(self, full_text):
        self._streaming = False
        self._height_timer.stop()
        self.label.setHtml(build_html(full_text))
        QTimer.singleShot(0, self._do_adjust_height)

    # ── Height ────────────────────────────────────────────────────────
    def _do_adjust_height(self):
        width = self.label.viewport().width()
        if width < 10:
            vp = _get_scroll_area_viewport_width(self)
            width = vp if vp else max(self._available_width - 60, 400)

        self.label.document().setTextWidth(width)
        doc_h = int(self.label.document().size().height())
        self.label.setFixedHeight(max(36, doc_h + 16))
        self.updateGeometry()

    def adjust_height(self):
        self._do_adjust_height()

    def resizeEvent(self, event):
        super().resizeEvent(event)
        if not self._height_timer.isActive():
            self._height_timer.start()