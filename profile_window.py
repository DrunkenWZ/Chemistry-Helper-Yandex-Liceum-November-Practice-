import sys
import sqlite3
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QTableView, QPushButton, QVBoxLayout, QMessageBox
from PyQt6.QtGui import QFont
from PyQt6.QtCore import QRect, QAbstractTableModel, Qt
from auth import AuthApp


class Table(QAbstractTableModel):
    def __init__(self, data):
        super().__init__()
        self._data = data

    def rowCount(self, parent=None):
        return len(self._data)

    def columnCount(self, parent=None):
        return len(self._data[0]) if self._data else 0

    def data(self, index, role=Qt.ItemDataRole.DisplayRole):
        if role == Qt.ItemDataRole.DisplayRole:
            return self._data[index.row()][index.column()]
        return None

class Profile_widget(QWidget):
    def __init__(self, user_id):
        super().__init__()
        self.user_id = user_id
        self.setGeometry(0, 0, 932, 730)
        self.setWindowTitle("Form")
        self.label = QLabel(self)
        self.label.setGeometry(QRect(36, 42, 511, 131))
        self.label.setFont(QFont("Nirmala UI", 36))
        self.label.setText("UNKNOW USER")
        self.tableView = QTableView(self)
        self.tableView.setGeometry(QRect(40, 160, 841, 531))
        self.pushButton = QPushButton(self)
        self.pushButton.setGeometry(QRect(800, 40, 75, 23))
        self.pushButton.setText("Load Tasks")
        self.pushButton.clicked.connect(self.load_tasks)
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.tableView)
        layout.addWidget(self.pushButton)
        self.setLayout(layout)

    def load_tasks(self):
        try:
            conn = sqlite3.connect('tasks_history.db')
            conntwo = sqlite3.connect('users.db')
            cursor = conn.cursor()
            cursortwo = conntwo.cursor()
            cursor.execute(f"SELECT task_type, text_task FROM history WHERE user_ID = SELECT id FROM users WHERE username = {AuthApp.get_username(self)}", (self.user_id,))
            rows = cursor.fetchall()
            conn.close()

            model = Table(rows)
            self.tableView.setModel(model)

        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    user_id = 1  
    window = Profile_widget(user_id)
    window.show()
    sys.exit(app.exec())
