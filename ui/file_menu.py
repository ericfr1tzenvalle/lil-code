from PySide6.QtWidgets import QMenu


class FileMenu(QMenu):
    def __init__(self, parent=None) -> None:
        super().__init__("File", parent)
        self.new_action = self.addAction("new")
        self.open_action = self.addAction("open")
        self.addSeparator()
        self.save_as_action = self.addAction("save as")
        self.save_action = self.addAction("save")
        self.new_action.setShortcut("Ctrl+N")
        self.save_as_action.setShortcut("Ctrl+Shift+S")
        self.save_action.setShortcut("Ctrl+S")
        self.open_action.setShortcut("Ctrl+O")

        self.setStyleSheet("""
        QMenu {
            background-color: #3bc3fe;
            color: #051b2c;
            border: none;
            font-family: "Consolas";
            font-size: 10px;
            margin-left: 5px;
        }
        QMenu::item:selected {
            background-color: #8bc8fe;
            color: #051b2c;
        }
        QMenu::item:disabled {
            color: #526b7e;
        }
        QMenu::separator {
            height: 1px;
            background-color: #173a54;
            margin: 5px 8px;
        }
        """)
