import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.hello = ["Hallo Welt", "Hei maailma", "Hola Mundo", "Привет мир"]
        self.hello2 = ["Hallo Welt", "Hei maailma", "Hola Mundo", "Привет мир"]

        self.button = QtWidgets.QPushButton("Click me!")
        self.text = QtWidgets.QLabel("Hello World",
                                     alignment=QtCore.Qt.AlignCenter)
        self.button2 = QtWidgets.QPushButton("Do not click me!")
        self.text2 = QtWidgets.QLabel("Hello World",
                                     alignment=QtCore.Qt.AlignTop)
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.text2)
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.button2)
        self.button.clicked.connect(self.magic1)
        self.button2.clicked.connect(self.magic2)

    @QtCore.Slot()
    def magic1(self):
        self.text.setText(random.choice(self.hello))
    def magic2(self):
        self.text2.setText(random.choice(self.hello2))

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())