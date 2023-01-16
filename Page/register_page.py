from selenium.webdriver.common.by import By

from BasePage.basepage import BasePage
from Locators.registration_locators import RegisterLocators


class Register(RegisterLocators, BasePage):
    def open(self):
        self._driver.get(self.url)
        self._driver.maximize_window()

    def register_with_invalid_phone(self):
        self._click(By.CLASS_NAME, self.create_account)
        self._clear(By.NAME, self.f_name)
        self._entry(By.NAME, self.f_name, "Miki")
        self._clear(By.NAME, self.l_name)
        self._entry(By.NAME, self.l_name, "Genet")
        self._clear(By.NAME, self.e_address)
        self._entry(By.NAME, self.e_address, "+65181651984")
        self._clear(By.NAME, self.r_pass)
        self._entry(By.NAME, self.r_pass, "1234567")
        self._select(By.NAME, self.year)
        self._click(By.CLASS_NAME, self.sex)
        self._click(By.NAME, self.signup)
        self._is_displayed(By.CLASS_NAME, self.pe_message)

    def register_with_invalid_email(self):
        self._click(By.CLASS_NAME, self.create_account)
        self._clear(By.NAME, self.f_name)
        self._entry(By.NAME, self.f_name, "Miki")
        self._clear(By.NAME, self.l_name)
        self._entry(By.NAME, self.l_name, "Genet")
        self._clear(By.NAME, self.e_address)
        self._entry(By.NAME, self.e_address, "gfchbkgmail.com")
        self._clear(By.NAME, self.r_pass)
        self._entry(By.NAME, self.r_pass, "1234567")
        self._select(By.NAME, self.year)
        self._click(By.CLASS_NAME, self.sex)
        self._click(By.NAME, self.signup)
        self._is_displayed(By.CLASS_NAME, self.pe_message)

    def register_with_less_password(self):
        self._click(By.CLASS_NAME, self.create_account)
        self._clear(By.NAME, self.f_name)
        self._entry(By.NAME, self.f_name, "Miki")
        self._clear(By.NAME, self.l_name)
        self._entry(By.NAME, self.l_name, "Genet")
        self._clear(By.NAME, self.e_address)
        self._entry(By.NAME, self.e_address, "0539024548")
        self._clear(By.NAME, self.r_pass)
        self._entry(By.NAME, self.r_pass, "1234567")
        self._select(By.NAME, self.year)
        self._click(By.CLASS_NAME, self.sex)
        self._click(By.NAME, self.signup)
        self._is_displayed(By.CLASS_NAME, self.password_message)

    def register_without_fname(self):
        self._click(By.CLASS_NAME, self.create_account)
        self._clear(By.NAME, self.f_name)
        self._entry(By.NAME, self.f_name, "")
        self._clear(By.NAME, self.l_name)
        self._entry(By.NAME, self.l_name, "Genet")
        self._clear(By.NAME, self.e_address)
        self._entry(By.NAME, self.e_address, "0539024548")
        self._clear(By.NAME, self.r_pass)
        self._entry(By.NAME, self.r_pass, "1234567")
        self._select(By.NAME, self.year)
        self._click(By.CLASS_NAME, self.sex)
        self._click(By.NAME, self.signup)
        self._is_displayed(By.CLASS_NAME, self.name_error)

    def register_without_lname(self):
        self._click(By.CLASS_NAME, self.create_account)
        self._clear(By.NAME, self.f_name)
        self._entry(By.NAME, self.f_name, "Miki")
        self._clear(By.NAME, self.l_name)
        self._entry(By.NAME, self.l_name, "")
        self._clear(By.NAME, self.e_address)
        self._entry(By.NAME, self.e_address, "0539024548")
        self._clear(By.NAME, self.r_pass)
        self._entry(By.NAME, self.r_pass, "1234567")
        self._select(By.NAME, self.year)
        self._click(By.CLASS_NAME, self.sex)
        self._click(By.NAME, self.signup)
        self._is_displayed(By.CLASS_NAME, self.pe_message)



