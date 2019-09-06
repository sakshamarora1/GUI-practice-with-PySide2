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

        v_box = QVBoxLayout()
        v_box.addWidget(self.line)
        
        h_box = QHBoxLayout()
        h_box.addWidget(self.clearbtn)
        h_box.addWidget(self.printbtn)

        v_box.addLayout(h_box)
        self.setLayout(v_box)

        self.clearbtn.setSizePolicy(QSizePolicy.Minimum,QSizePolicy.Minimum)
        self.printbtn.setSizePolicy(QSizePolicy.Minimum,QSizePolicy.Minimum)
        self.line.setSizePolicy(QSizePolicy.Minimum,QSizePolicy.Minimum)

        self.clearbtn.clicked.connect(self.btn_click)
        self.printbtn.clicked.connect(self.btn_click)

        self.setWindowTitle("Line Edit")
        self.show()

    def btn_click(self):
        sender = self.sender()
        if sender.text() == "Print":
            print(self.line.text())
        else:
            self.line.clear()

app = QApplication(sys.argv)
windoe = Window()
sys,exit(app.exec_())