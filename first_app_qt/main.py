# Import Modules

# Main App Objects and Settings
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QBoxLayout

#Create all App Object
app = QApplication([])
main_window=QWidget()
main_window.setWindowTitle("Random")
main_window.resize(300,200)


#All Design

#Events

#Show-Run App
main_window.show()
app.exec_()