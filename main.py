from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import QApplication, QPushButton, QMainWindow, QWidget
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Bart - The Bank Chart App')
        self.setMinimumSize(400, 300)

        button = QPushButton('Import New CSV')
        self.setCentralWidget(button)

def main():
    app = QApplication([])

    window = MainWindow()

    window.show()

    app.exec()


if __name__ == "__main__":
    main()
