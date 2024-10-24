from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from time import sleep



@given('open webpage')
def open_webpage(context):
    context.add.reely_main_page.open_webpage()
    sleep(10)

@when('log into webpage')
def log_in_to_webpage(context):
    context.add.reely_main_page.log_in_to_webpage()
    sleep(10)


@when('click on secondary webpage')
def click_on_secondary_webpage(context):
    context.add.reely_main_page.click_on_secondary_webpage()
    sleep(10)


@then('Verify Webpage')
def verify_webpage(context):
    context.add.reely_secondary_page.verify_webpage()
    sleep(10)

@when('click on filter tab')
def click_on_filter_tab(context):
    context.add.reely_secondary_page.click_on_filter_tab()
    sleep(10)


@when('Filter the products by price range from 1200000 to 2000000 AED')
def click_on_filter_products_by_price_range(context):
    context.add.reely_secondary_page.click_on_filter_products_by_price_range()
    sleep(10)


@then('Verify the price in all cards is inside the range (1200000 - 2000000)')
def verify_all_cards_inside_range(context):
    context.add.reely_secondary_page.verify_all_cards_inside_range()
    sleep(10)