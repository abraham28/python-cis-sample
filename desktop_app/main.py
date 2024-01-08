import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        # Create a button
        button = QPushButton('Click me!', self)
        button.clicked.connect(self.on_button_click)

        # Set up the main window
        self.setGeometry(100, 100, 400, 300)
        self.setWindowTitle('Client Information System')

    def on_button_click(self):
        print('Button clicked!')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
