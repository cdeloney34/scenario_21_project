from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import Page
from time import sleep

class ReelySecondaryPage(Page):
    verify_secondary_pg = (By.XPATH,"//div[contains(text(), 'Secondary')]")
    pagination_next_button = (By.XPATH,"//*[@wized='nextPageMLS']")
    pagination_previous_button = (By.XPATH,"//*[@wized='previousPageMLS']")

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





