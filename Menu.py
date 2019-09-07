import sys
from PySide2.QtWidgets import *

class Menu(QMainWindow):

    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):

        bar = self.menuBar()

        file = bar.addMenu("File")
        edit = bar.addMenu("Edit")
        view = bar.addMenu("View")
        help_ = bar.addMenu("Help")

        new_action = QAction("New", self)
        new_action.setShortcut("Ctrl+N")

        save_action = QAction("Save", self)
        save_action.setShortcut("Ctrl+S")

        print_action = QAction("Print", self)
        print_action.setShortcut("Ctrl+P")

        quit_action = QAction("&Quit", self)
        quit_action.setShortcut("Ctrl+Q")

        replace_action = QAction("Replace", self)
        replace_action.setShortcut("Ctrl+R")

        find_action = QAction("Find", self)
        find_action.setShortcut("Ctrl+F")

        undo_action = QAction("Undo", self)
        undo_action.setShortcut("Ctrl+Z")

        redo_action = QAction("Redo", self)
        redo_action.setShortcut("Ctrl+Y")
        
        copy_action = QAction("Copy", self)
        copy_action.setShortcut("Ctrl+C")
         
        cut_action = QAction("Cut", self)
        cut_action.setShortcut("Ctrl+X")
        
        paste_action = QAction("Paste", self)
        paste_action.setShortcut("Ctrl+V")

        file.addAction(new_action)
        file.addAction(save_action)
        file.addAction(print_action)
        file.addSeparator()
        file.addAction(quit_action)

        find_menu = edit.addMenu("Find")
        
        edit.addSeparator()
        edit.addAction(undo_action)
        edit.addAction(redo_action)

        edit.addSeparator()
        edit.addAction(copy_action)
        edit.addAction(cut_action)
        edit.addAction(paste_action)

        find_menu.addAction(find_action)
        find_menu.addAction(replace_action)

        quit_action.triggered.connect(self.quit_trigger)
        file.triggered.connect(self.selected)
        edit.triggered.connect(self.selected)        

        self.resize(700,400)
        self.setWindowTitle("My Menu")
        self.show()

    def quit_trigger(self):
        qApp.quit()

    def selected(self,q):
        print(q.text() + " selected ")

app = QApplication(sys.argv)
menu = Menu()
sys.exit(app.exec_())