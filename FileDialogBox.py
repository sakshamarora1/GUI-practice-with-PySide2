import sys , os
from PySide2.QtWidgets import *

class Notepad(QWidget):

    def __init__(self):
        super(Notepad, self).__init__()

        self.init_ui()

    def init_ui(self):
            self.text = QTextEdit(self)
            self.clr_btn = QPushButton("Clear")
            self.save_btn = QPushButton("Save")
            self.open_btn = QPushButton("Open")

            h_layout = QHBoxLayout()
            h_layout.addWidget(self.clr_btn)
            h_layout.addWidget(self.open_btn)
            h_layout.addWidget(self.save_btn)

            layout = QVBoxLayout()
            layout.addWidget(self.text)
            layout.addLayout(h_layout)
            self.setLayout(layout)

            self.save_btn.clicked.connect(self.save_text)
            self.clr_btn.clicked.connect(self.clr_text)
            self.open_btn.clicked.connect(self.open_text)

            self.setWindowTitle("File Dialog Box")
            self.show()

    def save_text(self):
        filename = QFileDialog.getSaveFileName(self, "Save File", os.getenv("GUI-practice-with-PySide2"))
        with open(filename[0],'w') as f:
            my_text = self.text.toPlainText()
            f.write(my_text)

    def clr_text(self):
        self.text.clear()

    def open_text(self):
        filename = QFileDialog.getOpenFileName(self, "Open File", os.getenv("GUI-practice-with-PySide2"))
        with open(filename[0],'r') as f:
            file_text = f.read()
            self.text.setText(file_text)

app = QApplication(sys.argv)
writer = Notepad()
sys.exit(app.exec_())
