import sys

from PySide6.QtWidgets import QApplication

from ui import MainWindow


def main() -> None:
    app = QApplication(sys.argv)

    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
