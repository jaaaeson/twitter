from twitter import *
import re

trends = trendsByLocation("Australia")
query = trends[1]# '"' + '" OR "'.join(trends) + '"'
print trends[1]
tweetss = tweets(query, count=1000)

for tweet in tweetss:
    print tweet

print

# MapReduce word count

def wordCount(tweetsList):
    words = []
    for tweet in tweetsList:
        words.extend(re.findall(r'(?:(?:https?://t\.co/)|[@#]?)\w+', tweet))
    d = {}
    for word in words:
        if word not in d and len(word) > 3 and not word.startswith('http'):
            ct = words.count(word)
            d[word] = ct
    return d

def dictListRev(dictionary):
    swag = []
    print len(dictionary)
    for k, v in dictionary.iteritems():
        swag.append((v, k))
    swag = sorted(swag,reverse=True)
    return swag

wordCount = wordCount(tweetss)

print(json.dumps(wordCount, sort_keys=True, \
                 indent=4, separators=(',', ': ')) )

listResults = dictListRev(wordCount)[0:10]
print listResults
x = [v for k, v in listResults[1:]]
y = [k for k, v in listResults[1:]]

import plotly.plotly as py
from plotly.graph_objs import *

data = Data([
             Bar(
                 x=x,
                 y=y
                 )
             ])
plot_url = py.plot(data, filename=str(listResults[0][1]))


"""import plotly.plotly as py
from plotly.graph_objs import *

tuples = wordCount.items()#.sort(cmp=lambda (k0, v0), (k1, v1): cmp(v1, v0))

x = [k for k, v in tuples][:10]
y = [v for k, v in tuples][:10]

data = Data([
             Bar(
                 x=x,
                 y=y
                 )
             ])
plot_url = py.plot(data, filename='basic-bar')

"""

'''
def dictionary(listTweets):
    words = []
    for tweet in listTweets:
        words.extend(re.findall(r'(?:(?:http://t\.co/)|[@#]?)\w+', tweet))
    list = []
    listWords = []
    for word in words:
        
        if word not in listWords:
            if len(word) > 3:
                listWords.append(word)
                list.append((listTweets.count(word), word))



    dTweets = sorted(list,reverse=True)
    return dTweets
'''


#print tweets("NFLCombine")

"""for i in range(5):
    print str(listResults[i][0]) + str(" ") + str(dTweets[i][1])"""

