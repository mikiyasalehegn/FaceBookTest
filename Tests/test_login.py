import pytest
from Locators.login_locators import LogInLocators, invalid_password, invalid_passandphone
from Page.login_page import LogInPage


class Test_login(LogInPage, LogInLocators):

    def object(self):
        logintest = LogInPage()
        return logintest

    def test_login_with_validphone_invaldpass(self):
        self.object().open()
        self.object().execute_validphone_invaldpass()

    def test_invalid_password_and_invalid_phone(self):
        self.object().open()
        self.object().valid_password_and_invalid_phone()

    def test_without_pass_and_phone(self):
        self.object().open()
        self.object().execute_without_pass_and_phone()

    def test__positive_login_with_phone(self):
        self.object().open()
        self.object().execute_positive_login_with_phone()

    def test_incorrect_password_correct_incorrect_phone(self):
        self.object().open()
        self.object().incorrect_password_correct_incorrect_phone()

    @pytest.mark.parametrize("phone, password, error_message", [invalid_password, invalid_passandphone])
    def test_negative_login(self, phone, password, error_message):
        self.object().open()
        self.object().negative_login(phone, password, error_message)



