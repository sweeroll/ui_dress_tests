from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators
from locators.base_page_locators import BasePageLocators


class LoginPage(BasePage):

    def auth(self, login: str, password: str):
        sign_in = self.find_element(BasePageLocators.SIGN_IN)
        self.click_element(sign_in)
        email_input = self.find_element(LoginPageLocators.EMAIL)
        self.fill_element(email_input, login)
        password_input = self.find_element(LoginPageLocators.PASSWORD)
        self.fill_element(password_input, password)
        submit_button = self.find_element(LoginPageLocators.LOGIN_SUBMIT)
        self.click_element(submit_button)
