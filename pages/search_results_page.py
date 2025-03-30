from selenium.webdriver.common.by import By

from pages.base_page import Page


class SearchResultsPage(Page):
    SEARCH_RESULTS_TEXT = (By.XPATH, "//div[@data-test='lp-resultsCount']")
    add_to_cart = (By.CSS_SELECTOR, "[id*='addToCartButtonOrTextIdFor'] ")

    def verify_search_results(self, expected_text):
        self.verify_partial_text(expected_text, *self.SEARCH_RESULTS_TEXT )

    def verify_results_url(self, expected_partial_url):
       self.verify_partial_url(expected_partial_url)

    def click_add_to_cart(self):
        self.click(*self.add_to_cart)