import configparser


config = configparser.RawConfigParser()
config.read(".\\Configuration\\configData.ini")


class ReadConfig:

    @staticmethod
    def getBaseUrl():
        url = config.get("commonData", "base_url")
        return url

    @staticmethod
    def getUserName():
        userName = config.get("commonData", "userName")
        return userName

    @staticmethod
    def getPassword():
        password = config.get("commonData", "password")
        return password

    @staticmethod
    def getValueFromConfigData(rowValue, variable):
        value = config.get(rowValue, variable)
        return value
