import sys
from PyQt5.QtWidgets import QApplication
from model import BrowserModel, Logger
from view import BrowserView
from controller import BrowserController

if __name__ == "__main__":
    app = QApplication(sys.argv)
    QApplication.setApplicationName('light_browser')

    log_enabled = '--log' in sys.argv or '-l' in sys.argv

    model = BrowserModel()
    view = BrowserView()
    logger = Logger("log.txt") if log_enabled else None
    controller = BrowserController(model, view, logger)
    
    view.show()
    sys.exit(app.exec_())
