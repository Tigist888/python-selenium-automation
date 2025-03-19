from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open target main page')
def open_target_main(context):
    context.driver.get('https://www.target.com/')


@when('Search for "camera"')
def search_camera(context):
  search_word='camera'
  context.driver.find_element(By.CSS_SELECTOR,'#search' ).send_keys( 'search_word')


@when('Click on Add to cart')
def click_add_to_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, "[id*='addToCartButtonOrTextIdFor'] ").click()


@when('Click on Add to cart from side navigation')
def click_add_to_cart_from_side(context):
    context.driver.find_element(By.CSS_SELECTOR, "[id*='addToCartButtonOrTextIdFor' ] ").click()

@when('open the cart page')
def open_cart_page(context):
    context.driver.find_element(By.CSS_SELECTOR,"[ data-test='@web/CartIcon'] "  ).click()


@then( 'verify cart has one item ')
def verify_cart_has_one_item(context):
    actual_result=context.driver.find_element(By.CSS_SELECTOR, "[data-test='cartItem-qty' ] " )
    assert actual_result =="1", f"Expected 1, got {actual_result}"
