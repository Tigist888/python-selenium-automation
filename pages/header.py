from selenium.webdriver.common.by import By
from pages.base_page import Page

class Header(Page):
    SEARCH_FIELD = (By.ID, 'search')
    SEARCH_BTN = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
    cart_Icon=(By.CSS_SELECTOR, "div[class='sc-55744c41-1 XzoLQ'] svg")
    sign_In=(By.CSS_SELECTOR, ".sc-43f80224-3.fBDEOp.h-margin-r-x3" )


    def search(self, text):
        print(f'Searching for {text}')
        self.input_text(text, *self.SEARCH_FIELD)
        self.click(*self.SEARCH_BTN)


    def click_on_cart_icon(self):
        self.click(*self.cart_Icon)

    def sign_in(self):
        self.click(*self.sign_In)


