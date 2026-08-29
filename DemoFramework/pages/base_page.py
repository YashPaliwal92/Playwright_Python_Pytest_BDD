from playwright.sync_api import Page


class BasePage:

    def __init__(self, page : Page):
        self.page = page

    def get_title(self):
        return self.page.title

    def get_url(self):
        return self.page.url
