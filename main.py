from PyQt5 import QtWidgets
from GUI1 import Ui_MainWindow1
import sys

class Start(QtWidgets.QMainWindow):
    def __init__(self):
        super(Start, self).__init__()
        self.ui = Ui_MainWindow1()
        self.ui.setupUi(self)
app = QtWidgets.QApplication([])
application = Start()
application.show()
sys.exit(app.exec())



