import configparser

def configReader(section,key):
    config = configparser.ConfigParser()
    config.read("../Library/config.cfg")
    return config.get(section,key)


