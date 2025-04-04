from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then


@given("Open sign in page")
def open_sign_in_page(context):
    context.apps.pages.sing_in_opened_page.sign_in_opened()

@given("Store original window ")
def store_original_window(context):
    context.original_window=context.driver.current_window_handle
    print("original window:", context.original_window)

@when("click on Target terms and conditions link")
def click_on_target_terms_and_conditions_link(context):
    context.apps.pages.sign_in_opened_page.click_target_terms_and_conditions()
    WebDriverWait(context.driver, 10).until(EC.new_window_is_opened(context.driver))

@when("Switch to the newly opened window")
def switch_to_newly_opened_window(context):
    all_windows =context.driver.window_handles
    print("all_windows:", all_windows)
    context.driver.switch_to.window(all_windows[1])
    print("current window:", context.driver.current_window_handle)

@then("Verify Terms and Conditions page is opened")
def verify_terms_and_conditions_page(context):
   context.apps.pages.sign_in_opened_page.verify_terms_and_conditions_page()

@then("User can close new window")
def user_close_new_window_(context):
    context.driver.close()
@then("return to original window")
def return_to_original_window(context):
    context.driver.switch_to.window(context.original_window)

