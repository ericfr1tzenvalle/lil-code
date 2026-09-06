import sys
from pathlib import Path

from PySide6.QtCore import Qt
from PySide6.QtGui import QFontDatabase
from PySide6.QtWidgets import QApplication

from ui import MainWindow


def main() -> None:
    QApplication.setAttribute(Qt.ApplicationAttribute.AA_DontUseNativeDialogs)
    app = QApplication(sys.argv)
    font_path = Path(__file__).resolve().parent / "styles" / "fonts" / "DevinneSwash.ttf"
    QFontDatabase.addApplicationFont(str(font_path))
    stylesheet_path = Path(__file__).resolve().parent / "styles" / "dracula.qss"
    app.setStyleSheet(stylesheet_path.read_text(encoding="utf-8"))

    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
