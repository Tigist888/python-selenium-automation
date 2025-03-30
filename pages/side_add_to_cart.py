from selenium.webdriver.common.by import By
from pages.base_page import Page


class Side_add_cartpage(Page):

    side_add_cart_btn =(By.CSS_SELECTOR, "[id*='addToCartButtonOrTextIdFor' ] ")

    def click_add_to_cart_from_side(self):
        self.click(self.side_add_cart_btn)