# from selenium.webdriver.common.by import By
# from behave import given, when, then
# from time import sleep
#
#
# @given('Open target main page')
# def open_target_main(context):
#     context.driver.get('https://www.target.com/')
#
# @when('click on cart icon')
# def search_product(context):
#     context.driver.find_element(By.CSS_SELECTOR, "[viewBox='0 0 24 24']").click()
#     # sleep(6)
#
# @then('verify your "cart is empty message" is shown')
# def verify_search_results(context):
#    expected_text = "Your cart is empty"
#    actual_text = context.driver.find_element(By.CSS_SELECTOR, '.styles_ndsHeading__HcGpD.styles_fontSize1__i0fbt.styles_x2Margin__M5gHh').text
#    assert expected_text in actual_text, f'Error. Text {expected_text} not in {actual_text}'
#
#
# # the below code done by instructor Lena
# CART_SUMMARY = (By.XPATH, "//div[./span[contains(text(), 'subtotal')]]")
# CART_ITEM_TITLE = (By.CSS_SELECTOR, "[data-test='cartItem-title']")
#
#
# @when('Open cart page')
# def open_cart(context):
#     context.driver.get('https://www.target.com/cart')
#
#
# @then('Verify cart has correct product')
# def verify_product_name(context):
#     # context.product_name => stored before
#     product_name_in_cart = context.driver.find_element(*CART_ITEM_TITLE).text
#     print('Name in cart: ', product_name_in_cart)
#     assert context.product_name[:20] == product_name_in_cart[:20], \
#         f'Expected {context.product_name[:20]} did not match {product_name_in_cart[:20]}'
#
#
# @then('Verify cart has {amount} item(s)')
# def verify_cart_items(context, amount):
#     cart_summary = context.driver.find_element(*CART_SUMMARY).text
#     assert f'{amount} item' in cart_summary, f"Expected {amount} items but got {cart_summary}"
#
#
# @then("Verify 'Your cart is empty' message is shown")
# def verify_cart_empty(context):
#     expected_result = 'Your cart is empty'
#     actual_result = context.driver.find_element(By.CSS_SELECTOR, "[data-test='boxEmptyMsg']").text
#     assert expected_result == actual_result, f'Expected {expected_result} did not match actual {actual_result}'