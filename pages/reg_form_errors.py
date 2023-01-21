from selenium.common import NoSuchElementException

from constants.start_page import StartPageConstants
from pages.base_page import BasePage


class RegFormErrors(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.const = StartPageConstants

    def reg_form_username(self):
        try:
            if self.compare_element_text(xpath=self.const.REGISTER_FORM_ERROR_USERNAME_XPATH,
                                         text=self.const.REGISTER_FORM_ERROR_TEXT_USERNAME):
                pass
        except NoSuchElementException:
            return False
        return True

    def reg_form_email(self):
        try:
            if self.compare_element_text(xpath=self.const.REGISTER_FORM_ERROR_EMAIL_XPATH,
                                         text=self.const.REGISTER_FORM_ERROR_TEXT_EMAIL):
                pass
        except NoSuchElementException:
            return False
        return True

    def reg_form_password(self):
        try:
            if self.compare_element_text(xpath=self.const.REGISTER_FORM_ERROR_PASSWORD_XPATH,
                                         text=self.const.REGISTER_FORM_ERROR_TEXT_PASSWORD):
                pass
        except NoSuchElementException:
            return False
        return True

    def reg_form_username_invalid_symb(self):
        try:
            if self.compare_element_text(xpath=self.const.REGISTER_FORM_ERROR_USERNAME_INV_SYMB_XPATH,
                                         text=self.const.REGISTER_FORM_ERROR_TEXT_USERNAME_INV_SYMB):
                pass
        except NoSuchElementException:
            return False
        return True
