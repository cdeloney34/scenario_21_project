from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep


class ReelyTotalprojectsPage(Page):
    reely_verify_text = (By.XPATH, "//*[text()='Total projects']")
    filter_button = (By.CSS_SELECTOR, "a[class='filter-button w-inline-block']")
    out_of_stock_button = (By.XPATH, "//div[@wized='priorityStatusOutOfStock']")
    apply_filter_button = (By.XPATH, "//a[@wized='applyFilterButton']")
    verification_status = (By.XPATH, "//*[text()='Out of stock']")
    mobile_filter_button = (By.XPATH,"//*[@class='filter-button']")
    mobile_out_of_stock_button=(By.XPATH,"//div[@wized='priorityStatusOutOfStock']")
    mobile_apply_filter_button=(By.XPATH,"//a[@wized='applyFilterButton']")

    def verify_right_page_open(self):
        actual_text = self.find_element(*self.reely_verify_text).text
        expected_text = "Total projects"
        assert expected_text in actual_text, f'Error! Text {expected_text} is not in {actual_text}'
        sleep(10)

    def filter_by_out_of_stock_status(self):
        self.click(*self.filter_button)
        self.click(*self.out_of_stock_button)
        self.click(*self.apply_filter_button)
        sleep(15)

    def mobile_filter_by_out_of_stock_status(self):
        self.click(*self.mobile_filter_button)
        self.click(*self.mobile_out_of_stock_button)
        self.click(*self.mobile_apply_filter_button)
        sleep(15)

    def verify_out_of_stock_tag(self):
        expected_tag = "Out of stock"
        out_of_stock_elements = self.find_elements(*self.verification_status)
        for element in out_of_stock_elements:
            actual_tag = element.text
            if expected_tag == actual_tag:
                    print(expected_tag)