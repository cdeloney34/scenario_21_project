from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep

class ReelyMainPage(Page):
    type_username = (By.XPATH,"//*[@type='email']")
    type_password = (By.XPATH,"//*[@type='password']")
    reely_signin_button = (By.XPATH,"//a[@wized='loginButton']")
    def open_reely_main_page(self):
        self.open('https://soft.reelly.io/sign-in')
        sleep(10)

    def log_in_to_the_page(self):
        self.input_text('cedricdeloney@gmail.com', *self.type_username)
        self.input_text('Goodtech1',*self.type_password)
        self.click(*self.reely_signin_button)
        sleep(10)

