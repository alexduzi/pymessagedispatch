'''
Created on 20 de fev de 2016

@author: duzi
'''

from flask_restful import Resource
from repository.servicequeuerepository import ServiceQueueRepository
import json

class MessageDispatchService(Resource):
    '''
    classdocs
    '''
    
    def __init__(self):
        '''
        Constructor class
        '''
        self.repository = ServiceQueueRepository()
    
    
    def get(self):
        #return { "Hello": "Hello World!" }
        return json.dumps( [service.to_dict() for service in self.repository.get_services()] )
        
        