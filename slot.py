import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit, QHBoxLayout
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class SlotMachine(QWidget):
    def __init__(self):
        super().__init__()
        self.balance = 100
        self.spin_value = 10

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Slot Machine')
        self.setGeometry(100, 100, 400, 300)
        self.setStyleSheet("background-color: #2c3e50; color: #ecf0f1;")

        layout = QVBoxLayout()

        title = QLabel('Slot Machine')
        title.setFont(QFont('Arial', 30))
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)

        self.slot_layout = QHBoxLayout()
        self.reel1 = QLabel("🍒")
        self.reel2 = QLabel("🍒")
        self.reel3 = QLabel("🍒")
        
        for reel in [self.reel1, self.reel2, self.reel3]:
            reel.setFont(QFont('Arial', 50))
            reel.setAlignment(Qt.AlignCenter)
            reel.setStyleSheet("background-color: #34495e; border-radius: 10px; padding: 10px;")
            self.slot_layout.addWidget(reel)

        layout.addLayout(self.slot_layout)

        self.spin_button = QPushButton('Spin')
        self.spin_button.setFont(QFont('Arial', 20))
        self.spin_button.setStyleSheet("background-color: #e74c3c; border-radius: 5px; padding: 10px;")
        self.spin_button.clicked.connect(self.spin)
        layout.addWidget(self.spin_button, alignment=Qt.AlignCenter)

        self.balance_label = QLabel(f"Balance: ${self.balance}")
        self.balance_label.setFont(QFont('Arial', 20))
        self.balance_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.balance_label)

        self.spin_value_label = QLabel("Spin Value:")
        self.spin_value_label.setFont(QFont('Arial', 20))
        layout.addWidget(self.spin_value_label)

        self.spin_value_entry = QLineEdit()
        self.spin_value_entry.setFont(QFont('Arial', 20))
        self.spin_value_entry.setText(str(self.spin_value))
        layout.addWidget(self.spin_value_entry)

        self.update_button = QPushButton('Update Spin Value')
        self.update_button.setFont(QFont('Arial', 20))
        self.update_button.setStyleSheet("background-color: #3498db; border-radius: 5px; padding: 10px;")
        self.update_button.clicked.connect(self.update_spin_value)
        layout.addWidget(self.update_button, alignment=Qt.AlignCenter)

        self.result_label = QLabel("")
        self.result_label.setFont(QFont('Arial', 20))
        self.result_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.result_label)

        self.setLayout(layout)

    def spin(self):
        symbols = ["🍒", "🔔", "🍋", "⭐", "🍉", "7️⃣"]
        result1 = random.choice(symbols)
        result2 = random.choice(symbols)
        result3 = random.choice(symbols)

        self.reel1.setText(result1)
        self.reel2.setText(result2)
        self.reel3.setText(result3)

        if result1 == result2 == result3:
            self.balance += self.spin_value * 10
            self.result_label.setText("Jackpot!")
            self.result_label.setStyleSheet("color: green;")
        else:
            self.balance -= self.spin_value
            self.result_label.setText("Try Again!")
            self.result_label.setStyleSheet("color: red;")

        self.balance_label.setText(f"Balance: ${self.balance}")

    def update_spin_value(self):
        self.spin_value = int(self.spin_value_entry.text())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = SlotMachine()
    ex.show()
    sys.exit(app.exec_())
