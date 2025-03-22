from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from target_search_script import expected_text


@given("open target main page")
def open_target_main(context):
    context.driver.get('https://www.target.com/')


#
@when('click sign in')
def click_sign_in(context):
    context.driver.find_element(By.CSS_SELECTOR, '.sc-43f80224-3.fBDEOp.h-margin-r-x3' ).click()
    #sleep(6)
    context.driver.implicitly_wait(5)


@when('From right side navigation menu,click sign in')
def right_side_click_sign_in(context):

    wait=WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-test='accountNav-signIn']"))
    )
    wait.click()
    #context.driver.find_element(By.CSS_SELECTOR, "[data-test='accountNav-signIn']").click()
    #sleep(6)


@then('verify sign in form opened')
def verify_search_results(context):
    expected_result='to be opened'
    actual_text = context.driver.find_element(By.XPATH, "//span[text()='Sign into your Target account']")
    assert expected_result in actual_text, f'Error. Text {expected_text} not in {actual_text}'