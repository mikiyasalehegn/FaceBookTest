from selenium.webdriver.common.by import By
from BasePage.basepage import BasePage
from Locators.forgot_password_locators import Locators


class ForgotPassword(BasePage, Locators):
    def open(self):
        self._driver.get(self.url)
        self._driver.maximize_window()

    def execute_forgot_password_with_invalid_phone(self):
        self._clear(By.XPATH, self.phone_xpath)
        self._entry(By.XPATH, self.phone_xpath, "0539024548")
        self._clear(By.XPATH, self.pass_xpath)
        self._entry(By.XPATH, self.pass_xpath, "miki98419")
        self._click(By.XPATH, self.login_xpath)
        self._click(By.CLASS_NAME, self.forgot_password_link)
        self._click(By.XPATH, self.not_you)
        self._entry(By.XPATH, self.address_field, "168459849")
        self._click(By.XPATH, self.search_button)
        self._is_displayed(By.XPATH, self.forgot_password_error)

    def execute_forgot_password_with_valid_phone(self):
        self._clear(By.XPATH, self.phone_xpath)
        self._entry(By.XPATH, self.phone_xpath, "0539024548")
        self._clear(By.XPATH, self.pass_xpath)
        self._entry(By.XPATH, self.pass_xpath, "miki98419")
        self._click(By.XPATH, self.login_xpath)
        self._click(By.CLASS_NAME, self.forgot_password_link)
        self._click(By.XPATH, self.continue_button)
        assert self._message(By.XPATH, self.instruction) == "We sent your code to:"
        assert self._message(By.XPATH, self.assert_phone) == "+972539024548"

    def execute_forgot_password_by_entering_incorrect_code(self):
        self._clear(By.XPATH, self.phone_xpath)
        self._entry(By.XPATH, self.phone_xpath, "0539024548")
        self._clear(By.XPATH, self.pass_xpath)
        self._entry(By.XPATH, self.pass_xpath, "miki98419")
        self._click(By.XPATH, self.login_xpath)
        self._click(By.CLASS_NAME, self.forgot_password_link)
        self._click(By.XPATH, self.continue_button)
        assert self._message(By.XPATH, self.instruction) == "We sent your code to:"
        assert self._message(By.XPATH, self.assert_phone) == "+972539024548"
        self._entry(By.XPATH, self.code_field, "164651")
        self._click(By.XPATH, self.continue_button)
        self._is_displayed(By.XPATH, self.code_error)
        alert = self._find(By.XPATH, self.code_error).value_of_css_property("background-color")
        assert alert == "rgba(0, 0, 0, 0)"

    def execute_forgot_password_with_valid_email(self):
        self._clear(By.XPATH, self.phone_xpath)
        self._entry(By.XPATH, self.phone_xpath, "0539024548")
        self._clear(By.XPATH, self.pass_xpath)
        self._entry(By.XPATH, self.pass_xpath, "miki98419")
        self._click(By.XPATH, self.login_xpath)
        self._click(By.CLASS_NAME, self.forgot_password_link)
        self._click(By.XPATH, self.not_you)
        self._entry(By.XPATH, self.address_field, "mengistumike9@gmail.com")
        self._click(By.XPATH, self.search_button)
        self._is_displayed(By.XPATH, self.forgot_password_error)
        assert self._message(By.XPATH, self.via_email) == "Send code via email"

    def execute_forgot_password_without_address(self):
        self._clear(By.XPATH, self.phone_xpath)
        self._entry(By.XPATH, self.phone_xpath, "0539024548")
        self._clear(By.XPATH, self.pass_xpath)
        self._entry(By.XPATH, self.pass_xpath, "miki98419")
        self._click(By.XPATH, self.login_xpath)
        self._click(By.CLASS_NAME, self.forgot_password_link)
        self._click(By.XPATH, self.not_you)
        self._click(By.XPATH, self.search_button)
        assert self._message(By.XPATH, self.empty_error) == "Please fill in at least one field"
        alert = self._find(By.XPATH, self.empty_error).value_of_css_property("background-color")
        assert alert == "rgba(0, 0, 0, 0)"

