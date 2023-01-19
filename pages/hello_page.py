import logging

from constants.hello_page import HelloPageConstants
from pages.base_page import BasePage


class HelloPage(BasePage):
    """Stores methods describes Hello page options"""

    def __init__(self, driver, username):
        super().__init__(driver)
        self.username_xpath = HelloPageConstants.username_xpath(username)
        self.log = logging.getLogger("[HelloPage]")

    def verify_success_sign_up(self, username):
        """Verify sign up username"""

        # Verify transfer to personal page
        assert self.compare_element_text(xpath=self.username_xpath, text=username)
