'''
Created on 20 de fev de 2016

@author: duzi
'''

from models.servicequeue import ServiceQueue
from messagedispatchserviceapi.repository.baserepository import BaseRepository


class ServiceQueueRepository(BaseRepository):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.GET_SERVICES_QUERY = "CALL PR_SELECT_GET_SERVICES();"
        
        super(ServiceQueueRepository, self).__init__()
        
    
    def get_services(self):
        super(ServiceQueueRepository, self).__open__()
        rows = super(ServiceQueueRepository, self).execute_query(self.GET_SERVICES_QUERY, [])
        super(ServiceQueueRepository, self).__close__()
        return [ServiceQueue(row) for row in rows]