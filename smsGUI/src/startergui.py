import sys
from PyQt5.QtWidgets import QApplication, QWidget
import navbar

def main():
    # Create an instance of QApplication
    app = QApplication(sys.argv)

    # Create a QWidget (window)
    window = QWidget()
    window.setWindowTitle('SMS Infocomm Motherboard Inspection')
    window.setGeometry(100, 100, 1024, 768)  # (x, y, width, height)

    #navbar
    navbars = navbar()
    # Show the window
    window.show()

    # Start the event loop
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
