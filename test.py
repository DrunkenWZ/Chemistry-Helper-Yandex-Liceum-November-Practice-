import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit
from chemlib import Formula, Reaction

class ChemicalBalancerApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Chemical Reaction Balancer")
        
        self.layout = QVBoxLayout()

        # Ввод реагентов
        self.label_reactants = QLabel("Enter Reactants (e.g., H2 + O2):")
        self.layout.addWidget(self.label_reactants)
        self.reactants_input = QLineEdit()
        self.layout.addWidget(self.reactants_input)

        # Ввод продуктов
        self.label_products = QLabel("Enter Products (e.g., H2O):")
        self.layout.addWidget(self.label_products)
        self.products_input = QLineEdit()
        self.layout.addWidget(self.products_input)

        # Кнопка для уравнивания реакции
        self.balance_button = QPushButton("Balance Reaction")
        self.balance_button.clicked.connect(self.balance_reaction)
        self.layout.addWidget(self.balance_button)

        # Область для вывода результата
        self.result_area = QTextEdit()
        self.result_area.setReadOnly(True)
        self.layout.addWidget(self.result_area)

        self.setLayout(self.layout)

    def balance_reaction(self):
        reactants_str = self.reactants_input.text().strip().split("+")
        products_str = self.products_input.text().strip().split("+")
        
        # Убираем лишние пробелы и создаем объекты формул
        reactants = [Formula(r.strip()) for r in reactants_str]
        products = [Formula(p.strip()) for p in products_str]

        try:
            # Создаем реакцию и уравниваем ее
            reaction = Reaction(reactants, products)
            balanced_reaction = reaction.balance()
            result = f"Balanced Reaction: {balanced_reaction}"
            self.result_area.setPlainText(result)
        except Exception as e:
            self.result_area.setPlainText(f"Error: {str(e)}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ChemicalBalancerApp()
    window.show()
    sys.exit(app.exec())
