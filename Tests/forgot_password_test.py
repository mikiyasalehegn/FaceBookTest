from Page.forgot_password_page import ForgotPassword


class Test_ForGotPassword(ForgotPassword):
    def obj(self):
        forgot = ForgotPassword()
        return forgot

    def test_forgot_password_with_invalid_phone(self):
        self.obj().open()
        self.obj().execute_forgot_password_with_invalid_phone()

    def test_forgot_password_with_valid_phone(self):
        self.obj().open()
        self.obj().execute_forgot_password_with_valid_phone()

    def test_forgot_password_by_entering_invalid_code(self):
        self.obj().open()
        self.obj().execute_forgot_password_by_entering_incorrect_code()

    def test_forgot_password_with_valid_email(self):
        self.obj().open()
        self.obj().execute_forgot_password_with_valid_email()

    def test_forgot_password_without_address(self):
        self.obj().open()
        self.obj().execute_forgot_password_without_address()