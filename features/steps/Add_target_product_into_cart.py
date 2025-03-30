from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


@given('launch target main page')
def open_target_main(context):
    context.app.pages.MainPage.open_url()


@when('Search for {search_word}')
def search_product(context, search_word):
  search_word='camera'
  context.app.pages.header.search(search_word)



@when('Click on Add to cart')
def click_add_to_cart(context):
    context.app.pages.Search_results_page.click_add_to_cart()


@when('Click on Add to cart from side navigation')
def click_add_to_cart_from_side(context):
    context.app.pages.side_add_to_cart.click_add_to_cart()


@when('open the cart page')
def open_cart_page(context):
    context.app.pages.header.click_add_to_cart()



@then( 'verify cart has one item')
def verify_cart_has_one_item(context):
    context.app.pages.cart_page.verify_cart_has_one_item()
