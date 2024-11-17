from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from time import sleep



@given('open page')
def open_page(context):
    context.add.reely_main_page.open_page()
    sleep(10)


@when('Log in to main page')
def login_to_main_page(context):
    context.add.reely_main_page.login_to_main_page()
    sleep(10)


@when('Click on off plan option')
def click_off_plan_option(context):
    context.add.reely_main_page.click_off_plan_option()
    sleep(10)


@then('Verify off plan page open')
def verify_off_plan_page_open(context):
    context.add.reely_off_plan_page.verify_off_plan_page_open()
    sleep(10)


@when('Go to the final page using the pagination')
def go_to_final_page(context):
    context.add.reely_off_plan_page.go_to_final_page()
    sleep(10)


@when('Go back to the first page using the pagination')
def go_back_to_first_page(context):
    context.add.reely_off_plan_page.go_back_to_first_page()
    sleep(10)


