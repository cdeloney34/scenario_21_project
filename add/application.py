from pages.main_page import MainPage
from pages.header import Header
from pages.search_results import SearchResultsPage
from pages.signin_page import SigninPage
from pages.reely_main_page import ReelyMainPage
from pages.reely_totalprojects_page import ReelyTotalprojectsPage

class Application:

    def __init__(self, driver):
        self.main_page = MainPage(driver)
        self.header = Header(driver)
        self.search_results_page = SearchResultsPage(driver)
        self.signin_page = SigninPage(driver)
        self.reely_main_page = ReelyMainPage(driver)
        self.reely_totalprojects_page = ReelyTotalprojectsPage(driver)

