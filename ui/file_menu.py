from PySide6.QtWidgets import QMenu

class FileMenu(QMenu):
    def __init__(self, parent=None) -> None:
        super().__init__("File", parent)
        self.new_action = self.addAction("new")
        self.open_action = self.addAction("open")
        self.save_as_action = self.addAction("save as")
        self.save_action = self.addAction("save")
        self.new_action.setShortcut("Ctrl+N")
        self.save_as_action.setShortcut("Ctrl+Shift+S")
        self.save_action.setShortcut("Ctrl+S")
        self.open_action.setShortcut("Ctrl+O")
