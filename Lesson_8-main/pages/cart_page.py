from selenium.webdriver.common.by import By

from pages.base_page import Page


class CartPage(Page):
    RIGHT_signin = (By.XPATH, "//span[@class='styles__ListItemText-sc-diphzn-1 jaMNVl']")
    Verify_items = (By.XPATH, "//span[text()='Added to cart']")

    def verify_cart_empty_message(self):
       self.verify_text("Your cart is empty",self.RIGHT_signin)
    pass