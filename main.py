from PyQt5.QtWidgets import *
import sys
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtCore import *

class MainWindow(QMainWindow):
    
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('http://google.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        navbar = QToolBar()
        self.addToolBar(navbar)
        
        back_btn = QAction('<', self)
        back_btn.triggered.connect(self.browser.back)
        next_btn = QAction('>', self)
        next_btn.triggered.connect(self.browser.forward)
        home_btn = QAction('Home', self)
        home_btn.triggered.connect(self.goHome)
        refresh_btn = QAction('Refresh', self)
        refresh_btn.triggered.connect(self.browser.reload)
        
        navbar.addAction(back_btn)
        navbar.addAction(next_btn)
        navbar.addAction(home_btn)
        navbar.addAction(refresh_btn)

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.goUrl)
        navbar.addWidget(self.url_bar)
        self.browser.urlChanged.connect(self.updateUrl)

    def goHome(self):
        self.browser.setUrl(QUrl('http://google.com'))

    def goUrl(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))

    def updateUrl(self, url):
        self.url_bar.setText(url.toString())

app = QApplication(sys.argv)
QApplication.setApplicationName('light_browser')
windows = MainWindow()

app.exec() 