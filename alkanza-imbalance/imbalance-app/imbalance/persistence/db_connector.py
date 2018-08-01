"""
Created on Jul 31, 2018

@author: Carlos Gaitan
"""
from pymongo import MongoClient
from imbalance.resources.params import MongoParams

class MongoConnector(object):
    """Performs requests to the MongoDB database"""


    def __init__(self):
        self.params = MongoParams()
        connection_url = self.params.connection_url()
        if not connection_url:
            raise ValueError("Must provide a valid host to connect to DB")
        else:
            self.connection_url = connection_url
        port = self.params.port()
        if not port:
            raise ValueError("Must provide a valid port to connect to DB")
        else:
            self.port = port
        database = self.params.database()
        if not database:
            raise ValueError("Must provide a valid database name to connect to DB")
        else:
            self.database = database
        collec = self.params.collec()
        if not collec:
            raise ValueError("Must provide a valid collection name to connect to DB")
        else:
            self.collec = collec
        user = self.params.user()
        if not user:
            raise ValueError("Must provide a valid user to connect to DB")
        else:
            self.user = user
        password = self.params.password()
        if not password:
            raise ValueError("Must provide a valid password to connect to DB")
        else:
            self.password = password
    
    def __connection (self):
        """returns the connection to the database"""
        client = MongoClient(self.connection_url, username=self.user, password=self.password, authSource=self.database, ssl=True, port=self.port)
        return client.get_database(self.database)

    def save_request (self, request):
        """saves the request to the database, if exists then only updates the data"""
        inserted_id = self.__connection().get_collection(self.collec).update({'date':request['date']},request,True)
        return str(inserted_id)
    
    def get_all_request (self):
        """gets all the request from the database"""
        all_requests = self.__connection().get_collection(self.collec).find()
        return list(all_requests)
    