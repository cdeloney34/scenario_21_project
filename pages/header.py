from pages.base_page import Page
from selenium.webdriver.common.by import By


class Header(Page):
    enter_coffee = (By.ID, 'search')
    click_search = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
    click_signin = (By.CSS_SELECTOR, "'a[aria-label='Account, sign in']")

    def search_product(self, item):
        self.input_text(item,self.enter_coffee)
        self.click(self.click_search)
        sleep(5)

    def click_cart(self):
        self.click(self.enter_coffee)

    def click_signin_button(self,*locator):
        self.click(self)