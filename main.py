from PyQt5.QtWidgets import *
import sys
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtCore import *

class MainWindow(QMainWindow):
    
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.showMaximized()

app = QApplication(sys.argv)
QApplication.setApplicationName('light_browser')
windows = MainWindow()

app.exec() 