'''
Created on 20 de fev de 2016

@author: duzi
'''
from utils.util import Utils
import MySQLdb 


class BaseRepository(object):
    '''
    classdocs
    '''


    def __init__(self, configuration = None):
        '''
        Constructor
        '''
        self.conn = None
        self.database_parameters = ["server", "user", "password", "database"]
        self.database_configuration = tuple()
        if configuration:
            self.database_configuration = configuration
        
        
    def __load_database_configuration__(self):
        config = Utils.load_configuration()
        if not config.has_section("DataBase"): return None
        else: return (config.get("DataBase", db_parameter) 
                      for db_parameter in self.database_parameters)

    
    def __open__(self):
        
        if not self.database_configuration:
            self.database_configuration = self.__load_database_configuration__()
            
        try:
            server, user, password, database = self.database_configuration
            self.conn = MySQLdb.connect(server, user, password, database)
        except Exception as e:
            print(e)
            
    
    
    def __close__(self):
        if self.conn:
            pass
    
    
    def __unpack_parameters__(self, parameters):
        return (parameter for parameter in parameters)
    
    
    def execute_query(self, query, parameters):
        self.__open__()
        cur = self.conn.cursor()
        cur.execute(query, self.__unpack_parameters__(parameters))
        rows = cur.fetchall()
        self.__close__()
        return rows
    
    
    
        