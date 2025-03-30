from selenium.webdriver.common.by import By
from pages.base_page import Page

class SignInOpenedPage(Page):

    Opened_signin_page=(By.CSS_SELECTOR, '.sc-b40687e3-1.lgZeIE')


    def sign_in_opened(self):
        expected_result = 'page to be opened'
        actual_result=self.find_element(*self.Opened_signin_page)
        assert expected_result== actual_result,f'Error. result {expected_result} not in {actual_result,}'