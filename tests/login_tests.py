from ddt import data, unpack, ddt

import test_data.test_data
from tests.base_test import BaseTest
from test_data.test_data import DataReader
from time import sleep

@ddt
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


    @data(*DataReader.get_csv_data("../test_data/valid_login_credentials.csv"))
    @unpack
    def testValidLogin(self, username, password):
        #username = "tester_alk"
        #wpisz login
        self.login_page.enter_username(username)
        sleep(3)
        #wpisz hasło
        self.login_page.enter_password(password)
        #naciśnij Log in
        self.login_page.click_log_in()
        #sprawdz czy na stronie jest Welcome tester_alk
        self.assertEqual(F"Welcome {username}",self.home_page.get_welcome_user_name_text())
        #sprawdz czy mozna kliknąć logout
        self.home_page.click_log_out()
        self.assertEqual("Log in",self.home_page.get_log_in_text())
        self.assertEqual("Sign up",self.home_page.get_sign_up_text())

        sleep(5)
        pass
