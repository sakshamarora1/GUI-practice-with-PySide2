import sys
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *

class boxlayout(QWidget):
    def __init__(self):
        super().__init__()

        layout = QHBoxLayout()
        self.setLayout(layout)

        layout.addStretch()
        label1 = QLabel("Label 1")
        layout.addWidget(label1)
        label2 = QLabel("Label 2")
        layout.addWidget(label2)
        layout2 = QBoxLayout(QBoxLayout.TopToBottom)
        layout.addStretch()
        layout.insertLayout(2,layout2)

        label3 = QLabel("Label 3")
        layout2.addWidget(label3)
        layout2.addStretch()
        label4 = QLabel("Label 4")
        layout2.addWidget(label4)

        self.setStyleSheet("background-color: rgb(230,230,255); margin:10px; padding:50px; border:3px solid rgb(0, 0, 0); font-size: 20px")

app = QApplication(sys.argv)
screen = boxlayout()
screen.show()

sys.exit(app.exec_())