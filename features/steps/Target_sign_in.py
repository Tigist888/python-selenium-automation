from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open target main page')
def open_target_main(context):
    context.driver.get('https://www.target.com/')



@when('click sign in')
def search_product(context):
    context.driver.find_element(By.CSS_SELECTOR, '.sc-43f80224-3.fBDEOp.h-margin-r-x3' ).click()
    sleep(6)




@when('From right side navigation menu,click sign in')
def search_product(context):
    context.driver.find_element(By.CSS_SELECTOR, "[ data-test='accountNav-signIn']").click()
    sleep(6)



@then('verify sign in form opened')
def verify_search_results(context):
    actual_text = context.driver.find_element(By.XPATH, "//span[text()='Sign into your Target account']")
    assert expected_text in actual_text, f'Error. Text {expected_text} not in {actual_text}'