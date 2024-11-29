from main_m import Ui_MainWindow
from PyQt6.QtWidgets import QMainWindow
from PyQt6 import QtCore, QtGui, QtWidgets
from solver_be import Solv
import sys


class MainM(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def open_window(self, window_name):
        print("открытие окна")
        try:
            s = window_name
            s.show()
        except Exception as e:
            print(f"Ошибка при открытии окна: {e}")
    


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    wind = MainM()
    wind.show()
    sys.exit(app.exec())
