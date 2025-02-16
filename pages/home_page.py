from pages.base_page import BasePage
from pages.login_page import LoginPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC # do sprawdzania czy elemtnty są klikalne
from time import sleep



class HomePageLocators:
    """
    Home page locators
    """
    LOG_IN_A = (By.ID, "login2") # dużymi literami piszemy stałą a nie zmienna, to jest krotka bo jej nie zmianiamy
    LOG_OUT_A = (By.ID, "logout2") # dużymi literami piszemy stałą a nie zmienna, to jest krotka bo jej nie zmianiamy
    LOGGED_USER_NAME = (By.ID, "nameofuser")

    pass

class HomePage(BasePage):
    """
    Home page object
    """
    # Tutaj będą rozmaite mechanizmy

    def click_log_in(self):
        """
        click log in
        :return:
        """
        # Find button log in and click it
        self.driver.find_element(*HomePageLocators.LOG_IN_A).click() # rozpakowanie krotki, zamiast jednego elemntu krotka są dwa elementy z krotki, gwiazdką można też spakować do krotki
        # return login page
        return LoginPage(self.driver)

    def click_log_out(self):
        """
        click log in
        :return:
        """
        # Find button log in and click it
        self.driver.find_element(*HomePageLocators.LOG_OUT_A).click() # rozpakowanie krotki, zamiast jednego elemntu krotka są dwa elementy z krotki, gwiazdką można też spakować do krotki



    def click_contact(self):
        """
        click contact
        :return:
        """
        # TODO:
        pass

    def _verife_page(self):
        # TODO:
        assert "STORE" == self.driver.title

    def get_welcome_user_name_text(self):
        """
        gets Welcome <USERNAME> message from top right of the page
        :return: Welcome <USERNAME> text
        """
        self.wait_5s.until(EC.text_to_be_present_in_element(HomePageLocators.LOGGED_USER_NAME, "Welcome"))
        return self.driver.find_element(*HomePageLocators.LOGGED_USER_NAME).text
