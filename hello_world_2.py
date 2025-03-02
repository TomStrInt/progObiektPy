import sys
from PySide6.QtWidgets import QApplication, QPushButton, QLabel
from PySide6.QtCore import Slot
from PySide6.QtGui import QdoubleValidator

app = QApplication(sys.argv)
label = QLabel("Hello World!")
label.show()


# Greetings
@Slot()
def say_hello():
    print("Button clicked, Hello!")

# Create a button

button = QPushButton("Click me")
# Connect the button to the function
button.clicked.connect(say_hello)
# Show the button
button.show()
# Run the main Qt loop
app.exec()