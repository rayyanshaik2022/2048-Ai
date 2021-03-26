from PyQt5 import QtCore, QtGui, QtWidgets
import gui

class Ui_test(object):
    def setupUi(self, test):
        test.setObjectName("test")
        test.resize(400, 200)
        self.pushButton = QtWidgets.QPushButton(test)
        self.pushButton.setGeometry(QtCore.QRect(241, 110, 121, 32))
        self.pushButton.setObjectName("pushButton")
        
        self.pushButton.clicked.connect(self.btnstate)
        
        self.horizontalSlider = QtWidgets.QSlider(test)
        self.horizontalSlider.setGeometry(QtCore.QRect(20, 60, 160, 22))
        self.horizontalSlider.setMaximum(100)
        self.horizontalSlider.setProperty("value", 0)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.comboBox = QtWidgets.QComboBox(test)
        self.comboBox.setGeometry(QtCore.QRect(230, 60, 141, 32))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalSlider_2 = QtWidgets.QSlider(test)
        self.horizontalSlider_2.setGeometry(QtCore.QRect(20, 120, 160, 22))
        self.horizontalSlider_2.setMinimum(1)
        self.horizontalSlider_2.setMaximum(60)
        self.horizontalSlider_2.setProperty("value", 30)
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setObjectName("horizontalSlider_2")
        self.label = QtWidgets.QLabel(test)
        self.label.setGeometry(QtCore.QRect(80, 40, 58, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(test)
        self.label_2.setGeometry(QtCore.QRect(70, 100, 71, 16))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(test)
        QtCore.QMetaObject.connectSlotsByName(test)

    def retranslateUi(self, test):
        _translate = QtCore.QCoreApplication.translate
        test.setWindowTitle(_translate("test", "2048 Monte Carlo AI"))
        self.pushButton.setText(_translate("test", "Run"))
        self.comboBox.setItemText(0, _translate("test", "Default"))
        self.comboBox.setItemText(1, _translate("test", "Tokyo Night"))
        self.comboBox.setItemText(2, _translate("test", "Tortoise"))
        self.label.setText(_translate("test", "Delay"))
        self.label_2.setText(_translate("test", "Simulations"))
    
    def btnstate(self):
        
        delay = self.horizontalSlider.value()/20
        simulations = self.horizontalSlider_2.value()
        theme = self.comboBox.currentText()
        print(theme)
        # create the game object
        g = gui.Gui(gui.Game(), delay, simulations, theme)
        g.new()
        g.run()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    test = QtWidgets.QWidget()
    ui = Ui_test()
    ui.setupUi(test)
    test.show()
    sys.exit(app.exec_())
