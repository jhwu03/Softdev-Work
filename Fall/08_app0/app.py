  
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    print(__name__)
    return "no hablo queso!!!"

@app.route("/main")

def hello():
    print(__name__)
    return "bye"

@app.route("/side")

def hellooo():
    print(__name__)
    return "wow another one"

if __name__ == "__main__":
    app.debug = True
    app.run()
