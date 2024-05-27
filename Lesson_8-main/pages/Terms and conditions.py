from selenium.webdriver.common.by import By

from pages.base_page import Page


class TermsAndConditions(Page):
    TAC_verify = (By.CSS_SELECTOR, "[data-test='@web/Breadcrumbs/BreadcrumbLink']")

    def verify_terms_and_conditions(self):
        self.find_element(self.TAC_verify)
