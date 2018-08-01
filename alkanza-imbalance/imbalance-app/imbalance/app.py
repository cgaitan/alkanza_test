"""
Created on Jul 31, 2018

@author: Carlos Gaitan
"""
import time
import datetime
from imbalance.logic.imb_calculator import ImbalanceCalculator
from imbalance.persistence.db_connector import MongoConnector
from imbalance.services.places_client import PlacesClient

class ImbalanceApp(object):
    """Performs the request to the google API with the data and saves the request."""

    def __init__(self, lat=None, lng=None, rad=None, user=None, types=None ):
        """
        :param lat: Maps API key. Required.
        :type lat: string
        
        :param lng: time out for the request in millis.
        :type lng: string
        
        :param rad: time out for retry the request in millis.
        :type rad: integer
        
        :param user: time out for the request in millis.
        :type user: string
        
        :param types: time out for retry the request in millis.
        :type types: string
        """
        if not lat:
            raise ValueError("Must provide API key to use Google services")
        else:
            self.lat = lat
        
        if not lng:
            raise ValueError("Must provide API key to use Google services")
        else:
            self.lng = lng
        
        if not rad:
            raise ValueError("Must provide API key to use Google services")
        else:
            self.rad = rad
        
        if not user:
            raise ValueError("Must provide API key to use Google services")
        else:
            self.user = user
        
        if not types:
            raise ValueError("Must provide API key to use Google services")
        else:
            self.types = types
           
    def usegoogleandcalculate (self) -> int:
        # get the client for the API
        places_client = PlacesClient()
        # prepare the request object
        request = {}
        request["location"]=self.lat + "," + self.lng
        request["radius"]=self.rad
        request["types"]=self.types
        #ask google for the places
        places = places_client.ask_places_to_maps(request)
        request["user"]=self.user
        request["date"]=datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
        # calculate the imbalance
        imbalance_calculator = ImbalanceCalculator()
        imbalance = imbalance_calculator.calculate_imbalance(self.lat, self.lng, places)
        request["imbalance"]=imbalance
        #request["places"]=places
        # save the request
        mongo_client = MongoConnector()
        mongo_client.save_request(request)
        return imbalance
