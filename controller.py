from PyQt5.QtCore import QUrl

class BrowserController:
    def __init__(self, model, view, logger=None):
        self.model = model
        self.view = view
        self.logger = logger
        
        self.view.browser.setUrl(self.model.get_home_url())

        self.view.back_btn.triggered.connect(self.view.browser.back)
        self.view.next_btn.triggered.connect(self.view.browser.forward)
        self.view.home_btn.triggered.connect(self.go_home)
        self.view.refresh_btn.triggered.connect(self.view.browser.reload)

        self.view.url_bar.returnPressed.connect(self.navigate_to_url)
        self.view.browser.urlChanged.connect(self.update_url)
    
    def go_home(self):
        self.view.browser.setUrl(self.model.get_home_url())
    
    def navigate_to_url(self):
        url = self.view.url_bar.text()
        self.view.browser.setUrl(QUrl(url))
    
    def update_url(self, url):
        self.view.url_bar.setText(url.toString())

        if self.logger:
            self.logger.log(url.toString())
