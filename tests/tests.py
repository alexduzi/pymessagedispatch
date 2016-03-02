'''
Created on 21 de fev de 2016

@author: duzi
'''
from utils.util import Utils 
from pytest import *
from repository import baserepository


def can_load_configuration():
    value = Utils().get_value("DataBase", "DBMESSAGEDISPATCH_CONTEXT")
    assert(value)


def test_connection():
    
    try:
        baseRepo = baserepository.BaseRepository()
        baseRepo.__open__()
        conn = baseRepo.conn
        print(conn)
    except:
        print("Cannot connect to the database")
    
    assert(conn)
    
    
def main():
    test_connection()