import configparser
import os
from pathlib import Path

def get_project_root() -> Path:
    output = Path(__file__).parent.parent
    output = str(output)
    result = output.split('\\')
    path = "/".join(result)
    return path

path = get_project_root()
config=configparser.RawConfigParser()
config.read(path)

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




