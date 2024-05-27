from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

verification_links = (By.CSS_SELECTOR, "a[data-test='@web/slingshot-components/CellsComponent/Link']")



@given('Open target circle page')
def open_target_circle_page(context):
    context.driver.get("('https://www.target.com/circle')")
sleep(10)
@then('Verify user can see the 10 Bonus links')
def verify_bonus_links(context):
    links = context.find_element(*verification_links)
    print(links)
    assert len(links) == 10, f"Expected 10 links to be found, got {len(links)}"
