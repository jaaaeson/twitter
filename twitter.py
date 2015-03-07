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

def tweets(q, lang="en", count=1000):
    data = get("search/tweets.json?q=" + urllib.quote_plus(q) + \
               "&lang=" + lang + \
               "&count=" + str(count) )
    return [tweet['text'] for tweet in data['statuses']]

woeidgen = yweather.Client()
def trendsByLocation(location):
    woeid = woeidgen.fetch_woeid(location)
    return [trend['name'] for trend in get("trends/place.json?id="+woeid)[0]['trends']]


def dictionary(stringTweets):
    listTweets = stringTweets.split(" ")
    list = []
    listWords = []
    for word in listTweets:
  
        if word.strip("\n\n") not in listWords:
            if len(word) > 3:
                listWords.append(word)
                list.append((listTweets.count(word.strip("\n\n")),(word.strip("\n\n"))))



    dTweets = sorted(list,reverse=True)
    return dTweets

listResults = dictionary(tweets("NFLCombine"))

"""for i in range(5):
    print str(listResults[i][0]) + str(" ") + str(dTweets[i][1])"""


x = [v for k, v in listResults][1:10]
y = [k for k, v in listResults][1:10]





import plotly.plotly as py
from plotly.graph_objs import *

import plotly.plotly as py
from plotly.graph_objs import *

data = Data([
             Bar(
                 x=x,
                 y=y
                 )
             ])
plot_url = py.plot(data, filename='basic-bar')


