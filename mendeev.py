import sys

from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow

SCREEN_SIZE = [1000, 1000]


class tab(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(1000, 1000, *SCREEN_SIZE)
        self.setWindowTitle('Отображение картинки')

        ## Изображение
        self.pixmap = QPixmap('men.jpg')
        # Если картинки нет, то QPixmap будет пустым, 
        # а исключения не будет
        self.image = QLabel(self)
        self.image.move(80, 60)
        self.image.resize(1980, 1080)
        # Отображаем содержимое QPixmap в объекте QLabel
        self.image.setPixmap(self.pixmap)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = tab()
    ex.show()
    sys.exit(app.exec())