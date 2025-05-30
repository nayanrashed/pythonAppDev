# Import Modules
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout,QHBoxLayout, QGridLayout, QLineEdit



# Main App Objects and Settings
app = QApplication([])
main_window = QWidget()
main_window.setWindowTitle("pyCalculator")
main_window.resize(300,300)


#Create all App Objects/Widgets
title = QLabel("Calculator Screen")
text_box = QLineEdit()
grid = QGridLayout()

button_text = ['7','8','9','/','4','5','6','*','1','2','3','-','0','.','=','+']

clear = QPushButton("C")
delete= QPushButton('Delete')


def button_clicked():
 button = app.sender()
 text = button.text()

 if text == '=':
  symbol = text_box.text()
  try:
   res = eval(symbol)
   text_box.setText(str(res))
  except Exception as e:
   print("error",e)  
 elif text == 'C':
  text_box.clear() 
 elif text == 'Delete':
  current_value = text_box.text()
  text_box.setText(current_value[:-1])
 else:
  current_value = text_box.text()
  text_box.setText(current_value+text)


#Loop for Creating Buttons
row=0
col=0

for text in button_text:
 button=QPushButton(text)
 button.clicked.connect(button_clicked)
 grid.addWidget(button,row,col)
 col+=1
 if col>3:
  col=0
  row+=1

#All Design
master_layout = QVBoxLayout()
master_layout.addWidget(text_box)
master_layout.addLayout(grid)

button_row = QHBoxLayout()
button_row.addWidget(clear)
button_row.addWidget(delete)

master_layout.addLayout(button_row)

main_window.setLayout(master_layout)

clear.clicked.connect(button_clicked)
delete.clicked.connect(button_clicked)
#Show-Run App
main_window.show()
app.exec_()