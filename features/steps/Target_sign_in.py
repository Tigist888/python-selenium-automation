from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from target_search_script import expected_text


@given("open target main page")
def open_target_main(context):
    context.app.pages.MainPage.open_main_page()


#
@when('click sign in')
def click_sign_in(context):
    context.app.pages.Header.sign_in()
    context.driver.implicitly_wait(5)


@when('From right side navigation menu,click sign in')
def right_side_click_sign_in(context):
    context.app.pages.side_signin_page.click_sign_in()
    wait=WebDriverWait(context.driver, 10).until(
    wait.click()


@then('verify sign in form opened')
def verify_sign_in_from_opened(context):
       context.app.pages.sign_in_opened_page.sign_in_opened()
