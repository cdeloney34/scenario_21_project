from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from time import sleep


@given('open reely.io')
def open_reely_io(context):
    context.add.reely_main_page.open_reely_io()


@when('login to reel.io')
def login_to_reely_io(context):
    context.add.reely_main_page.login_to_reely_io()


@when('click on offplan')
def click_offplan(context):
    context.add.reely_main_page.click_offplan()


@when('click on the first product')
def click_first_product(context):
    context.add.reely_off_plan_page.click_first_product()


@then('verify the two options of visualizations are architecture, interior')
def verify_two_options_of_visualizations(context):
    context.add.reely_off_plan_page.verify_two_options_of_visualizations()


@then('verify the visualization options are clickable')
def verify_options_clickable(context):
    context.add.reely_off_plan_page.verify_options_clickable()
