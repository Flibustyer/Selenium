from selenium.webdriver.common.by import By


class BasePage:
    """Describes base methods for the website"""

    def __init__(self, driver):
        self.driver = driver

    def fill_field(self, xpath, value):
        """Fill field using provided value"""
        element = self.driver.find_element(By.XPATH, xpath)
        element.clear()
        element.send_keys(value)

    def click(self, xpath):
        """Find and click on the element by providing xpath"""
        self.driver.find_element(By.XPATH, xpath).click()

    def compare_element_text(self, text, xpath):
        element = self.driver.find_element(By.XPATH, xpath)
        return element.text == text
