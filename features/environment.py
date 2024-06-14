from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from add.application import Application


# Run Behave tests with Allure results
# behave -f allure_behave.formatter:AllureFormatter -o test_results/ features/tests/

def browser_init(context, scenario_name):
    """
    :param context: Behave context
    """
    #driver_path = ChromeDriverManager().install()
    #service = Service(driver_path)
    #context.driver = webdriver.Chrome(service=service)


# context.driver.set_window_size(2560, 1440)

# driver_path = GeckoDriverManager().install()
# driver_path = './geckodriver.exe'
# service = Service(driver_path)
# context.driver = webdriver.Firefox(service=service)

### browser With Drivers: provide path to driver file
# service = Service(executable_path='C:/Users/cedri/Downloads/internship-project/geckodriver.exe')
# context.driver = webdriver.Firefox(service=service)

### SAFARFI ###
# context.driver = webdriver.Safari()

### HEADLESS MODE ###
# options = webdriver.ChromeOptions()
# options.add_argument('headless')
# service = Service(ChromeDriverManager().install())
# context.driver = webdriver.Chrome(
# options=options,
# service=service
# )

# Browserstack
# Register for BrowserStack, then grab it from https://www.browserstack.com/accounts/settings
# bs_user = 'cedricdeloney_MEl0B9'
# bs_key = 'nB5DGTNRygoG3hm4bKxN'
# url = f'https://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'

# options = Options()
# bstack_options = {
# 'os': 'Windows',
# 'osVersion': '10',
# 'browserName': 'Chrome',
# 'sessionName': scenario_name
# }

# options.set_capability('bstack:options', bstack_options)
# context.driver = webdriver.Remote(command_executor=url, options=options)

    mobile_emulation = {
        "deviceMetrics": {"width": 415, "height": 896, "pixelRatio": 3.0},
        "userAgent": "Mozilla/5.0 (iPhone; CPU iphone OS 12_1_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0 Mobile/15E148 Safari/604.1",
        "clientHints": {"platform": "iPhone", "mobile": True}}
    chrome_options = Options()
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    context.driver = webdriver.Chrome(options=chrome_options)


    context.driver.maximize_window()
    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.add = Application(context.driver)





def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context, scenario.name)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()
