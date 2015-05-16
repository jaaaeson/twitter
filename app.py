from flask import Flask,render_template

# this makes app an instance of the Flask class
# and it passed the special variable __name__ into
# the constructor

from twitter import *
from wordCount import *

import plotly.plotly as py
from plotly.graph_objs import *

import urllib

def topTrend(loc):
    trends = trendsByLocation(loc)
    query = trends[1]
    print trends[0]
    print trends[1]
    tweetss = tweets(query, count=10000)
    wCount = wordCount(tweetss)
    lCount = locCount(tweetss)
    listResults = dictListRev(wCount)[0:10]
    print listResults
    
    #Most commmon words
    x = [v for k, v in listResults[1:]]
    y = [k for k, v in listResults[1:]]
    
    repTweet = closeMatch(listResults, tweetss)
    sortLoc = sorted(lCount, key=lambda tup: tup[0], reverse=True)[:10]
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
                                )
                    )
    fig = Figure(data=data, layout=layout)
    plot_url0 = py.plot(fig, filename="Common Words: " + str(listResults[0][1]))
    print plot_url0

    #Locations of common tweets
    xb = [v for k, v in sortLoc]
    yb = [k for k, v in sortLoc]

    datab = Data([
                 Bar(
                     x=xb,
                     y=yb,
                     name='',
                     marker=Marker(
                                   color='rgb(0, 149 ,255)'
                                   ))
                 ])

    layoutb = Layout(
                    title=listResults[0][1],
                    xaxis=XAxis(
                                title='Locations',
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
    figb = Figure(data=datab, layout=layoutb)
    plot_url1 = py.plot(figb, filename="Locations: " + str(listResults[0][1]))
    print plot_url1
    return (listResults[0][1], plot_url0, plot_url1, repTweet)


app = Flask(__name__)

#@app.route("/home")
@app.route("/<loc>")
def home(loc):
    ttrend, url0, url1, repTweet = topTrend(loc)
    return render_template("display.html", place=urllib.unquote_plus(loc), trend=ttrend, ploturl0=url0, ploturl1=url1, topTweet = repTweet)
#    return render_template("results.html", trends=trends())

if __name__=="__main__":
    app.debug=True
    app.run() 
    #app.run(host="0.0.0.0",port=8888)
