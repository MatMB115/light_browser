from PyQt5.QtCore import QUrl
import datetime

class BrowserModel:
    def __init__(self):
        self.home_url = QUrl('https://google.com')
    
    def get_home_url(self):
        return self.home_url


class Logger:
    def __init__(self, filename):
        self.filename = filename
    
    def log(self, message):
        with open(self.filename, "a") as file:
            timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            file.write(f"{timestamp} - {message}\n")
