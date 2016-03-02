'''
Created on 22 de fev de 2016

@author: duzi
'''

class ServiceQueue:
    '''
    classdocs
    '''
    
    ROW_DICT = { "ID": 0, "ServiceName": 1, "Host": 2 }
    

    def __init__(self, row):
        '''
        Constructor
        '''
        self.id = row[ServiceQueue.ROW_DICT["ID"]]
        self.service_name = row[ServiceQueue.ROW_DICT["ServiceName"]]
        self.host = row[ServiceQueue.ROW_DICT["Host"]]
        
        
    def __str__(self):
        '''
        '''
        return "{} {} {}".format( self.id,
                                  self.service_name,
                                  self.host)
        
    
    def to_dict(self):
        return { "id": self.id, 
                 "service_name": self.service_name,
                 "host": self.host }
        
        
        
        
        
        