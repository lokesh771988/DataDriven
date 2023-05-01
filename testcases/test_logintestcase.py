import time

import pytest
from selenium import webdriver
from Objects.loginObjects import Login
from utilities.readproperty import ReadConfig
from utilities import CustomLogger
from utilities import readData


class Test_Login:
    base_url = ReadConfig.getValueFromConfigData("commonData", "base_url")
    userName = ReadConfig.getValueFromConfigData("commonData", "userName")
    password = ReadConfig.getValueFromConfigData("commonData", "password")
    logger = CustomLogger.get_logger("Login Page")

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_home_page_validation(self, setup):
        self.logger.info("================== opening browser for TC1 verify home page =========")
        self.driver = setup
        self.driver.get(self.base_url)
        title = self.driver.title
        self.logger.info("Getting Title of the home page== " + title)
        self.driver.close()
        if title == ReadConfig.getValueFromConfigData("message", "home_title"):
            self.logger.info("================== verifying home title =========")
            assert True
        else:
            self.logger.info("==================not able to verify home title =========")
            assert False

    @pytest.mark.smoke
    def test_login_page_validation(self, setup):
        self.logger.info("================== opening browser for TC2 verify login page =========")
        self.driver = setup
        self.driver.get(self.base_url)
        self.lp = Login(self.driver)
        time.sleep(5)
        self.logger.info("================== providing user name =========")
        self.lp.setUserName(self.userName)
        self.logger.info("=============== providing password ==============")
        self.lp.setPassword(self.password)
        self.logger.info("=============== clicking login button in login page ==============")
        self.lp.clickLoginButton()
        time.sleep(5)
        title = self.driver.title
        if title == ReadConfig.getValueFromConfigData("message", "login_title"):
            self.driver.save_screenshot(".\\Screenshots\\loginSuccess.png")
            self.logger.info("=============== verifying login successful message ==============")
            assert True
        else:
            assert False
        self.driver.close()

    @pytest.mark.regression
    def test_login_page_validation_using_excel(self, setup):
        path = ReadConfig.getValueFromConfigData("filePath", "path")
        rows = readData.getRowCount(path, "Sheet1")
        for r in range(2, rows + 1):
            userName = readData.getReadData(path, "Sheet1", r, 1)
            password = readData.getReadData(path, "Sheet1", r, 2)
            self.logger.info("================== opening browser for TC3 verify login page using excel =========")
            self.driver = setup
            self.driver.get(self.base_url)
            self.lp = Login(self.driver)
            time.sleep(2)
            self.logger.info("================== providing user name using excel=========")
            self.lp.setUserName(userName)
            self.logger.info("=============== providing password using excel==============")
            self.lp.setPassword(password)
            self.logger.info("=============== clicking login button in login page ==============")
            self.lp.clickLoginButton()
            time.sleep(5)
            title = self.driver.title
            if title == ReadConfig.getValueFromConfigData("message", "login_title"):
                readData.writeData(path, "Sheet1", r, 3, "Pass")
                self.driver.save_screenshot(".\\Screenshots\\loginSuccess.png")
                self.logger.info("=============== verifying login successful message ==============")
            else:
                readData.writeData(path, "Sheet1", r, 3, "Fail")
                self.logger.info("=============== verifying login Fail message ==============")

