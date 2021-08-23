from locators.login import LoginPageLocators


class LoginPage:
    def __init__(self, app):
        self.app = app

    def auth(self, login: str, password: str):
        sign_in = self.app.driver.find_element(*LoginPageLocators.SIGN_IN)
        sign_in.click()
        email_input = self.app.driver.find_element(*LoginPageLocators.EMAIL)
        email_input.send_keys(login)
        password_input = self.app.driver.find_element(*LoginPageLocators.PASSWORD)
        password_input.send_keys(password)
        submit_button = self.app.driver.find_element(*LoginPageLocators.LOGIN_SUBMIT)
        submit_button.click()
