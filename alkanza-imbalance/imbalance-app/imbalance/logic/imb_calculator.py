"""
Created on Jul 31, 2018

@author: Carlos Gaitan
"""
from geopy import distance

class ImbalanceCalculator(object):
    """Gives the methods to calculate the imbalance"""
    def __init__(self):
        """constructor"""
        
    def calculate_imbalance (self, lat, lng, places) -> int:
        """
        :param lat: latitude of the reference point.
        :type lat: string
        
        :param lng: longitude of the reference point.
        :type lng: string
        
        :param places: all the places returned by the google API
        :type places: list
        """
        if not lat:
            raise ValueError("Must provide a valid latitude")
    
        if not lng:
            raise ValueError("Must provide a valid longitude")
    
        if not places:
            raise ValueError("Must provide a valid places")
        distance_list = []
        for place in places:
            coords_1 = (lat, lng)
            location = place["geometry"]["location"]
            coords_2 = (location["lat"], location["lng"])
            distance_list.append(distance.distance(coords_1, coords_2).meters)
            
        # for now lets do a brute force approach
        imbalance = self.__brute_force(distance_list)
        return imbalance
    
    def __brute_force (self, distances) -> int:
        """
        :param distances: all the distance between the places and the reference point.
        :type distances: list
        """
        imbalance = 0
        for i in range(len(distances)):
            for j in range(len(distances)):
                if i != j:
                    imbalance += abs(distances[i]-distances[j])
        return imbalance