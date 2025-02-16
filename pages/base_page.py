from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support import expected_conditions as EC # do sprawdzania czy elemtnty są klikalne


class BasePage:
    """
    Base class for each page - robić tak a nie Hashem bo # nie jest widoczny po najechaniu na nazwę klasy
    """
    def __init__(self, driver):
        self.driver = driver
        self.wait_5s = WebDriverWait(self.driver,5) # 5 sekundowa czekaczka do wywoływania wszędzie
        self.alert = Alert(self.driver)
        self._verife_page()



    def _verife_page(self):     #prywatna, nie wywołujemy sami tylko w init

        return


