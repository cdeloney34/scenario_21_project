from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

type_username= (By.XPATH,"//*[@type='email']")
type_password= (By.XPATH,"//*[@type='password']")
signin_button= (By.XPATH,"//a[@wized='loginButton']")

@given('Open Reely sign in page')
def open_reely_sign_in_page(context):
    context.add.open_reely_sign_in_page.open_reely_sign_in_page()

@when('Log in to the page')
def log_in_to_the_page(context):
context.find_element


@then('Verify the right page opens.')
def verify_right_page_open(context):


@when('Filter by status of "Out of Stock".')
def filter_by_out_of_stock_status(context):


@then('Verify each product contains the Out of Stock tag')
def verify_out_of_stock_tag(context):



