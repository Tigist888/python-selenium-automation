from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

#2. Create a test case that will open the Target Circle page

@given('open the Target Circle page')
def open_target_main_circle(context):
    context.driver.get('https://www.target.com/circle')



@then('verify there are at least 10 benefit cells')
def verify_benefit_cells(context):
    benefit_cells=context.driver.find_elements(By.CSS_SELECTOR, '.cell-item-content')
    assert len(benefit_cells) >= 10, f"Expected at least 10 benefit cells, but found {len(benefit_cells)}"
