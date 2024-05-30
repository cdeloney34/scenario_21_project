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

driver.find_element(By.CSS_SELECTOR,"div[class='styles__CartIconDiv-sc-jff2tp-1 bECXM']").click()
driver.find_element(By.CSS_SELECTOR,"h1[class='styles__StyledHeading-sc-1xmf98v-0 lfA-Dem']")
sleep(10)