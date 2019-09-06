import sys
from PySide2.QtWidgets import *

class Window(QWidget):

    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.label = QLabel()
        self.box = QRadioButton("Do you like dogs?")
        self.box2 = QRadioButton("Do you like cats?")
        self.box3 = QRadioButton("Do you hate both of them?")

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.box)
        layout.addWidget(self.box2)
        layout.addWidget(self.box3)

        self.setLayout(layout)

        self.box.toggled.connect(lambda: self.btn_click(self.box.isChecked(),self.box2.isChecked(),self.box3.isChecked(),self.label))
        self.box2.toggled.connect(lambda: self.btn_click(self.box.isChecked(),self.box2.isChecked(),self.box3.isChecked(),self.label))
        self.box3.toggled.connect(lambda: self.btn_click(self.box.isChecked(),self.box2.isChecked(),self.box3.isChecked(),self.label))

        self.setWindowTitle("RadioButton")
        self.show()

    def btn_click(self, box, box2, box3, label):
        if box:
            label.setText("You're awesome!")

        elif box2:
            label.setText("You're a good person.")

        elif box3:
            label.setText("You are a bad person.")

app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())
