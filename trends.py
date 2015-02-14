from twitter import *

rqdata = trendsByLocation("New York") # search("#fail :)")
trends = rqdata[0]['trends']
for trend in trends:
    print trend["name"]

