from flask import Flask,render_template
from twitter import *
# this makes app an instance of the Flask class
# and it passed the special variable __name__ into
# the constructor


def trends():
    L = trendsByLocation('New York')
    yolo = []
    for trend in L:
        yolo.append(
            {
                "name": trend,
                "tweets": tweets(trend)
            }
        )
    return yolo

app = Flask(__name__)

@app.route("/home")
@app.route("/") 
def home():
    return render_template("results.html", trends=trends())

if __name__=="__main__":
    app.debug=True
    app.run() 
    #app.run(host="0.0.0.0",port=8888)
