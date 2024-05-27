from selenium.webdriver.common.by import By
from pages.base_page import Page

class SigninPage(Page):
    verify_signin_form = (By.CSS_SELECTOR, By.XPATH, "//span[text()='Sign into your Target account']")
    TAL_LINK = (By.XPATH,"//a[text()='Terms']")


    def open_target_signin_page(self):
        self.open('https://www.target.com/login')


    def verify_signin(self):
        self.find_element(self.verify_signin_form)

    def click_tal_link(self):
        self.click(*self.TAL_LINK)