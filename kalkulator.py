import sys
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton, QLineEdit
from PySide6.QtGui import QPixmap


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

    
if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
