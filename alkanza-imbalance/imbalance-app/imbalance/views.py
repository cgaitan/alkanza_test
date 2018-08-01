"""
Created on Jul 31, 2018

@author: Carlos Gaitan
"""

from django.shortcuts import render
from imbalance import forms
from imbalance.app import ImbalanceApp
from imbalance.persistence.db_connector import MongoConnector

def index(request):
    if request.method== 'POST':
        try:
            form = forms.RequestForm(request.POST)
            if form.is_valid():
                latitude=form.cleaned_data['latitude']
                longitude=form.cleaned_data['longitude']
                radius=form.cleaned_data['radius']
                user=form.cleaned_data['user']
                types=form.cleaned_data['types']
                app = ImbalanceApp(latitude, longitude, radius, user, types)
                imbalance = app.usegoogleandcalculate();
                db_connector = MongoConnector()
                request_list = db_connector.get_all_request()
                return render(request,'index.html',{'request_form':form,'answer_imbalance':imbalance, "all_requests":request_list})
        except Exception as ex:
            print(str(ex))
            request.method='GET'
            return render(request,'index.html',{'request_form':form,'errorMessage':'invalid Search Parameters'})
    return render(request,'index.html',{'request_form':forms.RequestForm(),'errorMessage':None})
