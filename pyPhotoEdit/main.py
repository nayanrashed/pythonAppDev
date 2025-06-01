# Import Modules
import os
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QPushButton,
    QListWidget,
    QComboBox,
    QHBoxLayout,
    QVBoxLayout,
    QLabel,
    QFileDialog,
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap


# App Settings
app = QApplication([])
main_window = QWidget()
main_window.setWindowTitle("pyPhotoEditor")
main_window.resize(900, 700)

# App widgets/Objects
btn_folder = QPushButton("Folder")
file_list = QListWidget()

btn_left = QPushButton("Left")
btn_right = QPushButton("Right")
mirror = QPushButton("Mirror")
sharpness = QPushButton("Sharpness")
gray = QPushButton("B/W")
saturation = QPushButton("Saturation")
contrast = QPushButton("Contrast")
blur = QPushButton("Blur")

# Drop Box
filter_box = QComboBox()
filter_box.addItem("Original")
filter_box.addItem("Left")
filter_box.addItem("Right")
filter_box.addItem("Mirror")
filter_box.addItem("Sharpness")
filter_box.addItem("B/W")
filter_box.addItem("Saturation")
filter_box.addItem("Contrast")
filter_box.addItem("Blur")

pic_box = QLabel("...Image...")

# App Design
master_layout = QHBoxLayout()

col1 = QVBoxLayout()
col2 = QVBoxLayout()

col1.addWidget(btn_folder)
col1.addWidget(file_list)
col1.addWidget(filter_box)
col1.addWidget(btn_left)
col1.addWidget(btn_right)
col1.addWidget(mirror)
col1.addWidget(sharpness)
col1.addWidget(saturation)
col1.addWidget(contrast)
col1.addWidget(blur)
col1.addWidget(gray)

col2.addWidget(pic_box)

master_layout.addLayout(col1, 25)
master_layout.addLayout(col2, 75)
main_window.setLayout(master_layout)

# All App functionality

working_directory = ""


# filter files and extensions
def filter(files, extensions):
    results = []
    for file in files:
        for ext in extensions:
            if file.endswith(ext):
                results.append(file)
    return results


# choose current working directory
def getWorkDirectory():
    global working_directory
    working_directory = QFileDialog.getExistingDirectory()
    extensions = [".jpg", ".jpeg", ".png", ".svg", ".webp"]
    filenames = filter(os.listdir(working_directory), extensions)
    file_list.clear()
    for filename in filenames:
        file_list.addItem(filename)


btn_folder.clicked.connect(getWorkDirectory)


main_window.show()
app.exec_()
