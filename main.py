from tkinter import Checkbutton

from PyQt6.QtCore import QDate
from PyQt6.QtWidgets import (QApplication, QTableWidgetItem, QMainWindow)
from mainWindow_ui import Ui_MainWindow
import random

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ABC = {"T", 'Y', 'G', 'B', 'S', "J", "3", '8', '2', '5', '1', "7"}
        self.ui.pushButton.clicked.connect(self.password)
    def password(self, i):
        ABC_keys_list = list(self.ABC)
        random_key = random.choice(ABC_keys_list)
        for i in range(4):
            self.ui.lineEdit.setText(random_key)

app = QApplication([])
window = MainWindow()
window.show()
app.exec()