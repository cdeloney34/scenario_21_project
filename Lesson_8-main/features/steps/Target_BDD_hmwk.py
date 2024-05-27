from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given("Open Target main page")
def open_Target(context):
    context.driver.get('https://www.target.com/')


@when("click on cart icon")
def click_on_cart_icon(context):
    context.driver.find_element(By.CSS_SELECTOR, "div[class='styles__CartIconDiv-sc-jff2tp-1 bECXM']").click()


@then("Verify your cart is empty text is shown.")
def verify_cart_is_empty(context):
    context.driver.find_element(By.CSS_SELECTOR, "h1[class='styles__StyledHeading-sc-1xmf98v-0 lfA-Dem']")
    sleep(10)


@given("Open Target web page")
def open_Target_web_page(context):
    context.driver.get('https://www.target.com/')


@when("Click sign in")
def click_sign_in(context):
    context.driver.find_element(By.XPATH, "//span[text()='Sign in']").click()


@when("click sign in on right side of the page")
def click_sign_in_right(context):
    context.driver.find_element(By.XPATH, "//span[@class='styles__ListItemText-sc-diphzn-1 jaMNVl']").click()
    sleep(10)


@then("Verify sign in page opened")
def verify_sign_in_is_opened(context):
    actual_text = context.driver.find_element(By.XPATH, "//span[text()='Sign into your Target account']").click()
