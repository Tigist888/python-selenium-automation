from selenium.webdriver.common.by import By
from pages.base_page import Page

class CartPage(Page):
    cart_empty_message=(By.XPATH, "//h1[normalize-space()='Your cart is empty']")
    cart_one_item=(By.CSS_SELECTOR, "[data-test='cartItem-qty' ]").

    def verify_cart_empty(self):

        expected_text = "Your cart is empty"
        self.verify_text('Your cart is empty',*self.cart_empty_message)

    def verify_cart_has_one_item(self):
        expected_text = "Qty1"
        actual_result=self.verify_text('Qty1',*self.cart_one_item)