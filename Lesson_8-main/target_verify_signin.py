from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# open the url
driver.get('https://www.target.com/')

#Click Signin button
driver.find_element(By.XPATH,"//span[text()='Sign in']").click()

#Click sign in button from side
driver.find_element(By.XPATH, "//span[@class='styles__ListItemText-sc-diphzn-1 jaMNVl']").click()
sleep(10)
#Verify "Sign in to your Target account is shown"
actual_text = driver.find_element(By.XPATH,"//span[text()='Sign into your Target account']").click()