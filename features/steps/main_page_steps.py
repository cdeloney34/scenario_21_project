from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep

CART_ICON = (By.CSS_SELECTOR, "div[class='styles__CartIconDiv-sc-jff2tp-1 bECXM']")
Click_signin = (By.XPATH, "//span[text()='Sign in']")
RIGHT_signin = (By.XPATH, "//span[@class='styles__ListItemText-sc-diphzn-1 jaMNVl']")


@given("Open Target main page")
def open_Target(context):
   # context.driver.get('https://www.target.com/')
    context.add.main_page.open_main()


@when("click on cart icon")
def click_on_cart_icon(context):
    #context.cart_icon = context.driver.find_element(*CART_ICON).click()
    #context.wait.until(EC.invisibility_of_element_located(CART_ICON)),
   # message = "Side nav, Add to Cart button did not disappear"
    context.add.header.search_product()

@when("Click sign in")
def click_sign_in(context):
    context.driver.find_element(*Click_signin).click()


@when("click sign in on right side of the page")
def click_sign_in_right(context):
    #context.driver.find_element(*RIGHT_signin).click()
    #sleep(10)
    context.add.search_result_page.verify_search_resluts(RIGHT_signin)

