from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC

#enter_coffee = (By.ID, 'search')
#click_search = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
#verify_coffee = (By.XPATH, "//span[text()='coffee']")search')


#@given('Open Target home-page')
#def open_Target(context):
    #context.driver.get('https://www.target.com/')
    #sleep(10)

#@when('Type Coffee in search')
#def type_Coffee(context):
   # context.wait.until(EC.presence_of_element_located(enter_coffee)),
   # message = 'Search Coffee is not present on page'
   # context.find_element(enter_coffee).send_keys('coffee')


#@when('click search button')
#def click_Search(context):
   # context.find_element(click_search).click()
    #context.wait.until(EC.element_to_be_clickable(click_search)),
   # message = 'Search button not clickable'

#@then('Verify coffee page appears')
#def verify_coffee_page(context):
   # context.find_element(verify_coffee)
    #context.wait.until(EC.presence_of_element_located(verify_coffee)),
   # message = 'Coffee doesnt appear on webpage'



