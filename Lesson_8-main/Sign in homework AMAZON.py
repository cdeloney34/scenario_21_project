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
driver.get('https://www.amazon.com/')

#By Amazon logo
driver.find_element(By.XPATH,"//a[text()='a-icon a-icon-logo']")

#By Email feld
driver.find_element(By.ID,'ap_email')

#By Continue Button
driver.find_element(By.ID,'continue' )

# By Conditions of use link
driver.find_element(By.XPATH, "//a[text()='/gp/help/customer/display.html/ref=ap_signin_notification_condition_of_use?ie=UTF8&amp;nodeId=508088']")

#By Privacy Notice link
driver.find_element(By.XPATH,"//a[text()=/gp/help/customer/display.html/ref=ap_signin_notification_privacy_notice?ie=UTF8&amp;nodeId=468496']")

#By Need Help link
driver.find_element(By.XPATH, "//a[text()='a-expander-prompt']")

#Forgot your Password link
driver.find_element(By.ID, 'auth-fpp-link-bottom')

#Create your Amazon account link
driver.find_element(By.XPATH, 'createAccountSubmit')









