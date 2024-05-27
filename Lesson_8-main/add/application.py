from pages.main_page import MainPage
from pages.header import Header
from pages.search_results import SearchResultsPage
from pages.signin_page import SigninPage


class Application:

    def __init__(self, driver):
        self.main_page = MainPage(driver)
        self.header = Header(driver)
        self.search_results_page = SearchResultsPage(driver)
        self.signin_page = SigninPage(driver)


