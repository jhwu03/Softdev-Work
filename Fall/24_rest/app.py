from flask import Flask, render_template
import urllib.request, json
app = Flask(__name__)

@app.route("/")
def root():
    u = urllib.request.urlopen("https://api.nasa.gov/planetary/apod?api_key=mIUff1bfoswWIAadUfgriVysmcUmJXOZvslga5rV")
    response = u.read()
    data = json.loads( response )
    return render_template("index.html", pic = data['url'],title = data['title'], caption = data['explanation'])

if __name__ == "__main__":
    app.debug = True
    app.run()
