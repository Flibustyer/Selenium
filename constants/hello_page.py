class HelloPageConstants:
    """Stores constants related to hello page"""

    @staticmethod
    def username_xpath(username):
        hello_page_username_xpath = f".//span[text()=' {username}']"
        return hello_page_username_xpath

    # Header
    CREATE_POST_BUTTON_XPATH = ".//a[@href='/create-post']"
