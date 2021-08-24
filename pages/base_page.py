from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators.base_page_locators import BasePageLocators


class BasePage:

    def __init__(self, app):
        self.app = app

    @property
    def is_auth(self, wait_time=10):
        header_user_info_elements = WebDriverWait(self.app.driver, wait_time).until(
            EC.presence_of_all_elements_located(
            BasePageLocators.HEADER_USER_INFO),
            message=f"Can't find elements by locator {BasePageLocators.HEADER_USER_INFO}"
        )
        if len(header_user_info_elements) == 2:
            return True
        else:
            return False

    def find_element(self, locator, wait_time=10):
        element = WebDriverWait(self.app.driver, wait_time).until(
            EC.presence_of_element_located(locator),
            message=f"Can't find element by locator {locator}"
        )
        return element

    def fill_element(self, element, text):
        element.clear()
        element.send_keys(text)
        return element

    def click_element(self, element):
        element.click()
