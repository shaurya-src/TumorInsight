from selenium import webdriver
import unittest
import page
from helper import *


class TumorInsightTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("C:\\chromedriver_win32\\chromedriver.exe")

        # TumorInsight is running locally on http://127.0.0.1:5000/
        self.driver.get("http://127.0.0.1:5000/")
        self.driver.maximize_window()

    def test_title(self):
        mainPage = page.MainPage(self.driver)
        assert mainPage.title_check()

    def test_login_page(self):
        mainPage = page.MainPage(self.driver)
        mainPage.go_to_login()
        cond = "Login" in self.driver.title
        test_result(cond, 2, "Navigation to Login Page from Home")
        assert cond

    def test_valid_user(self):
        loginPage = page.LoginPage(self.driver)
        loginPage.open_login()
        loginPage.user_name = "root"
        loginPage.user_pass = "root"
        loginPage.go_login()
        self.driver.implicitly_wait(10)
        cond = "Login" not in self.driver.title
        test_result(cond, 3, "existing user Login")
        assert cond

    def test_invalid_user(self):
        loginPage = page.LoginPage(self.driver)
        loginPage.open_login()
        loginPage.user_name = "invalidusername"
        loginPage.user_pass = "dummy"
        loginPage.go_login()
        self.driver.implicitly_wait(10)
        cond = "Login" in self.driver.title
        test_result(cond, 4, "Invalid user Login")
        assert cond

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
