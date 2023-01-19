import logging
import time

from constants.start_page import StartPageConstants
from pages.base_page import BasePage
from pages.reg_form_errors import RegFormErrors


class StartPage(BasePage):
    """Stores methods describes start page options"""

    def __init__(self, driver):
        super().__init__(driver)
        self.const = StartPageConstants
        self.errors = RegFormErrors(driver)
        self.log = logging.getLogger("[StartPage]")

    def sign_in(self, username, password):
        """Sign in using provided values"""

        # Fill in fields
        self.fill_field(xpath=self.const.SIGN_IN_USERNAME_FIELD_XPATH, value=username)
        self.fill_field(xpath=self.const.SIGN_IN_PASSWORD_FIELD_XPATH, value=password)
        time.sleep(1)
        # Click on SignIn button
        self.click(xpath=self.const.SIGN_IN_SUBMIT_BUTTON_XPATH)
        time.sleep(1)

    def verify_sign_in_error(self):
        """Verify that text matches to the error text"""
        assert self.compare_element_text(xpath=self.const.SIGN_IN_ERROR_POPUP_XPATH,
                                         text=self.const.SIGN_IN_ERROR_POPUP_TEXT)

    def sign_up(self, username, email, password):
        """Sign up using provided values"""

        # Fill in fields
        self.fill_field(xpath=self.const.REGISTER_FORM_USERNAME, value=username)
        self.fill_field(xpath=self.const.REGISTER_FORM_EMAIL, value=email)
        self.fill_field(xpath=self.const.REGISTER_FORM_PASSWORD, value=password)
        time.sleep(2)
        # Click on SignIn button
        self.click(xpath=self.const.REGISTER_FORM_SIGN_UP_BUTTON_XPATH)
        time.sleep(2)

        from pages.hello_page import HelloPage
        return HelloPage(self.driver, username=username)

    def verify_sign_up_error(self):
        """Verify that text matches to the error text"""
        if self.errors.reg_form_username():
            pass
        elif self.errors.reg_form_email():
            pass
        elif self.errors.reg_form_password():
            pass
        elif self.errors.reg_form_username_invalid_symb():
            pass
