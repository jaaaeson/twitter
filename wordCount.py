from twitter import *
import re

#trends = trendsByLocation("United States")
#query = trends[1]# '"' + '" OR "'.join(trends) + '"'
#print trends[1]
#tweetss = tweets(query, count=1000)

#for tweet in tweetss:
#   print tweet

# MapReduce word count

def isSignificant(word):
    return word.lower() not in [u'there',u'this',u'that',u'also',u'with',u'then',u'your',u'during',u'than']


def wordCount(tweetsList):
    words = []
    for tweet in tweetsList:
        words.extend(re.findall(r'(?:(?:https?://t\.co/)|[@#]?)\w+', tweet[0]))
    d = {}
    for word in words:
        if word.lower() not in d and len(word) > 3 and not word.startswith('http') and isSignificant(word):
            ct = words.count(word)
            d[word.lower()] = ct
    return d

def locCount(locationList):
    locations = []
    print "LOCATION LIST:"
    print locationList
    for location in locationList:
        locations.append(location[1])
    print locations
    e = []
    for location in locations:
        if location not in e:
            if location != "":
                e.append((locations.count(location), location.lower()))
    return e

def dictListRev(dictionary):
    swag = []
    #    print len(dictionary)
    for k, v in dictionary.iteritems():
        swag.append((v, k))
    swag = sorted(swag,reverse=True)
    return swag

#wordCount = wordCount(tweetss)

#print(json.dumps(wordCount, sort_keys=True, \
 #                indent=4, separators=(',', ': ')) )

#listResults = dictListRev(wordCount)[0:10]
#print listResults
#x = [v for k, v in listResults[1:]]
#y = [k for k, v in listResults[1:]]

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


#repTweet = closeMatch(listResults, tweetss)
