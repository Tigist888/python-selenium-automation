from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('the user opens the Target main page')
def open_target_main(context):
    context.app.main_page.open_main_page()

    # context.driver.get('https://www.target.com/')


# cart is on the header list so we are going to add it header page
@when('the user clicks on the cart icon')
def click_on_cart_icon(context):
    # context.driver.find_element(By.CSS_SELECTOR, "div[class='sc-55744c41-1 XzoLQ'] svg").click()
    context.app.header.click_on_cart_icon()

@then('the message "Your cart is empty" should be displayed')
def verify_cart_empty(context):
    context.app.cart_page.verify_message_empty()
# the below can be deleted
   # expected_text = "Your cart is empty"
   # actual_text = context.driver.find_element(By.CSS_SELECTOR, '.styles_ndsHeading__HcGpD.styles_fontSize1__i0fbt.styles_x2Margin__M5gHh').text
   # assert expected_text in actual_text, f'Error. Text {expected_text} not in {actual_text}'


