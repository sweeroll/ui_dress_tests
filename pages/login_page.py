from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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

    @property
    def is_auth(self, wait_time=10):
        header_user_info_elements = WebDriverWait(self.app.driver, wait_time).until(
            EC.presence_of_all_elements_located(LoginPageLocators.HEADER_USER_INFO),
            message=f"Can't find elements by locator {LoginPageLocators.HEADER_USER_INFO}")
        if len(header_user_info_elements) == 2:
            return True
        else:
            return False
