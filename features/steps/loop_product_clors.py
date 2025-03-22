from selenium.webdriver.common.by import By
from behave import given, then
from time import sleep



@given('open target product page')
def open_product_page(context):
    context.driver.get('https://www.target.com/p/A-91511634')



@then('verify user can click through colors')
def verify_color_selection(context):
    # Find all color options
    color_options = context.driver.find_elements(By.XPATH, "//li[@class='styles_ndsCarouselItem__dnUkr']")

    for color in color_options:
        color.click()
        sleep(1)

        # Verify selected color is displayed
        selected_color = context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/VariationComponent'] div")
        assert selected_color.is_displayed(), "Selected color is not displayed correctly"

    print("All colors were clicked and verified successfully.")