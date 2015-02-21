from twitter import *

rqdata = search("japan", count=10)["statuses"]
for entry in rqdata:
    print entry['text']

#print(json.dumps(rqdata, sort_keys=True, \
#                 indent=4, separators=(',', ': ')) )


