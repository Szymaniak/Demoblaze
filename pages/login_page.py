from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC # do sprawdzania czy elemtnty są klikalne

class LoginPageLocators:
    LOG_IN_BUTTON = (By.XPATH, '//button[@onclick="logIn()"]')
    LOG_IN_USERNAME = (By.ID, 'loginusername')
    LOG_IN_PASSWORD = (By.ID, 'loginpassword')


class LoginPage(BasePage):
    """
    Login page object
    """
    def click_log_in(self):
        """
        waits 5 seconds for login button and clicks it
        :return:
        """
        el = self.driver.find_element(*LoginPageLocators.LOG_IN_BUTTON)
        self.wait_5s.until(EC.element_to_be_clickable(el))
        el.click()

    def get_alert_message(self):
        """
        Wait 5 seconds for alert and returns its text
        :return: alert text
        """
        self.wait_5s.until(EC.alert_is_present())
        return self.alert.text

    def confirm_alert(self):
        """
        Confirm alert (clicks OK)
        """
        self.alert.accept()

    def enter_username(self, username):
        self.driver.find_element(*LoginPageLocators.LOG_IN_USERNAME).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*LoginPageLocators.LOG_IN_PASSWORD).send_keys(password)

    def _verife_page(self):
        print("weryfikacja strony logowania")
        self.wait_5s.until(EC.visibility_of_element_located(LoginPageLocators.LOG_IN_USERNAME))
        self.wait_5s.until(EC.visibility_of_element_located(LoginPageLocators.LOG_IN_PASSWORD))





