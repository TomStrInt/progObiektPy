import sys
from PySide6.QtWidgets import QApplication, QPushButton, QLabel
from PySide6.QtCore import Slot


app = QApplication(sys.argv)
label = QLabel("Hello World!")
# This HTML approach will be valid too!
#label = QLabel("<font color=blue size=40>Hello World!</font>")
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