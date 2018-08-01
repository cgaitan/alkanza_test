"""
Created on Jul 31, 2018

@author: Carlos Gaitan
"""
import requests
import json
from imbalance.resources.params import GoogleParams

class PlacesClient(object):
    """Performs requests to the Google Maps search API."""


    def __init__(self):
        """
        :param key: Maps API key. Required.
        :type key: string
        
        :param timeout: time out for the request in millis.
        :type timeout: integer
        
        :param retry_timeout: time out for retry the request in millis.
        :type retry_timeout: integer
        """
        self.params = GoogleParams()
        key = self.params.key()
        if not key:
            raise ValueError("Must provide API key to use Google services")
        else:
            self.key = key
        places_search_url = self.params.places_search_url()
        if not places_search_url:
            raise ValueError("Must provide a valid url to use Google services")
        else:
            self.places_search_url = places_search_url
        places_search_parameters = self.params.places_search_parameters()
        if not places_search_parameters:
            raise ValueError("Must provide a valid parameters to use Google services")
        else:
            self.places_search_parameters = places_search_parameters
    
    def parameters_to_ask (self):
        """returns the needed parameters to search a place"""
        return self.places_search_parameters
    
    def ask_places_to_maps (self, parameters: dict) -> list:
        """uses google API and returns a list of JSON places"""
        param_separator = ''
        params = ''
        for param, value in parameters.items():
            params += param_separator + param + '=' + str(value) 
            param_separator = '&'
        params += param_separator + "key=" + self.key
        final_url = self.places_search_url + params 
        answer = requests.get(final_url, None)
        if answer.ok:
            results = json.loads(answer.text)
            return results["results"]
        else:
            return None
    
    