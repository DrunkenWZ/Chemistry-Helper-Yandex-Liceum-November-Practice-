import sys
from PyQt6 import QtWidgets
from auth_logic import create_database, add_user, check_user

class AuthApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    def init_ui(self):
        username = ""
        self.setWindowTitle('Авторизация')
        self.setGeometry(100, 100, 300, 150)
        self.layout = QtWidgets.QVBoxLayout()
        
        self.username_label = QtWidgets.QLabel('Имя пользователя:')
        self.layout.addWidget(self.username_label)
        
        self.username_input = QtWidgets.QLineEdit()
        self.layout.addWidget(self.username_input)
        
        self.password_label = QtWidgets.QLabel('Пароль:')
        self.layout.addWidget(self.password_label)
        
        self.password_input = QtWidgets.QLineEdit()
        self.password_input.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.layout.addWidget(self.password_input)
        
        self.login_button = QtWidgets.QPushButton('Войти')
        self.login_button.clicked.connect(self.login)
        
        self.register_button = QtWidgets.QPushButton('Регистрация')
        self.register_button.clicked.connect(self.register)
        
        self.layout.addWidget(self.login_button)
        self.layout.addWidget(self.register_button)
        
        self.setLayout(self.layout)

    def login(self):
        username = self.username_input.text()
        password = self.password_input.text()
        if check_user(username, password):
            print("Авторизация успешна")  
            QtWidgets.QMessageBox.information(self, 'Успех', 'Вы успешно вошли в систему!')
        else:
            print("Неправильное имя пользователя или пароль")
            QtWidgets.QMessageBox.warning(self, 'Ошибка', 'Неправильное имя пользователя или пароль.')

    def register(self):
        username = self.username_input.text()
        password = self.password_input.text()

        if add_user(username, password):
            QtWidgets.QMessageBox.information(self, 'Успех', 'Вы успешно зарегистрированы!')
        else:
            QtWidgets.QMessageBox.warning(self, 'Ошибка', 'Пользователь с таким именем уже существует.')
    
    def get_username(self):
        return self.username


if __name__ == '__main__':
    create_database()
    app = QtWidgets.QApplication(sys.argv)
    window = AuthApp()
    window.show()
    sys.exit(app.exec())
