
from chempy import balance_stoichiometry
from PyQt6 import QtCore, QtGui, QtWidgets
from chemlib import Compound
import sqlite3
from PyQt6.QtWidgets import QMainWindow, QWidget

class Solver(QWidget):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(753, 460)
        self.label_3 = QtWidgets.QLabel(parent=Form)
        self.label_3.setGeometry(QtCore.QRect(250, 20, 241, 81))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(28)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setAutoFillBackground(False)
        self.label_3.setObjectName("label_3")
        self.comboBox = QtWidgets.QComboBox(parent=Form)
        self.comboBox.setGeometry(QtCore.QRect(310, 120, 131, 31))
        self.comboBox.setObjectName("comboBox")
        self.label_4 = QtWidgets.QLabel(parent=Form)
        self.label_4.setGeometry(QtCore.QRect(310, 60, 121, 71))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setAutoFillBackground(False)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=Form)
        self.label_5.setGeometry(QtCore.QRect(30, 150, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setAutoFillBackground(False)
        self.label_5.setObjectName("label_5")
        self.input_value_browser = QtWidgets.QTextEdit(parent=Form)
        self.input_value_browser.setGeometry(QtCore.QRect(140, 160, 561, 31))
        self.input_value_browser.setObjectName("textEdit_3")
        self.label_6 = QtWidgets.QLabel(parent=Form)
        self.label_6.setGeometry(QtCore.QRect(30, 310, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setAutoFillBackground(False)
        self.label_6.setObjectName("label_6")
        self.output_value_browser = QtWidgets.QLineEdit(parent=Form)
        self.output_value_browser.setGeometry(QtCore.QRect(120, 310, 551, 41))
        self.output_value_browser.setObjectName("output_value_browser")
        self.pushButtonGet = QtWidgets.QPushButton(parent=Form)
        self.pushButtonGet.setGeometry(QtCore.QRect(320, 250, 111, 51))
        self.pushButtonGet.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Solver", "Solver"))
        """self.label_3.setText(_translate("Form", "Решение Задач"))
        self.comboBox.setItemText(0, _translate("Form", "Уравнять Реакцию"))
        self.comboBox.setItemText(1, _translate("Form", "Вычислить молякулярную массу вещества"))
        self.comboBox.setItemText(2, _translate("Form", "массовая доля n-ого элемента в веществе"))
        self.comboBox.setItemText(3, _translate("Form", "расчет массы для получения элемента"))
        self.comboBox.setItemText(4, _translate("Form", "Масса и число молекул"))
        self.comboBox.setItemText(5, _translate("Form", "Электронная формула и количество валентных электронов"))"""
        self.comboBox.addItems(["Уравнять Реакцию", "Вычислить молякулярную массу вещества", "массовая доля n-ого элемента в веществе"])
        self.label_4.setText(_translate("Form", "Тип задачи"))
        self.label_5.setText(_translate("Form", "Вводное:"))
        self.label_6.setText(_translate("Form", "Выход:"))
        self.pushButtonGet.setText(_translate("Form", "Получить"))
        self.pushButtonGet.clicked.connect(self.on_combobox_changed)

    
    





def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Solver()
    ui.setupUi(Form)
    Form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())