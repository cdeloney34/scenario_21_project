from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep


class ReelyTotalprojectsPage(Page):
    reely_verify_text = (By.XPATH,"//*[text()='Total projects']")
    filter_button = (By.XPATH,"//a[@wized='openFiltersWindow']")
    out_of_stock_button = (By.XPATH, "//div[@wized='priorityStatusOutOfStock']")
    apply_filter_button = (By.XPATH, "//a[@wized='applyFilterButton']")
    verification_status = (By.XPATH,"//*[text()='Out of stock']")


    def verify_right_page_open(self):
        actual_text = self.find_element(*self.verify_text).text
        expected_text = "Total projects"
        assert expected_text in actual_text, f'Error! Text {expected_text} is not in {actual_text}'
        sleep(10)


    def filter_by_out_of_stock_status(self):
        self.click(*self.filter_button)
        self.click(*self.out_of_stock_button)
        self.click(*self.apply_filter_button)




