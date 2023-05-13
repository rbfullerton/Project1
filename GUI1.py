from PyQt5 import QtCore, QtGui, QtWidgets
from GUI2 import Ui_MainWindow2


class Ui_MainWindow1(object):
    def openWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow2()
        self.ui.setupUi(self.window)
        self.window.show()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.MainLabel = QtWidgets.QLabel(self.centralwidget)
        self.MainLabel.setGeometry(QtCore.QRect(160, 40, 471, 71))
        font = QtGui.QFont()
        font.setPointSize(31)
        self.MainLabel.setFont(font)
        self.MainLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.MainLabel.setObjectName("MainLabel")
        self.ImageStart = QtWidgets.QLabel(self.centralwidget)
        self.ImageStart.setEnabled(True)
        self.ImageStart.setGeometry(QtCore.QRect(210, 130, 381, 301))
        font = QtGui.QFont()
        font.setPointSize(6)
        self.ImageStart.setFont(font)
        self.ImageStart.setText("")
        self.ImageStart.setPixmap(QtGui.QPixmap("GUI/th-1054332373.jpg"))
        self.ImageStart.setScaledContents(True)
        self.ImageStart.setObjectName("ImageStart")
        self.ButtonBegin = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.openWindow())
        self.ButtonBegin.setGeometry(QtCore.QRect(220, 460, 391, 71))
        font = QtGui.QFont()
        font.setPointSize(35)
        self.ButtonBegin.setFont(font)
        self.ButtonBegin.setObjectName("ButtonBegin")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Grocery Shopper"))
        self.MainLabel.setText(_translate("MainWindow", "Grocery Shopper"))
        self.ButtonBegin.setText(_translate("MainWindow", "BEGIN"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow1()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
