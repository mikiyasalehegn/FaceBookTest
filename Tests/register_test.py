from Page.register_page import Register


class Test_Register(Register):

    def object(self):
        register = Test_Register()
        return register

    def test_register_with_invalid_phone(self):
        self.object().open()
        self.register_with_invalid_phone()

    def test_register_with_invalid_email(self):
        self.object().open()
        self.register_with_invalid_email()

    def test_register_without_fname(self):
        self.object().open()
        self.register_without_fname()

    def test_register_with_less_password(self):
        self.object().open()
        self.register_with_less_password()

    def test_register_without_lname(self):
        self.object().open()
        self.object().register_without_lname()

