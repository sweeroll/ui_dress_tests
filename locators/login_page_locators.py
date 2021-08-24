from selenium.webdriver.common.by import By


class LoginPageLocators:
    EMAIL = (By.ID, "email")
    PASSWORD = (By.ID, "passwd")
    LOGIN_SUBMIT = (By.ID, "SubmitLogin")
