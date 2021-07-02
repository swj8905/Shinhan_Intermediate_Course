from PyQt5.QtWidgets import *
import sys
from PyQt5 import uic
import os
from math import *

def resource_path(relative_path):
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

os.environ["QT_MAC_WANTS_LAYER"] = "1" # 맥 쓰시는 분들만!

# ui_file = "./calculator.ui"
ui_file = resource_path("./calculator.ui")

class MainDialog(QDialog):
    def __init__(self):
        QDialog.__init__(self, None)
        uic.loadUi(ui_file, self)

        self.button.clicked.connect(self.calculate)

    def calculate(self):
        user_input = self.inputbox.text()
        result = eval(user_input)
        self.history.append(f"{user_input}\n= {result}\n")
        self.inputbox.clear()

QApplication.setStyle("fusion")
app = QApplication(sys.argv)
main_dialog = MainDialog()
main_dialog.show()
sys.exit(app.exec_())