from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from time import sleep

#type_username= (By.XPATH,"//*[@type='email']")
#type_password= (By.XPATH,"//*[@type='password']")
#signin_button= (By.XPATH,"//a[@wized='loginButton']")

@given('Open Reely main page')
def open_reely_main_page(context):
    context.add.reely_main_page.open_reely_main_page()

@when('Log in to the page')
def log_in_to_the_page(context):
    context.add.reely_main_page.log_in_to_the_page()
    sleep(10)


@then('Verify the right page opens.')
def verify_right_page_open(context):
    context.add.reely_totalprojects_page.verify_right_page_open()


#@when('Filter by status of "Out of Stock".')
#def filter_by_out_of_stock_status(context):


#@then('Verify each product contains the Out of Stock tag')
#def verify_out_of_stock_tag(context):



