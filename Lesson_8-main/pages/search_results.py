from selenium.webdriver.common.by import By

from pages.base_page import Page

class SearchResultsPage(Page):
    Verify_items = (By.XPATH, "//span[text()='Added to cart']")

    def verify_search_results(self):
        self.driver.find_element(*self.Verify_items)