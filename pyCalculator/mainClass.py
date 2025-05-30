# Import Modules
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QGridLayout, QLineEdit


class CalcApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("pyCalculator")
        self.resize(300, 300)

        # Create App Widgets
        self.text_box = QLineEdit()
        self.grid = QGridLayout()

        self.button_text = ['7', '8', '9', '/',
                            '4', '5', '6', '*',
                            '1', '2', '3', '-',
                            '0', '.', '=', '+']

        # Loop for Creating Buttons
        row = 0
        col = 0
        for text in self.button_text:
            button = QPushButton(text)
            button.clicked.connect(self.button_clicked)
            self.grid.addWidget(button, row, col)
            col += 1
            if col > 3:
                col = 0
                row += 1

        self.clear = QPushButton("C")
        self.delete = QPushButton("Delete")
        self.clear.clicked.connect(self.button_clicked)
        self.delete.clicked.connect(self.button_clicked)

        # Layouts
        self.master_layout = QVBoxLayout()
        self.master_layout.addWidget(self.text_box)
        self.master_layout.addLayout(self.grid)

        self.button_row = QHBoxLayout()
        self.button_row.addWidget(self.clear)
        self.button_row.addWidget(self.delete)
        self.master_layout.addLayout(self.button_row)

        self.setLayout(self.master_layout)

    def button_clicked(self):
        button = self.sender()
        text = button.text()

        if text == '=':
            symbol = self.text_box.text()
            try:
                res = eval(symbol)
                self.text_box.setText(str(res))
            except Exception as e:
                print("Error:", e)
        elif text == 'C':
            self.text_box.clear()
        elif text == 'Delete':
            current_value = self.text_box.text()
            self.text_box.setText(current_value[:-1])
        else:
            current_value = self.text_box.text()
            self.text_box.setText(current_value + text)


# Run App
if __name__ == "__main__":
    app = QApplication([])
    main_window = CalcApp()
    main_window.show()
    app.exec_()
