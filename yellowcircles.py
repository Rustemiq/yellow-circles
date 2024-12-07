import sys
from PyQt6 import uic
from PyQt6.QtCore import QPoint
from PyQt6.QtWidgets import QApplication, QMainWindow
from UI import Ui_MainWindow
from PyQt6.QtGui import QPainter, QColor
from random import randint


class YellowCircles(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.addButton.clicked.connect(self.drawCircle)
        self.draw = False

    def drawCircle(self):
        self.draw = True
        self.update()

    def paintEvent(self, event):
        if self.draw:
            qp = QPainter()
            qp.begin(self)
            r = randint(0, 255)
            g = randint(0, 255)
            b = randint(0, 255)
            color = QColor(r, g, b)
            qp.setBrush(color)
            pos = QPoint(randint(50, 250), randint(50, 250))
            R = randint(20, 50)
            qp.drawEllipse(pos, R, R)
            qp.end()
            self.draw = False

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = YellowCircles()
    ex.show()
    sys.exit(app.exec())