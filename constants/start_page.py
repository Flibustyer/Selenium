class StartPageConstants:
    """Stores constants related to start page"""

    # Sign_in
    SIGN_IN_USERNAME_FIELD_XPATH = ".//input[@placeholder='Username']"
    SIGN_IN_PASSWORD_FIELD_XPATH = ".//input[@name='password'][@class='form-control form-control-sm input-dark']"
    SIGN_IN_SUBMIT_BUTTON_TEXT = 'Sign In'
    SIGN_IN_SUBMIT_BUTTON_XPATH = f".//button[text()='{SIGN_IN_SUBMIT_BUTTON_TEXT}']"
    SIGN_IN_ERROR_POPUP_XPATH = ".//div[@class='alert alert-danger text-center']"
    SIGN_IN_ERROR_POPUP_TEXT = 'Invalid username pasword'

    # Sign_up
    REGISTER_FORM_USERNAME = ".//input[@id='username-register']"
    REGISTER_FORM_PASSWORD = ".//input[@id='password-register']"
    REGISTER_FORM_EMAIL = ".//input[@id='email-register']"
    REGISTER_FORM_SIGN_UP_BUTTON_XPATH = ".//button[@type='submit']"
    REGISTER_FORM_ERROR_TEXT_USERNAME = 'That username is already taken.'
    REGISTER_FORM_ERROR_TEXT_USERNAME_INV_SYMB = 'Username can only contain letters and numbers.'
    REGISTER_FORM_ERROR_TEXT_EMAIL = 'That email is already being used.'
    REGISTER_FORM_ERROR_TEXT_PASSWORD = 'Password cannot exceed 50 characters.'
    REGISTER_FORM_ERROR_USERNAME_XPATH = f"//div[@class='form-group']/div[text()= '{REGISTER_FORM_ERROR_TEXT_USERNAME}']"
    REGISTER_FORM_ERROR_USERNAME_INV_SYMB_XPATH = f"//div[@class='form-group']/div[text()= '{REGISTER_FORM_ERROR_TEXT_USERNAME_INV_SYMB}']"
    REGISTER_FORM_ERROR_EMAIL_XPATH = f"//div[@class='form-group']/div[text()= '{REGISTER_FORM_ERROR_TEXT_EMAIL}']"
    REGISTER_FORM_ERROR_PASSWORD_XPATH = f"//div[@class='form-group']/div[text()= '{REGISTER_FORM_ERROR_TEXT_PASSWORD}']"
