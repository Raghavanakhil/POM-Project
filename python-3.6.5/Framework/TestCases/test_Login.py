import pytest
from StartBrowser import hitBrowser
from Configuration import Config
from Pages import loginPage

def test_Loginpage():
    driver = hitBrowser.Browser()
    register = loginPage.Login(driver)
    register.username("admin")
    register.password("admin123")
    register.login()




