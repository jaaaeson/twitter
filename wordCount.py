from twitter import *
import re

trends = trendsByLocation("New York")
query = '"' + '" OR "'.join(trends) + '"'
tweets = tweets(query, count=1000)

for tweet in tweets:
    print tweet

print

# MapReduce word count

def wordCount(tweets):
    words = []
    for tweet in tweets:
        words.extend(re.findall(r'(?:(?:http://t\.co/)|[@#]?)\w+', tweet))
    d = {}
    for word in words:
        if word not in d:
            d[word] = words.count(word)
    return d

wordCount = wordCount(tweets)

#print wordCount
print(json.dumps(wordCount, sort_keys=True, \
                 indent=4, separators=(',', ': ')) )
