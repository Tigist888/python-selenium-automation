from selenium.webdriver.common.by import By
from pages.base_page import Page

class SignInOpenedPage(Page):

    Opened_signin_page=(By.CSS_SELECTOR, "//span[normalize-space()='Sign into your Target account']")
    sign_in_button=(By.CSS_SELECTOR, '#login')
    target_terms_and_conditions=(By.XPATH,    " //a[normalize-space()='Target terms and conditions']")

    def sign_in_opened(self):
        expected_result = 'Sign into your Target account'
        actual_result=self.find_element(*self.Opened_signin_page)
        assert expected_result== actual_result,f'Error. result {expected_result} not in {actual_result,}'

    def click_sign_in_with_password(self):
        self.find_element(*self.sign_in_button)

    def click_target_terms_and_conditions(self):
        self.find_element(*self.target_terms_and_conditions).click()

