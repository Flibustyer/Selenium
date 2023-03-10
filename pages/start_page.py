import logging

from constants.start_page import StartPageConstants
from pages.base_page import BasePage
from pages.utils import wait_until_ok


class StartPage(BasePage):
    """Stores methods describes start page options"""

    def __init__(self, driver):
        super().__init__(driver)
        self.const = StartPageConstants
        self.log = logging.getLogger("[StartPage]")

    def sign_in(self, username, password):
        """Sign in using provided values"""

        # Fill in fields
        self.fill_field(xpath=self.const.SIGN_IN_USERNAME_FIELD_XPATH, value=username)
        self.fill_field(xpath=self.const.SIGN_IN_PASSWORD_FIELD_XPATH, value=password)
        # Click on SignIn button
        self.click(xpath=self.const.SIGN_IN_SUBMIT_BUTTON_XPATH)

        from pages.hello_page import HelloPage
        return HelloPage(self.driver, username=username)

    def verify_sign_in_error(self):
        """Verify that text matches to the error text"""
        assert self.compare_element_text(xpath=self.const.SIGN_IN_ERROR_POPUP_XPATH,
                                         text=self.const.SIGN_IN_ERROR_POPUP_TEXT)

    @wait_until_ok(timeout=3, period=0.5)
    def click_and_validate_sign_up(self):
        """Click on Sign up button until disappear"""
        self.click(xpath=self.const.REGISTER_FORM_SIGN_UP_BUTTON_XPATH)
        assert not self.is_element_exist(
            xpath=self.const.REGISTER_FORM_SIGN_UP_BUTTON_XPATH), "Sigh up button didn't disappear"

    def sign_up(self, username, email, password, verify=True):
        """Sign up using provided values"""

        # Fill in fields
        self.fill_field(xpath=self.const.REGISTER_FORM_USERNAME, value=username)
        self.fill_field(xpath=self.const.REGISTER_FORM_EMAIL, value=email)
        self.fill_field(xpath=self.const.REGISTER_FORM_PASSWORD, value=password)
        # Click on SignIn button
        if verify:
            self.click_and_validate_sign_up()
        else:
            self.click(xpath=self.const.REGISTER_FORM_SIGN_UP_BUTTON_XPATH)

        from pages.hello_page import HelloPage
        return HelloPage(self.driver, username=username)

    def verify_sign_up_error(self):
        """Verify that text matches to the error text"""
        if self.is_element_exist(xpath=self.const.REGISTER_FORM_ERROR_EMAIL_XPATH):
            assert self.compare_element_text(xpath=self.const.REGISTER_FORM_ERROR_EMAIL_XPATH,
                                             text=self.const.REGISTER_FORM_ERROR_TEXT_EMAIL)
        elif self.is_element_exist(xpath=self.const.REGISTER_FORM_ERROR_USERNAME_INV_SYMB_XPATH):
            assert self.compare_element_text(xpath=self.const.REGISTER_FORM_ERROR_USERNAME_INV_SYMB_XPATH,
                                             text=self.const.REGISTER_FORM_ERROR_TEXT_USERNAME_INV_SYMB)
        elif self.is_element_exist(xpath=self.const.REGISTER_FORM_ERROR_PASSWORD_XPATH):
            assert self.compare_element_text(xpath=self.const.REGISTER_FORM_ERROR_PASSWORD_XPATH,
                                             text=self.const.REGISTER_FORM_ERROR_TEXT_PASSWORD)
        elif self.is_element_exist(xpath=self.const.REGISTER_FORM_ERROR_USERNAME_XPATH):
            assert self.compare_element_text(xpath=self.const.REGISTER_FORM_ERROR_USERNAME_XPATH,
                                             text=self.const.REGISTER_FORM_ERROR_TEXT_USERNAME)
