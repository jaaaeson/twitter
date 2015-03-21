from twitter import *
import re

trends = trendsByLocation("United States")
query = trends[1]# '"' + '" OR "'.join(trends) + '"'
print trends[1]
tweetss = tweets(query, count=1000)

#for tweet in tweetss:
#   print tweet

print

# MapReduce word count

def wordCount(tweetsList):
    words = []
    for tweet in tweetsList:
        words.extend(re.findall(r'(?:(?:https?://t\.co/)|[@#]?)\w+', tweet))
    d = {}
    for word in words:
        if word.lower() not in d and len(word) > 3 and not word.startswith('http'):
            ct = words.count(word)
            d[word.lower()] = ct
    return d

def dictListRev(dictionary):
    swag = []
    #    print len(dictionary)
    for k, v in dictionary.iteritems():
        swag.append((v, k))
    swag = sorted(swag,reverse=True)
    return swag

wordCount = wordCount(tweetss)

#print(json.dumps(wordCount, sort_keys=True, \
 #                indent=4, separators=(',', ': ')) )

listResults = dictListRev(wordCount)[0:10]
#print listResults
x = [v for k, v in listResults[1:]]
y = [k for k, v in listResults[1:]]

def maxIndex(L):
    max = 0
    maxdex = -1
    for i in xrange(len(L)):
        if L[i] > max:
            max = L[i]
            maxdex = i
    return maxdex

def closeMatch(comWords, tweetsList):
    scoreboard = [0 for tweet in tweetsList]
    for (count, word) in comWords[1:]:
        for (i, tweet) in enumerate(tweetsList):
            if word in tweet:
                scoreboard[i] += count
    return tweetsList[maxIndex(scoreboard)]

print closeMatch(listResults, tweetss)

import plotly.plotly as py
from plotly.graph_objs import *

data = Data([
             Bar(
                 x=x,
                 y=y,
                 name='',
                 marker=Marker(
                               color='rgb(0, 149 ,255)'
                               ))
             ])

layout = Layout(
                title=listResults[0][1],
                xaxis=XAxis(
                            title='Hashtags and Words',
                            titlefont=Font(
                                           size=16,
                                           color='rgb(107, 107, 107)'
                                           ),

                            tickfont=Font(
                                          size=14,
                                          color='rgb(107, 107, 107)'
                                          )
                            ),
                yaxis=YAxis(
                            title='Number of Occurrences',
                            titlefont=Font(
                                           size=16,
                                           color='rgb(107, 107, 107)'
                                           ),
                            tickfont=Font(
                                          size=14,
                                          color='rgb(107, 107, 107)'
                                          )
                            ))
fig = Figure(data=data, layout=layout)
plot_url = py.plot(fig, filename=str(listResults[0][1]))