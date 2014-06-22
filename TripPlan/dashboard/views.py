from django.shortcuts import render_to_response
from TripPlan.yelp import api

# default view
def index(request):
	yelp_response = api.yelp_request("New York", "dinner")

	# apply data to render view
	return render_to_response('index.html', yelp_response)

# customized yelp search
def user_input(request):
	yelp_response = api.yelp_request(request.GET.get('location'), request.GET.get('term'))
	
	# apply data to render view
	return render_to_response('results.html', yelp_response)
