import requests 
import urllib2, urllib
import base64
# r = requests.get('https://api.github.com/events')

## Encoding consumer key and consumer secret ##
request_token = {}
key = "3sTAvWUnGJZA2m5zzrctNUiFs"
secret = "78ma62jkA7d4mrm6xXTUcRzzX6F4iGaIFGpoFUSAevqUuZt4wC"
 
credentials = key + ":" + secret

credentials = base64.b64encode(credentials)

print(credentials)

## Making HTTP Post requests ##
grant_type = "client_credentials"
headers = {}
headers["Authorization"] = credentials
headers["Content-Type"] = "application/x-www-form-urlencoded;charset=UTF-8."
headers["grant_type"] = "client_credentials"

r = requests.post("https://api.twitter.com/oauth2/token", headers=headers)