from selenium.webdriver.common.by import By

from pages.base_page import Page


class TargetAppPage(Page):
    PP_LINK = (By.XPATH, "//a[text()='Privacy policy']")

    def open_target_app(self):
        self.open_url('https://www.target.com/c/target-app/')

    def click_privacy_policy_link(self):
        self.click(*self.PP_LINK)

    def verify_privacy_policy_opened(self):
        self.verify_partial_url('target-privacy-policy')