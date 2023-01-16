from selenium.webdriver.common.by import By

from BasePage.basepage import BasePage
from Locators.login_locators import LogInLocators


class LogInPage(BasePage, LogInLocators):

    def open(self):
        self._driver.get(self.url)
        self._driver.maximize_window()

    def execute_validphone_invaldpass(self):
        self._clear(By.XPATH, self.phone_xpath)
        self._entry(By.XPATH, self.phone_xpath, "0539024548")
        self._clear(By.XPATH, self.pass_xpath)
        self._entry(By.XPATH, self.pass_xpath, "miki98419")
        self._click(By.XPATH, self.login_xpath)
        self._is_displayed(By.XPATH, self.error_xpath)

    def valid_password_and_invalid_phone(self):
        self._clear(By.XPATH, self.phone_xpath)
        self._entry(By.XPATH, self.phone_xpath, "9919852996575")
        self._clear(By.XPATH, self.pass_xpath)
        self._entry(By.XPATH, self.pass_xpath, "mikimeng17")
        self._click(By.XPATH, self.login_xpath)
        assert self._message(By.XPATH, self.error_xpath) == self.e_message

    def execute_without_pass_and_phone(self):
        self._click(By.XPATH, self.login_xpath)
        assert self._message(By.XPATH, self.error_xpath) == self.e_message

    def execute_positive_login_with_phone(self):
        self._clear(By.XPATH, self.phone_xpath)
        self._entry(By.XPATH, self.phone_xpath, "0539024548")
        self._clear(By.XPATH, self.pass_xpath)
        self._entry(By.XPATH, self.pass_xpath, "mikimeng17")
        self._click(By.XPATH, self.login_xpath)
        assert self._message(By.XPATH, self.positive_xpath) == "Welcome to Facebook, Mikiyas"

    def incorrect_password_correct_incorrect_phone(self):
        self._clear(By.XPATH, self.phone_xpath)
        self._entry(By.XPATH, self.phone_xpath, "651651651")
        self._clear(By.XPATH, self.pass_xpath)
        self._entry(By.XPATH, self.pass_xpath, "mi6845fgh")
        self._click(By.XPATH, self.login_xpath)
        self._is_displayed(By.XPATH, self.error_xpath)
# -----------------------------------------------------------------------------------

    def negative_login(self, phone, password, error):
        self._clear(By.XPATH, self.phone_xpath)
        self._entry(By.XPATH, self.phone_xpath, phone)
        self._clear(By.XPATH, self.pass_xpath)
        self._entry(By.XPATH, self.pass_xpath, password)
        self._click(By.XPATH, self.login_xpath)
        self._is_displayed(By.XPATH, error)



