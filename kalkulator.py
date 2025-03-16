import sys
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton, QLineEdit
from PySide6.QtGui import QDoubleValidator, QPixmap


class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Prosty Kalkulator")
        self.resize(450, 500)

        self.label = QLabel(self)
        self.label.setGeometry(50, 50, 300, 200)
        pixmap = QPixmap("hipogryf.jpeg")
        self.label.setPixmap(pixmap)
        self.label.setScaledContents(True)

    # pierwszy input
        self.input1 = QLineEdit(self)
        self.input1.setGeometry(50, 300, 150, 30)
        self.input1.setPlaceholderText("Podaj liczbę")
        self.input1.setValidator(QDoubleValidator())  
    #drugi input
        self.input2 = QLineEdit(self)
        self.input2.setGeometry(220, 300, 150, 30)
        self.input2.setPlaceholderText("Podaj liczbę")
        self.input2.setValidator(QDoubleValidator()) 

    # wyswietlanie wyniku
        self.result_label = QLabel(self)
        self.result_label.setGeometry(50, 350, 300, 30)
        self.result_label.setText(" ")
        self.result_label.setStyleSheet("font-size: 25px; color: yellow;")

    # Przyciski:
        #dodawanie
        self.add_button = QPushButton("+", self)
        self.add_button.setGeometry(50, 390, 80, 40)
        self.add_button.clicked.connect(self.add_numbers)
        #odejmowanie
        self.subtract_button = QPushButton("-", self)
        self.subtract_button.setGeometry(140, 390, 80, 40)
        self.subtract_button.clicked.connect(self.subtract_numbers)
        #mnozenie
        self.multiply_button = QPushButton("x", self)
        self.multiply_button.setGeometry(230, 390, 80, 40)
        self.multiply_button.clicked.connect(self.multiply_numbers)
        #dzielenie
        self.divide_button = QPushButton("/", self)
        self.divide_button.setGeometry(320, 390, 80, 40)
        self.divide_button.clicked.connect(self.divide_numbers)

    def get_inputs(self):       #pobieranie danych
        try:
            num1 = float(self.input1.text())
            num2 = float(self.input2.text())
            return num1, num2
        except ValueError:
            self.result_label.setText("Błędne dane!")
            return None, None

    def add_numbers(self):  #dodawanie
        num1, num2 = self.get_inputs()
        if num1 is not None and num2 is not None:
            result = num1 + num2
            self.result_label.setText(f"= {result}")

    def subtract_numbers(self):     #odejmowanie
        num1, num2 = self.get_inputs()
        if num1 is not None and num2 is not None:
            result = num1 - num2
            self.result_label.setText(f"= {result}")

    def multiply_numbers(self):
        num1, num2 = self.get_inputs()
        if num1 is not None and num2 is not None:
            result = num1 * num2
            self.result_label.setText(f"= {result}")

    def divide_numbers(self):
        num1, num2 = self.get_inputs()
        if num1 is not None and num2 is not None:
            if num2 == 0:
                self.result_label.setText("Nie dziel przez zero!")
            else:
                result = num1 / num2
                self.result_label.setText(f"= {result}")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Calculator()
    window.show()

    sys.exit(app.exec())

