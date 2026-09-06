from PySide6.QtGui import QCloseEvent, QKeySequence, QShortcut
from PySide6.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QVBoxLayout, QWidget
from editor.code_editor import CodeEditor
from files.file_manager import FileManager
from ui.file_menu import FileMenu
from ui.top_bar import TopBar



class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("lil code")
        self.resize(600,300)
        self.central_container = QWidget()
        self.central_layout = QVBoxLayout(self.central_container)
        self.central_layout.setContentsMargins(0, 0, 0, 0)
        self.central_layout.setSpacing(0)
        self.top_bar = TopBar()
        self.central_layout.addWidget(self.top_bar)

        self.file_manager = FileManager()
        self.code_editor = CodeEditor()
        self.central_layout.addWidget(self.code_editor)
        self.setCentralWidget(self.central_container)
        self.setup_file_menu()
        self.setup_menu_shortcut()
        self.connect_actions()
        self.update_window_title()

        self.code_editor.editor.textChanged.connect(self.update_window_title)

    def update_window_title(self) -> None:
        if self.file_manager.current_file is None:
            filename = "untitled"
        else:
            filename = self.file_manager.current_file.name

        if self.has_unsaved_changes():
            filename = f"{filename}[*]"

        self.setWindowTitle(f"lil code - {filename}")
        self.top_bar.label_file.setText(filename)

    def has_unsaved_changes(self) -> bool:
        current_content = self.code_editor.editor.toPlainText()
        return self.file_manager.has_unsaved_changes(current_content)

    def closeEvent(self, event: QCloseEvent) -> None:
        if self.confirm_unsaved_changes():
            event.accept()
        else:
            event.ignore()

    def setup_file_menu(self) -> None:
        self.file_menu = FileMenu(self)
        self.menuBar().addMenu(self.file_menu)
        self.menuBar().setNativeMenuBar(False)
        self.menuBar().hide()

    def setup_menu_shortcut(self):
        self.menu_shortcut = QShortcut(QKeySequence("Ctrl + M"), self)
        self.menu_shortcut.activated.connect(self.toggle_menu_bar)

    def toggle_menu_bar(self):
        menu_bar = self.menuBar()
        menu_bar.setVisible(not menu_bar.isVisible())


    def connect_actions(self) -> None:
        file_actions = (
            self.file_menu.new_action,
            self.file_menu.open_action,
            self.file_menu.save_action,
            self.file_menu.save_as_action,
        )

        for action in file_actions:
            self.addAction(action)

        self.file_menu.new_action.triggered.connect(self.new_file)
        self.file_menu.open_action.triggered.connect(self.open_file)
        self.file_menu.save_as_action.triggered.connect(self.save_as)
        self.file_menu.save_action.triggered.connect(self.save)

    def confirm_unsaved_changes(self) -> bool:
        if self.has_unsaved_changes():
            msg_box = QMessageBox(self)
            msg_box.setWindowTitle("Save Changes")
            msg_box.setText("You have unsaved changes. Do you want to save them?")
            msg_box.setStandardButtons(QMessageBox.StandardButton.Save | QMessageBox.StandardButton.Discard | QMessageBox.StandardButton.Cancel)
            result = msg_box.exec()
            if result == QMessageBox.StandardButton.Save:
                if not self.save():
                    return False
            elif result == QMessageBox.StandardButton.Cancel:
                return False
        return True

    def new_file(self) -> None:
        if not self.confirm_unsaved_changes():
            return
        self.file_manager.new_file()
        self.code_editor.editor.clear()
        self.update_window_title()

    def open_file(self) -> None:
        if not self.confirm_unsaved_changes():
            return
        path, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Python Files (*.py);; JavaScript Files (*.js);; All Files (*)")
        if path:
            try:
                content = self.file_manager.open_file(path)
            except UnicodeDecodeError as error:
                self.show_file_error("Encoding Error", error)
                return
            except OSError as error:
                self.show_file_error("Open File Error", error)
                return

            self.code_editor.editor.setPlainText(content)
            self.mark_document_as_saved()

    def save_as(self) -> bool:
        path, _ = QFileDialog.getSaveFileName(self, "Save File", "", "Python Files (*.py);; JavaScript Files (*.js);; All Files (*)")
        if path:
            content = self.code_editor.editor.toPlainText()
            try:
                self.file_manager.save_as(path, content)
            except OSError as error:
                self.show_file_error("Save File Error", error)
                return False

            self.mark_document_as_saved()
            return True
        return False

    def mark_document_as_saved(self) -> None:
        self.code_editor.editor.document().setModified(False)
        self.update_window_title()

    def save(self) -> bool:
        if self.file_manager.current_file is None:
            return self.save_as()

        content = self.code_editor.editor.toPlainText()
        try:
            self.file_manager.save_file(content)
        except OSError as error:
            self.show_file_error("Save File Error", error)
            return False

        self.mark_document_as_saved()
        return True

    def show_file_error(self, title: str, error: Exception) -> None:
        QMessageBox.critical(
            self,
            title,
            str(error),
        )
