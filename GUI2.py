from PyQt5 import QtCore, QtGui, QtWidgets
from GUI3 import Ui_MainWindow3

class Ui_MainWindow2(object):
    NumHam = 6
    NumBurger = 5
    NumTurkey = 7
    NumChicken = 4
    NumLettuce = 4
    NumOnion = 1.5
    NumCarrot = 6
    NumCucumber = 2
    NumIce = 6
    NumPie = 10
    NumCake = 12

    def openWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow3()
        self.ui.setupUi(self.window)
        self.window.show()

    def click(self):
        def Ham():
            if self.HamBox.isChecked() and int(self.HamNum.value()) != 0:
                self.NumHam = int(self.HamNum.value() * self.NumHam)
                return f"Ham ({self.HamNum.value()}) : ${self.NumHam:.2f}"
            else:
                self.NumHam = 0
                return " "

        def Burger():
            if self.BurgerBox.isChecked() and int(self.BurgerNum.value()) != 0:
                self.NumBurger = int(self.BurgerNum.value() * self.NumBurger)
                return f'Hamburger ({self.BurgerNum.value()}) : ${self.NumBurger:.2f}'
            else:
                self.NumBurger = 0
                return " "

        def Turkey():
            if self.TurkeyBox.isChecked() and int(self.TurkeyNum.value()) != 0:
                self.NumTurkey = int(self.TurkeyNum.value() * self.NumTurkey)
                return f"Turkey ({self.TurkeyNum.value()}) : ${self.NumTurkey:.2f}"
            else:
                self.NumTurkey = 0
                return " "

        def Chicken():
            if self.ChickenBox.isChecked() and int(self.ChickenNum.value()) != 0:
                self.NumChicken = int(self.ChickenNum.value() * self.NumChicken)
                return f"Chicken ({self.ChickenNum.value()}) : ${self.NumChicken:.2f}"
            else:
                self.NumChicken = 0
                return " "

        def Lettuce():
            if self.LettuceBox.isChecked() and int(self.LettuceNum.value()) != 0:
                self.NumLettuce = int(self.LettuceNum.value() * self.NumLettuce)
                return f"Lettuce ({self.LettuceNum.value()}) : ${self.NumLettuce:.2f}"
            else:
                self.NumLettuce = 0
                return " "

        def Onion():
            if self.OnionBox.isChecked() and int(self.OnionNum.value()) != 0:
                self.NumOnion = int(self.OnionNum.value() * self.NumOnion)
                return f"Onion ({self.OnionNum.value()}) : ${self.NumOnion:.2f}"
            else:
                self.NumOnion = 0
                return " "

        def Carrot():
            if self.CarrotBox.isChecked() and int(self.CarrotNum.value()) != 0:
                self.NumCarrot = int(self.CarrotNum.value() * self.NumCarrot)
                return f"Carrot ({self.CarrotNum.value()}) : ${self.NumCarrot:.2f}"
            else:
                self.NumCarrot = 0
                return " "

        def Cucumber():
            if self.CucumberBox.isChecked() and int(self.CucumberNum.value()) != 0:
                self.NumCucumber = int(self.CucumberNum.value() * self.NumCucumber)
                return f"Cucumber ({self.CucumberNum.value()}) : ${self.NumCucumber:.2f}"
            else:
                self.NumCucumber = 0
                return " "

        def Ice():
            if self.IceBox.isChecked() and int(self.IceNum.value()) != 0:
                self.NumIce = int(self.IceNum.value() * self.NumIce)
                return f"Ice ({self.IceNum.value()}) : ${self.NumIce:.2f}"
            else:
                self.NumIce = 0
                return " "

        def Pie():
            if self.PieBox.isChecked() and int(self.PieNum.value()) != 0:
                self.NumPie = int(self.PieNum.value() * self.NumPie)
                return f"Pie ({self.PieNum.value()}) : ${self.NumPie:.2f}"
            else:
                self.NumPie = 0
                return " "

        def Cake():
            if self.CakeBox.isChecked() and int(self.CakeNum.value()) != 0:
                self.NumCake = int(self.CakeNum.value() * self.NumCake)
                return f"Cake ({self.CakeNum.value()}) : ${self.NumCake:.2f}"
            else:
                self.NumCake = 0
                return " "
        self.ui.EndSummary.setText(f'{Ham()} \n{Burger()} \n{Turkey()} \n{Chicken()} \n{Lettuce()} \n{Onion()} \n{Carrot()} \n{Cucumber()} \n{Ice()} \n{Pie()} \n{Cake()}')
        self.ui.TotalPrice.setText(f'${self.NumHam + self.NumBurger + self.NumTurkey + self.NumChicken + self.NumLettuce + self.NumOnion + self.NumCarrot + self.NumCucumber + self.NumHam + self.NumIce+ self.NumPie + self.NumCake :.2f}')
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.MainLabelChoice = QtWidgets.QLabel(self.centralwidget)
        self.MainLabelChoice.setGeometry(QtCore.QRect(0, 10, 471, 71))
        font = QtGui.QFont()
        font.setPointSize(31)
        self.MainLabelChoice.setFont(font)
        self.MainLabelChoice.setAlignment(QtCore.Qt.AlignCenter)
        self.MainLabelChoice.setObjectName("MainLabelChoice")
        self.MeatLabel = QtWidgets.QLabel(self.centralwidget)
        self.MeatLabel.setGeometry(QtCore.QRect(30, 100, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(19)
        self.MeatLabel.setFont(font)
        self.MeatLabel.setObjectName("MeatLabel")
        self.VeggieLabel = QtWidgets.QLabel(self.centralwidget)
        self.VeggieLabel.setGeometry(QtCore.QRect(340, 100, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(19)
        self.VeggieLabel.setFont(font)
        self.VeggieLabel.setObjectName("VeggieLabel")
        self.DessertLabel = QtWidgets.QLabel(self.centralwidget)
        self.DessertLabel.setGeometry(QtCore.QRect(570, 100, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(19)
        self.DessertLabel.setFont(font)
        self.DessertLabel.setObjectName("DessertLabel")
        self.CheckOut = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.openWindow())
        self.CheckOut.setGeometry(QtCore.QRect(410, 430, 341, 81))
        self.CheckOut.setMinimumSize(QtCore.QSize(0, 0))
        self.CheckOut.setMaximumSize(QtCore.QSize(800, 600))
        font = QtGui.QFont()
        font.setPointSize(27)
        self.CheckOut.setFont(font)
        self.CheckOut.setObjectName("CheckOut")
        self.HamBox = QtWidgets.QCheckBox(self.centralwidget)
        self.HamBox.setGeometry(QtCore.QRect(30, 160, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.HamBox.setFont(font)
        self.HamBox.setObjectName("HamBox")
        self.BurgerBox = QtWidgets.QCheckBox(self.centralwidget)
        self.BurgerBox.setGeometry(QtCore.QRect(30, 210, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.BurgerBox.setFont(font)
        self.BurgerBox.setObjectName("BurgerBox")
        self.TurkeyBox = QtWidgets.QCheckBox(self.centralwidget)
        self.TurkeyBox.setGeometry(QtCore.QRect(30, 260, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.TurkeyBox.setFont(font)
        self.TurkeyBox.setObjectName("TurkeyBox")
        self.ChickenBox = QtWidgets.QCheckBox(self.centralwidget)
        self.ChickenBox.setGeometry(QtCore.QRect(30, 310, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.ChickenBox.setFont(font)
        self.ChickenBox.setObjectName("ChickenBox")
        self.HamNum = QtWidgets.QSpinBox(self.centralwidget)
        self.HamNum.setGeometry(QtCore.QRect(200, 170, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.HamNum.setFont(font)
        self.HamNum.setObjectName("HamNum")
        self.BurgerNum = QtWidgets.QSpinBox(self.centralwidget)
        self.BurgerNum.setGeometry(QtCore.QRect(200, 220, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.BurgerNum.setFont(font)
        self.BurgerNum.setObjectName("BurgerNum")
        self.TurkeyNum = QtWidgets.QSpinBox(self.centralwidget)
        self.TurkeyNum.setGeometry(QtCore.QRect(200, 270, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.TurkeyNum.setFont(font)
        self.TurkeyNum.setObjectName("TurkeyNum")
        self.ChickenNum = QtWidgets.QSpinBox(self.centralwidget)
        self.ChickenNum.setGeometry(QtCore.QRect(200, 320, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ChickenNum.setFont(font)
        self.ChickenNum.setObjectName("ChickenNum")
        self.OnionBox = QtWidgets.QCheckBox(self.centralwidget)
        self.OnionBox.setGeometry(QtCore.QRect(310, 210, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.OnionBox.setFont(font)
        self.OnionBox.setObjectName("OnionBox")
        self.LettuceBox = QtWidgets.QCheckBox(self.centralwidget)
        self.LettuceBox.setGeometry(QtCore.QRect(310, 160, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.LettuceBox.setFont(font)
        self.LettuceBox.setObjectName("LettuceBox")
        self.CucumberBox = QtWidgets.QCheckBox(self.centralwidget)
        self.CucumberBox.setGeometry(QtCore.QRect(310, 310, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.CucumberBox.setFont(font)
        self.CucumberBox.setObjectName("CucumberBox")
        self.CarrotNum = QtWidgets.QSpinBox(self.centralwidget)
        self.CarrotNum.setGeometry(QtCore.QRect(480, 270, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.CarrotNum.setFont(font)
        self.CarrotNum.setObjectName("CarrotNum")
        self.CarrotBox = QtWidgets.QCheckBox(self.centralwidget)
        self.CarrotBox.setGeometry(QtCore.QRect(310, 260, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.CarrotBox.setFont(font)
        self.CarrotBox.setObjectName("CarrotBox")
        self.OnionNum = QtWidgets.QSpinBox(self.centralwidget)
        self.OnionNum.setGeometry(QtCore.QRect(480, 220, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.OnionNum.setFont(font)
        self.OnionNum.setObjectName("OnionNum")
        self.LettuceNum = QtWidgets.QSpinBox(self.centralwidget)
        self.LettuceNum.setGeometry(QtCore.QRect(480, 170, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.LettuceNum.setFont(font)
        self.LettuceNum.setObjectName("LettuceNum")
        self.CucumberNum = QtWidgets.QSpinBox(self.centralwidget)
        self.CucumberNum.setGeometry(QtCore.QRect(480, 320, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.CucumberNum.setFont(font)
        self.CucumberNum.setObjectName("CucumberNum")
        self.IceNum = QtWidgets.QSpinBox(self.centralwidget)
        self.IceNum.setGeometry(QtCore.QRect(730, 170, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.IceNum.setFont(font)
        self.IceNum.setObjectName("IceNum")
        self.PieBox = QtWidgets.QCheckBox(self.centralwidget)
        self.PieBox.setGeometry(QtCore.QRect(560, 210, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.PieBox.setFont(font)
        self.PieBox.setObjectName("PieBox")
        self.IceBox = QtWidgets.QCheckBox(self.centralwidget)
        self.IceBox.setGeometry(QtCore.QRect(560, 160, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.IceBox.setFont(font)
        self.IceBox.setObjectName("IceBox")
        self.PieNum = QtWidgets.QSpinBox(self.centralwidget)
        self.PieNum.setGeometry(QtCore.QRect(730, 220, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.PieNum.setFont(font)
        self.PieNum.setObjectName("PieNum")
        self.CakeNum = QtWidgets.QSpinBox(self.centralwidget)
        self.CakeNum.setGeometry(QtCore.QRect(730, 270, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.CakeNum.setFont(font)
        self.CakeNum.setObjectName("CakeNum")
        self.CakeBox = QtWidgets.QCheckBox(self.centralwidget)
        self.CakeBox.setGeometry(QtCore.QRect(560, 260, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.CakeBox.setFont(font)
        self.CakeBox.setObjectName("CakeBox")
        self.BillOut = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.click())
        self.BillOut.setGeometry(QtCore.QRect(30, 430, 341, 81))
        self.BillOut.setMinimumSize(QtCore.QSize(0, 0))
        self.BillOut.setMaximumSize(QtCore.QSize(800, 600))
        font = QtGui.QFont()
        font.setPointSize(27)
        self.BillOut.setFont(font)
        self.BillOut.setObjectName("BillOut")
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
        self.MainLabelChoice.setText(_translate("MainWindow", "Grocery Shopper"))
        self.MeatLabel.setText(_translate("MainWindow", "Meat"))
        self.VeggieLabel.setText(_translate("MainWindow", "Vegetables "))
        self.DessertLabel.setText(_translate("MainWindow", "Desserts"))
        self.CheckOut.setText(_translate("MainWindow", "Check Out"))
        self.HamBox.setText(_translate("MainWindow", "Ham"))
        self.BurgerBox.setText(_translate("MainWindow", "Hamburger"))
        self.TurkeyBox.setText(_translate("MainWindow", "Turkey"))
        self.ChickenBox.setText(_translate("MainWindow", "Chicken"))
        self.OnionBox.setText(_translate("MainWindow", "Onion"))
        self.LettuceBox.setText(_translate("MainWindow", "Lettuce"))
        self.CucumberBox.setText(_translate("MainWindow", "Cucumber"))
        self.CarrotBox.setText(_translate("MainWindow", "Carrot"))
        self.PieBox.setText(_translate("MainWindow", "Pie"))
        self.IceBox.setText(_translate("MainWindow", "Ice Cream"))
        self.CakeBox.setText(_translate("MainWindow", "Cake"))
        self.BillOut.setText(_translate("MainWindow", "Show Bill"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow2()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
