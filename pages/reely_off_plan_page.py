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
    off_plan_image=(By.XPATH,"//*[@wized='projectImage']")
    off_plan_title=(By.XPATH,"//*[@wized='projectName']")
    filters_button = (By.XPATH,"//*[@class='filter-button']")
    sales_status_button = (By.XPATH,"//*[@wized='saleStatusFilter']")
    out_of_stock_option = (By.XPATH,"//*[@value='Out of stock']")
    out_of_stock_tag = (By.XPATH,"//div[contains(text(), 'Out of stock')]")
    architecture_tab_verification = (By.XPATH,"//div[contains(text(), 'Architecture')]")
    interior_tab_verification = (By.XPATH,"//div[contains(text(), 'Interior')]")
    architectural_tab = (By.XPATH,"//a[@data-w-tab='Tab 1']")
    interior_tab = (By.XPATH,"//*[@wized='interiorTabProject']")


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

    def verify_off_plan_opens(self):
        actual_text = self.find_element(*self.verify_off_plan_page).text
        expected_text = "Off-plan"
        assert expected_text in actual_text, f'Error! Text {expected_text} is not in {actual_text}'
        sleep(10)

   # def verify_each_product_has_title_picture(self):
            # Verify images
       # images = self.find_elements(self.off_plan_image)
      #  for image in images:
       #     image_src = image.get_attribute("src")  # Get the 'src' attribute of the image
        #    if not image_src:  # If 'src' is empty or None, the image is missing
             #   print('This item does not have an image')
         #   else:
          #      print("This item has an image")

      #  titles = self.find_elements(self.off_plan_title)
      #  for title in titles:
      #      title_text = title.text
      #      if not title_text:
      #          print(f'this item does not have a title')
      #      else:
       #         print("All of these items have titles")


    def verify_each_product_has_title_picture(self):
    # Verify images and titles
        images = self.find_elements(*self.off_plan_image)  # Using the XPath locator for images
        titles = self.find_elements(*self.off_plan_title)  # Using the XPATH locator for titles

    # Ensure the same number of images and titles
        if len(images) != len(titles):
            print("The number of images and titles do not match.")
            return

    # Loop through images and titles together
        for image, title in zip(images, titles):
            image_src = image.get_attribute("src")  # Get the 'src' attribute of the image
            title_text = title.text  # Get the text of the title

        # Check if the image is missing
            if not image_src:
                print(f'This product with title "{title_text}" does not have an image')
            else:
                print(f'This product with title "{title_text}" has an image')

         # Check if the title is missing
            if not title_text:
                print(f'This product does not have a title')
            else:
                print(f'This product with title "{title_text}" has a title')

    def verify_offplan_page(self):
        actual_text = self.find_element(*self.verify_off_plan_page).text
        expected_text = "Off-plan"
        assert expected_text in actual_text, f'Error! Text {expected_text} is not in {actual_text}'
        sleep(10)

    def click_filters(self):
        self.click(*self.sales_status_button)
        sleep(10)




    def filter_out_of_stock(self):
        self.click(*self.out_of_stock_option)
        sleep(10)



    def verify_out_of_stock_tab(self):
        tags = self.find_elements(*self.out_of_stock_tag)


        for tag in tags:
            tag_text =tag.text
            if 'out of stock' not in tag_text.lower():
                print(f'{tag_text} is not out of stock')
            else:
                print(f'{tag_text} is out of stock')

    def click_first_product(self):
        self.click(*self.off_plan_image)
        sleep(10)



    def verify_two_options_of_visualizations(self):
        actual_text = self.find_element(*self.architecture_tab_verification).text
        expected_text = "Architecture"
        assert expected_text in actual_text, f'Error! Text {expected_text} is not in {actual_text}'
        sleep(10)

        actual_text = self.find_element(*self.interior_tab_verification).text
        expected_text = "Interior"
        assert expected_text in actual_text, f'Error! Text {expected_text} is not in {actual_text}'
        sleep(10)


    def verify_options_clickable(self):
        self.click(*self.interior_tab)
        self.click(*self.architectural_tab)







