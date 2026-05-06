from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QVBoxLayout,
                              QFrame, QSizePolicy, QTextBrowser,
                              QScrollArea, QLabel)
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QFont, QTextDocument, QPixmap, QPainter, QPainterPath
import markdown
from markdown.extensions.codehilite import CodeHiliteExtension
from markdown.extensions.fenced_code import FencedCodeExtension
import os


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
    """Walk up the parent chain to find QScrollArea viewport width."""
    p = widget.parent()
    while p is not None:
        if isinstance(p, QScrollArea):
            vw = p.viewport().width()
            return max(vw - 10, 100)
        p = p.parent()
    return None


def _rounded_pixmap(pixmap: QPixmap, radius: int = 6) -> QPixmap:
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


class ChatBubble(QWidget):
    _FONT     = QFont("Roboto", 10)
    _CHIP_H   = 56    # must match _AttachChip.CHIP_H in auto_grow_text_edit
    _CHIP_GAP = 6     # gap between chip and text label inside bubble

    def __init__(self, text="", is_user=False, available_width=800, attachment=None):
        super().__init__()
        self._attachment   = attachment
        self.is_user       = is_user
        self._available_width = available_width
        self._user_text    = text if is_user else ""
        self._shown_once   = False
        self._streaming    = False

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
        bubble_layout.setSpacing(self._CHIP_GAP)

        self.label = QTextBrowser()
        self.label.setOpenExternalLinks(True)
        self.label.setFrameShape(QTextBrowser.NoFrame)
        self.label.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.label.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.label.setMinimumHeight(36)
        self.label.document().setDocumentMargin(2)

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

            # ── Attachment chip (if any) ───────────────────────────────────────
            if self._attachment:
                chip_frame = self._build_attachment_chip(self._attachment)
                bubble_layout.addWidget(chip_frame)

            bubble_layout.addWidget(self.label)

            if text:
                self.label.setPlainText(text)
                self._set_user_height_with_width(text, available_width)

        else:
            self.bubble.setStyleSheet(
                "QFrame { background-color: #2d3240; border-radius: 12px; }")
            self.label.setStyleSheet(
                "QTextBrowser { color: rgba(255,255,255,220); "
                "background: transparent; font-family: Roboto; "
                "font-size: 10pt; border: none; }")
            outer.addWidget(self.bubble, 1)
            bubble_layout.addWidget(self.label)

            if text:
                self.label.setHtml(build_html(text))
                QTimer.singleShot(0, self._do_adjust_height)

    # ── Build chip widget for inside the user bubble ───────────────────────────
    def _build_attachment_chip(self, attachment: dict) -> QFrame:
        chip = QFrame()
        chip.setFixedHeight(self._CHIP_H)
        chip.setStyleSheet("""
            QFrame {
                background-color: rgba(255,255,255,18);
                border-radius: 10px;
                border: none;
            }
        """)
        row = QHBoxLayout(chip)
        row.setContentsMargins(8, 5, 10, 5)
        row.setSpacing(8)

        # Thumbnail or ext badge
        thumb = QLabel()
        thumb.setAlignment(Qt.AlignCenter)
        px = attachment.get("pixmap")
        if px and not px.isNull():
            scaled = px.scaled(56, 42, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            thumb.setPixmap(_rounded_pixmap(scaled))
            thumb.setFixedSize(56, 42)
        else:
            ext = (os.path.splitext(attachment["filename"])[1]
                   .upper().lstrip('.') or "FILE")
            thumb.setText(ext)
            thumb.setFixedSize(40, 34)
            thumb.setStyleSheet("""
                background-color: rgba(255,255,255,22);
                border-radius: 6px; color: white;
                font-size: 9px; font-family: 'Roboto'; font-weight: bold;
            """)
        row.addWidget(thumb)

        # Name + type column
        col = QVBoxLayout()
        col.setSpacing(1)
        col.setContentsMargins(0, 0, 0, 0)

        fn = QLabel()
        fn.setText(fn.fontMetrics().elidedText(
            attachment["filename"], Qt.ElideMiddle, 190))
        fn.setToolTip(attachment["filename"])
        fn.setStyleSheet("""
            color: rgba(255,255,255,210);
            font-family: 'Roboto'; font-size: 9pt;
            background: transparent; border: none;
        """)
        col.addWidget(fn)

        ext_str = os.path.splitext(attachment["filename"])[1].upper().lstrip('.')
        type_lbl = QLabel(f"{ext_str} file" if ext_str else "file")
        type_lbl.setStyleSheet("""
            color: rgba(255,255,255,90);
            font-family: 'Roboto'; font-size: 8pt;
            background: transparent; border: none;
        """)
        col.addWidget(type_lbl)
        row.addLayout(col)
        row.addStretch()

        return chip

    # ── User bubble height calculation ─────────────────────────────────────────
    def _set_user_height_with_width(self, text, container_width):
        """
        Pixel-perfect height using QTextDocument so word-wrap matches Qt exactly.
        Accounts for attachment chip if present.

        Padding layers (container_width → inner text width):
          outer QHBoxLayout  left=10, right=10   → 20px
          bubble QVBoxLayout left=12, right=12   → 24px
          QTextBrowser doc margin  2+2           → 4px
          safety buffer                          → 4px
          Total horizontal padding               → 52px

        Bubble vertical layout:
          bubble VBox top=10, bottom=10          → 20px total
          chip (if present): CHIP_H + CHIP_GAP  → 56 + 6 = 62px
          label extra                            → 4px
        """
        MAX_BUBBLE      = 550
        H_PAD           = 52    # left+right padding from container to inner text
        BUBBLE_VPAD     = 20    # bubble top+bottom margins
        LABEL_EXTRA     = 4

        chip_height = (self._CHIP_H + self._CHIP_GAP) if self._attachment else 0

        bubble_w = min(container_width, MAX_BUBBLE)
        inner_w  = max(bubble_w - H_PAD, 60)

        doc = QTextDocument()
        doc.setDefaultFont(self._FONT)
        doc.setPlainText(text)
        doc.setTextWidth(inner_w)

        doc_h    = int(doc.size().height())
        label_h  = max(36, doc_h + LABEL_EXTRA)
        bubble_h = chip_height + label_h + BUBBLE_VPAD

        self.label.setFixedHeight(label_h)
        self.bubble.setFixedHeight(bubble_h)
        self.updateGeometry()

    # ── showEvent: real geometry now available ─────────────────────────────────
    def showEvent(self, event):
        super().showEvent(event)
        if self.is_user and self._user_text and not self._shown_once:
            self._shown_once = True
            vp_width = _get_scroll_area_viewport_width(self)
            if vp_width and vp_width > 50:
                self._set_user_height_with_width(self._user_text, vp_width)
            else:
                bw = self.bubble.width()
                if bw > 20:
                    self._set_user_height_with_width(self._user_text, bw + 52)

    # ── Streaming ──────────────────────────────────────────────────────────────
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

    # ── Height ────────────────────────────────────────────────────────────────
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
            self._height_timer.start(150)