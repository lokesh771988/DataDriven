from selenium import webdriver
from selenium.webdriver.common.by import By


class Login:
    txt_login_name = "userName"
    txt_login_name_psw = "password"
    btm_login_name = "submit"

    def __init__(self, driver):
        self.driver = driver

    def setUserName(self, userName, txt_login_name=txt_login_name):
        self.driver.find_element(By.NAME, txt_login_name).clear()
        self.driver.find_element(By.NAME, txt_login_name).send_keys(userName)

    def setPassword(self, psw, txt_login_name_psw=txt_login_name_psw):
        self.driver.find_element(By.NAME, txt_login_name_psw).clear()
        self.driver.find_element(By.NAME, txt_login_name_psw).send_keys(psw)

    def clickLoginButton(self, btm_login_name=btm_login_name):
        self.driver.find_element(By.NAME, btm_login_name).click()
