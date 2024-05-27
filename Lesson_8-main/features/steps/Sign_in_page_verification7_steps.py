from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from behave import given, when, then
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from add.application import Application

click_signin = (By.CSS_SELECTOR, "a[aria-label='Account, sign in']")
right_nav_signin = (By.CSS_SELECTOR, "a[data-test='accountNav-signIn']")
verify_signin_form = (By.XPATH, "//span[text()='Sign into your Target account']")


@when('Click signin button')
def click_signin_button(context):
    context.driver.find_element(*click_signin).click()


@when('click right navigation sign in')
def click_right_navigation_signin(context):
    sleep(5)
    context.driver.find_element(*right_nav_signin).click()


@then("Verify Sign in form opened")
def verify_sign_in_is_opened(context):
    sleep(5)
    actual_text = context.driver.find_element(By.XPATH, "//span[text()='Sign into your Target account']").text
    expected_text = 'Sign into your Target account'
    assert actual_text == expected_text, f'Expected {expected_text}, but got {actual_text}'