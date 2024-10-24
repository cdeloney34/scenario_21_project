from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import Page
from time import sleep

class ReelySecondaryPage(Page):
    verify_secondary_pg = (By.XPATH,"//div[contains(text(), 'Secondary')]")
    pagination_next_button = (By.XPATH,"//*[@wized='nextPageMLS']")
    pagination_previous_button = (By.XPATH,"//*[@wized='previousPageMLS']")
    filter_button = (By.XPATH,"//*[@class='filter-button']")
    want_to_sell_button = (By.XPATH,"//*[@wized='ListingTypeSell']")
    want_to_buy_button = (By.XPATH,"//*[@wized='ListingTypeBuy']")
    appy_filter_button = (By.XPATH,"//*[@wized='applyFilterButtonMLS']")
    for_sale_tag =(By.XPATH,"//*[@wized='saleTagMLS']")
    to_buy_tag = (By.XPATH,"//*[@wized='saleTagBoxMLS']")
    unit_price_from_tab = (By.XPATH,"//*[@wized='unitPriceFromFilter']")
    unit_price_to_tab = (By.XPATH,"//*[@wized='unitPriceToFilter']")
    unit_price_verification = (By.XPATH,"//*[@wized='unitPriceMLS']")


    def verify_secondary_page_opens(self):
         actual_text = self.find_element(*self.verify_secondary_pg).text
         expected_text = "Secondary"
         assert expected_text in actual_text, f'Error! Text {expected_text} is not in {actual_text}'
         sleep(10)


    def click_final_page(self):
        current_page =1
        total_pages =97

        while current_page < total_pages:
            #wait for button to be clickable
            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((self.pagination_next_button)))
            #click next button
            self.click(*self.pagination_next_button)
            current_page +=1 # clicking the the next button by 1 page increment

        print(f"Total Pages: {total_pages}, going back to first page")
        self.go_to_first_page()






    def go_to_first_page(self):
        #set a click counter
        clicks_to_first_page = 0
        while clicks_to_first_page <97:
            WebDriverWait(self.driver,20).until(EC.element_to_be_clickable((self.pagination_previous_button)))

            # Click the previous button
            self.click(*self.pagination_previous_button)
            clicks_to_first_page += 1  # Increment click count

        print("Returned to the first page.")

    def verify_right_page_open(self):
        actual_text = self.find_element(*self.verify_secondary_pg).text
        expected_text = "Secondary"
        assert expected_text in actual_text, f'Error! Text {expected_text} is not in {actual_text}'
        sleep(10)

    def click_filters(self):
        self.click(*self.filter_button)
        sleep(10)
    def filter_by_want_to_sell(self):
        self.click(*self.filter_button)
        sleep(10)


    def apply_filter(self):
        self.click(*self.filter_button)
        sleep(10)



    def verify_all_cards_have_sale_tag(self):
        tags = self.find_elements(*self.for_sale_tag)

        for tag in tags:
            tag_text = tag.text

            if tag_text != "For sale":
                print(f"Tag '{tag_text}' is not 'For sale'.")
                return

        print("All tags are 'For sale'.")

    def verify_page_opens(self):
        actual_text = self.find_element(*self.verify_secondary_pg).text
        expected_text = "Secondary"
        assert expected_text in actual_text, f'Error! Text {expected_text} is not in {actual_text}'
        sleep(10)

    def click_filters_tab(self):
        self.click(*self.filter_button)
        sleep(10)


    def filter_by_want_to_buy(self):
        self.click(*self.want_to_buy_button)

    def apply_filter_tab(self):
        self.click(*self.filter_button)
        sleep(10)

    def verify_all_cards_have_want_to_buy_tag(self):
        tags = self.find_elements(*self.to_buy_tag)

        for tag in tags:
            tag_text = tag.text

            if tag_text != "want to buy":
                print(f"Tag '{tag_text}' is not in 'Want to Buy'.")
                return

            print("All tags are 'Want to buy'")

    def verify_webpage(self):
        actual_text = self.find_element(*self.verify_secondary_pg).text
        expected_text = "Secondary"
        assert expected_text in actual_text, f'Error! Text {expected_text} is not in {actual_text}'
        sleep(10)

    def click_on_filter_tab(self):
        self.click(*self.filter_button)
        sleep(10)

    def click_on_filter_products_by_price_range(self):
        self.input_text('1200000',*self.unit_price_from_tab)
        self.input_text('2000000',*self.unit_price_to_tab)
        self.click(*self.appy_filter_button)


    def verify_all_cards_inside_range(self):
        numbers = self.find_elements(*self.unit_price_verification)

        for number in numbers:
            price_text = number.text
            if price_text.isdigit():
                price = int(price_text)  # Convert to integer
                if 1200000 <= price <= 2000000:
                    print(f"Number {price} falls in range.")
                else:
                    print(f'Number {price} is not in range.')
            else:
                print(f'Invalid price format: {price_text}')















