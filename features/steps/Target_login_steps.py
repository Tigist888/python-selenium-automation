from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then

@given('open target main page' )
def open_target_main_page(context):
    context.base_url()

@when(' Click Sign In' )
def click_sign_in(context):
    context.pages.header.sign_In().click()
    #context.driver.find.element(By.XPATH,   "//span[@class='sc-43f80224-3 fBDEOp h-margin-r-x3']") .click()

@when('From side navigation, click sign in')
def side_navigation_click_signin(context):
    context.pages.side_sign_in().click()

    #context.driver.find.element(By.XPATH,   " //button[normalize-space()='Sign in']" ).CLICK()

@when('Input email and password on SignIn page')
def input_email_password(context):
    context.apps.pages.Input_email_password.email.send_keys("johnthevet@joytoc.com")
    context.apps.pages.Input_email_password.pwd.send_keys("test1234")

@when(' Click Sign In')
def click_sign_in_with_password(context):
    context.apps.pages.click_sign_in_with_password().click()


@then('Verify login success')
def verify_login_success(context):
   


    

