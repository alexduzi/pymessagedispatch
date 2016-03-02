'''
Created on 20 de fev de 2016

@author: duzi
'''
from configparser import ConfigParser

class Utils:
    
    '''
    classdocs
    '''

    @staticmethod
    def load_configuration():
        config = ConfigParser()
        config.read("app.cfg")
        return config
    
    
    @staticmethod
    def get_value(section, option):
        config = Utils.load_configuration()
        if config.has_section(section): return config.get(section, option)
        else : return None
            