from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep

class ReelyMainPage(Page):
    type_username = (By.XPATH,"//*[@type='email']")
    type_password = (By.XPATH,"//*[@type='password']")
    reely_signin_button = (By.XPATH,"//a[@wized='loginButton']")
    secondary_page_button = (By.XPATH,"//*[@id='w-node-_99a5c496-8f77-9959-16dd-e8eb9b22b697-9b22b68b']")

    def open_reely_main_page(self):
        self.open('https://soft.reelly.io/sign-in')
        sleep(10)

    def log_in_to_the_page(self):
        self.input_text('cedricdeloney@gmail.com', *self.type_username)
        self.input_text('Goodtech1',*self.type_password)
        self.click(*self.reely_signin_button)
        sleep(10)

    def open_main_page(self):
        self.open('https://soft.reelly.io/sign-in')
        sleep(10)

    def log_in(self):
        self.input_text('cedricdeloney@gmail.com', *self.type_username)
        self.input_text('Goodtech1', *self.type_password)
        self.click(*self.reely_signin_button)
        sleep(10)

    def click_secondary_option(self):
        self.click(*self.secondary_page_button)
        sleep(10)




