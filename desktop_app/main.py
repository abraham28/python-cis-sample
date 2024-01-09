from PyQt6.QtWidgets import QMainWindow, QApplication
from screens.home import HomeWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.home = HomeWindow()

        self.setWindowTitle('Client Information System')

        self.setCentralWidget(self.home)


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
