from pages.base_page import Page
from pages.cart_page import CartPage
from pages.header import Header
from pages.main_page import MainPage
from pages.search_results_page import SearchResultsPage
from pages.side_sign_in_page import SignInPage
from pages.sign_in_opened_page import SignInOpenedPage
from pages.login_email_password import LoginEmailPassword
from pages.target_app_page import TargetAppPage


class Application:

    def __init__(self, driver):
        self.driver = driver

        self.header = Header(driver)
        self.main_page = MainPage(driver)
        self.search_results_page = SearchResultsPage(driver)
        self.cart_page = CartPage(driver)
        self.click_sign_in= SignInPage(driver)
        self.sign_in_opened= SignInOpenedPage(driver)
        self.login_email_password=LoginEmailPassword(driver)
        self.target_app_page = TargetAppPage(driver)

        ##self.filename.py=classname(driver)