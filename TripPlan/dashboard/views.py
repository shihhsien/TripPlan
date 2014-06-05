from django.http import HttpResponse
from django.conf import settings
from django.template import Context, loader, Template
from django.shortcuts import render_to_response
from TripPlan.yelp import api
import oauth2, yaml, urllib, json

# default view
def index(request):
	yelp_response = api.yelp_request("11215", "bar")

	# apply data to render view
	return render_to_response('index.html', yelp_response)

# customized yelp search
def user_input(request, location, term):
	yelp_response = api.yelp_request(location, term)
	
	# apply data to render view
	return render_to_response('results.html', yelp_response)
