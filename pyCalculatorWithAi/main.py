from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QPushButton, 
                            QVBoxLayout, QHBoxLayout, QGridLayout, QLineEdit)
from PyQt5.QtGui import QKeyEvent
import re

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("pyCalculator")
        self.resize(300, 400)
        self.setStyleSheet("""
            QWidget {
                background-color: #2b2b2b;
                color: #ffffff;
                font-size: 18px;
            }
            QPushButton {
                background-color: #3b3b3b;
                border: 1px solid #4b4b4b;
                border-radius: 5px;
                padding: 10px;
                min-width: 50px;
            }
            QPushButton:hover {
                background-color: #4b4b4b;
            }
            QPushButton:pressed {
                background-color: #5b5b5b;
            }
            QLineEdit {
                background-color: #1b1b1b;
                border: 2px solid #4b4b4b;
                border-radius: 5px;
                padding: 10px;
                font-size: 24px;
            }
            #equals {
                background-color: #ff9500;
                color: white;
            }
            #clear, #delete {
                background-color: #d4d4d2;
                color: black;
            }
            #operator {
                background-color: #ff9500;
                color: white;
            }
        """)
        
        self.init_ui()
        
    def init_ui(self):
        # Create widgets
        self.text_box = QLineEdit()
        self.text_box.setAlignment(Qt.AlignRight)
        self.text_box.setReadOnly(True)
        self.text_box.setObjectName("display")
        
        # Button layout
        self.grid = QGridLayout()
        self.grid.setSpacing(5)
        
        # Button texts
        button_text = [
            ('7', '8', '9', '/'),
            ('4', '5', '6', '*'),
            ('1', '2', '3', '-'),
            ('0', '.', '=', '+')
        ]
        
        # Create buttons
        for row, buttons in enumerate(button_text):
            for col, text in enumerate(buttons):
                button = QPushButton(text)
                button.clicked.connect(self.button_clicked)
                
                # Set button IDs for styling
                if text in ['/', '*', '-', '+']:
                    button.setObjectName("operator")
                elif text == '=':
                    button.setObjectName("equals")
                
                self.grid.addWidget(button, row, col)
        
        # Special buttons
        self.clear = QPushButton("C")
        self.clear.setObjectName("clear")
        self.clear.clicked.connect(self.clear_input)
        
        self.delete = QPushButton("⌫")
        self.delete.setObjectName("delete")
        self.delete.clicked.connect(self.delete_last)
        
        # Layout
        button_row = QHBoxLayout()
        button_row.addWidget(self.clear)
        button_row.addWidget(self.delete)
        
        master_layout = QVBoxLayout()
        master_layout.addWidget(self.text_box)
        master_layout.addLayout(self.grid)
        master_layout.addLayout(button_row)
        
        self.setLayout(master_layout)
    
    def keyPressEvent(self, event):
        key = event.text()
        
        if key in '0123456789':
            self.append_text(key)
        elif key in '+-*/.=':
            self.append_text(key)
        elif event.key() == Qt.Key_Backspace:
            self.delete_last()
        elif event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return:
            self.calculate()
        elif event.key() == Qt.Key_Escape:
            self.clear_input()
    
    def button_clicked(self):
        button = self.sender()
        text = button.text()
        
        if text == '=':
            self.calculate()
        else:
            self.append_text(text)
    
    def append_text(self, text):
        current = self.text_box.text()
        self.text_box.setText(current + text)
    
    def delete_last(self):
        current = self.text_box.text()
        self.text_box.setText(current[:-1])
    
    def clear_input(self):
        self.text_box.clear()
    
    def calculate(self):
        expression = self.text_box.text()
        
        try:
            # Safer evaluation using regex validation
            if not self.validate_expression(expression):
                raise ValueError("Invalid expression")
            
            # Replace × with * and ÷ with / for eval
            expression = expression.replace('×', '*').replace('÷', '/')
            
            # Evaluate the expression
            result = str(eval(expression))
            
            # Handle decimal places (optional)
            if '.' in result:
                result = '{0:.8f}'.format(float(result)).rstrip('0').rstrip('.')
            
            self.text_box.setText(result)
        except Exception as e:
            self.text_box.setText("Error")
    
    def validate_expression(self, expr):
        # Basic validation using regex
        pattern = r'^[\d\+\-\*\/\.\s]+$'
        return re.match(pattern, expr) is not None

if __name__ == "__main__":
    app = QApplication([])
    calculator = Calculator()
    calculator.show()
    app.exec_()