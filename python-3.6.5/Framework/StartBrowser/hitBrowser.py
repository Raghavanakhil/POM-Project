import selenium
from selenium.webdriver import Chrome
from selenium import webdriver
from Configuration import Config
def Browser():
    global driver
    path = "../Driver/chromedriver.exe"
    driver =Chrome(executable_path=path)
    driver.get(Config.configReader("Details","url"))
    driver.maximize_window()
    return driver

def Browserclose():
    driver.close()
