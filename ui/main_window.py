from PySide6.QtWidgets import QMainWindow
from editor import CodeEditor

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("lil code")
        self.resize(600,300)
        self.setCentralWidget(CodeEditor())

