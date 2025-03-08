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


# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# open the url
driver.get("https://www.amazon.com")


#Amazon logo
# driver.find_element(By.XPATH,"//i[@class='a-icon a-icon-logo']")
# driver.find_element(By.XPATH, "//i[contains(@class, 'a-icon-logo')]")
# driver.find_element(By.XPATH,  "//a[@href='/ref=ap_frn_logo']")

driver.find_element(By.XPATH, "//i[@class='a-icon a-icon-logo']")

#Email field
driver.find_element(By.XPATH,"//input[@name='email']").send_keys("<EMAIL>")
driver.find_element(By.XPATH, "//input[@id='ap_email']")

#continue button
driver.find_element(By.ID,'continue')

#conditions of use link
driver.find_element(By.XPATH, "//a[text()='Conditions of Use']")

# privacy Notice link
driver.find_element(By.XPATH, "//a[text()='Privacy Notice']")

#Need help link
driver.find_element(By.XPATH,"//span[@class='a-expander-prompt']")

#Forgot your password link
driver.find_element(By.ID,   'auth-fpp-link-bottom ')

#other issues with sign-in lnk
driver.find_element(By.ID,  'ap-other-signin-issues-link')


#create your amazon account button
driver.find_element(By.ID, 'createAccountSubmit')


# 2. Create a test case for the SignIn page using python & selenium script.
# (Make sure to use Incognito browser mode when searching for locators)

#Open https://www.target.com/
driver.get("https://www.target.com")

# click signin button
driver.find_element(By.XPATH,"//span[text()='Sign in ']")
driver.find_element(By.XPATH, "//span[@class='sc-43f80224-3 fBDEOp h-margin-r-x3']").click()

#click signin from side navigation
driver.find_element(By.XPATH,"//button[@data-test='accountNav-signIn']").click()

sleep(5)

