import requests 
import urllib2, urllib
import base64
import json
import yweather

headers = {}
consumer_key = "3sTAvWUnGJZA2m5zzrctNUiFs"
consumer_secret = "78ma62jkA7d4mrm6xXTUcRzzX6F4iGaIFGpoFUSAevqUuZt4wC"
authorization = consumer_key+":"+consumer_secret
headers['Authorization'] = "Basic " + base64.b64encode(authorization)
headers["Content-Type"] = "application/x-www-form-urlencoded;charset=UTF-8."

data = {}
data["grant_type"] = "client_credentials"
r = requests.post("https://api.twitter.com/oauth2/token", headers=headers, data=data)

auth = json.loads(r.text)

def get(url):
    headers = {
        'Authorization': auth['token_type'] + " " + auth['access_token']
    }
    rq = requests.get("https://api.twitter.com/1.1/" + url, headers=headers)
    return json.loads(rq.text)

client = yweather.Client()
WOEID = client.fetch_woeid('New York City')

rqdata = get("trends/place.json?id=" +WOEID)

trends = rqdata[0]['trends']

for trend in trends:
    print trend["name"]

