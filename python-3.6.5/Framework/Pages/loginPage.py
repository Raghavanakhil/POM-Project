from Configuration import Config

class Login():
    def __init__(self,obj):
        global driver
        driver = obj

    def username(self,uname):
        driver.find_element_by_xpath(Config.configReader("Login", "username")).send_keys(uname)

    def password(self,pwd):
        driver.find_element_by_xpath(Config.configReader("Login", "password")).send_keys(pwd)

    def login(self):
        driver.find_element_by_xpath(Config.configReader("Login","login")).click()

    def message(self):
        driver.find_element_by_xpath(Config.configReader("Login", "message"))




