"""
Created on Jul 31, 2018

@author: Carlos Gaitan
"""
from django import forms

class RequestForm(forms.Form):        
    latitude = forms.CharField(max_length=254, help_text='Required. fill with a valid latitude Example:4.6883842.')
    longitude = forms.CharField(max_length=254, help_text='Required. fill with a valid longitude Example:-74.0745095.')
    radius = forms.IntegerField(help_text='Required. fill with a valid radius in meters Example:500.')
    user = forms.CharField(max_length=254, help_text='Required. fill with a valid user Example:juan.')
    types = forms.CharField(max_length=254, help_text='Required. fill with a valid type Example:hospital.')