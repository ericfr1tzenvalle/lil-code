import sys
from ui import MainWindow
from PySide6.QtWidgets import QApplication

def main():
    app = QApplication(sys.argv)

    main_window = MainWindow()
    main_window.show()

    sys.exit(app.exec())

if __name__ == '__main__':
    main()