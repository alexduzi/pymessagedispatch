'''
Created on 19 de fev de 2016

@author: duzi
'''
import pika
import urllib
import json
import logging

class QueueControl(object):
    '''
    classdocs
    '''

    URL_GET = ""
    

    def __init__(self, queue_name, hots, port, virtual_host):
        '''
        Constructor
        '''
        self.queue_name = queue_name
        self.queues = json.load(urllib.request.urlopen(QueueControl.URL_GET))
        self.connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        self.channel = self.connection.channel()
        self._consume_messages_()
        self.log = logging.Logger("name", "level")
        
        
    def _consume_messages_(self):
        '''
        '''
        self.channel.basic_consume( QueueControl.receive_message,
                                    queue='hello',
                                    no_ack=True)
        self.log(' [*] Waiting for messages. To exit press CTRL+C')
        self.channel.start_consuming()
        
        
    @staticmethod
    def receive_message(ch, method, properties, body):
        pass
        
        
        
        
        
            