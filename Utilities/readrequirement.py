import configparser

config=configparser.RawConfigParser()
config.read("C:/Users/Acer/PycharmProjects/ProtoCommerce/Configuration/config.txt")

class Readconfig():
    @staticmethod
    def getapplicationURL():
        url=config.get("common info","url")
        return url
    @staticmethod
    def getName():
        Name=config.get("common info","Name")
        return Name
    @staticmethod
    def getEmail():
        Email=config.get("common info","Email")
        return Email
    @staticmethod
    def getPassword():
        Password=config.get("common info","Password")
        return Password
    @staticmethod
    def getDOB():
        DOB=config.read("common info","DOB")
        return DOB




