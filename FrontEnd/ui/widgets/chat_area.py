from PyQt5.QtWidgets import QWidget, QVBoxLayout, QScrollArea

class ChatArea(QScrollArea):
    def __init__(self):
        super().__init__()
        self.container = QWidget()
        self.layout = QVBoxLayout(self.container)
        self.layout.setSpacing(10)

        self.setWidgetResizable(True)
        self.setWidget(self.container)

    def add_bubble(self, bubble):
        self.layout.addWidget(bubble)
        self.scroll_to_bottom()

    def scroll_to_bottom(self):
        self.verticalScrollBar().setValue(
            self.verticalScrollBar().maximum()
        )
        