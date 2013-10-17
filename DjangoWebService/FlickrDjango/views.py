# Create your views here.
from django.http import HttpResponse
import urllib2
import json
import django.utils.http
from urllib import urlencode, urlopen
import urllib
import pprint

HOST = 'http://api.flickr.com'
API = '/services/rest'
API_KEY = 'ad577200a30f4a09cb5bd01c439648ce'

import pprint

pp = pprint.PrettyPrinter(indent=4)

def _doget(method, **params):

		url = '%s%s/?api_key=%s&method=%s&%s&format=json'% \
		(HOST, API, API_KEY, method, urlencode(params))

		pp.pprint(url)
		request = urllib2.Request(url)
		pp.pprint(request)

		response = urllib2.urlopen(request)

		pp.pprint('response is')
		data = response.read()

		pp.pprint(data)

		if 'jsonFlickrApi(' in data:
		    return data[14:-1]

		return data
		
		# return resp_parsed


def detail(request, to_search):
    return HttpResponse(_doget('flickr.photos.search', text = to_search, per_page='5'), content_type="text/plain")

def index(request):
    return HttpResponse("Hellow worl")
