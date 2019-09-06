import sys
from PySide2.QtWidgets import *

class Window(QWidget):

    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.label = QLabel()
        self.button = QPushButton("Push Me")
        self.checkbox = QCheckBox("Do you like Python?")

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.checkbox)
        layout.addWidget(self.button)

        self.setLayout(layout)

        self.button.clicked.connect(lambda: self.btn_click(self.checkbox.isChecked(),self.label))

        self.setWindowTitle("CheckBox")
        self.show()

    def btn_click(self, check, label):
        if check:
            label.setText("You're awesome !!")

        else:
            label.setText("You're kinda.. okay...")


app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())
