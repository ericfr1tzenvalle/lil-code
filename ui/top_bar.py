from PySide6.QtWidgets import QWidget, QHBoxLayout, QLabel, QPushButton
from PySide6.QtCore import Qt


class TopBar(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setFixedHeight(36)

        self.main_layout = QHBoxLayout(self)
        self.main_layout.setContentsMargins(12, 3, 12, 3)
        self.label_app_name = QLabel('lilcode')
        self.label_file = QLabel('untitled')
        self.button_run = QPushButton('▶︎')
        self.button_run.setFixedSize(32, 26)
        self.setAttribute(
            Qt.WidgetAttribute.WA_StyledBackground,
            True,
        )
        self.setStyleSheet("""
            background-color: #8bc8fe;
            color: #051b2c;
            font-family: "Consolas";
            font-size: 12px;
        """)

        self.button_run.setStyleSheet("""
            border: none
        """)

        self.main_layout.addWidget(self.label_app_name, 0, Qt.AlignmentFlag.AlignLeft)
        self.main_layout.addWidget(self.label_file, 1, Qt.AlignmentFlag.AlignCenter)
        self.main_layout.addWidget(self.button_run, 0, Qt.AlignmentFlag.AlignRight)
