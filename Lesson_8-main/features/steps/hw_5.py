

from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('User can go https://www.target.com/p/A-91511634  page')
def user_go_target_product_page(context):
    context.driver.get('https://www.target.com/p/A-91511634')

@then("Verify user can click on colors")
def verify_colors(context):
    expected colors = {"dark kahaki","black/gum", "stone/grey", "white/gum"}
    actual_colors = {}

    colors= context.driver.find_elements(By.CSS_SELECTOR,'div[class*="styles_buttonWrapper"] a[rel="nofollow"] img')
    for color in colors:
        color.click()

        selected_color = context.driver.find_element(By.CSS_SELECTOR,'div[class*="styles_buttonWrapper"] a[rel="nofollow"] img')
        selected_color = selected_color.split('/n')[1]
        actual_colors.append(selected_color)

    assert expected_colors == actual_colors, f'Expected colors {expected_colors} did not match {actual_colors}'
