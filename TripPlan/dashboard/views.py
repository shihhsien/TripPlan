from django.http import HttpResponse
from django.conf import settings
import oauth2, yaml, urllib

# remove below to api.py in yelp

def view(request):

	# Defining API keys provided by Yelp and stored in config.yaml
	consumer_key = settings.CONFIG['yelp']['api']['v2.0']['consumer_key']
	consumer_secret = settings.CONFIG['yelp']['api']['v2.0']['consumer_secret']
	token = settings.CONFIG['yelp']['api']['v2.0']['token']
	token_secret = settings.CONFIG['yelp']['api']['v2.0']['token_secret']

	consumer = oauth2.Consumer(consumer_key, consumer_secret)

	# Modify the url below for customized search
	url = 'http://api.yelp.com/v2/search?term=bars&location=sf'

	# Signing the url with API keys
	oauth_request = oauth2.Request('GET', url, {})
	oauth_request.update({'oauth_nonce': oauth2.generate_nonce(),
	                      'oauth_timestamp': oauth2.generate_timestamp(),
	                      'oauth_token': token,
	                      'oauth_consumer_key': consumer_key})

	token = oauth2.Token(token, token_secret)

	oauth_request.sign_request(oauth2.SignatureMethod_HMAC_SHA1(), consumer, token)

	signed_url = oauth_request.to_url()

	# Retrive raw yelp data using the signed url
	yelp_url_connection = urllib.urlopen(signed_url)
	raw_yelp_data = yelp_url_connection.read()
	yelp_url_connection.close()

	# html = signed_url
	return HttpResponse(raw_yelp_data)