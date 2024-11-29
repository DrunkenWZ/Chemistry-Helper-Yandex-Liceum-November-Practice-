from main_m import Ui_MainWindow
from PyQt6 import QtCore, QtGui, QtWidgets
from solver_be import Solv




class MainM(Ui_MainWindow):
    def __init__(self):
        super().__init__()

    def open_login_window(self):
        print("открытие профиля")
        try:
            window = AuthApp()
            window.show()
        except Exception as e:
            print(f"Ошибка при открытии окна логина: {e}")

    def open_mendelev(self):
        print("открытие таблицы")
        try:
            profile_window = me.tab()
            profile_window.show()
        except Exception as e:
            print(f"Ошибка при открытии окна таблицы: {e}")

    def open_rastr(self):
        print("открытие таблицы")
        try:
            profile_window = rs.tab()
            profile_window.show()
        except Exception as e:
            print(f"Ошибка при открытии окна таблицы: {e}")

    def open_solver(self):
        print("открытие окна")
        try:
            s = Solv()
            s.show()
        except Exception as e:
            print(f"Ошибка при открытии окна: {e}")
    


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = MainM()
    ui.setupUi(MainWindow, ui.open_solver, ui.open_login_window)
    MainWindow.show()
    sys.exit(app.exec())
