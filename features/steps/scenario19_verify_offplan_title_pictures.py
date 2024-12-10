from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from time import sleep


@given('open reely pg')
def open_reely_pg(context):
    context.add.reely_main_page.open_reely_pg()


@when('log into Reely')
def log_into_Reely(context):
    context.add.reely_main_page.log_into_Reely()


@when('click off plan tab')
def click_off_plan_tab(context):
    context.add.reely_main_page.click_off_plan_tab()


@then('verify off plan opens')
def verify_off_plan_opens(context):
    context.add.reely_off_plan_page.verify_off_plan_opens()


@then("Verify each product on this page contains a title and picture visible")
def verify_each_product_has_title_picture(context):
    context.add.reely_off_plan_page.verify_each_product_has_title_picture()