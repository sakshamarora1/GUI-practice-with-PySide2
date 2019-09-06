import sys
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.line = QLineEdit()
        self.clearbtn = QPushButton("Clear")
        self.printbtn = QPushButton("Print")
        self.slider = QSlider(Qt.Horizontal)
        
        self.slider.setMinimum(0)
        self.slider.setMaximum(100)
        self.slider.setValue(30)
        self.slider.setTickInterval(20)
        self.slider.setTickPosition(QSlider.TicksAbove)
        self.slider.setSingleStep(2)

        v_box = QVBoxLayout()
        v_box.addWidget(self.line)
        
        h_box = QHBoxLayout()
        h_box.addWidget(self.clearbtn)
        h_box.addWidget(self.printbtn)
        
        v_box.addLayout(h_box)
        v_box.addWidget(self.slider)
        self.setLayout(v_box)

        self.setWindowTitle("Slider")
        self.show()

        self.printbtn.clicked.connect(lambda: self.btn_click(self.printbtn, "hello from print"))
        self.slider.valueChanged.connect(self.v_change)
        self.clearbtn.clicked.connect(lambda: self.btn_click(self.clearbtn, "hello from clear"))

    def btn_click(self,b,string):

        if b.text() == "Print":
            print(self.line.text())
        
        elif b.text() == "Clear":
            self.line.clear()
        
        print(string)

    def v_change(self):
        myval = str(self.slider.value())
        self.line.setText(myval)

app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())