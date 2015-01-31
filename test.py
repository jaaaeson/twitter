import requests 
import urllib2, urllib
import base64
import json
# r = requests.get('https://api.github.com/events')

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
print(r.text)

auth = json.loads(r.text)
