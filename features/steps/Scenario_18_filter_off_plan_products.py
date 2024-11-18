from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from time import sleep


@given('Open Reely')
def Open_reely(context):
    context.add.reely_main_page.Open_reely()
    sleep(10)


@when('Log in to Reely')
def Log_in_to_Reely(context):
    context.add.reely_main_page.Log_in_to_Reely()
    sleep(10)


@when('Click on off plan tab')
def Click_on_off_plan_tab(context):
    context.add.reely_main_page.Click_on_off_plan_tab()
    sleep(10)


@then('Verify off plan page')
def Verify_off_plan_page(context):
    context.add.reely_off_plan_page.Verify_off_plan_page()
    sleep(10)


@when('Filter the products by price range from 1200000 to 2000000 AED.')
def Filter_products_by_price_range(context):
    context.add.reely_off_plan_page.Filter_products_by_price_range()
    sleep(10)


@then('Verify the price in all cards is inside the range (1200000 - 2000000).')
def Verify_price_in_all_cards(context):
    context.add.reely_off_plan_page.Verify_price_in_all_cards()
    sleep(10)
