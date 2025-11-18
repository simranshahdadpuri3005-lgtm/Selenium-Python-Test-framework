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
        self.logger.debug("Starting Admin Login Test using Excel Data")
        self.driver = setup
        self.driver.get(self.admin_page_url)
        time.sleep(3)

        self.adminlp = Login_Admin_Page(self.driver)

        self.rows = excel_utils.get_row_count(self.path, "LoginDetails")
        print("Number of rows in Excel sheet:", self.rows)
        self.logger.info(f"Total test cases (rows) found: {self.rows - 1}")

        for r in range(2, self.rows + 1):  # Start from 2 if row 1 is header
            username = excel_utils.read_file(self.path, "LoginDetails", r, 1)
            password = excel_utils.read_file(self.path, "LoginDetails", r, 2)
            exp_result = excel_utils.read_file(self.path, "LoginDetails", r, 3)

            # Skip empty or invalid rows
            if not username or not password:
                self.logger.warning(f"Skipping row {r}: Missing username or password")
                continue

            self.logger.info(f"Attempting login with Username: {username}, Expected Result: {exp_result}")

            # Clear and re-enter data for each iteration
            self.adminlp.enter_username(username)
            self.adminlp.enter_password(password)
            time.sleep(1)

            self.adminlp.click_login()
            time.sleep(3)

            try:
                actual_dashboard_text = self.adminlp.get_products_text()
            except Exception:
                actual_dashboard_text = "No Data"

            expected_dashboard_text = "Account Set-up"

            # Determine Pass/Fail
            if actual_dashboard_text == expected_dashboard_text and exp_result == "Pass":
                self.logger.info(f"Row {r}: Test Passed ✅")
                self.status_list.append("Pass")
            elif actual_dashboard_text != expected_dashboard_text and exp_result == "Fail":
                self.logger.info(f"Row {r}: Negative Test Passed ✅ (Login should fail)")
                self.status_list.append("Pass")
            else:
                self.logger.error(f"Row {r}: Test Failed ❌ (Expected {exp_result}, got {actual_dashboard_text})")
                self.status_list.append("Fail")

            # Optional: navigate back to login page for next iteration
            self.driver.get(self.admin_page_url)
            time.sleep(2)

        print("Final test status list:", self.status_list)
        self.logger.info(f"Final test status list: {self.status_list}")

        # Assert after all rows are tested
        if "Fail" in self.status_list:
            self.logger.error("Some admin login test cases failed ❌")
            assert False
        else:
            self.logger.info("All admin login test cases passed ✅")
            assert True

        self.driver.quit()
