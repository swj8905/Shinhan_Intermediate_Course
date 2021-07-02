from PyQt5.QtWidgets import *
import sys
from PyQt5 import uic
import os

os.environ["QT_MAC_WANTS_LAYER"] = "1" # 맥 쓰시는 분들만!

ui_file = "./test.ui"

class MainDialog(QDialog):
    def __init__(self):
        QDialog.__init__(self, None)
        uic.loadUi(ui_file, self)

        self.button.clicked.connect(self.showString)

    def showString(self):
        result = self.inputbox.text()
        self.label.setText(result)


QApplication.setStyle("fusion")
app = QApplication(sys.argv)
main_dialog = MainDialog()
main_dialog.show()
sys.exit(app.exec_())