import logging

from constants.hello_page import HelloPageConstants
from pages.base_page import BasePage


class HelloPage(BasePage):
    """Stores methods describes Hello page options"""

    def __init__(self, driver, username):
        super().__init__(driver)
        self.username_xpath = HelloPageConstants.username_xpath(username)
        self.const = HelloPageConstants
        self.log = logging.getLogger("[HelloPage]")

    def verify_success_sign_up(self, username):
        """Verify sign up username"""
        assert self.compare_element_text(xpath=self.username_xpath, text=username)

    def verify_success_sign_in(self, username):
        """Verify sign up username"""
        assert self.compare_element_text(xpath=self.username_xpath, text=username)

    def navigate_to_create_post(self):
        """Navigate to create post via header button"""
        self.click(xpath=self.const.CREATE_POST_BUTTON_XPATH)

        from pages.create_post_page import CreatePostPage
        return CreatePostPage(self.driver)
