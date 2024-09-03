from PyQt5.QtCore import QUrl

class BrowserModel:
    def __init__(self):
        self.home_url = QUrl('http://google.com')
    
    def get_home_url(self):
        return self.home_url
