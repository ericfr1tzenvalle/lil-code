from PySide6.QtGui import QCloseEvent
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QToolButton
from editor import CodeEditor
from files.file_manager import FileManager
from .file_menu import FileMenu



class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("lil code")
        self.resize(600,300)
        self.file_manager = FileManager()
        self.code_editor = CodeEditor()
        self.setup_file_menu()
        self.connect_actions()
        self.setCentralWidget(self.code_editor)
        self.update_window_title()

    def update_window_title(self) -> None:
        if self.file_manager.current_file is None:
            filename = 'untitled'
        else:
            filename = self.file_manager.current_file.name
        self.setWindowTitle(f'lil code - {filename}')

    def closeEvent(self, event: QCloseEvent) -> None:
        if self.confirm_unsaved_changes():
            event.accept()
        else:
            event.ignore()

    def setup_file_menu(self) -> None:
        self.file_menu = FileMenu(self)
        self.menu_button = QToolButton(self)
        self.menu_button.setText("☰")
        self.menu_button.setMenu(self.file_menu)
        self.menu_button.setPopupMode(QToolButton.ToolButtonPopupMode.InstantPopup)
        self.menuBar().setCornerWidget(self.menu_button, Qt.Corner.TopLeftCorner)
        self.menuBar().setStyleSheet("background-color: #8bc8fe ; color: #051b2c; border: none")

    def connect_actions(self) -> None:
        self.file_menu.new_action.triggered.connect(self.new_file)
        self.file_menu.open_action.triggered.connect(self.open_file)
        self.file_menu.save_as_action.triggered.connect(self.save_as)
        self.file_menu.save_action.triggered.connect(self.save)

    def confirm_unsaved_changes(self) -> bool:
        if self.code_editor.editor.document().isModified():
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
