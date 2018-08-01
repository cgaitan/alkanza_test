"""
Created on Jul 31, 2018

@author: Carlos Gaitan
"""
import yaml

class GoogleParams(object):
    """loads the params from the yaml file for the application."""

    def __init__(self, params_route="imbalance/resources/config.yml"):
        """
        :param params_route: route to the application parameters.
        :type params_route: string
        """
        if not params_route:
            raise ValueError("Must provide a file with the application parameters.")
        
        with open(params_route, 'r') as ymlfile:
            cfg_file = yaml.load(ymlfile)
            self.cfg = cfg_file['google']
        
    def key (self):
        """returns the API key needed for create requests to Google API""" 
        return self.cfg['key']
    
    def places_detail_url (self):
        """returns the API places_detail_url needed for create requests to detail places API""" 
        return self.cfg['places_detail_url']
    
    def places_detail_parameters (self):
        """returns the API places_detail_parameters needed for create requests to detail places API""" 
        return self.cfg['places_detail_parameters']
    
    def places_search_url (self):
        """returns the API places_search_url needed for create requests to detail places API""" 
        return self.cfg['places_search_url']
    
    def places_search_parameters (self):
        """returns the API places_search_parameters needed for create requests to detail places API""" 
        return self.cfg['places_search_parameters']
    
class MongoParams(object):
    """loads the params from the yaml file for the application."""

    def __init__(self, params_route="imbalance/resources/config.yml"):
        """
        :param params_route: route to the application parameters.
        :type params_route: string
        """
        if not params_route:
            raise ValueError("Must provide a file with the application parameters.")
        
        with open(params_route, 'r') as ymlfile:
            cfg_file = yaml.load(ymlfile)
            self.cfg = cfg_file['db']
        
    def connection_url (self):
        """returns the connection_url needed to connect to the DB""" 
        return self.cfg['connection_url']
        
    def port (self):
        """returns the port needed to connect to the DB""" 
        return self.cfg['port']
        
    def database (self):
        """returns the database needed to connect to the DB""" 
        return self.cfg['database']
        
    def collec (self):
        """returns the collection needed to connect to the DB""" 
        return self.cfg['collec']
        
    def user (self):
        """returns the user needed to connect to the DB""" 
        return self.cfg['user']
        
    def password (self):
        """returns the password needed to connect to to DB""" 
        return self.cfg['password']
    
    
    