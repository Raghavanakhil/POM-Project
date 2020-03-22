import pytest
from StartBrowser import hitBrowser
from Configuration import Config
from Pages import loginPage
from DataDriven import dataGenerator

@pytest.mark.parametrize('data',dataGenerator.dataGenerator())
def test_Loginpage(data):
    driver = hitBrowser.Browser()
    register = loginPage.Login(driver)
    register.username(data[0])
    register.password(data[1])
    register.login()











