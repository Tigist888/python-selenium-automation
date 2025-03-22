from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


@given('the user opens the Target Help page')
def open_target_help_page(context):
    context.driver.get('https://help.target.com/help')

@then('verify the following UI elements should be present')
def verify_ui_elements_present(context):
    wait = WebDriverWait(context.driver, 10)


    target_help = context.driver.find_element(By.CSS_SELECTOR, "[style='flex-grow: 2; margin-bottom: 1rem']" )
    search_box =context.driver.find_element(By.CSS_SELECTOR, "[id='j_id0:j_id2:j_id32:name']" )
    search_button=context.driver.find_element(By.CSS_SELECTOR, "[name='j_id0:j_id2:j_id32:j_id34']" )
    help_section = context.driver.find_elements(By.CSS_SELECTOR, ".container.clearfix > :nth-child(4)")
    browse_all_help_pages = context.driver.find_element(By.XPATH, "//h2[text()='Browse all Help pages']")


    assert target_help.is_displayed(), "Target Help section is missing"
    assert search_box.is_displayed(), "Search box is missing"
    assert search_button.is_displayed(), "Search button is missing"
    assert help_section.is_displayed(), "Help section is missing"
    assert browse_all_help_pages.is_displayed(), "Browse All Help Pages section is missing"

