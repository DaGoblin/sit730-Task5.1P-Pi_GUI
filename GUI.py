from PyQt5 import QtWidgets
from PyQt5.QtGui import QCloseEvent
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(6, GPIO.OUT)

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setGeometry(20, 20, 300, 300)
        self.setWindowTitle("Task 5.1P")
        self.initUI()
        allLEDsOff()
    
    def initUI(self):
        self.radioBtn1 = QtWidgets.QRadioButton(self)
        self.radioBtn1.setText("red")
        self.radioBtn1.move(50,50)
        self.radioBtn1.toggled.connect(self.redLED)

        self.radioBtn2 = QtWidgets.QRadioButton(self)
        self.radioBtn2.setText("green")
        self.radioBtn2.move(50,100)
        self.radioBtn2.toggled.connect(self.greenLED)

        self.radioBtn3 = QtWidgets.QRadioButton(self)
        self.radioBtn3.setText("blue")
        self.radioBtn3.move(50,150)
        self.radioBtn3.toggled.connect(self.blueLED)

    def redLED(self):
        if self.radioBtn1.isChecked():
            GPIO.output(5, GPIO.HIGH)
        else:
            GPIO.output(5, GPIO.LOW)

    def greenLED(self):
        if self.radioBtn2.isChecked():
            GPIO.output(6, GPIO.HIGH)
        else:
            GPIO.output(6, GPIO.LOW)


    def blueLED(self):
        if self.radioBtn3.isChecked():
            GPIO.output(26, GPIO.HIGH)
        else:
            GPIO.output(26, GPIO.LOW)

    def closeEvent(self, *args, **kwargs):
        super(QMainWindow, self).closeEvent(*args, **kwargs)
        allLEDsOff()

def window():
    app = QApplication(sys.argv)
    win = MainWindow()

    win.show()
    sys.exit(app.exec_())

def allLEDsOff():
    GPIO.output(26, GPIO.LOW)
    GPIO.output(6, GPIO.LOW)
    GPIO.output(5, GPIO.LOW)

window()