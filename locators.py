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

# by ID
driver.find_element(By.ID, 'twotabsearchtextbox' )
driver.find_element(By.ID,  'nav-search-submit-button')

# By Xpath
driver.find_element(By.XPATH, "//input[@aria-label='Search Amazon']") # //tag[@attr='value']
driver.find_element(By.XPATH, "//input[@role='searchbox']")

# Byt Xpath, multiple attributes
driver.find_element(By.XPATH, "//input[@tabindex='0' and @name='field-keywords']")
driver.find_element(By.XPATH, "//input[@tabindex='0' and @name='field-keywords' and @role='searchbox']")

# By xpath, without a tag
driver.find_element(BY.XPATH, "//*[@aria-label='Search Amazon']")  # * it means any tag.


# by xpath, using text
driver.find_element(By.XPATH, "//a[text()='Best Sellers']")
driver.find_element(By.XPATH, "//a[text()='Best Sellers' and  @class='nav-a  ']")
driver.find_element(By.XPATH, "// @class='nav-a  ' and  text()='Best Sellers']")

# partial text  match
driver.find_element(By.XPATH, "//h2[contains(text(), 'Luxury']")

driver.find_element(By.XPATH, "//select(contains(@class, 'nav-search-dropdown')]")

