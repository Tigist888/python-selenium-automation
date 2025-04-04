from selenium.webdriver.common.by import By
from pages.base_page import Page

class TermAndConditionsPage(Page):

   term_conditions=(By.XPATH, "//h1[normalize-space()='Terms & Conditions']")

   def terms_and_conditions_page(self):
       expected_text = "Terms & Conditions"
       actual_text=self.find_element(*self.term_conditions)
       assert expected_text == actual_text.text, f'Expected: {expected_text}, not match Actual: {actual_text}'
