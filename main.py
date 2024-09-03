import sys
from PyQt5.QtWidgets import QApplication
from model import BrowserModel
from view import BrowserView
from controller import BrowserController

if __name__ == "__main__":
    app = QApplication(sys.argv)
    QApplication.setApplicationName('light_browser')

    model = BrowserModel()
    view = BrowserView()
    controller = BrowserController(model, view)
    
    view.show()
    sys.exit(app.exec_())
