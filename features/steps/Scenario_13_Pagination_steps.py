from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from time import sleep


@given('Open the main page')
def open_main_page(context):
    context.add.reely_main_page.open_main_page()
    sleep(10)

@when('Log in')
def log_in(context):
    context.add.reely_main_page.log_in()
    sleep(10)

@when('Click secondary option at the left side menu')
def click_secondary_option(context):
    context.add.reely_main_page.click_secondary_option()
    sleep(10)


@then('Verify the secondary page opens')
def verify_secondary_page_opens(context):
    context.add.reely_secondary_page.verify_secondary_page_opens()
    sleep(10)

@when('Go to the final page using the pagination button')
def click_final_page(context):
    context.add.reely_secondary_page.click_final_page()
    sleep(10)

@when('Go back to the first page using the pagination button')
def go_to_first_page(context):
    context.add.reely_secondary_page.go_to_first_page()
    sleep(10)