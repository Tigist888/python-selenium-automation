from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from behave import given, then



@given('open target product page')
def open_product_page(context):
    context.driver.get('https://www.target.com/p/A-91511634')



@then('verify user can click through colors')
def verify_color_selection(context):
    wait = WebDriverWait(context.driver, 10)

    # Find all color options
    color_options = wait.until(
        EC.presence_of_all_elements_located((By.XPATH, "//li[contains(@class, 'ndsCarouselItem')]")))

    for color in color_options:
        color.click()

        # Verify selected color is displayed
        selected_color = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='@web/VariationComponent'] div")))
        assert selected_color.is_displayed(), "Selected color is not displayed correctly"

    print("All colors were clicked and verified successfully.")