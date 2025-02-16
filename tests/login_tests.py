from os import access, wait3

from tests.base_test import BaseTest
from time import sleep

class LoginTest(BaseTest):
    def setUp(self):
        super().setUp()
        # dodatkowy warunek stępny - wejście na stronę logowania
        self.login_page = self.home_page.click_log_in()


    def testEmptyLogin(self):
        # nie wpsiujemy nic
        # Kliknij login
        self.login_page.click_log_in()
        self.assertEqual(self.login_page.get_alert_message(),"Please fill out Username and Password.")
        sleep(2)
        self.login_page.confirm_alert()
        sleep(2)

    def testValidLogin(self):
        username = "tester_alk"
        #wpisz login
        self.login_page.enter_username("tester_alk")
        sleep(3)
        #wpisz hasło
        self.login_page.enter_password("haslo")
        #naciśnij Log in
        self.login_page.click_log_in()
        #sprawdz czy na stronie jest Welcome tester_alk
        self.assertEqual(F"Welcome {username}",self.home_page.get_welcome_user_name_text())
        #sprawdz czy mozna kliknąć logout
        self.home_page.click_log_out()
        pass
