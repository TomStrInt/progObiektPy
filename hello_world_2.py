import sys
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton, QLineEdit
from PySide6.QtGui import QPixmap


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Hello World")
        self.resize(400, 550)

        # tworzenie pola z obrazkiem
        self.label = QLabel(self)
        self.label.setGeometry(50, 50, 300, 200)
        pixmap = QPixmap("hipogryf.jpeg")
        self.label.setPixmap(pixmap)
        self.label.setScaledContents(True)

        # pole inputu
        self.input_field = QLineEdit(self)
        self.input_field.setGeometry(50, 270, 300, 30)
        self.input_field.setPlaceholderText("Wpisz jakis tekst")

        # tworzenie outputu 
        self.output_label = QLabel(self)
        self.output_label.setGeometry(50, 320, 300, 30)
        self.output_label.setText(" ")
        self.output_label.setStyleSheet("font-size: 14px; color: orange") 


        # tworzenie buttona:
        self.click_me_button = QPushButton("Nacisnij!", self)
        self.click_me_button.setGeometry(50, 360, 100, 40)
        self.click_me_button.clicked.connect(self.on_button_clicked)

        # czyszczenie inputu
        self.clear_button = QPushButton("Wyczysc", self)
        self.clear_button.setGeometry(250, 360, 100, 40)
        self.clear_button.clicked.connect(self.clear_input)
        # przycisk do wysiwtlania tekstu:
        self.display_button = QPushButton("Wyswitel tekst", self)
        self.display_button.setGeometry(150, 420, 100, 40)
        self.display_button.clicked.connect(self.display_input_text)
       
    def on_button_clicked(self):
        self.output_label.setText("Hello World") #wyswietla "Hello World"

    def clear_input(self):
        self.input_field.clear() #czysci input
        

    def display_input_text(self):
        text = self.input_field.text()
        if text.strip():  
            self.output_label.setText(text)
        else:
            self.output_label.setText("Prosze wpisac tekst!")  

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
