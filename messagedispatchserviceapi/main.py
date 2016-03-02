'''
Created on 20 de fev de 2016

@author: duzi
'''

from flask import Flask
from flask_restful import Api
from messagedispatchserviceapi.messagedispatchservice import MessageDispatchService



app = Flask(__name__)
api = Api(app)

api.add_resource(MessageDispatchService, '/get_services')


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()