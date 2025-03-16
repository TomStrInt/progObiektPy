import sys
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton, QLineEdit


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Prosty kalkulator")
        self.resize(400, 300)

        self.input_field = QLineEdit(self)
        self.input_field.setGeometry(50, 50, 300, 30)
        self.input_field.setPlaceholderText("Wpisz rownanie (na przyklad 2+4, 120/5)")
        #wyswyetlanie wyniku:

        self.output_label = QLabel(self)
        self.output_label.setGeometry(50, 100, 300, 30)
        self.output_label.setText("") 
        self.output_label.setStyleSheet("font-size: 25px; color: yellow;") 

        # button -- wynik
        self.solve_button = QPushButton("Podaj wynik", self)
        self.solve_button.setGeometry(150, 150, 100, 40)
        self.solve_button.clicked.connect(self.solve_equation)

    def solve_equation(self):
        try:
            equation = self.input_field.text()
            result = eval(equation)  
            self.output_label.setText(f"{result}")
        except:
            self.output_label.setText("Blad!: zle wpisales!")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
