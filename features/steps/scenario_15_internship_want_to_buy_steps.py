from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from time import sleep



@given('Open Reely page')
def open_reely_page(context):
    context.add.reely_main_page.open_reely_page()
    sleep(10)

@when('Log in to page')
def log_in_to_page(context):
    context.add.reely_main_page.log_in_to_page()
    sleep(10)

@when('click on secondary page')
def click_secondary_page(context):
    context.add.reely_main_page.click_secondary_page()
    sleep(10)


@then('Verify page opens')
def verify_page_opens(context):
    context.add.reely_secondary_page.verify_page_opens()
    sleep(10)

@when('Click on filters tab')
def click_filters_tab(context):
    context.add.reely_secondary_page.click_filters_tab()
    sleep(10)


@when('Filter the products by want to buy')
def filter_by_want_to_buy(context):
    context.add.reely_secondary_page.filter_by_want_to_buy()
    sleep(10)


@when('Click on Apply filter tab')
def apply_filter_tab(context):
    context.add.reely_secondary_page.apply_filter_tab()
    sleep(10)


@then('Verify all cards have Want to buy tag')
def verify_all_cards_have_want_to_buy_tag(context):
    context.add.reely_secondary_page.verify_all_cards_have_want_to_buy_tag()
    sleep(10)
