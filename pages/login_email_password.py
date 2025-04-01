from selenium.webdriver.common.by import By
from pages.base_page import Page


class LoginEmailPassword(Page):
    username = (By.NAME, "username")
    password = (By.NAME, "password")

   def  Input_email_password(self, email, pwd):
        email =self.input_text(self.username,  email)
        pwd=self.input_text(self.password,  pwd)
