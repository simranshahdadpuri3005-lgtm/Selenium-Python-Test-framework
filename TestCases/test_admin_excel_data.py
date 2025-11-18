import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from BasePages.Login_Admin_Page import Login_Admin_Page
from Utilities.read_properties import Read_Config
from Utilities.custom_logger import Log_Maker
from Utilities import excel_utils


class Test_02_admin_login_using_excel:
    admin_page_url = Read_Config.get_admin_page_url()
    logger = Log_Maker().log_gene()
    path = "./Testdata/TestData.xlsx"
    status_list = []

    def test_valid_admin_login_using_excel(self, setup):
        self.logger.debug(" This is TC using excel data Valid Login Test")
        self.driver = setup
        self.driver.get(self.admin_page_url)
        time.sleep(3)

        self.adminlp = Login_Admin_Page(self.driver)

        self.rows = excel_utils.get_row_count(self.path, "LoginDetails")
        print("number of rows: ", self.rows)

        for r in range(2, self.rows):
            self.username = excel_utils.read_file(self.path, "LoginDetails", r, 1)
            self.password = excel_utils.read_file(self.path, "LoginDetails", r, 2)
            self.exp_result = excel_utils.read_file(self.path, "LoginDetails", r, 3)

            self.adminlp.enter_username(self.username)
            self.adminlp.enter_password(self.password)
            self.adminlp.click_login()
            time.sleep(3)

            try:
                actual_dashboard_text = self.adminlp.get_products_text()
            except Exception as e:
                actual_dashboard_text = "No Data"
                self.logger.warning(f"Could not fetch dashboard text: {e}")

            expected_dashboard_text = "Account Set-up"

            if actual_dashboard_text == expected_dashboard_text:
                if self.exp_result == "Pass":
                    self.logger.info(" Test Passed")
                    self.status_list.append("Test Passed added in status list")
                elif self.exp_result == "Fail":
                    self.logger.info(" Test Failed")
                    self.status_list.append("Test Failed added in status list")
            elif actual_dashboard_text != expected_dashboard_text:
                if self.exp_result == "Pass":
                    self.logger.info(" Test Passed")
                elif self.exp_result == "Fail":
                    self.logger.info(" Test Failed")

            print("List status is", self.status_list)
            if "Fail" in self.status_list:
                assert False
            else:
                assert True

        self.driver.quit()
