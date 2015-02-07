import requests # thus far, only in Python 2.x
import urllib2, urllib
import base64
import json
import yweather # for WOEIDs

## Encoding consumer key and consumer secret ##
headers = {}
consumer_key = "3sTAvWUnGJZA2m5zzrctNUiFs"
consumer_secret = "78ma62jkA7d4mrm6xXTUcRzzX6F4iGaIFGpoFUSAevqUuZt4wC"
authorization = consumer_key+":"+consumer_secret
headers['Authorization'] = "Basic " + base64.b64encode(authorization)
headers["Content-Type"] = "application/x-www-form-urlencoded;charset=UTF-8."

data = {}
data["grant_type"] = "client_credentials"
r = requests.post("https://api.twitter.com/oauth2/token", headers=headers, data=data)
#print(r.text)

auth = json.loads(r.text)
#print("Token type: " + auth['token_type'])
#print("Access token: " + auth['access_token'])
def get(url):
    headers = {
        'Authorization': auth['token_type'] + " " + auth['access_token']
    }
    rq = requests.get("https://api.twitter.com/1.1/" + url, headers=headers)
    return json.loads(rq.text)

def search(q, lang="en", count=10):
    return get("search/tweets.json?q=" + urllib.quote_plus(q) + \
                              "&lang=" + lang + \
                             "&count=" + str(count) )

woeidgen = yweather.Client()
def trendsByLocation(location):
    woeid = woeidgen.fetch_woeid(location)
    return get("trends/place.json?id="+woeid)

rqdata = trendsByLocation("New York") # search("#fail :)")
print(json.dumps(rqdata, sort_keys=True, \
                 indent=4, separators=(',', ': ')) )

