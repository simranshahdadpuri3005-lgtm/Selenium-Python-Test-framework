import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from BasePages.Login_Admin_Page import Login_Admin_Page
from Utilities.read_properties import Read_Config
from Utilities.custom_logger import Log_Maker


class Test_01_admin_login:


    admin_page_url = Read_Config.get_admin_page_url()
    username = Read_Config.get_username()
    password = Read_Config.get_password()
    invalid_username = Read_Config.get_invalid_username()
    logger = Log_Maker().log_gene()


    @pytest.mark.regression
    def test_title_verification(self, setup):
        self.logger.debug(" This is TC01, Test_title_verification")
        self.driver = setup
        self.driver.get(self.admin_page_url)
        time.sleep(3)

        expected_title ="MyDirectPlan"
        actual_title = self.driver.title

        if actual_title == expected_title:
            assert True
            self.driver.save_screenshot("./Screenshots/Title_Verification.png")
        else:
            assert False
        self.driver.quit()


    def test_valid_admin_login(self, setup):
        self.logger.debug(" This is TC02, Valid Login Test")
        self.driver = setup
        self.driver.get(self.admin_page_url)
        time.sleep(3)

        self.adminlp = Login_Admin_Page(self.driver)
        self.adminlp.enter_username(self.username)
        time.sleep(3)
        self.adminlp.enter_password(self.password)
        time.sleep(3)
        self.adminlp.click_login()
        time.sleep(3)

        pagetitle = self.adminlp.get_products_text()
        expected_pagetitle = "Account Set-up"

        if pagetitle == expected_pagetitle:
            assert True
            self.driver.save_screenshot("./Screenshots/Valid_Login.png")
        else:
            assert False
        self.driver.quit()

    @pytest.mark.sanity
    def test_invalid_admin_login(self, setup):
        self.logger.debug(" This is TC03, Invalid Login Test")
        self.driver = setup
        self.driver.get(self.admin_page_url)
        time.sleep(3)

        self.adminlp = Login_Admin_Page(self.driver)
        self.adminlp.enter_username(self.invalid_username)
        time.sleep(3)
        self.adminlp.enter_password(self.password)
        time.sleep(3)
        self.adminlp.click_login()
        time.sleep(3)

        actual_error_message = self.adminlp.get_error_message()
        expected_error_message = "We do not recognize this email address. Please enter a valid email address registered with MyDirectPlan and try again."

        if actual_error_message == expected_error_message:
            assert True
            self.driver.save_screenshot("./Screenshots/Invalid_Login.png")
        else:
            assert False
        self.driver.quit()


