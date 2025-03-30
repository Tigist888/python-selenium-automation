from selenium.webdriver.common.by import By
from pages.base_page import Page




class SignInPage(Page):
    sign_in_button =(By.XPATH, "//button[normalize-space()='Sign in']")

    def click_sign_in(self):
        self.click(*self.sign_in_button)