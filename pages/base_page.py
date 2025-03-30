class Page:

    def __init__(self, driver):
        self.driver = driver
        self.base_url='https://www.target.com/'

    def open_url(self, url):
        self.driver.get(url)

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)

    def click(self, *locator):
        self.driver.find_element(*locator).click()

    def input_text(self, text, *locator):
        self.driver.find_element(*locator).send_keys(text)

    def verify_text(self, expected_text, *locator):
        actual_text= self.find_element(*locator).text
        assert actual_text == expected_text, f'the expected text {expected_text } did not match the actual text {actual_text}'


    def verify_partial_text(self, expected_text, *locator):
        actual_text= self.find_element(*locator).text
        assert actual_text in expected_text, f'the expected text {expected_text } did not found in actual  {actual_text}'

    def verify_partial_url(self, expected_partial_url):
        current_url = self.driver.current_url
        print(f'current url {current_url}')
        assert expected_partial_url in current_url,f'expected text {expected_partial_url} but found {current_url}'