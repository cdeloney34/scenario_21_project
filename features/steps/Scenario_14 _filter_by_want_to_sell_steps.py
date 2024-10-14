from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from time import sleep


@given('Open main page')
def open_main_page(context):
    context.add.reely_main_page.open_main_page()
    sleep(10)

@when('Log in to the webpage')
def log_in_to_webpage(context):
    context.add.reely_main_page.log_in_to_webpage()
    sleep(10)

@when('Click secondary option at the left side menu page')
def click_secondary_option_menu_page(context):
    context.add.reely_main_page.click_secondary_option_menu_page()
    sleep(10)


@when('Verify the right page open')
def verify_right_page_open(context):
    context.add.reely_secondary_page.verify_right_page_open()
    sleep(10)

@when('Click on filters')
def click_filters(context):
    context.add.reely_secondary_page.click_filters()
    sleep(10)

@when('Filter the products by want to sell')
def filter_by_want_to_sell(context):
    context.add.reely_secondary_page.filter_by_want_to_sell()
    sleep(10)


@when('Click on Apply filter')
def apply_filter(context):
    context.add.reely_secondary_page.apply_filter()
    sleep(10)


@then('Verify all cards have for sale tag')
def verify_all_cards_have_sale_tag(context):
    context.add.reely_secondary_page.verify_all_cards_have_sale_tag()
    sleep(10)


