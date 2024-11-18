from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import Page
from time import sleep


class ReelyOffPlanPage(Page):
    verify_off_plan_page = (By.XPATH,"//div[contains(text(),'Off-plan')]")
    pagination_next_button = (By.XPATH,"//*[@wized='nextPageProperties']")
    pagination_previous_button = (By.XPATH,"//*[@wized='previousPageProperties']")
    filter_button = (By.XPATH,"//*[@class='filter-button w-inline-block']")
    from_field = (By.XPATH,"//*[@wized='unitPriceFromFilter']")
    to_field = (By.XPATH,"//*[@wized='unitPriceToFilter']")
    apply_filters_button = (By.XPATH,"//*[@wized='applyFilterButton']")
    price_value = (By.XPATH,"//*[@class='price-value']")



    def verify_off_plan_page_open(self):
        actual_text = self.find_element(*self.verify_off_plan_page).text
        expected_text = "Off-plan"
        assert expected_text in actual_text, f'Error! Text {expected_text} is not in {actual_text}'
        sleep(10)

    def go_to_final_page(self):
        current_page = 1
        total_pages = 55

        while current_page < total_pages:
            # wait for button to be clickable
            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((self.pagination_next_button)))
            # click next button
            self.click(*self.pagination_next_button)
            current_page += 1  # clicking the the next button by 1 page increment

        print(f"Total Pages: {total_pages}, going back to first page")
        self.go_back_to_first_page()


    def go_back_to_first_page(self):
        # set a click counter
        clicks_to_first_page = 0
        while clicks_to_first_page < 55:
            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((self.pagination_previous_button)))

            # Click the previous button
            self.click(*self.pagination_previous_button)
            clicks_to_first_page += 1  # Increment click count

        print("Returned to the first page.")


    def Verify_off_plan_page(self):
        actual_text = self.find_element(*self.verify_off_plan_page).text
        expected_text = "Off-plan"
        assert expected_text in actual_text, f'Error! Text {expected_text} is not in {actual_text}'
        sleep(10)

    def Filter_products_by_price_range(self):
        # Wait for the filter button to be clickable
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(self.filter_button)
        ).click()

        # Wait for the "from" field to be visible and enter text
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(self.from_field)
        )
        self.input_text('1200000', *self.from_field)

        # Wait for the "to" field to be visible and enter text
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(self.to_field)
        )
        self.input_text('2000000', *self.to_field)

        # Wait for the apply filters button to be clickable and click it
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(self.apply_filters_button)
        ).click()


    def Verify_price_in_all_cards(self):
        numbers = self.find_elements(*self.price_value)

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
                sleep(20)



