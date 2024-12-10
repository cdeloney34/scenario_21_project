from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep

class ReelyMainPage(Page):
    type_username = (By.XPATH,"//*[@type='email']")
    type_password = (By.XPATH,"//*[@type='password']")
    reely_signin_button = (By.XPATH,"//a[@wized='loginButton']")
    secondary_page_button = (By.XPATH,"//*[@id='w-node-_99a5c496-8f77-9959-16dd-e8eb9b22b697-9b22b68b']")
    off_plan_page_button = (By.XPATH,"//*[@class='_1-link-menu w-inline-block w--current']")
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

    def open_reely_main_page(self):
        self.open('https://soft.reelly.io/sign-in')
        sleep(10)


    def log_in_to_webpage(self):
        self.input_text('cedricdeloney@gmail.com', *self.type_username)
        self.input_text('Goodtech1', *self.type_password)
        self.click(*self.reely_signin_button)
        sleep(10)

    def click_secondary_option_menu_page(self):
        self.click(*self.secondary_page_button)
        sleep(10)


    def open_reely_page(self):
        self.open('https://soft.reelly.io/sign-in')
        sleep(10)

    def log_in_to_page(self):
        self.input_text('cedricdeloney@gmail.com', *self.type_username)
        self.input_text('Goodtech1', *self.type_password)
        self.click(*self.reely_signin_button)
        sleep(10)

    def click_secondary_page(self):
        self.click(*self.secondary_page_button)
        sleep(10)

    def open_webpage(self):
        self.open('https://soft.reelly.io/sign-in')
        sleep(10)

    def log_in_to_webpage(self):
        self.input_text('cedricdeloney@gmail.com', *self.type_username)
        self.input_text('Goodtech1', *self.type_password)
        self.click(*self.reely_signin_button)
        sleep(10)

    def click_on_secondary_webpage(self):
        self.click(*self.secondary_page_button)
        sleep(10)

    def open_page(self):
        self.open('https://soft.reelly.io/sign-in')
        sleep(10)

    def login_to_main_page(self):
        self.input_text('cedricdeloney@gmail.com', *self.type_username)
        self.input_text('Goodtech1', *self.type_password)
        self.click(*self.reely_signin_button)
        sleep(10)

    def click_off_plan_option(self):
        self.click(*self.off_plan_page_button)
        sleep(10)

    def Open_reely(self):
        self.open('https://soft.reelly.io/sign-in')
        sleep(10)

    def Log_in_to_Reely(self):
        self.input_text('cedricdeloney@gmail.com', *self.type_username)
        self.input_text('Goodtech1', *self.type_password)
        self.click(*self.reely_signin_button)
        sleep(10)

    def Click_on_off_plan_tab(self):
        self.click(*self.off_plan_page_button)
        sleep(10)

    def open_reely_pg(self):
        self.open('https://soft.reelly.io/sign-in')
        sleep(10)

    def log_into_Reely(self):
        self.input_text('cedricdeloney@gmail.com', *self.type_username)
        self.input_text('Goodtech1', *self.type_password)
        self.click(*self.reely_signin_button)
        sleep(10)

    def click_off_plan_tab(self):
        self.click(*self.off_plan_page_button)
        sleep(10)

    def open_reely_io_pg(self):
        self.open('https://soft.reelly.io/sign-in')
        sleep(10)

    def log_into_reely_pg(self):
        self.input_text('cedricdeloney@gmail.com', *self.type_username)
        self.input_text('Goodtech1', *self.type_password)
        self.click(*self.reely_signin_button)
        sleep(10)

    def go_to_offplan_page(self):
        self.click(*self.off_plan_page_button)
        sleep(10)

    def open_reely_io(self):
        self.open('https://soft.reelly.io/sign-in')
        sleep(10)

    def login_to_reely_io(self):
        self.input_text('cedricdeloney@gmail.com', *self.type_username)
        self.input_text('Goodtech1', *self.type_password)
        self.click(*self.reely_signin_button)
        sleep(10)

    def click_offplan(self):
        self.click(*self.off_plan_page_button)
        sleep(10)






























