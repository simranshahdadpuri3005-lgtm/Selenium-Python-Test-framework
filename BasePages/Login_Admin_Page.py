from selenium.webdriver.common.by import By


class Login_Admin_Page:

    text_username_id = "mat-input-0"
    text_password_id = "mat-input-1"
    button_login_id = "signIn_btn"
    text_products_xpath = "//span[text()='Account Set-up']"
    error_message_xpath = "//simple-snack-bar//div[1]"

    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        self.driver.find_element(By.ID, self.text_username_id).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.ID, self.text_password_id).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.ID, self.button_login_id).click()

    def get_products_text(self):
        pagetitle = self.driver.find_element(By.XPATH, self.text_products_xpath).text
        return pagetitle

    def get_error_message(self):
        error_message = self.driver.find_element(By.XPATH, self.error_message_xpath).text
        return error_message