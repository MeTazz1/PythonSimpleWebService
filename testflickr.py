import webapp2
import json
from urllib import urlencode, urlopen
from xml.dom import minidom
from google.appengine.api import urlfetch
from google.appengine.ext.webapp.util import run_wsgi_app
import hashlib
import os
import urlparse

HOST = 'http://api.flickr.com'
API = '/services/rest'
API_KEY = 'ad577200a30f4a09cb5bd01c439648ce'

def _doget(method, **params):
		url = '%s%s/?api_key=%s&method=%s&%s&format=json'% \
		      (HOST, API, API_KEY, method, urlencode(params))

		res = urlfetch.fetch(url).content

		if 'jsonFlickrApi(' in res:
		    return res[14:-1]
		return json.loads(res)

class MainPage(webapp2.RequestHandler):

 def get(self):

        self.response.headers['Content-Type'] = 'text/plain'
        par = urlparse.parse_qs(urlparse.urlparse(self.request.url).query)
        self.response.write(_doget('flickr.photos.search', text = par['search'], per_page='5')) 

application = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)