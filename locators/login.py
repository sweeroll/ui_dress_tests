from selenium.webdriver.common.by import By


class LoginPageLocators:
    SIGN_IN = (By.CLASS_NAME, "header_user_info")
    EMAIL = (By.ID, "email")
    PASSWORD = (By.ID, "passwd")
    LOGIN_SUBMIT = (By.ID, "SubmitLogin")
    ACCOUNT_NAME = (By.CLASS_NAME, "account")