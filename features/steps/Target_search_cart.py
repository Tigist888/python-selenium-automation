from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open target main page')
def open_target_main(context):
    context.driver.get('https://www.target.com/')

    @when('click on cart icon')
    def search_product(context):
       context.driver.find_element(By.CSS_SELECTOR, "[color='#333']").click()
        sleep(6)

    @then('verify your "cart is empty message" is shown')
    def verify_search_results(context):
        actual_text = context.driver.find_element(By.CSS_SELECTOR, '.styles_ndsHeading__HcGpD.styles_fontSize1__i0fbt.styles_x2Margin__M5gHh').text
        expected_text = 'Your cart is empty'
        assert expected_text in actual_text, f'Error. Text {expected_text} not in {actual_text}'