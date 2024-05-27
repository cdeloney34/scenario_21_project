from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

type_in_search_field = (By.ID, 'search')
search_button = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
click_add_to_cart_button = (By.CSS_SELECTOR,"[data-test=chooseOptionsButton]")
click_second_add_to_cart_button = (By.CSS_SELECTOR,"[data-test='orderPickupButton']")
Verify_items = (By.XPATH, "//span[text()='Added to cart']")


@given('Open Target main webpage.')
def open_target_main_page(context):
    context.driver.get('https://www.target.com/')


@when('Type basketball into search field.')
def Type_basketball_into_search_field(context):
    context.driver.find_element(*type_in_search_field).send_keys('basketball')


@when('Click on the search button.')
def click_on_search_button(context):
    context.driver.find_element(*search_button).click()
    sleep(10)

@when('Click on the add to cart button.')
def click_on_cart_button(context):
    context.driver.find_element(*click_add_to_cart_button).click()
    sleep(10)

@when('Click on second cart button.')
def click_second_button(context):
    context.driver.find_element(*click_second_add_to_cart_button).click()
    sleep(10)

@then('Verify item was added to cart.')
def verify_item_added(context):
    sleep(10)
    actual_text = context.driver.find_element(*Verify_items)
    expected_text = 'Added to cart'
    assert actual_text == expected_text, f'Expected {expected_text}, but got {actual_text}'