from PyQt5.QtWidgets import QMainWindow, QToolBar, QAction, QLineEdit
from PyQt5.QtWebEngineWidgets import QWebEngineView

class BrowserView(QMainWindow):
    def __init__(self):
        super(BrowserView, self).__init__()
        
        # Initialize the browser view
        self.browser = QWebEngineView()
        self.setCentralWidget(self.browser)
        self.showMaximized()
        
        # Navigation bar setup
        self.navbar = QToolBar()
        self.addToolBar(self.navbar)
        
        self.back_btn = QAction('<', self)
        self.next_btn = QAction('>', self)
        self.home_btn = QAction('Home', self)
        self.refresh_btn = QAction('Refresh', self)
        
        self.navbar.addAction(self.back_btn)
        self.navbar.addAction(self.next_btn)
        self.navbar.addAction(self.home_btn)
        self.navbar.addAction(self.refresh_btn)
        
        self.url_bar = QLineEdit()
        self.navbar.addWidget(self.url_bar)
