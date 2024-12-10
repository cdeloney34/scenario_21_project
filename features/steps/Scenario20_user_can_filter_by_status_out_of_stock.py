from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from time import sleep


@given('Open reely.io pg')
def open_reely_io_pg(context):
    context.add.reely_main_page.open_reely_io_pg()


@when('Log into Reely pg')
def log_into_reely_pg(context):
    context.add.reely_main_page.log_into_reely_pg()


@when('go to offplan page')
def go_to_offplan_page(context):
    context.add.reely_main_page.go_to_offplan_page()


@then('Verify offplan page')
def verify_offplan_page(context):
    context.add.reely_off_plan_page.verify_offplan_page()


@when('click filters')
def click_filters(context):
    context.add.reely_off_plan_page.click_filters()


@when('Filter by status of out-of-stock')
def filter_out_of_stock(context):
    context.add.reely_off_plan_page.filter_out_of_stock()


@then('Verify each product contains the out of stock tab')
def verify_out_of_stock_tab(context):
    context.add.reely_off_plan_page.verify_out_of_stock_tab()
