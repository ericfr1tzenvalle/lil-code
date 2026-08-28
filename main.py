import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QPlainTextEdit, QPushButton, QVBoxLayout
from PySide6.QtGui import QFont
# App -> QMainWindow -> QWidget -> QVBoxLayout -> QWidget (top-bar) + QPlainTextEdit 

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("lil code")
        self.resize(600,300)
        self.setCentralWidget(CodeEditor())

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
        

app = QApplication(sys.argv)

window = MainWindow()
window.show()

sys.exit(app.exec())

