from PySide6.QtWidgets import QPlainTextEdit, QVBoxLayout, QWidget
from PySide6.QtGui import QFont

class CodeEditor(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0,0,0,0)
        self.layout.setSpacing(0)
        self.editor = QPlainTextEdit()
        self.font_editor = QFont('Consolas', 18)
        self.layout.addWidget(self.editor)
        self.setStyleSheet("background-color: black; border: none; color: white")
        self.editor.setFont(self.font_editor)
        
