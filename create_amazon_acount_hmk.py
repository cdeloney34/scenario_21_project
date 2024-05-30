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

# Amazon logo
driver.find_element(By.CSS_SELECTOR,"i.a-icon.a-icon-logo")

# Create account
driver.find_element(By.CSS_SELECTOR,"h1.a-spacing-small")

# Your name
driver.find_element(By.CSS_SELECTOR,"input#ap_customer_name")

# By Moblile phone number or email
driver.find_element(By.CSS_SELECTOR,"input#ap_email")

# By Password
driver.find_element(By.CSS_SELECTOR,"input#ap_password")

#By Re-enter Password
driver.find_element(By.CSS_SELECTOR,"input#ap_password_check")

#By Create you Amazon Account/Continue button
driver.find_element(By.CSS_SELECTOR,"input#continue")

#By Conditions of use
driver.find_element(By.CSS_SELECTOR, "a[href='/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088']")

#By Privacy Notice
driver.find_element(By.CSS_SELECTOR, "a[href='/gp/help/customer/display.html/ref=ap_register_notification_privacy_notice?ie=UTF8&nodeId=468496']")

#By Sign in
driver.find_element(By.CSS_SELECTOR,"a[class='a-link-emphasis']") 

