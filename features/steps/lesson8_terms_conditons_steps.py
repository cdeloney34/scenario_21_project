from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep





@given('Open sign in page')
def open_sign_in_page(context):
    context.add.open_target_signin_page.open_sign_in_page()

@given('Store original window')
def store_original_window(context):
    #context.original_window = context.driver.current_window_handle
    #print('Current:', context.original_window)
    #print('All window:', context.driver.current_window_handles)
    context.original_window = context.add.target_signin_page.get_curent_window()

@when('Click on Target terms and condition link')
def click_tal(context):
    context.add.target_signin_page.click_tal_link()



@then('Verify Terms and Conditions page is opened')
def verify_terms_and_conditions_pg(context):
    context.add.termsAndConditionsPage.verify_terms_and_conditions()

@when('User can close new window')
def switch_widow(context):
    context.add.target_signin_page.switch_widow()

@when('Close current page')
def close(context):
    context.add.target_signin_page.close()


@then('switch back to original')
def return_to_original_window(context):
    context.add.target_signin_page.switch_widow_by_id(context.original_window)



