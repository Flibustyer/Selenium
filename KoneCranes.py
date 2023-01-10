"""Test related to registration form and process"""

# import logging
# import pytest
# import random
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestStartPage:

    def test_registration_form(self):
        # open start page
        driver = webdriver.Chrome(executable_path="C:\chromedriver\chromedriver.exe")
        driver.get("https://konecranes.service-now.com/navpage.do")

        # Fill in Login
        username_field = driver.find_element(by=By.XPATH, value=".//input[@type='email']")
        username_field.clear()
        username = "andrii.ovanesian.ext@konecranes.com"
        username_field.send_keys(username)
        time.sleep(1)

        # Click on Next button
        next_button = driver.find_element(by=By.XPATH, value=".//input[@type='submit']")
        next_button.click()
        time.sleep(1)

        # Fill in password
        password_field = driver.find_element(by=By.XPATH, value=".//input[@name='passwd']")
        password_field.clear()
        password_field.send_keys("Prime5510")
        time.sleep(1)

        # Click on Sign In button
        next_button = driver.find_element(by=By.XPATH, value=".//input[@type='submit']")
        next_button.click()
        time.sleep(4)

        # # Verify transfer to personal page
        # page_title = driver.find_element(by=By.XPATH, value=f".//span[text()=' {username}']")
        # assert page_title.text == username
        # self.log.info("Transfer  to personal page (registration) was verified")
        # time.sleep(1)
        # driver.close()
