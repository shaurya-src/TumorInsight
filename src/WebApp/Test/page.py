from locator import *
from element import BasePageElement
from helper import *


class LoginUser(BasePageElement):
    locator = "/html/body/div[1]/div/div/form/div[1]/input"


class LoginPass(BasePageElement):
    locator = "/html/body/div/div/div/form/div[2]/input"


class SignupUser(BasePageElement):
    locator = "/html/body/div[1]/div/div/form/div[1]/input"


class SignupMail(BasePageElement):
    locator = "/html/body/div/div/div/form/div[2]/input"


class SignupPass(BasePageElement):
    locator = "/html/body/div/div/div/form/div[3]/input"


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver


class MainPage(BasePage):
    def title_check(self):
        cond = "TumorInsight" in self.driver.title
        test_result(cond, "1", "Title of the HomePage")
        return "TumorInsight" in self.driver.title

    def go_to_github(self):
        wait_elem(self.driver, self.driver.find_element(*MainPageLocators.GITHUB_SOCIAL))
        element = self.driver.find_element(*MainPageLocators.GITHUB_SOCIAL)
        element.click()

    def go_to_login(self):
        wait_elem(self.driver, self.driver.find_element(*MainPageLocators.LOGIN_BUTTON))
        element = self.driver.find_element(*MainPageLocators.LOGIN_BUTTON)
        element.click()

    def go_to_signup(self):
        wait_elem(self.driver, self.driver.find_element(*MainPageLocators.SIGNUP_BUTTON))
        element = self.driver.find_element(*MainPageLocators.SIGNUP_BUTTON)
        element.click()


class LoginPage(BasePage):
    user_name = LoginUser()
    user_pass = LoginPass()

    def open_login(self):
        self.driver.get("http://127.0.0.1:5000/login")
        self.driver.implicitly_wait(10)

    def go_login(self):
        wait_elem(self.driver, self.driver.find_element(*LoginPageLocators.CONFIRM_LOGIN))
        elem = self.driver.find_element(*LoginPageLocators.CONFIRM_LOGIN)
        elem.click()


class SignupPage(BasePage):
    new_user = SignupUser()
    new_mail = SignupMail()
    new_pass = SignupPass()
