from flask import Flask,render_template

# this makes app an instance of the Flask class
# and it passed the special variable __name__ into
# the constructor

from twitter import *
from wordCount import *

import plotly.plotly as py
from plotly.graph_objs import *

def topTrend(loc):
    trends = trendsByLocation(loc)
    query = trends[1]
    print trends[0]
    print trends[1]
    tweetss = tweets(query, count=1000)
    wCount = wordCount(tweetss)
    lCount = locCount(tweetss)
    listResults = dictListRev(wCount)[0:10]
    print listResults
    
    #Most commmon words
    #x = [v for k, v in listResults[1:]]
    #y = [k for k, v in listResults[1:]]
    
    #Locations of common tweets
    x = [v for k, v in lCount[1:10]]
    y = [k for k, v in lCount[1:10]]
    
    
    repTweet = closeMatch(listResults, tweetss)
    sortLoc = sorted(lCount, key=lambda tup: tup[0])
    print sortLoc
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
    print plot_url
    return (listResults[0][1], plot_url, repTweet)

app = Flask(__name__)

#@app.route("/home")
@app.route("/<loc>")
def home(loc):
    ttrend, url, repTweet = topTrend(loc)
    return render_template("display.html", trend=ttrend, ploturl=url, topTweet = repTweet)
#    return render_template("results.html", trends=trends())

if __name__=="__main__":
    app.debug=True
    app.run() 
    #app.run(host="0.0.0.0",port=8888)
