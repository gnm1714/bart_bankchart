import typing

from PyQt5 import QtGui
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import QApplication, QPushButton, QMainWindow, QWidget
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.csv_btn_tgl = False

        self.setWindowTitle('Bart - The Bank Chart App')
        self.setMinimumSize(400, 300)

        self.button = (QPushButton('Import New CSV'))
        self.button.setCheckable(True)
        self.button.clicked.connect(self.csv_btn_prsd)
        self.setCentralWidget(self.button)

    def csv_btn_prsd(self, checked):
        print("Button Pressed. Toggle status: ", checked)
        self.csv_btn_tgl = checked

    def mousePressEvent(self, e):
        if e.button() == Qt.LeftButton:
            super().self.button.setText("Button Pressed!")

def main():
    app = QApplication([])

    window = MainWindow()

    window.show()

    app.exec()


if __name__ == "__main__":
    main()
