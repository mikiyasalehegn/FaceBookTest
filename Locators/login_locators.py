error_xpath = "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/form[1]/div[1]/div[1]/div[2]"
invalid_password = ("0539024548", "miki98419", error_xpath)
invalid_passandphone = ("651651651", "mi6845fgh", error_xpath)


class LogInLocators:
    url = "https://www.facebook.com/"
    phone_xpath = "//input[@id='email']"
    pass_xpath = "//input[@id='pass']"
    login_xpath = "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/form[1]/div[2]/button[1]"
    error_xpath = "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/form[1]/div[1]/div[1]/div[2]"
    error_class_name = "_39il"
    # error_without = "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/form[1]/div[1]/div[1]/div[2]"
    e_message = "The email address or mobile number you entered isn't connected to an account. Find your account and log in."
    positive_xpath = "//span[contains(text(),'Welcome to Facebook, Mikiyas')]"
    invalid_password = ("0539024548", "miki98419", error_xpath)
    invalid_passandphone = ("651651651", "mi6845fgh", error_xpath)
