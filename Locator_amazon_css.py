#homwork 3
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome()
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/')

#Amazon logo
## CSS, class (if the class value has space in between ,it means it is more than one class .for example the below has two class )
driver.find_element(By.CSS_SELECTOR, '.a-icon.a-icon-logo')

#amazon "create account"
# CSS, tag
driver.find_element(By.CSS_SELECTOR, 'h1.a-spacing-small')

# "your name "
# CSS, by ID => #
driver.find_element(By.CSS_SELECTOR,  '#ap_customer_name')

#Email

driver.find_element(By.CSS_SELECTOR, '#ap_email')
driver.find_element(By.CSS_SELECTOR, '.a-input-text.a-span12.auth-required-field.auth-require-claim-validation')
driver.find_element(By.CSS_SELECTOR, ' input.a-input-text.a-span12.auth-required-field.auth-require-claim-validation')

#"Re-enter password"
driver.find_element(By.CSS_SELECTOR, '#ap_password_check')
driver.find_element(By.CSS_SELECTOR, "[name='passwordCheck' ]")

#continue
driver.find_element(By.CSS_SELECTOR, '.a-button.a-button-span12.a-button-primary.auth-requires-verify-modal').click()

#conditiions of use
# CSS, attributes, contains => *= []
driver.find_element(By.CSS_SELECTOR, "[href*='Conditions of Use']")
driver.find_element(By.CSS_SELECTOR, "[href*='Privacy Notice']")

# sign in
driver.find_element(By.CSS_SELECTOR, '.a-link-emphasis').click()