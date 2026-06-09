from configparser import ConfigParser

def get_config(category,key):
    config=ConfigParser()
    config.read("PytestDemo/DataDriven_Config/config.ini")
    return config.get(category,key)