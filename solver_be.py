from PyQt6 import QtCore, QtGui, QtWidgets
from solver import Solver
from chempy import balance_stoichiometry
from PyQt6 import QtCore, QtGui, QtWidgets
from chemlib import Compound
import sqlite3
import sys


con = sqlite3.connect("users.db")
cur = con.cursor()


class Uncorrect_value(Exception):
    pass

class Unknow_error(Exception):
    pass


def create_database():
    conn = sqlite3.connect('tasks_history.db')
    cursor = conn.cursor()
    conn.commit()
    conn.close()


def save_task_to_history(user_id, type_of_task, input_text):
    conn = sqlite3.connect('tasks_history.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        INSERT INTO history (user_id, task_type, text_task)
        VALUES (?, ?, ?)
    ''', (user_id, type_of_task, input_text))
    
    conn.commit()
    conn.close()


class Solv(Solver): 
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Решатель")


    def on_combobox_changed(self, index):
        selected_value = self.comboBox.currentText()
        self.call_function(selected_value)


    def call_function(self, value):
        if value == "Уравнять Реакцию":
            self.Solve_Example()
        elif value == "Вычислить молякулярную массу вещества":
            self.Moll_Mass()
        elif value == "массовая доля n-ого элемента в веществе":
            self.Moll_Mass_in()
            print(1)
        

    def Solve_Example(self):
        try:
            output_final = []
            input_value = self.input_value_browser.toPlainText()
            input_value = input_value.split(" ")
            reagent = []
            product = []
            reagent_ready = []
            product_ready = []

           
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

           
            output_value = balance_stoichiometry(reagent_ready, product_ready)
            reagent_ready = output_value[0]
            product_ready = output_value[1]

            left_final = []
            right_final = []

          
            for key, value in reagent_ready.items():
                if value == 1: 
                    left_final.append(f"{key}")
                else:
                    left_final.append(f"{value}{key}")

            for key, value in product_ready.items():
                if value == 1:  
                    right_final.append(f"{key}")
                else:
                    right_final.append(f"{value}{key}")

        
            right_final = list(dict.fromkeys(right_final))

            output_final.append(' + '.join(left_final))
            output_final.append("=")
            output_final.append(' + '.join(right_final))
            
            self.output_value_browser.setText(' '.join(output_final)) 


            user_id = 1 
            type_of_task = "Уравнять Реакцию"
            input_text = self.input_value_browser.toPlainText()
            save_task_to_history(user_id, type_of_task, input_text)
        except Exception as e:
            self.output_value_browser.setText(f"Ошибка: {e}")


    def Moll_Mass(self):
        try:
            input_value = self.input_value_browser.toPlainText()
            input_value = Compound(input_value)
            self.output_value_browser.setText('%.0f' % input_value.molar_mass())
        except Exception as e:
            self.output_value_browser.setText(f"Ошибка: {e}")

    
    def Moll_Mass_in(self):
        try:
            input_text = self.input_value_browser.toPlainText().split(",")
            print(input_text)
            item = Compound(input_text[0])
            element = input_text[1]
            print(item, element)  
            element.lstrip()
            self.output_value_browser.setText('%.0f' % item.percentage_by_mass(element))
            

        except Exception as e:
            self.output_value_browser.setText(f"Ошибка: {e}")


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)

    def start(self):
        if __name__ == "__main__":
            import sys
            app = QtWidgets.QApplication(sys.argv)
            Form = QtWidgets.QWidget()
            ui = Solv()
            ui.setupUi(Form)
            Form.show()
            sys.excepthook = except_hook
            sys.exit(app.exec())
