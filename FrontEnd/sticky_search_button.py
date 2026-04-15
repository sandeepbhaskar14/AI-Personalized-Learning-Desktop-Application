from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QObject, QEvent


class StickyButton(QPushButton):
    """
    Generic sticky button for QTextEdit.
    Supports bottom-left and bottom-right anchoring.
    """

    def __init__(self, parent=None):
        super().__init__(parent)

        self._text_edit = None
        self._margin = 4
        self._anchor = "bottom-right"  # default

        self.setFixedSize(48, 48)

    def setTextEdit(self, text_edit):
        self._text_edit = text_edit
        text_edit.installEventFilter(self)
        self.update_position()

    def setAnchor(self, anchor: str):
        """
        anchor: 'bottom-right' or 'bottom-left'
        """
        self._anchor = anchor
        self.update_position()

    def eventFilter(self, obj: QObject, event: QEvent):
        if obj == self._text_edit and event.type() == QEvent.Resize:
            self.update_position()
        return super().eventFilter(obj, event)

    def update_position(self):
        if not self._text_edit:
            return

        te = self._text_edit
        btn = self

        # Vertical position (same for both)
        y = te.y() + te.height() - btn.height() - self._margin

        # Horizontal position depends on anchor
        if self._anchor == "bottom-left":
            x = te.x() + self._margin
        else:  # bottom-right
            x = te.x() + te.width() - btn.width() - self._margin

        btn.move(x, y)
        btn.raise_()
