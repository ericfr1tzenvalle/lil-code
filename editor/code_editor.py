from PySide6.QtWidgets import QPlainTextEdit, QVBoxLayout, QWidget
from PySide6.QtGui import QFont

from editor.python_highlighter import PythonHighlighter

class CodeEditor(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.layout_editor = QVBoxLayout(self)
        self.layout_editor.setContentsMargins(0,0,0,0)
        self.layout_editor.setSpacing(0)
        self.editor = QPlainTextEdit()
        self.highlight = PythonHighlighter(self.editor.document())
        self.font_editor = QFont('Consolas', 18)
        self.font_editor.setStyleHint(QFont.StyleHint.Monospace)
        self.layout_editor.addWidget(self.editor)
        self.setStyleSheet("background-color: #051b2c; border: none; color: #8bc8fe ; padding: 10px;")
        self.editor.setFont(self.font_editor)
        
