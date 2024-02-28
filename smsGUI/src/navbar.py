import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget

class navBar(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('PyQt5 Navbar Example')
        self.setGeometry(100, 100, 600, 400)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        # Create navigation buttons
        button1 = QPushButton('Button 1', self)
        button2 = QPushButton('Button 2', self)
        button3 = QPushButton('Button 3', self)

        # Add buttons to layout
        layout.addWidget(button1)
        layout.addWidget(button2)
        layout.addWidget(button3)