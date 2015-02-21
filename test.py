from twitter import *

rqdata = trendsByLocation("New York")

print(json.dumps(rqdata, sort_keys=True, \
                 indent=4, separators=(',', ': ')) )

