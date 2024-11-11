
from chempy import balance_stoichiometry
from PyQt6 import QtCore, QtGui, QtWidgets

class Uncorrect_value(Exception):
    pass

class Unknow_error(Exception):
    pass


class Solver(object):
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
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
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
        self.label_3.setText(_translate("Form", "Решение Задач"))
        self.comboBox.setItemText(0, _translate("Form", "Уравнять Реакцию"))
        self.comboBox.setItemText(1, _translate("Form", "Вычислить молякулярную массу вещества"))
        self.comboBox.setItemText(2, _translate("Form", "массовая доля n-ого элемента в веществе"))
        self.comboBox.setItemText(3, _translate("Form", "расчет массы для получения элемента"))
        self.comboBox.setItemText(4, _translate("Form", "Масса и число молекул"))
        self.comboBox.setItemText(5, _translate("Form", "Электронная формула и количество валентных электронов"))
        self.label_4.setText(_translate("Form", "Тип задачи"))
        self.label_5.setText(_translate("Form", "Вводное:"))
        self.label_6.setText(_translate("Form", "Выход:"))
        self.pushButtonGet.setText(_translate("Form", "Получить"))
        self.pushButtonGet.clicked.connect(self.Solve_Example)
        

    def Solve_Example(self):
        try:
            output_final = []
            input_value = self.input_value_browser.toPlainText()
            input_value = input_value.split(" ")
            reagent = []
            product = []
            reagent_ready = []
            product_ready = []
        except Unknow_error as e:
            self.output_value_browser.setText(f"Ошибка: {e}")
        try:
            for i in range(len(input_value)):
                if input_value[i] != "=":
                    reagent.append(input_value[i])
                else:
                    break
            product = set(input_value) - set(reagent)
            product = list(product)
            for i in range(len(reagent)):
                if str(reagent[i]) != "+":
                    reagent_ready.append(reagent[i])
            for i in range(len(product)):
                if str(product[i]) != "=":
                    product_ready.append(product[i])
            output_value = (balance_stoichiometry(reagent_ready, product_ready))
            reagent_ready = output_value[0]
            product_ready = output_value[1]
            left_final = []
            left_finals = []
            right_final = []
            right_finals = []
            for key, value in reagent_ready.items():
                left_final.append(str(value) + key)
            for p in range(len(left_final)):
                if left_final[p] != "1":
                    left_finals.append(left_final[p])
                else:
                    pass

            for ke, vv in product_ready.items():
                right_final.append(str(vv) + ke)
                for p in range(len(right_final)):
                    if right_final[p] != "1":
                        right_finals.append(right_final[p])
                    else:
                        pass
            output_final.append(' + '.join(list(left_finals)))
            output_final.append("=")
            output_final.append(' + '.join(list(right_finals)))
            print(' '.join(list(output_final)))

        except Uncorrect_value as m:
            self.output_value_browser.setText(f"Ошибка: {m}") 



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
