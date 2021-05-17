from selenium.webdriver.common.by import By


class MainPageLocators(object):
    LOGIN_BUTTON = (By.XPATH, "/html/body/header/div/nav/ul/li[5]/a")
    SIGNUP_BUTTON = (By.XPATH, "/html/body/footer/div[1]/div/div/div[3]/ul/li[5]/a")
    GITHUB_SOCIAL = (By.XPATH, "/html/body/footer/div[1]/div/div/div[1]/div/a[1]")


class LoginPageLocators(object):
    NEW_ACC = (By.XPATH, "/html/body/div/div/div/form/div[4]/a")
    CONFIRM_LOGIN = (By.XPATH, "/html/body/div/div/div/form/div[3]/button")
    USER_NAME = (By.ID, "uname")
    USER_PASS = (By.ID, "passw")


class SignupPageLocators(object):
    LOGIN_LINK = (By.XPATH, "/html/body/div/div/div/form/div[5]/a")
    CONFIRM_REGISTER = (By.XPATH, "/html/body/div/div/div/form/div[4]/button")
    NEW_NAME = (By.ID, "uname")
    NEW_MAIL = (By.ID, "mail")
    NEW_PASS = (By.ID, "passw")
